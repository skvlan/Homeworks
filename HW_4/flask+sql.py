from flask import Flask, request, jsonify
from HW_4.database_handler import execute_query
from webargs import fields
from webargs.flaskparser import use_args



app = Flask(__name__)

order_price_args = {
        "country": fields.Str(required=False)
    }

@app.route('/order-price')
@use_args(order_price_args, location="query")
def order_price(args):
    country = args.get('country')

    query = """
    SELECT inv.BillingCountry, SUM(ii.UnitPrice * ii.Quantity) AS TotalSales FROM invoices AS inv
    JOIN invoice_items AS ii ON inv.InvoiceId = ii.InvoiceId
    """

    if country:
        query += "WHERE inv.BillingCountry = ?"
        query += "GROUP BY inv.BillingCountry"
        sales_data = execute_query(query, (country,))
    else:
        query += " GROUP BY inv.BillingCountry"
        sales_data = execute_query(query)

    result = [{"Country": row[0], "TotalSales": row[1]} for row in sales_data]

    return jsonify(result)


@app.route('/track-info/<int:track_id>')
def get_all_info_about_track(track_id):
    query = """
    SELECT t.TrackId, t.Name AS TrackName, t.Composer, t.Milliseconds, t.Bytes, t.UnitPrice,
           a.Title AS AlbumTitle, ar.Name AS ArtistName, g.Name AS GenreName, mt.Name AS MediaTypeName FROM tracks t
    JOIN albums a ON t.AlbumId = a.AlbumId
    JOIN artists ar ON a.ArtistId = ar.ArtistId
    JOIN genres g ON t.GenreId = g.GenreId
    JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId WHERE t.TrackId = ?
    """

    track_info = execute_query(query, (track_id,))

    if track_info:
        return jsonify(track_info[0])



@app.route('/total-album-duration')
def get_total_album_duration():
    query = "SELECT SUM(Milliseconds) / 3600000.0 AS TotalHours FROM tracks"
    total_hours = execute_query(query)

    return jsonify({"total_duration_hours": total_hours[0][0]})

if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )