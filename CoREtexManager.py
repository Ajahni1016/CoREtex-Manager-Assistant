import json

bookCount = -1
books = []


"""
Given the file location of a JSON file, parseJSON(file) loads the JSON data and stores
it in a global array named books.
"""
def parseJSON(file):
    global books
    global bookCount

    f = open(file)

    data = json.load(f)

    for i in data:
        books.append(i)
        bookCount += 1

    books.pop()

    f.close()


"""
Given a book object, printbook(b) prints out the metadata of a given book in the following format:

Gift of Fire
By: George Foreman
ISBN: 134-54-6464
Genre: English
Currently Available

Intro to Javascript
By: Cassidy Smith
ISBN: 457-14-8261
Genre: CS
Borrowed by Gavin
"""
def printBook(b):
    if b["Title"]!=None:
        print(b["Title"])
    if b["Author"]!=None:
        print("By: ",b["Author"])
    if b["ISBN"]!=None:
        print("ISBN: ",b["ISBN"])
    if b["Genre"]!=None:
        print("Genre: ",b["Genre"])
    if b["Rented "]!=None:
        print("Borrowed by ",b["Rented "],"\n")
    else:
        print("Currently Available\n")


"""
searchBooks(y) goes through every book in the JSON file and checks if there
is a partial match for the title, author, or ISBN. (Not case sensitive)
"""
def searchBooks():
    y = input("\n*You can search by title, author, or ISBN*\nEnter a search term: ")
    count = 0
    print('\n')

    for i in books:
        if i["Title"]!=None and y.lower() in i['Title'].lower():
            count+=1
            printBook(i)
        elif i["Author"]!=None and y.lower() in i['Author'].lower():
            count+=1
            printBook(i)
        elif i["ISBN"]!=None and y.replace('-', '').replace(' ', '') in i['ISBN'].replace('-', '').replace(' ', ''): #Removes white space and hyphens
            count+=1
            printBook(i)

    print("\n",count,"result(s) found.")
    enter = input("Press enter to continue...")



"""
showGenre() displays a list of all books of a chosen genre.
Displays a numbered list of all available genres that can be chosen from.
User can type in the genre name or its corresponding number.
"""
def showGenre():
    genre = input("\nAvailable genres:\n1 - Mathematics\n2 - Computer Science\n3 - Writing\n4 - Science Fiction\n5 - Poetry and Folktales\n6 - Politics\n7 - History\n8 - Art and Music\n9 - Anthropology and Archaeology\n10 - Physics\n11 - Biology & Earth Science\n12 - Chemistry\n13 - Astronomy\n14 - Engineering\n\nWhat genre would you like to view?: ")
    print('\n')

    if(genre.strip() == "1"):
        genre = 'Mathematics'
    elif(genre.strip() == '2'):
        genre = "Computer Science"
    elif(genre.strip() == '3'):
        genre = "Writing"
    elif(genre.strip() == '4'):
        genre = "Science Fiction"
    elif(genre.strip() == '5'):
        genre = "Poetry and Folktales"
    elif(genre.strip() == '6'):
        genre = "Politics"
    elif(genre.strip() == '7'):
        genre = "History"
    elif(genre.strip() == '8'):
        genre = "Art and Music"
    elif(genre.strip() == '9'):
        genre = "Anthropology and Archaeology"
    elif(genre.strip() == '10'):
        genre = "Physics"
    elif(genre.strip() == '11'):
        genre = "Biology & Earth Science"
    elif(genre.strip() == '12'):
        genre = "Chemistry"
    elif(genre.strip() == '13'):
        genre = "Astronomy"
    elif(genre.strip() == '13'):
        genre = "Engineering"

    count = 0
    for b in books:
        if(b["Genre"]!=None and b["Genre"].lower()==genre.lower()):
            count+=1
            printBook(b)

    print("\n",count,"result(s) found.")
    enter = input("Press enter to continue...")


"""
viewAllBooks() displays a list of every book currently in the CoRE Library
"""
def viewAllBooks():
    print('\n')

    count=0
    for b in books:
        printBook(b)
        count += 1

    print("\n",count,"result(s) found.")
    enter = input("Press enter to continue...")



def main():
    parseJSON('coretexBooks.json')
    print("\nWelcome to the CoREtex Manager Assistant. There are currently",bookCount,"books in the CoREtex.\n")
    running = 1

    while running == 1:
        print("\n===========================================================================================\n\n1 - Search for a book\n2 - View books by genre\n3 - View all books\n4 - Exit\n")

        x = input("What would you like to do today? ")
        if(x.strip()=='1'):
            searchBooks()
        if(x.strip()=='2'):
            showGenre()
        if(x.strip()=='3'):
            viewAllBooks()
        if(x.strip()=='4'):
            running = 0
        # else:
        #     print("\nInvalid input. Pleese enter a number from 1 - 4\n")



main()
