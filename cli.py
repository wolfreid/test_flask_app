"""Command line interface for database management."""

import click
from flask.cli import with_appcontext
from app import create_app, db
from models import Book, Reader, Review, Annotation

@click.command()
@with_appcontext
def init_db():
    """Initialize the database."""
    db.create_all()
    click.echo('Initialized the database.')

@click.command()
@with_appcontext
def seed_db():
    """Seed the database with sample data."""
    from app_data import seed_database
    seed_database()
    click.echo('Database seeded with sample data.')

@click.command()
@with_appcontext
def reset_db():
    """Reset the database (drop all tables and recreate)."""
    db.drop_all()
    db.create_all()
    click.echo('Database reset successfully.')

def register_commands(app):
    """Register CLI commands with the Flask app."""
    app.cli.add_command(init_db)
    app.cli.add_command(seed_db)
    app.cli.add_command(reset_db)

if __name__ == '__main__':
    app = create_app()
    register_commands(app)
    
    with app.app_context():
        # Example of using the commands programmatically
        print("Available commands: init-db, seed-db, reset-db")
        print("Run with: flask init-db")