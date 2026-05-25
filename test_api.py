import requests

base_url = "https://upfront-snort-concur.ngrok-free.dev"

print("Home:")
print(requests.get(base_url + "/").text)

print("\nMetadata:")
print(requests.get(base_url + "/api/metadata").json())

print("\nAll foods:")
print(requests.get(base_url + "/api/foods").json())

print("\nSafe foods:")
print(requests.get(base_url + "/api/foods/safe").json())

print("\nWarning or under-review foods:")
print(requests.get(base_url + "/api/foods/warnings").json())

print("\nRecall-related foods:")
print(requests.get(base_url + "/api/foods/recalls").json())

print("\nFoods in Meat category:")
print(requests.get(base_url + "/api/foods/category/Meat").json())

print("\nFoods inspected by FDA:")
print(requests.get(base_url + "/api/foods/agency/FDA").json())

print("\nSearch safe FDA foods:")
print(requests.get(base_url + "/api/foods/search?status=Safe&agency=FDA").json())

print("\nSummary:")
print(requests.get(base_url + "/api/foods/summary").json())