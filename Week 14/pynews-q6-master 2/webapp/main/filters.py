from . import main_blueprint

@main_blueprint.app_template_filter() # Not @main_blueprint.template_filter()
def quote_format(quote):
    """
    Format <quote> in our standard quote format:
        "The Quote Is Here"
    :param quote: (str)
    :return: (str) The formatted quote
    """

    quote = quote.title()

    # If the quote already have quotation marks arround it
    # Delete them
    quote.strip('"')

    # Add our own quotation marks and italic
    quote = f'"{quote}"'

    return quote


@main_blueprint.app_template_filter()
def encrypt(encryption_char="*"):

    # Generate a function that encrypts a given string with <encryption_char>
    def filt(s):
        """
        Encrypt a string "foostring" to "*********"
        :param s: The string to encrypt
        :return: The encrypted string
        """

        # Add as many <encryption_char> as the letters in s
        encrypted = encryption_char*len(s)

        return encrypted

    # Return this function
    return filt