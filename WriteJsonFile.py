import json
import sys


def save_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku JSON: {e}")

if __name__ == "__main__":
    data={
    "Doris": {
        "age": 30,
        "favoriteFood": "Pizza"
    },
    "Malwa": {
        "age": 25,
        "favoriteFood": "Pasta"
    },
    "Mei": {
        "age": 35,
        "favoriteFood": "Sushi"
    }
}
    save_json(data, sys.argv[1])
    print(f"Dane zapisane do pliku JSON: {sys.argv[1]}")
