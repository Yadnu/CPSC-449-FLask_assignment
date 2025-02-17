from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


def load_users():
    with open('users.json') as f:
        return json.load(f)

@app.route('/')
def home():
    users_data = load_users()
    return render_template('index.html', users=users_data["users"])

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    users_data = load_users()
    user = next((user for user in users_data["users"] if user["id"] == user_id), None)
    if user:
        return render_template('user.html', user=user)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
