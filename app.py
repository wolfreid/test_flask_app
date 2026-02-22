from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    return app


if __name__ == "__main__":
    import os
    app = create_app()
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
