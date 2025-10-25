book_authors = {
    'Winnie the pooh': 'A. A. Milne',
    'The tale of peter rabbit': 'Beatrix Potter',
    'The wind in the willows': 'Kenneth Grahame',
    'The lion, the witch and the wardrobe': 'C. S. Lewis',
    'Charlie and the chocolate factory': 'Roald Dahl'
}

book = input('Please enter the title of a book: ')
add = input("Would you like to add a book> Y or N: ")
amend = input("Would you like to change the author of a book? Y or N: ")
#task 3.1
book = book[0].upper() + book[1:]

#task 3.2
author_wanted = input("Enter the book you want the author of: ")
print(f"{book_authors[author_wanted]} is the author of {author_wanted}")

# task 3.3
if add.upper() == "Y":
    book_to_be_added = input("Enter the book you want to be added. ")
    author_to_be_added = input("Enter the author of the book to be added")
    book_authors[book_to_be_added] = author_to_be_added
print(book_authors)

#task 3.4

if amend.upper() == "Y": 
    book_to_amend = input("Enter the book to amend. ")
    while True:
        gotnum = False
        new_author = input("Enter the new author")
        for i in new_author:
            if i.isdigit():
                gotnum = True
                break
            
        if gotnum == False:
            break
            
book_authors[book_to_amend] = new_author