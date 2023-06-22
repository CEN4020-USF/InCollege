import sqlite3
import json
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


def add_user(username, password, first_name, last_name, major="CS", uni="USF", email=1, sms=1, advert=1,
             lang="English", sign_in=1, friends="{\"friends\": []}", pending_from="{\"friends\": []}",
             pending_to="{\"friends\": []}"):
    conn, cursor = db_connect()

    # Execute a query to insert data into the table
    insert_query = \
        "INSERT INTO Users (Username, Password, first_name, last_name," \
        " EmailEnabled, SMSEnabled, AdvertisingEnabled, Language, is_signed_in, Major, University," \
        " Friends, PendingFrom, PendingTo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (username, password, first_name, last_name, email, sms, advert, lang,
              sign_in, major, uni, friends, pending_from, pending_to)
    cursor.execute(insert_query, values)

    db_close(conn, cursor)


def remove_user(username):
    conn, cursor = db_connect()

    delete_query = "DELETE FROM Users WHERE username = ?"
    values = (username,)
    cursor.execute(delete_query, values)

    db_close(conn, cursor)


def edit_user(username):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET Username = ? WHERE Username = ?"
    values = (username, username)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def get_user(username):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE Username = ?"
    values = (username,)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def check_name(firstname, last_name, is_mock=False):
    conn, cursor = db_connect()

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


def get_first_name(firstname):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE first_name = ?"
    values = (firstname,)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def get_last_name(lastname):
    conn, cursor = db_connect()

    select_query = "SELECT * FROM Users WHERE last_name = ?"
    values = (lastname,)
    cursor.execute(select_query, values)

    user = cursor.fetchone()

    db_close(conn, cursor)

    return user


def count_users():
    conn, cursor = db_connect()

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


def count_jobs():
    conn, cursor = db_connect()

    count_query = "SELECT COUNT(*) FROM Jobs"
    cursor.execute(count_query)

    count = cursor.fetchone()[0]

    db_close(conn, cursor)

    return count


def toggle_sms(username, toggle):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET SMSEnabled = ? WHERE Username = ?"
    values = (toggle, username)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def toggle_email(username, toggle):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET EmailEnabled = ? WHERE Username = ?"
    values = (toggle, username)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def toggle_advertising(username, toggle):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET AdvertisingEnabled = ? WHERE Username = ?"
    values = (toggle, username)
    cursor.execute(update_query, values)

    db_close(conn, cursor)


def change_language(username, language):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET Language = ? WHERE Username = ?"
    values = (language, username)
    cursor.execute(update_query, values)

    db_close(conn, cursor)

#will set the user who signed in to be signed into the data base based on their user name
def user_signed_in(username):
    conn, cursor = db_connect()

    update_query = "UPDATE Users SET is_signed_in = 1 WHERE Username = ?"
    values = (username,)
    cursor.execute(update_query, values)

    db_close(conn, cursor)

#sets all users in the data base to be signed out
def sign_out_all():
    conn, cursor = db_connect()

    cursor.execute("UPDATE Users SET is_signed_in = 0")
    conn.commit()

    db_close(conn, cursor)

#checks if there is a user signed in, if so return true else return false
def is_user_signed_in():
    conn, cursor = db_connect()
    flag = False

    cursor.execute("SELECT COUNT(*) FROM Users WHERE is_signed_in = 1")
    result = cursor.fetchone()[0]

    if result > 0:
        flag = True

    db_close(conn, cursor)
    return flag


def add_friend(current_user, target_user):
    conn, cursor = db_connect()

    select_query = "SELECT Friends FROM Users WHERE Username=?"
    values = (current_user,)
    cursor.execute(select_query, values)
    current_user_friends = cursor.fetchone()

    values = (target_user[0],)
    cursor.execute(select_query, values)
    target_user_friends = cursor.fetchone()

    if current_user_friends:
        current_friends_json_str = current_user_friends[0]
        current_friends_json = json.loads(current_friends_json_str)
        current_friends_json['friends'].append(target_user[0])
        current_friends_json = json.dumps(current_friends_json)
        cursor.execute("UPDATE Users SET Friends=? WHERE Username=?", (current_friends_json, current_user))

        target_friends_json_str = target_user_friends[0]
        target_friends_json = json.loads(target_friends_json_str)
        target_friends_json['friends'].append(current_user)
        target_friends_json = json.dumps(target_friends_json)
        cursor.execute("UPDATE Users SET Friends=? WHERE Username=?", (target_friends_json, target_user[0]))

        conn.commit()
    db_close(conn, cursor)


def delete_friend(current_user, target_user):
    conn, cursor = db_connect()

    select_query = "SELECT Friends FROM Users WHERE Username=?"
    values = (current_user,)
    cursor.execute(select_query, values)
    current_user_friends = cursor.fetchone()

    values = (target_user[0],)
    cursor.execute(select_query, values)
    target_user_friends = cursor.fetchone()

    if current_user_friends:
        friends_json = json.loads(current_user_friends[0])
        if target_user[0] in friends_json['friends']:
            friends_json['friends'].remove(target_user[0])
            friends_json_str = json.dumps(friends_json)
            cursor.execute("UPDATE Users SET Friends=? WHERE Username=?", (friends_json_str, current_user))

        friends_json = json.loads(target_user_friends[0])
        if current_user in friends_json['friends']:
            friends_json['friends'].remove(current_user)
            friends_json_str = json.dumps(friends_json)
            cursor.execute("UPDATE Users SET Friends=? WHERE Username=?", (friends_json_str, target_user[0]))

        conn.commit()

    db_close(conn, cursor)


def add_pending(current_user, target_user):
    conn, cursor = db_connect()

    select_query = "SELECT PendingTo FROM Users WHERE Username=?"
    values = (current_user,)
    cursor.execute(select_query, values)
    current_user_friends = cursor.fetchone()

    select_query = "SELECT PendingFrom FROM Users WHERE Username=?"
    values = (target_user[0],)
    cursor.execute(select_query, values)
    target_user_friends = cursor.fetchone()

    if current_user_friends:
        current_friends_json_str = current_user_friends[0]
        current_friends_json = json.loads(current_friends_json_str)
        current_friends_json['friends'].append(target_user[0])
        current_friends_json = json.dumps(current_friends_json)
        cursor.execute("UPDATE Users SET PendingTo=? WHERE Username=?", (current_friends_json, current_user))
        target_friends_json_str = target_user_friends[0]
        target_friends_json = json.loads(target_friends_json_str)
        target_friends_json['friends'].append(current_user)
        target_friends_json = json.dumps(target_friends_json)
        cursor.execute("UPDATE Users SET PendingFrom=? WHERE Username=?", (target_friends_json, target_user[0]))

        conn.commit()
    db_close(conn, cursor)


def delete_pending(current_user, target_user):
    conn, cursor = db_connect()

    select_query = "SELECT PendingTo FROM Users WHERE Username=?"
    values = (current_user,)
    cursor.execute(select_query, values)
    current_user_friends = cursor.fetchone()

    select_query = "SELECT PendingFrom FROM Users WHERE Username=?"
    values = (target_user[0],)
    cursor.execute(select_query, values)
    target_user_friends = cursor.fetchone()

    if current_user_friends:
        current_friends_json_str = current_user_friends[0]
        current_friends_json = json.loads(current_friends_json_str)
        if target_user[0] in current_friends_json['friends']:
            current_friends_json['friends'].remove(target_user[0])
            current_friends_json = json.dumps(current_friends_json)
            cursor.execute("UPDATE Users SET PendingTo=? WHERE Username=?", (current_friends_json, current_user))
        target_friends_json_str = target_user_friends[0]
        target_friends_json = json.loads(target_friends_json_str)
        if current_user in target_friends_json['friends']:
            target_friends_json['friends'].remove(current_user)
            target_friends_json = json.dumps(target_friends_json)
            cursor.execute("UPDATE Users SET PendingFrom=? WHERE Username=?", (target_friends_json, target_user[0]))

        conn.commit()
    db_close(conn, cursor)





