import csv


def find_books(from_year, to_year):
    found_books = []
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            for year in range(from_year, to_year + 1):
                year = str(year)
                if year == row["Year of release"]:
                    found_books.append(row)
    if not found_books:
        print("Таких книг нет!\n")
    else:
        print("Книги из заданного диапазона годов:")
        for row in found_books:
            print(row["Book"], "|", row["Author"], "|", row["Year of release"])


try:
    from_year, to_year = int(input("Введите первый год: ")), int(input("Введите конечный год: "))
    print("")
    find_books(from_year, to_year)
except ValueError:
    print("Введено не число!")
