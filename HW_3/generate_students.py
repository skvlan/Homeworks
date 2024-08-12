from faker import Faker
from flask import Flask, request, Response, jsonify
import requests
import csv
import io
from webargs import fields
from webargs.flaskparser import use_args, parser


app = Flask(__name__)

faker_instance = Faker()
@app.route("/generate-students")
def generate_students():
    number_of_students = request.args.get("number_of_students", '1000')
    number_of_students = int(number_of_students)

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(['Name', ' Last Name', '    Email', '          Password', '       Age'])

    for _ in range(number_of_students):
        writer.writerow([
            faker_instance.first_name(),
            faker_instance.last_name(),
            faker_instance.email(),
            faker_instance.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
            faker_instance.random_int(min=18, max=60)
        ])

    output.seek(0)

    return Response(
        output,
        mimetype="text/plain",                          #we can use csv instead of plain to download students.csv on pc
        headers={"Content-Disposition": "inline;filename=students.csv"}
    )


"""get_bitcoin_value"""

def get_available_currencies():
    url = "https://bitpay.com/api/rates"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [currency['code'] for currency in data]
    return []

available_currencies = get_available_currencies()
'''
def validate_currency_code(value):
    if value.upper() not in available_currencies:
        raise ValueError("Currency not found")
    return value.upper()

args_schema = {
    'currency': fields.Str(
        required=False,
        missing='USD',
        validate=validate_currency_code,
        error_messages={"validator_failed": "Currency not found"}
    ),
    'convert': fields.Float(
        required=False,
        missing=1.0,
        error_messages={"invalid": "The amount must be a number."}
    )
}

'''


def get_symbol(currency_code):
    url = "https://bitpay.com/currencies"
    response = requests.get(url)

    if response.status_code == 200:
        currencies = response.json().get('data', [])
        for currency in currencies:
            if currency['code'].upper() == currency_code.upper():
                return currency.get('symbol', currency_code)

    return currency_code

def get_bitcoin_value(currency_code='USD', bitcoin_amount=1):
    url = f"https://bitpay.com/api/rates/{currency_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rate']
        total_value = rate * bitcoin_amount
        currency_symbol = get_symbol(currency_code)

        return f"{total_value:.2f} {currency_symbol}"
    else:
        return "Error fetching data from BitPay API"



@app.route('/bitcoin_rate')
#@use_args(args_schema, location="query")
def bitcoin_rate():
    currency_code = request.args.get('currency', default='USD')
    bitcoin_amount = float(request.args.get('convert', default=1))

    result = get_bitcoin_value(currency_code, bitcoin_amount)

    if result:
        return jsonify({"currency": currency_code, "bitcoin_amount": bitcoin_amount, "total_value": result})
    else:
        return jsonify({"error": "Error retrieving data from API"}), 400

#@parser.error_handler
#def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
#    abort(jsonify(err.messages), 400)

if __name__ == '__main__':
    app.run(
        port=5000, debug=True
    )

