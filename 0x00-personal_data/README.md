# 0x00. Personal data

## About
* Personally Identifiable Information (PII)
* Personal data
* Protecting PII and personal data
* Log keeping

## Tasks
0. Function called `filter_datum` that returns the log message obfuscated.
    * [filtered_logger.py](filtered_logger.py)
1. `RedactingFormatter` class for creating custom log formatters that redact specified sensitive information
    * [filtered_logger.py](filtered_logger.py)
2. `get_logger` function that returns a `logging.Logger` object that obfuscates specified PII fields
    * [filtered_logger.py](filtered_logger.py)
3. `get_db function that returns a `mysql.connector.connection.MySQLConnection` object for db_connection.
    * [filtered_logger.py](filtered_logger.py)
4. `main` function that uses `get_db` function to retrieve data from `users` table and display each row using logger object with `RedactingFormatter` formatter.
    * [filtered_logger.py](filtered_logger.py)
5 `hash_password` function that encrypts password using `bycrpt` package.
    * [encrypt_password.py](encrypt_password.py)
6. `is_valid` function that checks password validity
    * [encrypt_password.py](encrypt_password.py)
