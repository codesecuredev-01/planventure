import sqlite3
import subprocess
import os

def find_user(username):
    # CRITICAL: SQL Injection vulnerability (B608)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def run_system_command(user_input):
    # CRITICAL: Command Injection vulnerability (B602/B605)
    os.system(f"echo {user_input}")
    subprocess.Popen(user_input, shell=True)
