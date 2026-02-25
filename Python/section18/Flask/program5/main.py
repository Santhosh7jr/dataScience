from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

items = [
    {"id" : 1, "name" : "item1", "description" : "this is item1"},
    {"id" : 2, "name" : "item2", "description" : "this is item2"}
]

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/item")
def get_items():
    return jsonify(items)

@app.route("/item/<int:item_id>")
def get_specific_item(item_id):
    
    return jsonify(next((item for item in items if item["id"] == item_id), {}))

@app.route("/items", methods = ['GET', 'POST'])
def post_item():

    if not request.json:
        return jsonify({"description" : "There is an Error!"})
    
    items.append({request.json})
    return jsonify(request.json)

@app.route("/item/<int:id>", methods = ['PUT'])
def put_item(id):
    items[id]["id"] = id + 1
    items[id]["name"] = f"Item {id + 1}"
    items[id]["description"] = f"this is item{id + 1}"

    return jsonify(items)

@app.route("/item/<int:id>", methods = ['DELETE'])
def delete_item(id):
    items.pop(id)

    return jsonify(items)

if __name__ == "__main__":
    app.run() 