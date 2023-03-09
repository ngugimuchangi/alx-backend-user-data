# 0x01. Basic authentication

## About
- Simple HTTP API for playing with `User` model.
- Implements `Basic Authentication` scheme

## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status`, `/stats`, `/authorized` and `/forbidden`
- `views/users.py`: all users endpoints
- `auth/auth.py`: authentication base module
- `auth/basic_auth.py`: basic authentication module

## Setup
```
$ pip3 install -r requirements.txt
```


## Run
- Without authentication
```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```
- Basic authentication
```
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```
## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `GET /api/v1/unauthorized`: returns a 401 response
- `GET /api/v1/forbidden`: returns a 403 response
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## Simple to use with curl

### Without authentication
```
$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
```
### Basic authentication
```
$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
[
  {
    "created_at": "2017-09-25 01:55:17", 
    "email": "bob@hbtn.io", 
    "first_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last_name": null, 
    "updated_at": "2017-09-25 01:55:17"
  }
]
```
