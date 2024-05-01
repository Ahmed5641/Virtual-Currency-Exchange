from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO, emit, join_room
import requests
<<<<<<< HEAD
import random
from datetime import datetime
import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
=======
import logging
from datetime import datetime
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crypto_exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
socketio = SocketIO(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_picture = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.String(500), nullable=True)
    contact_details = db.Column(db.String(200), nullable=True)
    profile_description = db.Column(db.String(500), nullable=True)
    simulated_portfolio = db.Column(db.String(1000), nullable=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    room = db.Column(db.String(100), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
<<<<<<< HEAD
def index():
    return render_template('index.html')

@app.route('/')
=======
>>>>>>> b828e01 (Initial commit of project files to ai_dev)
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
<<<<<<< HEAD
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

=======
        username, email, password = request.form.get('username'), request.form.get('email'), request.form.get('password')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists', 'error')
            return redirect(url_for('register'))

>>>>>>> b828e01 (Initial commit of project files to ai_dev)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
<<<<<<< HEAD
        username = request.form['username']
        password = request.form['password']
=======
        username, password = request.form.get('username'), request.form.get('password')
>>>>>>> b828e01 (Initial commit of project files to ai_dev)
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    cryptos = [
        {'name': 'Bitcoin', 'symbol': 'BTC', 'whitepaper_url': 'https://bitcoin.org/bitcoin.pdf'},
        {'name': 'Ethereum', 'symbol': 'ETH', 'whitepaper_url': 'https://ethereum.org/en/whitepaper/'},
        {'name': 'Ripple', 'symbol': 'XRP', 'whitepaper_url': 'https://ripple.com/files/ripple_consensus_whitepaper.pdf'},
        {'name': 'Cardano', 'symbol': 'ADA', 'whitepaper_url': 'https://docs.cardano.org/en/latest/explore-cardano/cardano-whitepaper.html'},
        {'name': 'Solana', 'symbol': 'SOL', 'whitepaper_url': 'https://solana.com/solana-whitepaper.pdf'},
<<<<<<< HEAD
        {'name': 'Polkadot', 'symbol': 'DOT', 'whitepaper_url': 'https://polkadot.network/PolkaDotPaper.pdf'},
        {'name': 'Binance Coin', 'symbol': 'BNB', 'whitepaper_url': 'https://www.binance.com/resources/ico/Binance_WhitePaper_en.pdf'},
        {'name': 'Chainlink', 'symbol': 'LINK', 'whitepaper_url': 'https://link.smartcontract.com/whitepaper'},
        {'name': 'Litecoin', 'symbol': 'LTC', 'whitepaper_url': 'https://litecoin.org/en/litecoin.pdf'},
        {'name': 'Dogecoin', 'symbol': 'DOGE', 'whitepaper_url': 'https://github.com/dogecoin/dogecoin/blob/master/README.md'},
    ]

    for crypto in cryptos:
        price, change = get_real_time_price(crypto['symbol'])
        crypto['price'] = price
        crypto['change'] = change

    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('dashboard.html', cryptos=cryptos, last_updated=last_updated)
=======
        {'name': 'Polkadot', 'symbol': 'DOT', 'whitepaper_url': 'https://polkadot.network/PolkaDotPaper.pdf', 'price': 10.5, 'change': 2.5},
        {'name': 'Binance Coin', 'symbol': 'BNB', 'whitepaper_url': 'https://www.binance.com/resources/ico/Binance_WhitePaper_en.pdf', 'price': 300, 'change': -1.2},
        {'name': 'Chainlink', 'symbol': 'LINK', 'whitepaper_url': 'https://link.smartcontract.com/whitepaper', 'price': 7.8, 'change': 5.6},
        {'name': 'Litecoin', 'symbol': 'LTC', 'whitepaper_url': 'https://litecoin.org/en/litecoin.pdf', 'price': 132.5, 'change': 1.8},
        {'name': 'Dogecoin', 'symbol': 'DOGE', 'whitepaper_url': 'https://github.com/dogecoin/dogecoin/blob/master/README.md', 'price': 0.05, 'change': -2.1}
    ]

    for i in range(5):
        price, change = get_real_time_price(cryptos[i]['symbol'])
        cryptos[i]['price'], cryptos[i]['change'] = price, change

    return render_template('dashboard.html', cryptos=cryptos, last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.profile_picture = request.form.get('profile_picture')
        current_user.bio = request.form.get('bio')
        current_user.contact_details = request.form.get('contact_details')
        current_user.profile_description = request.form.get('profile_description')
        db.session.commit()
        flash('Profile updated successfully', 'success')
    return render_template('profile.html', user=current_user)

@app.route('/portfolio')
@login_required
def portfolio():
    simulated_portfolio = get_simulated_portfolio(current_user.id)
    return render_template('portfolio.html', portfolio=simulated_portfolio)

@app.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
    if request.method == 'POST':
<<<<<<< HEAD
        currency = request.form['currency']
        amount = float(request.form['amount'])
        simulated_portfolio = get_simulated_portfolio(current_user.id)
        simulated_portfolio[currency] = simulated_portfolio.get(currency, 0) + amount
        current_user.simulated_portfolio = str(simulated_portfolio)
        db.session.commit()
=======
        currency, amount = request.form.get('currency'), float(request.form.get('amount'))
        simulated_portfolio = get_simulated_portfolio(current_user.id)
        simulated_portfolio[currency] = simulated_portfolio.get(currency, 0) + amount
        current_user.simulated_portfolio = str(simulated_portfolio)
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

        transaction = Transaction(user_id=current_user.id, currency=currency, amount=amount, transaction_type='buy', timestamp=datetime.now())
        db.session.add(transaction)
        db.session.commit()

        flash('Simulated buy order placed successfully', 'success')
        return redirect(url_for('portfolio'))
    return render_template('buy.html')

@app.route('/sell', methods=['GET', 'POST'])
@login_required
def sell():
    if request.method == 'POST':
<<<<<<< HEAD
        currency = request.form['currency']
        amount = float(request.form['amount'])
=======
        currency, amount = request.form.get('currency'), float(request.form.get('amount'))
>>>>>>> b828e01 (Initial commit of project files to ai_dev)
        simulated_portfolio = get_simulated_portfolio(current_user.id)
        if simulated_portfolio.get(currency, 0) >= amount:
            simulated_portfolio[currency] -= amount
            current_user.simulated_portfolio = str(simulated_portfolio)
<<<<<<< HEAD
            db.session.commit()
=======
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

            transaction = Transaction(user_id=current_user.id, currency=currency, amount=amount, transaction_type='sell', timestamp=datetime.now())
            db.session.add(transaction)
            db.session.commit()

            flash('Simulated sell order placed successfully', 'success')
        else:
            flash('Insufficient balance', 'error')
        return redirect(url_for('portfolio'))
    return render_template('sell.html')

@app.route('/history')
@login_required
def history():
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.timestamp.desc()).all()
    return render_template('history.html', transactions=transactions)

<<<<<<< HEAD
@app.route('/chat/<room>', methods=['GET', 'POST'])
@login_required
def chat_room(room):
    messages = Message.query.filter_by(room=room).all()
    print(messages)
    if request.method == 'POST':
        message = request.form['message']
        new_message = Message(text=message, user_id=current_user.id, username=current_user.username, room=room)
        db.session.add(new_message)
        db.session.commit()
        emit('message', {'username': current_user.username, 'message': message, 'room': room}, room=room)
    return render_template('chat_room.html', room=room, messages=messages )
=======
@app.route('/chat/<room>')
@login_required
def chat_room(room):
    messages = Message.query.filter_by(room=room).all()
    return render_template('chat_room.html', room=room, messages=messages)
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': f'{current_user.username} has entered the room.'}, room=room)
    messages = Message.query.filter_by(room=room).order_by(Message.id.desc()).limit(50).all()
<<<<<<< HEAD
    messages = list(reversed(messages))
    emit('message', [{'username': m.username, 'message': m.text, 'room': m.room} for m in messages], room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    username = current_user.username
    new_message = Message(text=message, user_id=current_user.id, username=username, room=room)
    db.session.add(new_message)
    db.session.commit()
    emit('message', {'username': username, 'message': message, 'room': room}, room=room)

@socketio.on('request_history')
def handle_request_history(data):
    room = data['room']
    messages = Message.query.filter_by(room=room).order_by(Message.id.desc()).limit(50).all()
    messages = list(reversed(messages))
    emit('history', [{'username': m.username, 'text': m.text, 'room': m.room} for m in messages], room=room)

def get_simulated_portfolio(user_id):
    user = User.query.get(user_id)
    if user.simulated_portfolio:
        return eval(user.simulated_portfolio)
    else:
        return {}




=======
    messages.reverse()
    emit('message', [{'username': m.username, 'message': m.text} for m in messages], room=room)

@socketio.on('message')
def handle_message(data):
    room, message = data['room'], data['message']
    new_message = Message(text=message, user_id=current_user.id, username=current_user.username, room=room)
    db.session.add(new_message)
    db.session.commit()
    emit('message', {'username': current_user.username, 'message': message}, room=room)

def get_simulated_portfolio(user_id):
    user = User.query.get(user_id)
    return eval(user.simulated_portfolio) if user.simulated_portfolio else {}
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

def get_real_time_price(currency):
    url_mapping = {
        'BTC': "https://api.coindesk.com/v1/bpi/currentprice/BTC.json",
        'ETH': "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_24hr_change=true",
        'XRP': "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd&include_24hr_change=true",
        'ADA': "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_24hr_change=true",
        'SOL': "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true"
    }

    url = url_mapping.get(currency)
    if not url:
        logging.error(f"No URL found for currency: {currency}")
        return None, None

<<<<<<< HEAD
    response = requests.get(url)
    data = response.json()

    try:
        if currency == 'BTC':
            price = data['bpi']['USD']['rate_float']
            change = data['bpi']['USD'].get('rate_float_change_24h', 0.0)
        elif currency == 'ETH':
            price = data['ethereum']['usd']
            change = data['ethereum']['usd_24h_change']
        elif currency == 'XRP':
            if 'ripple' in data:
                price = data['ripple']['usd']
                change = data['ripple']['usd_24h_change']
            else:
                logging.error(f"Ripple data not found in response: {data}")
                return None, None
        elif currency == 'ADA':
            price = data['cardano']['usd']
            change = data['cardano']['usd_24h_change']
        elif currency == 'SOL':
            price = data['solana']['usd']
            change = data['solana']['usd_24h_change']
        return price, change
    except KeyError as e:
        logging.error(f"Key error in data structure for {currency}: {e}, data received: {data}")
        return None, None

=======
    try:
        response = requests.get(url)
        data = response.json()

        if currency == 'BTC':
            price, change = data['bpi']['USD']['rate_float'], data['bpi']['USD'].get('rate_float_change_24h', 0.0)
        else:
            price, change = data[currency.lower()]['usd'], data[currency.lower()]['usd_24h_change']

        return price, change
    except (KeyError, requests.exceptions.RequestException) as e:
        logging.error(f"Error fetching data for {currency}: {e}")
        return None, None
>>>>>>> b828e01 (Initial commit of project files to ai_dev)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)