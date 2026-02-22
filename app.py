import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Initialize extensions
db = SQLAlchemy()

def create_app(config_name=None):
    """Application factory pattern for creating Flask app instances."""
    app = Flask(__name__)
    
    # Determine configuration
    config_name = config_name or os.environ.get('FLASK_CONFIG', 'default')
    
    # Configure the app
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Initialize extensions with app
    db.init_app(app)
    
    # Register blueprints/routes
    register_routes(app)
    
    # Register CLI commands
    register_commands(app)
    
    # Import models to ensure they are registered with SQLAlchemy
    from models import Book, Reader, Review, Annotation
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

def register_routes(app):
    """Register application routes."""
    from routes import register_routes as register_app_routes
    register_app_routes(app)

def register_commands(app):
    """Register CLI commands."""
    from cli import register_commands as register_cli_commands
    register_cli_commands(app)

# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
