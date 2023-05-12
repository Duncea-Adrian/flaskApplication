import json

from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the JSON data
with open('products.json', 'r') as f:
    data = json.load(f)


@app.route('/', methods=['GET'])
def allData():
    results = []
    for item in data:
        results.append(item)
    return jsonify(results)


# Define the endpoint
@app.route('/cauta/title/', methods=['GET'])
def search():
    title = request.args.get('title')
    results = []
    for item in data:
        if item['Title'] == title:
            results.append(item)
    return jsonify(results)


@app.route('/title', methods=['GET'])
def allTitles():
    results = []
    for item in data:
        results.append(item['Title'])
    return jsonify(results)


if __name__ == '__main__':
    app.run()
