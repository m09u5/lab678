import sys
import yaml

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku YAML: {e}")

if __name__ == "__main__":
    data = {
    'Doris': {
        'age': 30,
        'favoriteFood': 'Pizza',
        'maritalStatus': 'Married',
        'location': 'Lesna'
    },
    'Malwa': {
        'age': 25,
        'favoriteFood': 'Pasta',
        'maritalStatus': 'Single'
    },
    'Sylwia': {
        'age': 33,
        'favoriteFood': 'Salad',
        'maritalStatus': 'Divorced'
    },
    'Woj': {
        'age': 40,
        'favoriteFood': 'Steak',
        'maritalStatus': 'Married'
    },
    'Marek': {
        'age': 35,
        'favoriteFood': 'Fish',
        'maritalStatus': 'Single'
    },
    'Ewka': {
        'age': 28,
        'favoriteFood': 'Chicken',
    }
}
    save_yaml(data, sys.argv[1])
    print(f"Dane zapisane do pliku YAML: {sys.argv[1]}")
