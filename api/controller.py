from db.cart import addCart, getCart, updateCart
from db.item import getItem, getAllItems

def post_cart():
    
    return addCart(), 200

def put_cart(cartId: str, itemId: str):
    
    itemsKey = 'items'
    # check if the cart exists in the 'db'
    cart = getCart(cartId)
    if not cart:
        return {'Error': f'Cart "{cartId}" not found'}, 404

    # check if the item specified exists the 'db'
    item = getItem(itemId)
    if not item:
        return {'Error': f'Item "{itemId}" not found'}, 404

    
    updateCart(cartId, cart)

    return cart, 200

def get_cart(cartId: str): 
    # check if the cart exists in the 'db'
    cart = getCart(cartId)
    if not cart:
        return {'Error': f'Cart "{carId}" not found'}
     if 'items' in cart: 
         cart[]

    
    for i in getAllItems(): 

   
        for i in items:
            
            getItem(itemId)[]

    return cart, 200