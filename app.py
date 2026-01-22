from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']

    mongo.db.todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })
    return jsonify({"message": "Item added"})

