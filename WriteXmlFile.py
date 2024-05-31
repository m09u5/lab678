import xmltodict
import sys
import xml.etree.ElementTree as ET

def save_xml(data, file_path):
    try:
        root = ET.Element("persons")
        for name, info in data.items():
            person=ET.SubElement(root, "person")
            ET.SubElement(person, "name").text = name
            for key, value in info.items():
                ET.SubElement(person, key).text = str(value)
        tree=ET.ElementTree(root)
        tree.write(file_path)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku XML: {e}")

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
        'maritalStatus': 'Married'
    },
    'Torba': {
        'age': 45,
        'favoriteFood': 'Burger',
        'maritalStatus': 'Widowed',
        'location': 'Kamien Pomorski'
    }
}
    save_xml(data, sys.argv[1])
    print(f"Dane zapisane do pliku XML: {sys.argv[1]}")
