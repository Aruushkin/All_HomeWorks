class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


kniga = Book('book', "stiv", 2022)

print(kniga.title, kniga.author, kniga.year)

