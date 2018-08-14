from .model_mixin import AuditableBaseModel, db


class User(AuditableBaseModel):

    __tablename__ = 'users'

    email = db.Column(db.String(60), index=True, unique=True)
    name = db.Column(db.String(60), index=True, unique=True)
    password = db.Column(db.String(128))
    shoppinglists = db.relationship('ShoppingList', backref='user', lazy='dynamic')
