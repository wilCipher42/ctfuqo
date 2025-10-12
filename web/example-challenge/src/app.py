from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('/tmp/users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                     (id INTEGER PRIMARY KEY, username TEXT, password TEXT, is_admin INTEGER)''')
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('admin', 'super_secret_password', 1)")
    cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('guest', 'guest123', 0)")
    conn.commit()
    conn.close()

init_db()

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Admin Login</title>
    <style>
        body { font-family: Arial; max-width: 400px; margin: 100px auto; }
        input { width: 100%; padding: 10px; margin: 10px 0; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>Admin Panel Login</h2>
    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}
    {% if flag %}
        <p style="color: green;"><strong>Flag: {{ flag }}</strong></p>
    {% endif %}
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    flag = None
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # VULNERABLE: SQL Injection
        conn = sqlite3.connect('/tmp/users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()
        
        if user:
            if user[3] == 1:  # is_admin
                flag = "flag{sql_1nj3ct10n_1s_d4ng3r0us}"
            else:
                error = "Access denied: Admin privileges required"
        else:
            error = "Invalid credentials"
    
    return render_template_string(LOGIN_PAGE, error=error, flag=flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
