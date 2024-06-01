import sys
import json
import yaml
import xmltodict

def parse_arguments():
    if len(sys.argv) != 3:
        print("Sposób użycia: program.py pathFile1.x pathFile2.y")
        print("gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).")
        sys.exit(1)
    path_file1 = sys.argv[1]
    path_file2 = sys.argv[2]
    format1 = sys.argv[1].split(".")[-1]
    format2 = sys.argv[2].split(".")[-1]
    if format1 not in ["xml", "json", "yml"] or format2 not in ["xml", "json", "yml"]:
        print("Nieprawidłowy format pliku. Obsługiwane formaty to .xml, .json i .yml (.yaml).")
        sys.exit(1)
    return path_file1, path_file2, format1, format2

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("JSON data loaded successfully")
        return data

    except Exception as e:
        print(f"Failed to load JSON file: {e}")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku JSON: {e}")

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie istnieje.")
        sys.exit(1)
    except yaml.YAMLError:
        print(f"Niewłaściwy format pliku YAML: '{file_path}'.")
        sys.exit(1)

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku YAML: {e}")

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data = xmltodict.parse(file.read())
            return data
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie istnieje.")
        sys.exit(1)
    except Exception as e:
        print(f"Niewłaściwy format pliku XML: '{file_path}': {e}")
        sys.exit(1)

def save_xml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            xml_str = xmltodict.unparse(data, pretty=True)
            file.write(xml_str)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku XML: {e}")

def convert_data(data, input_format, output_format):
    if input_format == output_format:
        return data

    if output_format == 'xml':
        return data

    return data

if __name__ == "__main__":
    path_file1, path_file2, format1, format2 = parse_arguments()

    if format1 == "json":
        data = load_json(path_file1)
    elif format1 == "yml":
        data = load_yaml(path_file1)
    elif format1 == "xml":
        data = load_xml(path_file1)

    converted_data = convert_data(data, format1, format2)

    if format2 == "json":
        save_json(converted_data, path_file2)
    elif format2 == "yml":
        save_yaml(converted_data, path_file2)
    elif format2 == "xml":
        save_xml(converted_data, path_file2)

    print(f"Dane przekonwertowane i zapisane do pliku: {path_file2}")
