"""Database seeding module for populating the database with sample data."""

import os
from app import create_app, db
from models import Book, Reader, Review, Annotation

def clear_database():
    """Clear all existing data from the database."""
    print("Clearing existing database data...")
    db.drop_all()
    db.create_all()

def create_sample_readers():
    """Create sample reader data."""
    print("Creating sample readers...")
    readers = [
        Reader(id=123, name='Ann', surname='Adams', email='ann_adams@example.com'),
        Reader(id=345, name='Sam', surname='Adams', email='sam.adams@example.edu'),
        Reader(id=450, name='Kim', surname='Smalls', email='kim_smalls@example.com'),
        Reader(id=568, name='Sam', surname='Smalls', email='sam.smalls@example.com'),
        Reader(id=753, name='Tom', surname='Fox', email='tom.fox@sample.edu'),
        Reader(id=653, name='Earl', surname='Grey', email='earl.grey@sample.com')
    ]
    
    for reader in readers:
        db.session.add(reader)
    
    return readers

def create_sample_books():
    """Create sample book data."""
    print("Creating sample books...")
    books = [
        Book(id=12, title='Hundred Years of Solitude', author_name='Gabriel', 
             author_surname='García Márquez', month='April', year=2020),
        Book(id=13, title='The Stranger', author_name='Albert', 
             author_surname='Camus', month='May', year=2020),
        Book(id=14, title='The Book of Why', author_name='Judea', 
             author_surname='Pearl', month='September', year=2019),
        Book(id=18, title='Demian', author_name='Hermann', 
             author_surname='Hesse', month='June', year=2018),
        Book(id=19, title='Guns, Germs and Steel', author_name='Jared', 
             author_surname='Diamond', month='August', year=2019)
    ]
    
    for book in books:
        db.session.add(book)
    
    return books

def create_sample_reviews(readers, books):
    """Create sample review data."""
    print("Creating sample reviews...")
    reviews = [
        Review(stars=5, text='This book is amazing...', book_id=books[0].id, reviewer_id=readers[0].id),
        Review(stars=3, text='The story is hard to follow.', book_id=books[0].id, reviewer_id=readers[1].id),
        Review(stars=2, text='The story is quite complicated.', book_id=books[1].id, reviewer_id=readers[0].id),
        Review(stars=4, text='Albert Camus is an amazing writer who really understands society.', 
               book_id=books[1].id, reviewer_id=readers[1].id),
        Review(stars=4, text='The book is simply written and a rather quick read, but the depth Camus manages to convey through this simplicity is astounding.', 
               book_id=books[1].id, reviewer_id=readers[1].id),
        Review(stars=3, text='Despite the fascinating subject matter I found this book a bit dry.', 
               book_id=books[4].id, reviewer_id=readers[3].id),
        Review(stars=5, text='I liked this book, and it taught me a bunch of things.', 
               book_id=books[4].id, reviewer_id=readers[2].id),
        Review(stars=4, text='Not bad.', book_id=books[0].id, reviewer_id=readers[4].id),
        Review(stars=3, text='Could not finish the book.', book_id=books[3].id, reviewer_id=readers[4].id)
    ]
    
    for review in reviews:
        db.session.add(review)
    
    return reviews

def create_sample_annotations(readers, books):
    """Create sample annotation data."""
    print("Creating sample annotations...")
    annotations = [
        Annotation(text='Human history is a function of geography.', 
                  reviewer_id=readers[3].id, book_id=books[4].id, page_number=45),
        Annotation(text='I opened myself to the gentle indifference of the world.', 
                  reviewer_id=readers[0].id, book_id=books[1].id, page_number=122),
        Annotation(text='Everything is true, and nothing is true!', 
                  reviewer_id=readers[1].id, book_id=books[1].id, page_number=89),
        Annotation(text='Good that you ask -- you should always ask, always have doubts.', 
                  reviewer_id=readers[2].id, book_id=books[3].id, page_number=67)
    ]
    
    for annotation in annotations:
        db.session.add(annotation)
    
    return annotations

def seed_database():
    """Main function to seed the database with sample data."""
    try:
        # Clear existing data
        clear_database()
        
        # Create sample data
        readers = create_sample_readers()
        db.session.commit()
        
        books = create_sample_books()
        db.session.commit()
        
        reviews = create_sample_reviews(readers, books)
        db.session.commit()
        
        annotations = create_sample_annotations(readers, books)
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(readers)} readers, {len(books)} books, {len(reviews)} reviews, and {len(annotations)} annotations.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.session.rollback()
        raise
    finally:
        db.session.close()

if __name__ == '__main__':
    # Create app context for database operations
    app = create_app()
    with app.app_context():
        seed_database()

