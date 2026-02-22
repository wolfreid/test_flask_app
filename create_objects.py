#This is a separate Python script in which we practice creating database objects
#You can also perform these operations in command-line terminal
from objects import Reader, Book, Review

b1 = Book(id = 123, title = 'Demian', author_name = 'Hermann', author_surname = 'Hesse', month = 'February', year = 2020)
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')
b2 = Book(id = 533, title = 'The Stranger', author_name ='Albert', author_surname = 'Camus', month = 'April',year = 2019)
r2 = Reader(id = 765, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')

rev1 = Review(id = 435, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
rev2 = Review(id = 450, text = 'This book is difficult!',stars = 2, reviewer_id = r2.id,book_id = b2.id)
print(b2.author_surname)
print(len(rev2.text.split()))

#Checkpoint 1: 

#Checkpoint 2: 

#Checkpoint 3: 

#Checkpoint 4: