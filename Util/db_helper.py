import sqlite3
DB_CONNECTION = "InCollegeDB"


def db_connect():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_CONNECTION)
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    return conn, cursor


def db_close(conn, cursor):
    # Commit the transaction to save the changes
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()


def add_user(username, password, first_name, last_name, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        insert_query = "INSERT INTO MOCK_USERS (Username, Password, first_name, last_name) VALUES (?, ?, ?, ?)"
        values = (username, password, first_name, last_name)
        cursor.execute(insert_query, values)

    else:
        # Execute a query to insert data into the table
        insert_query = "INSERT INTO Users (Username, Password, first_name, last_name) VALUES (?, ?, ?, ?)"
        values = (username, password, first_name, last_name)
        cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_user(username, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        delete_query = "DELETE FROM MOCK_USERS WHERE username = ?"
        values = (username,)
        cursor.execute(delete_query, values)
    else:
        delete_query = "DELETE FROM Users WHERE username = ?"
        values = (username,)
        cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_user(username, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        update_query = "UPDATE MOCK_USERS SET Username = ? WHERE Username = ?"
        values = (username, username)
        cursor.execute(update_query, values)
    else:
        update_query = "UPDATE Users SET Username = ? WHERE Username = ?"
        values = (username, username)
        cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_user(username, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        select_query = "SELECT * FROM MOCK_USERS WHERE Username = ?"
        values = (username,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()
    else:
        select_query = "SELECT * FROM Users WHERE Username = ?"
        values = (username,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()

    db_close(conn, cursor)

    return user

def check_name(firstname, last_name, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        select_query = "SELECT * FROM MOCK_USERS WHERE first_name = ?"
        values = (firstname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()
    else:
        select_query = "SELECT * FROM Users WHERE first_name = ?"
        values = (firstname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()
        if user is not None:
            if user[3] == last_name:
                flag = True     #First name corresponds with last name and its in table
            else:
                flag = False    #First and last name do not correspond or name is not in table
        else:
            flag = False
    db_close(conn, cursor)

    return flag

def get_first_name(firstname, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        select_query = "SELECT * FROM MOCK_USERS WHERE first_name = ?"
        values = (firstname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()
    else:
        select_query = "SELECT * FROM Users WHERE first_name = ?"
        values = (firstname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()

    db_close(conn, cursor)

    return user

def get_last_name(lastname, is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        select_query = "SELECT * FROM MOCK_USERS WHERE last_name = ?"
        values = (lastname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()
    else:
        select_query = "SELECT * FROM Users WHERE last_name = ?"
        values = (lastname,)
        cursor.execute(select_query, values)

        user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def count_users(is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        count_query = "SELECT COUNT(*) FROM MOCK_USERS"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]
    else:
        count_query = "SELECT COUNT(*) FROM Users"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]

    db_close(conn, cursor)

    return count


def add_job(title, description, employer, location, salary, created_by):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = "INSERT INTO Jobs (Title, Description, Employer, Location, Salary, Created_By) VALUES (?, ?, ?, ?, ?, ?)"
    values = (title, description, employer, location, salary, created_by)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_job(job_id):
    conn, cursor = db_connect()

    delete_query = "DELETE FROM Jobs WHERE id = ?"
    values = (job_id,)
    cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_job(job_id, company, position, salary):
    conn, cursor = db_connect()

    update_query = "UPDATE Jobs SET Company = ?, Position = ?, Salary = ? WHERE id = ?"
    values = (company, position, salary, job_id)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_job(job_id):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Jobs WHERE id = ?"
    values = (job_id,)
    cursor.execute(select_query, values)

    job = cursor.fetchone()

    db_close(conn, cursor)

    return job

def count_jobs(is_mock=False):
    conn, cursor = db_connect()

    if is_mock:
        count_query = "SELECT COUNT(*) FROM MOCK_JOBS"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]
    else:
        count_query = "SELECT COUNT(*) FROM Jobs"
        cursor.execute(count_query)

        count = cursor.fetchone()[0]

    db_close(conn, cursor)

    return count