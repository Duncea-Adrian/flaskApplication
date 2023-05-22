import json

from flask import Flask, request, jsonify

app = Flask(__name__)
# Am deschis fisierul json si am adaugat continutul lui in variabila data
with open('products.json', 'r') as f:
    data = json.load(f)

# Endpoint-ul / returneaza tot continutul fisierului json
@app.route('/', methods=['GET'])
def allData():
    results = []
    for item in data:
        results.append(item)
    return jsonify(results)

# Endoint-ul /cauta/title/<cuvant_cautat returneaza continutul titlului cautat
@app.route('/cauta/title/<cuvant_cautat>', methods=['GET'])
def search(cuvant_cautat):
    results = []
    for item in data:
        if item['Title'] == cuvant_cautat:
            results.append(item)
    return jsonify(results)

# Endpoint-ul /title returneaza toate titlurile din fisierul json
@app.route('/title', methods=['GET'])
def allTitles():
    results = []
    for item in data:
        results.append(item['Title'])
    return jsonify(results)


if __name__ == '__main__':
    app.run()
