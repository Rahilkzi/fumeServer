import json

json_file_path = "E:\\PRACTICAL\\Semester 6\\Data Science\\Data\\Crescent.JSON"

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

try:
    json_data = read_json_file(json_file_path)
    print("JSON Data:")
    print(json.dumps(json_data, indent=2))
except FileNotFoundError:
    print(f"Error: File not found at path '{json_file_path}'")
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in file at path '{json_file_path}'")
