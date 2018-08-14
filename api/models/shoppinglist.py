from .model_mixin import AuditableBaseModel, db


class ShoppingList(AuditableBaseModel):

    __tablename__ = 'shoppinglists'

    name = db.Column(db.String(60), unique=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    items = db.relationship('ShoppingListItem', backref='shoppinglist', lazy='dynamic')
