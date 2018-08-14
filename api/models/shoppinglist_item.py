from .model_mixin import AuditableBaseModel, db


class ShoppingListItem(AuditableBaseModel):

    __tablename__ = 'shoppinglist_items'

    name = db.Column(db.String(60), unique=True)
    shoppinglist_id = db.Column(db.String, db.ForeignKey('shoppinglists.id'))
