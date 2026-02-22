from flask import render_template, request, url_for, redirect, abort
from models import Book, Reader, Review, Annotation

def register_routes(app):
    """Register all application routes."""
    
    @app.route('/')
    @app.route('/home')
    def home():
        """Home page displaying all books."""
        books = Book.query.all()
        return render_template('home.html', books=books)
    
    @app.route('/profile/<int:user_id>')
    def profile(user_id):
        """User profile page."""
        reader = Reader.query.filter_by(id=user_id).first()
        if not reader:
            abort(404, description="There is no user with this ID.")
        return render_template('profile.html', reader=reader)
    
    @app.route('/books/<int:year>')
    def books_by_year(year):
        """Display books filtered by year."""
        books = Book.query.filter_by(year=year).all()
        return render_template('display_books.html', year=year, books=books)
    
    @app.route('/reviews/<int:review_id>')
    def review_detail(review_id):
        """Display a specific review."""
        review = Review.query.filter_by(id=review_id).first()
        if not review:
            abort(404, description="Review not found.")
        return render_template('_review.html', review=review)
    
    @app.route('/books')
    def all_books():
        """Display all books with pagination."""
        page = request.args.get('page', 1, type=int)
        books = Book.query.paginate(page=page, per_page=10, error_out=False)
        return render_template('display_books.html', books=books)
    
    @app.route('/book/<int:book_id>')
    def book_detail(book_id):
        """Display detailed information about a book."""
        book = Book.query.filter_by(id=book_id).first()
        if not book:
            abort(404, description="Book not found.")
        reviews = book.reviews.all()
        return render_template('book_detail.html', book=book, reviews=reviews)