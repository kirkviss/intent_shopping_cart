import os, sys
from pytest import fixture
import connexion
import json

cwd = os.getcwd()
sys.path.insert(0, cwd )
flaskApp = connexion.FlaskApp(__name__, specification_dir=f'{cwd}/openapi')
flaskApp.add_api('api.yaml')

@fixture(scope='module')
def client():
    with flaskApp.app.test_client() as client: 
        yield client
@fixture
def cart(client): 
    response = client.post('v0/cart')
    cart = json.loads(response.data)
    # return cart
    yield cart
    client.delete(f'v0/cart/{cart["id"]}')


# test that cart is created on a post call 
def test_post_cart(client):
    response = client.post('v0/cart')
    cart = json.loads(response.data)

    assert cart
    assert 'id' in cart
    assert 'items' in cart
    assert 'total' in cart
    assert response.status_code == 200

# test grabbing an existing 
def test_get_cart(client, cart):
    response = client.get(f'/v0/cart/{cart["id"]}')
    assert response.status_code == 200
    result = json.loads(response.data)
    for key in cart:
        assert cart[key] == result[key]

def test_get_cart_not_found(client):
    response = client.get(f'/v0/cart/non existant id')
    assert response.status == '404 NOT FOUND'

def test_updating_cart_items(client, cart):
    response = client.put(f'/v0/cart/{cart["id"]}/D')
    result = json.loads(response.data)
    assert 'D' in result['items']
    assert result['total'] == 0.15

def test_total_calc_multi_item(client, cart):
    itemStr = 'ABCDABAA'
    for char in itemStr:
        client.put(f'/v0/cart/{cart["id"]}/{char}')
    
    response = client.get(f'/v0/cart/{cart["id"]}')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['total'] == 32.40

def test_total_calc_with_discount_used(client, cart):
    itemStr = 'CCCCCCC'
    for char in itemStr:
        client.put(f'/v0/cart/{cart["id"]}/{char}')
    
    response = client.get(f'/v0/cart/{cart["id"]}')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['total'] == 7.25

def test_total_calc_without_discount_used(client, cart):
    itemStr = 'ABCD'
    for char in itemStr:
        client.put(f'/v0/cart/{cart["id"]}/{char}')
    
    response = client.get(f'/v0/cart/{cart["id"]}')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['total'] == 15.40

def test_update_unknown_item(client, cart):
    
    response = client.put(f'/v0/cart/{cart["id"]}/Z')
    assert response.status_code == 404

def test_update_lowercase_item(client, cart):
    response = client.put(f'/v0/cart/{cart["id"]}/a')
    result = json.loads(response.data)
    assert response.status_code == 200
    assert 'A' in result['items']

# test if an item that has multiple discounts for different quantities of an item, the total provides the lowest possible value
def test_multiple_discounts(client, cart): 

    for i in range(1,14):
        client.put(f'/v0/cart/{cart["id"]}/E')
    
    response = client.get(f'/v0/cart/{cart["id"]}')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert result['total'] == 9

def test_delete_item_from_cart(client, cart):
    client.put(f'/v0/cart/{cart["id"]}/D')
    response = client.delete(f'/v0/cart/{cart["id"]}/D')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert not 'D' in result['items']
    
    followUpResponse = client.get(f'/v0/cart/{cart["id"]}')
    result = json.loads(followUpResponse.data)
    assert not 'D' in result['items']
    
def test_multiple_delete(client, cart):
    for i in range(1, 10 ): 
        client.put(f'/v0/cart/{cart["id"]}/D')

    for i in range(1,5):
        response = client.delete(f'/v0/cart/{cart["id"]}/D')
        assert response.status_code == 200
        
        
    followUpResponse = client.get(f'/v0/cart/{cart["id"]}')
    result = json.loads(followUpResponse.data)
    assert result['items']['D'] == 5
    
