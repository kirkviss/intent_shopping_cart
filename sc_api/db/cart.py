import json
import uuid
import os 

def seedCarts(amount: str):
    for i in range(0, amount):
        addCart()

def getCart( cartId): 
    carts = readCarts()
    if cartId in carts:
        return carts[cartId]
    return None

def updateCart(cartId, newCart):
    carts = readCarts()
    
    if cartId in carts:
        newCart['id'] = cartId 
        carts[cartId] = newCart
        writeCarts(newCart)
        return newCart
    return None

def addCart():
    carts = readCarts()
    newId = str(uuid.uuid1())

    # in the rare (near impossible) chance used uuid is created 
    while (newId in carts):
        newId = uuid.uuid1()
    cart = {
        'id': newId
    }
    carts[newId] = cart
    writeCarts(carts)
    return cart

def deleteCart(cartId): 
    carts = readCarts()
    if cartId in carts: 
        del carts[cartId]
        return cartId
    return None

# overwrite the file with the new content
def writeCarts(carts: dict):
    with open( f'{os.path.dirname(os.path.abspath(__file__))}/carts.json', 'w') as cartFile:
         cartFile.write(json.dumps(carts))

# pull all the content from the json file and then convert it to a json object
def readCarts():
    with open ( f'{os.path.dirname(os.path.abspath(__file__))}/carts.json', 'r') as cartFile:
        return json.loads(cartFile.read())