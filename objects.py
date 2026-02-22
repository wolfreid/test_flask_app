
#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) # book title
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) #author surname
    month = db.Column(db.String(20), index = True, unique = False) #the month of the book suggestion
    year = db.Column(db.Integer, index = True, unique = False) #the year of the book suggestion
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') #relationship of Books and Reviews with cascading delete 
    annotations = db.relationship('Annotation', backref='book', lazy='dynamic',cascade = "all, delete, delete-orphan")
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)

#Add your columns for the Reader model here below.
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic',cascade = "all,delete,delete-orphan")#реализация отношения один ко многим, backref - переменная идентификации задающего фильтр
    annotations = db.relationship('Annotation', backref='author', lazy='dynamic') #author - генеральная единица
    #get a nice printout for Reader objects
    def __repr__(self):
        return "Reader ID: {}, name:{} email: {}".format(self.id,self.surname, self.email)

#declaring the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    #get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)

#declaring the Annotation model
class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200), unique = False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    #get a nice printout for Annotation objects
    def __repr__(self):
        return '<Annotation {}-{}:{} >'.format(self.reviewer_id, self.book_id, self.text)

#some routing for displaying the home page
import routes
