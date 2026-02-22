from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timezone


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testapp2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    """Book model for storing book information."""
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), index=True, unique=True, nullable=False)
    author_name = db.Column(db.String(50), index=True, nullable=False)
    author_surname = db.Column(db.String(80), index=True, nullable=False)
    month = db.Column(db.String(20), index=True)
    year = db.Column(db.Integer, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # Relationships
    reviews = db.relationship('Review', backref='book', lazy='dynamic', cascade='all, delete-orphan')
    annotations = db.relationship('Annotation', backref='book', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Book "{self.title}" by {self.author_name} {self.author_surname} ({self.month} {self.year})>'
    
    @property
    def full_author_name(self):
        """Return the full author name."""
        return f'{self.author_name} {self.author_surname}'
    
    @property
    def average_rating(self):
        """Calculate the average rating for this book."""
        reviews = self.reviews.filter(Review.stars.isnot(None)).all()
        if not reviews:
            return None
        return sum(review.stars for review in reviews) / len(reviews)

class Reader(db.Model):
    """Reader model for storing reader information."""
    __tablename__ = 'readers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False)
    surname = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # Relationships
    reviews = db.relationship('Review', backref='reviewer', lazy='dynamic', cascade='all, delete-orphan')
    annotations = db.relationship('Annotation', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return f'<Reader {self.full_name} ({self.email})>'
    
    @property
    def full_name(self):
        """Return the full name of the reader."""
        return f'{self.name} {self.surname}'
    
    def get_reviews_count(self):
        """Return the number of reviews written by this reader."""
        return self.reviews.count()

class Review(db.Model):
    """Review model for storing book reviews."""
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # Foreign Keys
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('readers.id'), nullable=False)
    
    def __repr__(self):
        return f'<Review: {self.stars} stars - "{self.text[:50]}...">'
    
    def __init__(self, stars, text, book_id, reviewer_id):
        if not 1 <= stars <= 5:
            raise ValueError("Stars must be between 1 and 5")
        self.stars = stars
        self.text = text
        self.book_id = book_id
        self.reviewer_id = reviewer_id

class Annotation(db.Model):
    """Annotation model for storing reader annotations on books."""
    __tablename__ = 'annotations'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    page_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    # Foreign Keys
    reviewer_id = db.Column(db.Integer, db.ForeignKey('readers.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    
    def __repr__(self):
        return f'<Annotation by Reader {self.reviewer_id} on Book {self.book_id}: "{self.text[:30]}...">'
    
    def __init__(self, text, reviewer_id, book_id, page_number=None):
        self.text = text
        self.reviewer_id = reviewer_id
        self.book_id = book_id
        self.page_number = page_number



with app.app_context():
    db.create_all()
    
#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just initialized your database!"
