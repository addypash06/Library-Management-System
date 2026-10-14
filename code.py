import csv
from dotenv import load_dotenv
import os

load_dotenv()
FILE = os.getenv("FILE")
 
def read_books():
    with open(FILE) as file:
        return list(csv.DictReader(file))
 
def save_books(books):
    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["book", "price"])
        writer.writeheader()
        writer.writerows(books)
 
def show(books):
    for each_book in books:
        print(f"{each_book['book']} --> ₹{each_book['price']}")
 
while True:
    print()
    menu = input(
        "1. Add book\n2. Search book\n3. See all books\n4. Update price\n"
        "5. Delete book\n6. Search by price\n7. Exit\n\t"
    ).lower()
 
    if menu in ["1", "add book"]:
        book_name = input("Enter the book name: ").lower()
        books = read_books()
 
        if book_name in [each_book["book"].lower() for each_book in books]:
            print("Book already exists!")
            continue
 
        book_price = int(input("Enter the book price: "))
        if book_price > 0:
            with open(FILE, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["book", "price"])
                writer.writerow({"book": book_name, "price": book_price})
        else:
            print("Book price should be greater than zero!")
 
    elif menu in ["2", "search book"]:
        books = read_books()
        if not books:
            print("The file is empty")
            continue
 
        book_search = input("Enter book name to be searched: ").lower()
        found = False
        for each_book in books:
            if book_search == each_book["book"].lower():
                print(f"{each_book['book']} --> ₹{each_book['price']}")
                found = True
 
        if not found:
            print("Book not found!")
 
    elif menu in ["3", "see all books"]:
        books = read_books()
        if not books:
            print("The file is empty")
            continue
 
        order = input("1. A → Z\n2. Z → A\n\t")
        if order == "2":
            books = sorted(books, key=lambda book: book["book"], reverse=True)
        else:
            books = sorted(books, key=lambda book: book["book"])
 
        show(books)
        print(f"\nTotal books: {len(books)}")
 
    elif menu in ["4", "update price"]:
        books = read_books()
        book_name = input("Enter the book name to update: ").lower()
 
        found = False
        for each_book in books:
            if each_book["book"].lower() == book_name:
                new_price = int(input("Enter the new price: "))
                if new_price > 0:
                    each_book["price"] = new_price
                    save_books(books)
                    print("Price updated!")
                else:
                    print("Book price should be greater than zero!")
                found = True
                break
 
        if not found:
            print("Book not found!")
 
    elif menu in ["5", "delete book"]:
        books = read_books()
        book_name = input("Enter the book name to delete: ").lower()
 
        # keep every book except the one we want to delete
        remaining = [each_book for each_book in books if each_book["book"].lower() != book_name]
 
        if len(remaining) == len(books):
            print("Book not found!")
        else:
            save_books(remaining)
            print("Book deleted!")
 
    elif menu in ["6", "search by price"]:
        books = read_books()
        max_price = int(input("Show books priced up to: ₹"))
 
        cheap_books = [each_book for each_book in books if int(each_book["price"]) <= max_price]
 
        if cheap_books:
            show(cheap_books)
        else:
            print("No books found in this price range!")
 
    elif menu in ["7", "exit"]:
        print("Exited successfully!")
        break

#   PSEUDOCODE

"""
menu: 1. Show all books, 2. Add books, 3. Search book

if show all books:
    with openfunction opening file:
        reader = csv.dictreader
        for loop:
            print(books : price)

if add book:
    input of name of book
    input of price of book
    with openfunction opening file:
        writer = csv,dictwriter
        writerow({"book":book, "price":price})

if search book:
    input of name of book:
    with openfunction opening file:
        reader ....
        for loop reader:
            if search book == each line[book name]
            print book with price

if exit:
    exit the programn
    

"""