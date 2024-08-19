from flask import Flask, jsonify, request
from webargs import fields
from webargs.flaskparser import use_args
from HW_5.database_handler import execute_query

app = Flask(__name__)


def normalize_genre_name(genre_name):
    return genre_name.replace(" ", "")

stats_by_city_args = {
    "genre": fields.Str(required=True, error_messages={"required": "Genre is a required parameter."})
}

@app.route('/stats_by_city')
@use_args(stats_by_city_args, location="query")
def stats_by_city(args):
    genre = args.get('genre')

    normalized_genre = normalize_genre_name(genre)

    query = """
    SELECT c.City, COUNT(*) as PlayCount
    FROM customers c
    JOIN invoices i ON c.CustomerId = i.CustomerId
    JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
    JOIN tracks t ON ii.TrackId = t.TrackId
    JOIN genres g ON t.GenreId = g.GenreId
    WHERE REPLACE(g.Name, ' ', '') = ?
    GROUP BY c.City
    ORDER BY PlayCount DESC
    LIMIT 1;
    """

    result = execute_query(query, (normalized_genre,))

    if not result:
        return jsonify({"message": "Genre not found"}), 404

    city, play_count = result[0]
    return jsonify({"city": city, "play_count": play_count})


if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )


