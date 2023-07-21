import csv

books = [("Book", "Author", "Year of release"),
         ["Crime and Punishment", "Fyodor Dostoevsky", "1866"],
         ["Six of Crows", "Bardugo Leigh", "2018"],
         ["Misery", "Stephen King", "1987"],
         ["Three Comrades", "Remarque Erich Maria", "1936"],
         ["A Thousand Boy Kisses", "Tillie Cole", "2016"]]

with open("books.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(books)
