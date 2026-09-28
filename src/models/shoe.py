from src.models.enums.shoe_brand import ShoeBrand
from src.models.enums.shoe_category import ShoeCategory
from src.models.enums.shoe_color import ShoeColor

class Shoe():
    id:int
    name:str
    price:float
    color:ShoeColor
    brand:ShoeBrand
    category:ShoeCategory