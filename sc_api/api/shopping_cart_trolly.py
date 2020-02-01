from  api.cart_items import get_items


class Shopping_Cart_Trolly:
    def __init__(self):
        self.cart_storage = dict()
        self.cart_count = 0
        # self.items = get_items()
    
    """ creates a 'cart' which is key value mapping 
    between a unique id and the array of items """
    def create_cart(self):
        cart_id = self.cart_count
        self.cart_count += 1
        items = []
        self.cart_storage[cart_id] = items
        return {
            'cart_id': cart_id,
            'items': items
        }

    # adds an item in the existing cart
    def add_to_cart(cart_id: int, item : str):
        if not id in cart_storage: 
            return 404, 'Cart not found'

        # check if the item match the pre-determined list
        # if item in items

        cart_storage[id].append(item)

    def get_cart_info(self, cart_id):
        if not id in self.cart_storage:
            return 404, 'Cart not found'

        return {
            'cart_id': cart_id,
            'items': self.cart_storage[cart_id]
        }
