from . import app

@app.template_filter()
def encrypt(s):
    encrypted = "*"*len(s)

    return encrypted