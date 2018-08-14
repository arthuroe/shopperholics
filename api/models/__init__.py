from sqlalchemy import event
from ..unique_id import PushID
from .model_mixin import ModelMixin, db, to_camel_case
from .user import User
from .shoppinglist import ShoppingList
from .shoppinglist_item import ShoppingListItem


def fancy_id_generator(mapper, connection, target):
    """A function to generate unique identifiers on insert."""
    push_id = PushID()
    target.id = push_id.next_id()


tables = [User, ShoppingList, ShoppingListItem]

for table in tables:
    event.listen(table, 'before_insert', fancy_id_generator)
