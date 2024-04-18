import pytest
from app import app, db, User, Message

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
    db.session.remove()
    db.drop_all()

def test_send_message(client):
    # fr test user
    user = User(username='testuser', email='testuser@example.com', password='testpassword')
    db.session.add(user)
    db.session.commit()

    # Log in 
    client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    })

    # Send a mesg
    room = 'testroom'
    message = 'Hello, world!'
    response = client.post(f'/chat/{room}', data={
        'message': message
    }, follow_redirects=True)

    assert response.status_code == 200

    # Check  database
    msg = Message.query.filter_by(text=message, room=room).first()
    assert msg is not None
    assert msg.username == 'testuser'

if __name__ == '__main__':
    pytest.main()