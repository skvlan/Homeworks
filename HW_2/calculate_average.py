from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/calculate-average", methods=['GET'])
def calculate_average():
    df = pd.read_csv('hw.csv')

    df.columns = df.columns.str.strip()

    column_name = request.args.get('column', default='Height(Inches)')
    column_name_1 = request.args.get('column1', default='Weight(Pounds)')

    if column_name not in df or column_name_1 not in df:
        return "Column doesn't found", 400

    average_height = df[column_name].mean()
    average_weight = df[column_name_1].mean()

    results = (f"Average value for {column_name} = {average_height}\n |"
               f" Average value for {column_name_1} = {average_weight}")

    return results



if __name__ == '__main__':
    app.run(
        port=5001, debug=True
    )





