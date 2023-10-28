import json
import sys

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(tests, values):
    for test in tests:
        if 'values' in test:
            for value in test['values']:
                value_id = value['id']
                if value_id in values:
                    value['value'] = values[value_id]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task3.py tests.json values.json report.json")
    else:
        tests_file = sys.argv[1]
        values_file = sys.argv[2]

        tests_data = load_json_file(tests_file)
        values_data = load_json_file(values_file)

        fill_values(tests_data, values_data)

        with open('report.json', 'w') as report_file:
            json.dump(tests_data, report_file, indent=4)

