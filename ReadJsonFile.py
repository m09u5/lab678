import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie istnieje.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Niewłaściwy format pliku JSON: '{file_path}'.")
        sys.exit(1)

if __name__ == "__main__":
    data = load_json(sys.argv[1])
    print("Dane wczytane z pliku JSON:", data)
