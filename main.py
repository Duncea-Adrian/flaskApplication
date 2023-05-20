import json

from flask import Flask, request, jsonify

app = Flask(__name__)

with open('products.json', 'r') as f:
    data = json.load(f)


@app.route('/', methods=['GET'])
def allData():
    results = []
    for item in data:
        results.append(item)
    return jsonify(results)


@app.route('/cauta/title/<cuvant_cautat>', methods=['GET'])
def search(cuvant_cautat):
    results = []
    for item in data:
        if item['Title'] == cuvant_cautat:
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
