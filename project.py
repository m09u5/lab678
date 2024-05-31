import sys

def parse_arguments():

    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
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

if __name__ == "__main__":
    path_file1, path_file2, format1, format2 = parse_arguments()
    print("Scieżka pliku wejściowego:", path_file1)
    print("Scieżka pliku wyjściowego:", path_file2)
    print("Format pliku wejściowego:", format1)
    print("Format pliku wyjściowego:", format2)

    