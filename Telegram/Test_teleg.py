import json

info, item_category, item_discr, when, where = ["57660", "Техника", "Телефон", "24.07.2005", "туалет"]

# Step 1: Read the existing JSON data from the file
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Step 2: Modify the Python object (add new data)
new_data = {
    "info": info,
    "category": item_category,
    "discryption": item_discr,
    "where": where,
    "when": when
}

# Check if data is a list, if not create a new list with existing data
if not isinstance(data, list):
    data = [data]

# Append the new data to the existing list
data.append(new_data)

# Step 3: Write the updated Python object back to the JSON file
with open("data.json", "w", encoding="utf-8") as file:
    # Write the JSON data to the file
    json.dump(data, file, ensure_ascii=False)
