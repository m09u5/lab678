import sys
import xmltodict

def load_xml(file_path):
    try:
        with open(file_path, 'r') as file:
            data=xmltodict.parse(file.read())
            return data
    except FileNotFoundError:
        print(f"Plik '{file_path}' nie istnieje.")
        sys.exit(1)
    except xmltodict.ParseError:
        print(f"Niewłaściwy format pliku XML: '{file_path}'.")
        sys.exit(1)

if __name__ == "__main__":
    root = load_xml(sys.argv[1])
    print("Dane wczytane z pliku XML:", root)
