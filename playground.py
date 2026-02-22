from app import db, Book, Reader, Review, Annotation
import app_data

db.session.delete(Reader.query.get(123)) #delete transaction

book_19 = Book.query.get(19)
book_19.month = "June"
db.session.commit()

#query all the readers from the Reader model
readers = Reader.query.all()
# print(readers) #all entries

reviews = Review.query.all()
# print(reviews) #all entries

#get an entry with id = 123 
# reader = Reader.query.get(123) #Fetching reader with id 123
# reviews_123 = reader.reviews.all() #Fetching reviews from this author
# print("GEt:",reader)
# print("GEt reviews relates reader(reviewer):",reviews_123)

""" Модификация строчек 10-12 """
# reviews_123 = Reader.query.get(123).reviews.all()

# review = Review.query.get(111)#fetching one review where id 111
# reviewer_111 = review.reviewer 
# book_111 = review.book
# print("Review",review,reviewer_111,book_111)

book_13 = Book.query.get(13).reviews.all() 
book_19_an = Book.query.get(19).annotations.all() 
author_331 = Annotation.query.get(331).author
adams =  Reader.query.filter(Reader.surname == 'Adams').all()
book_pre2019 = Book.query.filter(Book.year<=2019, Book.month == 'June').first()
s_name = Reader.query.filter(Reader.surname.endswith('s')).all()
sample_emails = Reader.query.filter(Reader.email.like('%@sample%')).all()
ordered_reviews = Review.query.order_by(Review.stars).all() #автр аннотации, реализация один к одному
# print("Book13 reviews for",Book.query.get(13).title+"\n",book_13)
# print("Book19 annotations for ",Book.query.get(19).title+"\n",book_19_an)
# print("annot 331",author_331.name,author_331.surname,Annotation.query.get(331).book.title)
# print("new",Book.query.get(13).reviews.first())
# print(adams)
# print(book_pre2019)
# print(ordered_reviews)


""" Модификация строчек 19-20 """
# reviewer_111 = Review.query.get(111).reviewer

book_1=Book.query.get(12)
reader = Reader.query.get(450)
# print("Reader with id = ", reader.id, "is called", reader.name)

#Loop through all the readers and print their e-mails
# print("\nPrint all the readers in a loop:")
#   print(reader.email)

# for review in reviews:
#   print(review.text)

#or inline
#[print(reader.email) for reader in readers]

# print("\nCheckpoint1: fetching all the reviews")
#reviews = 

# print("\nCheckpoint2: looping through all the reviews and printing their text")
#your loop line 1
#you loop line 2

# print("\nCheckpoint3: fetching a book with id = 13 using the get() function")
#book_1 = 


new_reader = Reader(name = "Peter", surname = "Johnson", email = "peter.johnson@example.com")
new_reader1 = Reader(name = "Nova", surname = "Yeni", email = "nova.yeni@sample.com")
new_reader2 = Reader(name = "Nova", surname = "Yuni", email = "nova.yeni@sample.com")
new_reader3 = Reader(name = "Tom", surname = "Grey", email = "tom.grey@example.edu")

print("Before addition: ")
for reader in Reader.query.all():
  print(reader.id, reader.email)

print("\nNote that before committing, the id of the new readers is: ", new_reader1.id, "\n")

db.session.add(new_reader)
try:
    db.session.commit()
except:
    db.session.rollback()


db.session.add(new_reader1)
try:
    db.session.commit()
    print("Commit succeded.", new_reader1, "added to the database permanently. The exception was not raised.\n")
except:
    db.session.rollback()

#adding the second reader - the commit should fail because e-mails should be unique
db.session.add(new_reader2)  
try:
    db.session.commit()
except Exception as ex:
    print("The commit of", new_reader2,"didn't succeed. Duplicate primary key values. We will empty the current session.\n")
    print("The error is the following:", ex)
    db.session.rollback() 

#adding the third reader - the commit should succeed
db.session.add(new_reader3)  
try:
    db.session.commit()
    print("Commit succeded.", new_reader3, "added to the database permanently. The exception was not raised.\n")
except Exception as ex:
    db.session.rollback() 

print("\nNote that after committing, the id of the new readers is now: ", new_reader1.id, "\n")

#print all the readers after the addition, and we see nova.yeni@sample.com there, but not twice
for reader in Reader.query.all():
  print(reader.id, reader.email)
print("\nThe new readers Nova Yeni and Tom Grey are in the database. Notice that Nova Yeni doesn't appear twice.\n")

print("\nCheckpoint 1: create a new_reader:")
#new_reader = 

print("\nCheckpoint 2: add the new reader to the database:")
#your code here

print("\nCheckpoint 3: commit and rollback if exception is raised:")
#try:
  #your code here
#except:
  #your code here

