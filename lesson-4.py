import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Load the data from the file
def load_data():
    with open('lesson-4.json') as f:
        data = json.load(f)
    return data

print(json.loads(json_string))