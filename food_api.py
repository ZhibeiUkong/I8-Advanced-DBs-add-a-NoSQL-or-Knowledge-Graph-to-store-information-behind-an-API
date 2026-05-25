from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

food_data = read_json_file("food_records.json")

@app.route("/")
def info():
    return food_data["about"]

@app.route("/api/metadata")
def metadata():
    return jsonify({
        "project": food_data["project"],
        "author": food_data["author"],
        "about": food_data["about"],
        "use": food_data["use"],
        "record_count": len(food_data["entries"])
    })

@app.route("/api/foods")
def all_foods():
    return jsonify(food_data["entries"])

@app.route("/api/foods/<product_id>")
def food_by_id(product_id):
    for food in food_data["entries"]:
        if food["product_id"].lower() == product_id.lower():
            return jsonify(food)
    return jsonify({"error": "Product not found"}), 404

@app.route("/api/foods/safe")
def safe_foods():
    result = []
    for food in food_data["entries"]:
        if food["safety_status"].lower() == "safe":
            result.append(food)
    return jsonify(result)

@app.route("/api/foods/warnings")
def warning_foods():
    result = []
    for food in food_data["entries"]:
        if food["safety_status"].lower() in ["warning", "under review"]:
            result.append(food)
    return jsonify(result)

@app.route("/api/foods/recalls")
def recall_related_foods():
    result = []
    for food in food_data["entries"]:
        if food["recall_status"].lower() != "no active recall":
            result.append(food)
    return jsonify(result)

@app.route("/api/foods/category/<category>")
def foods_by_category(category):
    result = []
    for food in food_data["entries"]:
        if food["category"].lower() == category.lower():
            result.append(food)
    return jsonify(result)

@app.route("/api/foods/agency/<agency>")
def foods_by_agency(agency):
    result = []
    for food in food_data["entries"]:
        if food["inspection_agency"].lower() == agency.lower():
            result.append(food)
    return jsonify(result)

@app.route("/api/foods/search")
def search_foods():
    status = request.args.get("status")
    category = request.args.get("category")
    agency = request.args.get("agency")

    result = food_data["entries"]

    if status:
        result = [food for food in result if food["safety_status"].lower() == status.lower()]

    if category:
        result = [food for food in result if food["category"].lower() == category.lower()]

    if agency:
        result = [food for food in result if food["inspection_agency"].lower() == agency.lower()]

    return jsonify(result)

@app.route("/api/foods/summary")
def summary():
    total_records = len(food_data["entries"])
    safe_count = 0
    warning_count = 0
    under_review_count = 0
    recall_related_count = 0

    for food in food_data["entries"]:
        if food["safety_status"].lower() == "safe":
            safe_count += 1
        elif food["safety_status"].lower() == "warning":
            warning_count += 1
        elif food["safety_status"].lower() == "under review":
            under_review_count += 1

        if food["recall_status"].lower() != "no active recall":
            recall_related_count += 1

    return jsonify({
        "total_records": total_records,
        "safe_count": safe_count,
        "warning_count": warning_count,
        "under_review_count": under_review_count,
        "recall_related_count": recall_related_count
    })

if __name__ == "__main__":
    app.run(port=5002)