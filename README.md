# Library Management System

A small command-line program for managing a book list stored in a CSV file. It lets you add, search, list, update, and delete books, as well as find books up to a chosen price. Please note it is my initial stage project only for python practice purposes.

## Requirements

- Python 3
- `python-dotenv`

Install the dependency with:

```bash
python -m pip install python-dotenv
```

## Setup

The application reads the CSV file path from the `FILE` environment variable, loaded from a `.env` file. In the project directory, create or update `.env` with:

```dotenv
FILE=Library.csv
```

The CSV file must have `book` and `price` columns, for example:

```csv
book,price
The Hobbit,500
```

Keep the `.env` file and the CSV file in the project directory when using the relative path shown above.

## Run

Open a terminal in the project directory and run:

```bash
python code.py
```

Choose an option from the menu:

1. **Add book** — add a book with a positive whole-number price.
2. **Search book** — look up a book by name.
3. **See all books** — list books in ascending or descending alphabetical order and show the total.
4. **Update price** — set a book's price to a positive whole number.
5. **Delete book** — remove a book by name.
6. **Search by price** — show books priced at or below the entered amount.
7. **Exit** — close the program.

Book-name matching is case-insensitive. Changes are saved to the CSV file.
