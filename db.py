"""
Yalg - yet another life game

Copyright (C) 2025  Klinkesorn Nguyen An Hoa

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Author contactable at k<dot>nguyen<dot>an<dot>hoa<at>gmail<dot>com
"""
import os, logging
import sqlite3
from contextlib import contextmanager
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file.

    Args:
        db_file: Database file path

    Returns:
        Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"#create_connection: Connected to SQLite database: {db_file}")
        return conn
    except Error as e:
        logging.error(f"#create_connection: Error connecting to database: {e}")
        return None

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement.

    Args:
        conn: Connection object
        create_table_sql: CREATE TABLE statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        logging.info("#create_table: Table created successfully")
    except Error as e:
        logging.error(f"#create_table: Error creating table: {e}")

def initialize_database(db_file):
    """Initialize the database with tables if they don't exist.

    Args:
        db_file: Database file path

    Returns:
        Connection object or None
    """
    # Create connection
    conn = create_connection(db_file)

    if conn is None:
        logging.error("#initialize_database: Cannot create the database connection.")
        return None

    # Define table creation SQL statements
    # Add as many tables as you need
    users_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    create_table(conn, users_table_sql)
    conn.cursor().execute(
        """
        INSERT OR REPLACE INTO users (
            username, email
        ) VALUES (?, ?)
        """,
        ('admin', 'admin@yagl.com')
    )

    items_table_sql = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """
    create_table(conn, items_table_sql)

    return conn

@contextmanager
def dbconn():
    # Database file path
    database = "data/yalg.db"

    # Initialize database
    conn = initialize_database(database)

    if conn is None:
        logging.error("#dbconn: Database initialization failed.")
        return None

    yield(conn)

    # Close the connection when done
    conn.close()
