from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, send, emit
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'replace_with_a_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_chat.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
socketio = SocketIO(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_desc = db.Column(db.String(500))  # New field for user profile description

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.profile_desc = request.form['profile_desc']
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('profile'))
    return render_template('profile.html')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password, method='sha256')

        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid login credentials.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    bitcoin_price = get_bitcoin_price()
    messages = Message.query.all()
    return render_template('dashboard.html', username=current_user.username, bitcoin_price=bitcoin_price, messages=messages)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

def get_bitcoin_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
    data = response.json()
    return data['bpi']['USD']['rate']


@socketio.on('message')
def handleMessage(data):
    text = data['text']
    # username is retrieved from the current_user context instead of the data payload
    username = current_user.username
    message = Message(text=text, user_id=current_user.id, username=username)
    db.session.add(message)
    db.session.commit()
    send({'text': text, 'username': username}, broadcast=True)

    text = data['text']
    username = data['username']
    message = Message(text=text, user_id=current_user.id, username=username)
    db.session.add(message)
    db.session.commit()
    send({'text': text, 'username': username}, broadcast=True)


@socketio.on('request_history')
def handle_request_history():
    # Query the last N messages from the database
    last_messages = Message.query.order_by(Message.id.desc()).limit(50).all()
    last_messages = list(reversed(last_messages))  # Reverse to display in correct order
    # Emit the 'history' event to the client with these messages
    emit('history', [{'username': m.username, 'text': m.text} for m in last_messages])

if __name__ == '__main__':
    db.create_all()


@app.route('/chat/security_tokens')
@login_required
def chat_security_tokens():
    messages = Message.query.filter_by(room='security_tokens').all()
    return render_template('chat_room.html', messages=messages, room_name='Security_tokens')

@app.route('/chat/privacy_coins')
@login_required
def chat_privacy_coins():
    messages = Message.query.filter_by(room='privacy_coins').all()
    return render_template('chat_room.html', messages=messages, room_name='Privacy_coins')

@app.route('/chat/stablecoins')
@login_required
def chat_stablecoins():
    messages = Message.query.filter_by(room='stablecoins').all()
    return render_template('chat_room.html', messages=messages, room_name='Stablecoins')

@app.route('/chat/governance_tokens')
@login_required
def chat_governance_tokens():
    messages = Message.query.filter_by(room='governance_tokens').all()
    return render_template('chat_room.html', messages=messages, room_name='Governance_tokens')

@app.route('/chat/nfts')
@login_required
def chat_nfts():
    messages = Message.query.filter_by(room='nfts').all()
    return render_template('chat_room.html', messages=messages, room_name='Nfts')

@app.route('/chat/layer_2_solutions')
@login_required
def chat_layer_2_solutions():
    messages = Message.query.filter_by(room='layer_2_solutions').all()
    return render_template('chat_room.html', messages=messages, room_name='Layer_2_solutions')

@app.route('/chat/community_and_meme_coins')
@login_required
def chat_community_and_meme_coins():
    messages = Message.query.filter_by(room='community_and_meme_coins').all()
    return render_template('chat_room.html', messages=messages, room_name='Community_and_meme_coins')
socketio.run(app, debug=True)