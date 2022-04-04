#!/usr/bin/python3

##############################################
#
# __init__.py
# main
#
##############################################
import flask

from .. import db, login_manager, mail_manager

main_blueprint = flask.Blueprint("main", __name__)

from . import routes, filters, models