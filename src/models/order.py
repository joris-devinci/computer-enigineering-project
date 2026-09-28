import time

from src.models.order_item import OrderItem

class Order():
    timestamp:time
    items:list[OrderItem]
