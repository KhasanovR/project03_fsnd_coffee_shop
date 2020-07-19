import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
db_drop_and_create_all()


'''
@TODO: Uncomment the following line to initialize the database
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''

# ---------------------------------------------------------------------------- #
# Routes                                                                       #
# ---------------------------------------------------------------------------- #

'''
@TODO: Implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} 
    where drinks is the list of drinks or 
    appropriate status code indicating reason for failure
'''

'''
@TODO: Implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} 
    where drinks is the list of drinks or 
    appropriate status code indicating reason for failure
'''

'''
@TODO: Implement endpoint 
    POST /drinks 
        it should create a new row in the drinks table 
        it should require the 'post:drinks' permission 
        it should contain the drink.long() data representation 
    returns status code 200 and json {"success": True, "drinks": drink} 
    where drink an array containing only the newly created drink or 
    appropriate status code indicating reason for failure 
'''

'''
@TODO: Implement endpoint 
    PATCH /drinks/<id> where <id> is the existing model id 
        it should respond with a 404 error if <id> is not found 
        it should update the corresponding row for <id> 
        it should require the 'patch:drinks' permission 
        it should contain the drink.long() data representation 
    returns status code 200 and json {"success": True, "drinks": drink} 
    where drink an array containing only the updated drink or 
    appropriate status code indicating reason for failure 
'''

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

# ---------------------------------------------------------------------------- #
# Error Handlers                                                               #
# ---------------------------------------------------------------------------- #

'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):

    try:
        msg = error['description']
    except TypeError:
        msg = "unprocessable"

    return jsonify({
        "success": False,
        "error": 422,
        "message": msg
    }), 422


'''
@TODO: Implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''


@app.errorhandler(400)
def bad_request(error):

    try:
        msg = error['description']
    except TypeError:
        msg = "resource not found"

    return jsonify({
        "success": False,
        "error": 400,
        "message": msg
    }), 400


'''
@TODO: Implement error handler for 404
    error handler should conform to general task above 
'''


@app.errorhandler(404)
def ressource_not_found(error):

    try:
        msg = error['description']
    except TypeError:
        msg = "resource not found"

    return jsonify({
        "success": False,
        "error": 404,
        "message": msg
    }), 404


'''
@TODO: Implement error handler for AuthError
    error handler should conform to general task above 
'''


@app.errorhandler(AuthError)
def authentification_failed(auth_error):

    try:
        msg = auth_error.error['description']
    except TypeError:
        msg = "authentification fails"

    return jsonify({
        "success": False,
        "error": auth_error.status_code,
        "message": msg
    }), 401
