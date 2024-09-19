# Initial data
books = (
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("1984", "George Orwell", 1949),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
)
tags = {"classic", "dystopian", "novel", "literature"}

# a. Access the second book's author from the books tuple and print it
second_book_author = books[1][1] 
print("Author of the second book:", second_book_author)

# b. Add a new record for the book "Brave New World" by Aldous Huxley, published in 1932
new_book = ("Brave New World", "Aldous Huxley", 1932)
books = books + (new_book,)
print("\nUpdated books tuple:")
print(books)

# c. Unpack the details of the third book into separate variables and print them
title, author, year = books[2]  
print(f"\nThird book details:\nTitle: {title}\nAuthor: {author}\nYear: {year}")

# d. Loop through the books tuple and print each book's title
print("\nBook Titles:")
for book in books:
    print(book[0]) 
    
# e. Add a new tag "sci-fi" to the tags set and print the updated set
tags.add("sci-fi")
print("\nUpdated tags set after adding 'sci-fi':")
print(tags)

# f. Use a method to remove the tag "novel" from the tags set and print the updated set
tags.discard("novel")  
print("\nUpdated tags set after removing 'novel':")
print(tags)
