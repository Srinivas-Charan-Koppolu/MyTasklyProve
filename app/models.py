from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        password_hash = generate_password_hash(password)
        self.password_hash = password_hash
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_user_id(username):
        user_id = User.query.filter_by(username=username).first()
        return user_id

    def __repr__(self):
        return f'<User user_id{self.id} username={self.username}>'


class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    def isAdmin(user_id):
        isAdminUser = AdminUser.query.filter_by(user_id=user_id).first()
        return isAdminUser != None

    def __repr__(self):
        return f'<AdminUser user_id={self.user_id}>'