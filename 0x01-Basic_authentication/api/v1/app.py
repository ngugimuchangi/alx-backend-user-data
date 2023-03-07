#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
# Check authentication type
auth_type = getenv('AUTH_TYPE')
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized access handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    """ Forbidden access handler
    """
    return jsonify({"error": "Forbidden"}), 403


# @app.before_request
# def before_request():
#     """ Actions before serving a request
#     """
#     # Authorization parameter not set
#     if not auth:
#         return
#     # Check if path doesn't require authorization
#     if not auth.require_auth(request.path, ['/api/v1/status/',
#                                             '/api/v1/unauthorized/',
#                                             '/api/v1/forbidden/']):
#         return
#     # Check authorization header if path requires authorization
#     if not auth.authorization_header(request):
#         abort(401)
#     # Check if current user is authorized to access the route
#     if not auth.current_user(request):
#         abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
