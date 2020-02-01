from db.cart import addCart, getCart, updateCartItems
from db.item import getItem, getAllItems

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
    
    updateCartItems(cartId, cart['items'])

    return cart, 200

def get_cart(cartId: str): 
    # check if the cart exists in the 'db'
    cart = getCart(cartId)
    if not cart:
        return {'Error': f'Cart "{carId}" not found'}
    total = 0
    for itemId, amount in cart['items'].items(): 
        item = getItem(itemId)
        unit_price = item['unit_price']
        vol_dic = item['volume_discounts']
        if len(vol_dic) > 0:
            discount_number = item['volume_discounts'][0]['number']
            discount_price = item['volume_discounts'][0]['price']
            total += (int(amount / discount_number) * discount_price) + (( amount % discount_number) *  unit_price)
            print( total)
        else: 
            total += (unit_price * amount)
    cart['total'] = total

    return cart, 200
