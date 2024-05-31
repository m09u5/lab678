import yaml
import sys

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

if __name__ == "__main__":
    data = load_yaml(sys.argv[1])
    print("Dane wczytane z pliku YAML:", data)
