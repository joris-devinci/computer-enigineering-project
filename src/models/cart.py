from src.models.user import User
from src.models.cart_item import CardItem

class Cart():
    id:int
    user:User # Maybe just user_id:int
    items:list[CardItem]
    
