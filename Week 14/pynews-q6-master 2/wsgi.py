from webapp import create_app
import config


app = create_app(config.current_config)


# This should be in create_app (you can create a function in a function.)
@app.shell_context_processor
def inject_variables_to_shell():
    """
    Return a dictionary of variables to inject ({variable_name: variable_value})
    Those variables will be accessible in the flask shell (without having to import them)
    """
    from webapp.auth.models import User
    from webapp.main.models import Quote, Book
    from webapp import db
    return {
        "User": User,
        "Quote": Quote,
        "Book": Book,
        "db": db,
        "dev_name": "Sasha",
    }


app.run(port=5000, debug=True)