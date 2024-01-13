import os, re
import random

class Books:
    def count_words(genre):
        total_words = 0
        genre_list = []
        for i in gen:
            if (i == "+"):
                word_list = genre.split("+")
            else:
                word_list = genre.split()
        for word in word_list:
            if word.lower() not in ["and", ",", "+"]:
                total_words += 1
                genre_list.append(word.lower())
        return total_words, genre_list

    def any_year(file_path, genre_list):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    Genre_File = f"Books/{line.strip()}.txt"
                    Genre_path = os.path.join(os.path.dirname(__file__), Genre_File)
                    try:
                        with open(Genre_path, 'r') as file:
                            lines = file.readlines()
                            ind = random.randint(0, 12)
                            for i in range(ind):
                                index = random.randint(0, 50)
                                random_line = lines[index]            
                                print(random_line.strip())                      
                    except FileNotFoundError:
                        print(f"File not found for genre: {line.strip()}")

class Movies:
    def count_words(genre):
        total_words = 0
        genre_list = []
        for i in genre:
            if (i == "+"):
                word_list = genre.split("+")
            else:
                word_list = genre.split()
        for word in word_list:
            if word.lower() not in ["and", "+", ","]:
                total_words += 1
                genre_list.append(word.lower())
        return total_words, genre_list

    def any_year(file_path, genre_list):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    Genre_File = f"Movies/{line.strip()}.txt"
                    Genre_path = os.path.join(os.path.dirname(__file__), Genre_File)
                    try:
                        with open(Genre_path, 'r') as file:
                            for l in file:
                                print(l.strip())
                                print("\n")                      
                    except FileNotFoundError:
                        print(f"Try another genre: {line.strip()}")

    def one_year(file_path, genre_list, year):
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() in genre_list:
                    Genre_File = f"Movies/{line.strip()}.txt"
                    Genre_path = os.path.join(os.path.dirname(__file__), Genre_File)
                    try:
                        with open(Genre_path, 'r') as file:
                            for l in file:
                                y = [char for char in l if char.isdigit()]
                                result = ''.join(y)
                                if int(result) >= int(year) and int(result) < (int(year)+10):
                                    print(l.strip())
                                else:
                                    y = []
                            print("\n")                      
                    except FileNotFoundError:
                        print(f"Try another genre: {line.strip()}")

def Book():
    GenreFile = "GenreBook.txt"
    Genrepath = os.path.join(os.path.dirname(__file__), GenreFile)

    gen = input("Enter the genres of Books do you wish to read?\n")
    gen = gen.replace(", ", " ")
    total_words, genre_list = Books.count_words(gen) 

    Books.any_year(Genrepath, genre_list)

def Movie():
    GenreFile = "Genre.txt"
    Genrepath = os.path.join(os.path.dirname(__file__), GenreFile)

    gen = input("Enter the genres of the movie you feel like watching?\n")
    gen = gen.replace(", ", " ")
    total_words, genre_list = Movies.count_words(gen) 

    year = input("Enter the era of the movie you want to watch(Ex: 2010s)\n")

    if  (year.lower() == "any" or year.lower() == "any year" or year.lower() == "any era"):
        Movies.any_year(Genrepath, genre_list)

    elif len(year) == 4 or len(year) == 5:
        year = ''.join(re.findall(r'\d', year))
        Movies.one_year(Genrepath, genre_list, year)
    
BM = input("""\nWelcome to Book and Movie Reccomendation!
Do you want to read a BOOK or watch a MOVIE\n""")
BM = BM.lower()

if "books" in BM or "book" in BM:
    Book()

elif "movies" in BM or "movie" in BM:
    Movie()