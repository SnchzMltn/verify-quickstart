import os

from flask import Flask, render_template

from dotenv import load_dotenv, find_dotenv


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'verify.sqlite'),
    )

    load_dotenv(find_dotenv())

    try:
        # Secret key
        app.secret_key = os.environ['SECRET_KEY']
    except KeyError:
        raise Exception('Missing environment variables. See .env.example for details')

    # register the database commands
    from verify import db
    db.init_app(app)

    @app.route('/users')
    def list_users():
        database = db.get_db()
        users = database.execute('SELECT * FROM user').fetchall()
        return render_template('users.html', users=users)

    # apply the blueprints to the app
    from verify import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app
