from db.cart import cartExists
from db.item import getItem

# Decorator to check if the cartId provided to the decorated function exists
def cartDecorator(function): 
    def wrapper(*args, **kwargs):
        if not cartExists(kwargs['cartId']):
            return {'Error': f'Cart "{cartId}" not found'}, 404
        return function(*args, **kwargs):
    return wrapper

# Decorator to check if the itemId provided to the decorated function exists 
def itemDecorator(function):
    def wrapper(*args, **kwargs): 
        if not itemExists():
            return {'Error': f'Item "{itemId}" not found'}, 404
        return function(*args, kwargs)
    return wrapper