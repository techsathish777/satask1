from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

# Load CSV data
data = pd.read_csv('dump.csv')

def get_companies():
    return data['Company'].unique().tolist()

def get_stock_data(company):
    return data[data['Company'] == company].to_dict(orient='records')

@app.route('/api/companies')
def companies():
    return jsonify(get_companies())

@app.route('/api/stock/<company>')
def stock(company):
    return jsonify(get_stock_data(company))

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
