# Food Safety API - Extended Version

## Project Overview

This project extends my previous individual API assignment by adding additional Flask API functions that return specific data from a food safety information structure. The information structure is based on our group project idea: a QR-code-based food safety system that allows consumers, suppliers, retailers, and regulators to access food origin, processing, safety status, recall status, allergen information, and inspection agency information.

The updated API uses a static JSON file, `food_records.json`, which is loaded into memory when the Flask server starts. The Flask app then provides multiple GET endpoints that allow users to retrieve all records, project metadata, individual products, safe products, warning or under-review products, recall-related products, category-based results, agency-based results, combined search results, and summary counts.

This supports portability because the information structure is stored in a structured JSON format and can be accessed through standard HTTP GET requests from a browser, Python script, or other applications.

## Information Structure

The main information structure is stored in `food_records.json`.

The JSON file includes project-level metadata and a list of food safety records. The metadata describes the project, author, purpose, and use of the API. The `entries` section stores the actual food safety records.

Each food record includes the following fields: `product_id`, `product_name`, `category`, `origin_location`, `supplier`, `processing_location`, `batch_number`, `harvest_date`, `package_date`, `safety_status`, `recall_status`, `allergen_info`, `inspection_agency`, and `last_updated`.

These fields help users understand where a food product comes from, how it was processed, whether it has a safety warning or recall-related issue, and which agency is responsible for inspection.

## Files in This Repository

This repository includes four main files: `food_records.json`, `food_api.py`, `test_api.py`, and `README.md`.

`food_records.json` stores the food safety information structure and project metadata in JSON format. `food_api.py` runs the Flask API server and exposes multiple API endpoints. `test_api.py` uses Python `requests.get()` to access the API through the ngrok public URL and print the returned data. `README.md` explains the project, setup process, API endpoints, testing process, and video tutorial link.

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Returns a short description of the API |
| `/api/metadata` | GET | Returns project metadata and total record count |
| `/api/foods` | GET | Returns all food safety records |
| `/api/foods/<product_id>` | GET | Returns one food record by product ID |
| `/api/foods/safe` | GET | Returns food records with a Safe status |
| `/api/foods/warnings` | GET | Returns food records with Warning or Under Review status |
| `/api/foods/recalls` | GET | Returns recall-related or safety-review records |
| `/api/foods/category/<category>` | GET | Returns food records by category |
| `/api/foods/agency/<agency>` | GET | Returns food records by inspection agency |
| `/api/foods/search?status=Safe&agency=FDA` | GET | Returns filtered food records based on query parameters |
| `/api/foods/summary` | GET | Returns summary counts for total, safe, warning, under-review, and recall-related records |

## Example API Requests

Local Flask server examples:

```text
http://127.0.0.1:5002/
http://127.0.0.1:5002/api/metadata
http://127.0.0.1:5002/api/foods
http://127.0.0.1:5002/api/foods/FS-001
http://127.0.0.1:5002/api/foods/safe
http://127.0.0.1:5002/api/foods/warnings
http://127.0.0.1:5002/api/foods/recalls
http://127.0.0.1:5002/api/foods/category/Meat
http://127.0.0.1:5002/api/foods/agency/FDA
http://127.0.0.1:5002/api/foods/search?status=Safe&agency=FDA
http://127.0.0.1:5002/api/foods/summary
```

ngrok public URL examples:

```text
https://upfront-snort-concur.ngrok-free.dev/
https://upfront-snort-concur.ngrok-free.dev/api/metadata
https://upfront-snort-concur.ngrok-free.dev/api/foods
https://upfront-snort-concur.ngrok-free.dev/api/foods/FS-001
https://upfront-snort-concur.ngrok-free.dev/api/foods/safe
https://upfront-snort-concur.ngrok-free.dev/api/foods/warnings
https://upfront-snort-concur.ngrok-free.dev/api/foods/recalls
https://upfront-snort-concur.ngrok-free.dev/api/foods/category/Meat
https://upfront-snort-concur.ngrok-free.dev/api/foods/agency/FDA
https://upfront-snort-concur.ngrok-free.dev/api/foods/search?status=Safe&agency=FDA
https://upfront-snort-concur.ngrok-free.dev/api/foods/summary
```

## How to Run the Flask Server Locally

Open Command Prompt and go to the project folder:

```bash
cd C:\Users\ROG\Downloads\myproject
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Install Flask:

```bash
python -m pip install Flask
```

Run the Flask server on port 5002:

```bash
python -m flask --app food_api run -p 5002
```

If the server runs successfully, the terminal should show:

```text
Running on http://127.0.0.1:5002
```

The Flask terminal must stay open while testing the API.

## How to Expose the API with ngrok

Keep the Flask server running. Then open a second Command Prompt window and run:

```bash
ngrok http http://localhost:5002
```

ngrok will create a public forwarding URL, such as:

```text
https://upfront-snort-concur.ngrok-free.dev
```

This public URL can be used to access the local Flask API from outside the local machine. The ngrok terminal must stay open while testing the public API endpoint. If ngrok is restarted, the public URL may change.

## How to Test the API with Python Requests

Install the requests library:

```bash
python -m pip install requests
```

Run the test file:

```bash
python test_api.py
```

The script sends GET requests to the ngrok URL and prints the API responses.

Example testing code:

```python
import requests
import json

base_url = "https://upfront-snort-concur.ngrok-free.dev"

headers = {
    "ngrok-skip-browser-warning": "true"
}

endpoints = [
    ("Home", "/"),
    ("Metadata", "/api/metadata"),
    ("All foods", "/api/foods"),
    ("Safe foods", "/api/foods/safe"),
    ("Warning or under-review foods", "/api/foods/warnings"),
    ("Recall-related foods", "/api/foods/recalls"),
    ("Foods in Meat category", "/api/foods/category/Meat"),
    ("Foods inspected by FDA", "/api/foods/agency/FDA"),
    ("Search safe FDA foods", "/api/foods/search?status=Safe&agency=FDA"),
    ("Summary", "/api/foods/summary")
]

for label, endpoint in endpoints:
    url = base_url + endpoint
    response = requests.get(url, headers=headers)

    print("\n" + "=" * 50)
    print(label)
    print("Endpoint:", endpoint)
    print("Status Code:", response.status_code)

    try:
        data = response.json()
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print(response.text)
```

## Added Functions in This Version

This updated version adds several new functions beyond the original API assignment. The `/api/metadata` endpoint returns project metadata and record count. The `/api/foods/safe` endpoint returns only safe products. The `/api/foods/warnings` endpoint returns products that are marked as Warning or Under Review. The `/api/foods/recalls` endpoint returns records with recall-related or safety-review information. The category and agency endpoints allow users to retrieve products by food category or inspection agency. The search endpoint supports combined filtering with query parameters, and the summary endpoint returns simple counts for the whole dataset.

These added functions make the API more useful because users can retrieve desired data instead of only receiving the full information structure.

## Video Tutorial

Second video tutorial link:
https://drive.google.com/file/d/1BKPs6dJ9WncHZdyj48Aih2p5b4LcKDOW/view?usp=sharing
## Notes

The Flask server must be running before ngrok is started. The ngrok terminal must remain open because the public URL only works while the ngrok session is active. If the ngrok URL changes, the `base_url` in `test_api.py` and the ngrok examples in this README should be updated.

This project satisfies the assignment requirements by extending the previous individual API assignment, using sample data from the group project, loading a static JSON file when the server starts, adding additional Flask functions to return desired data, exposing the endpoint through ngrok, and demonstrating API access through Python `requests.get()`.
