# Test Flask App - Refactored Book Review Platform

A refactored Flask web application for managing books, readers, and reviews. This application demonstrates best practices for Flask development with proper separation of concerns, application factory pattern, and clean code organization.

## Features

- **Book Management**: Add and view books with author information
- **User Profiles**: Reader profiles with review history
- **Review System**: Star ratings and text reviews for books
- **Annotations**: Reader annotations on specific books
- **Responsive Design**: Clean HTML templates with CSS styling

## Architecture

The application follows Flask best practices with:

- **Application Factory Pattern**: Clean app initialization
- **Separation of Concerns**: Models, routes, and configuration in separate modules
- **Environment-based Configuration**: Development, testing, and production configs
- **CLI Commands**: Database management through Flask CLI
- **Error Handling**: Proper HTTP error responses
- **Database Relationships**: One-to-many and foreign key relationships

## Project Structure

```
test_flask_app/
├── app.py              # Application factory and main entry point
├── models.py           # Database models (Book, Reader, Review, Annotation)
├── routes.py           # Application routes and views
├── config.py           # Configuration classes for different environments
├── cli.py              # CLI commands for database management
├── app_data.py         # Database seeding utilities
├── requirements.txt    # Python dependencies
├── .env.template      # Environment variables template
├── static/
│   └── css/
│       └── style.css
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   ├── profile.html
│   └── ...
└── tests/             # Test suite
    └── test_app.py
```

## Setup and Installation

### 1. Clone and Navigate
```bash
cd test_flask_app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```
**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Configuration
```bash
cp .env.template .env
# Edit .env file with your configuration
```

### 6. Initialize Database
```bash
flask init-db
flask seed-db
```

## Usage

### Running the Application
```bash
# Development mode
python app.py

# Or using Flask CLI
flask run

# Production mode with Gunicorn
gunicorn --bind 0.0.0.0:8000 app:app
```

### Database Management
```bash
flask init-db      # Initialize empty database
flask seed-db      # Populate with sample data
flask reset-db     # Drop and recreate all tables
```

### Running Tests
```bash
python -m pytest tests/
```

## API Endpoints

- `GET /` - Home page with book listing
- `GET /profile/<user_id>` - User profile page
- `GET /books/<year>` - Books filtered by publication year
- `GET /books` - All books with pagination
- `GET /book/<book_id>` - Individual book details
- `GET /reviews/<review_id>` - Individual review details

## Database Models

### Book
- Title, author name/surname, publication month/year
- Relationships to reviews and annotations
- Properties: `full_author_name`, `average_rating`

### Reader
- Name, surname, email
- Relationships to reviews and annotations
- Properties: `full_name`, review count method

### Review
- Star rating (1-5), review text, timestamps
- Foreign keys to Book and Reader
- Validation for star ratings

### Annotation
- Text annotation, optional page number
- Foreign keys to Book and Reader
- Timestamps for creation

## Configuration

The application supports multiple environments:

- **Development**: Debug enabled, SQL echo, SQLite database
- **Testing**: In-memory SQLite, CSRF disabled
- **Production**: Debug disabled, logging configured

Set the environment using:
```bash
export FLASK_CONFIG=production  # Linux/macOS
set FLASK_CONFIG=production     # Windows
```

## Deployment

### Using Gunicorn (Production)
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 app:app
```

### Using Docker
```bash
# Create Dockerfile in project root
docker build -t test-flask-app .
docker run -p 8000:8000 test-flask-app
```

## Contributing

1. Follow PEP 8 style guidelines
2. Add tests for new features
3. Update this README for significant changes
4. Use meaningful commit messages

## Dependencies

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Gunicorn**: WSGI HTTP Server
- **python-dotenv**: Environment variable loading
- **pytest**: Testing framework

## License

This project is for educational purposes.