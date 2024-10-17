# import json
import re
# json_string = '{"name": "John", "age": 30, "city": "New York"}'

# # Load the data from the file
# def load_data():
#     with open('lesson-4.json') as f:
#         data = json.load(f)
#     return data

# print(json.loads(json_string))

# print(b'\xe2\x93\xb4'.decode("utf-8"))

a = "240,00"
b = "2,240"
print(re.sub(r"(\d\d+),(\d+)", r"\1.\2", a))

