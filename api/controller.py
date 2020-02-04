from db.cart import addCart, getCart, updateCartItems
from db.item import getItem, getAllItems
from bin.item_calc import get_total

def post_cart():
    
    return addCart(), 200


def put_cart(cartId: str, itemId: str):
    itemId = itemId.upper()

    itemsKey = 'items'
    # check if the cart exists in the 'db'
    cart = getCart(cartId)
    if not cart:
        return {'Error': f'Cart "{cartId}" not found'}, 404

    # check if the item specified exists the 'db'
    item = getItem(itemId)
    if not item:
        return {'Error': f'Item "{itemId}" not found'}, 404

    if itemId in cart['items']: 
        cart['items'][itemId] += 1
    else: 
        cart['items'][itemId] = 1
    
    cart['total'] = get_total(cart['items'])
    updateCartItems(cartId, cart['items'])

    return cart, 200

# TODO
# def deleteCartItem(cartId: str, itemId: str):
# def deleteCart():

# return all item with in the item db
def get_items():
    return getAllItems()

def get_cart(cartId: str): 
    # check if the cart exists in the 'db'
    cart = getCart(cartId)
    if not cart:
        return {'Error': f'Cart "{carId}" not found'}
    cart['total'] = get_total(cart['items'])

    return cart, 200
