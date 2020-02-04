from db.item import getItem


def get_total(cartItems: dict):
    total = 0
    for itemId, amount in cartItems.items():
        item = getItem(itemId)

        # sort by the lowest price
        sortedDiscounts = sorted(item['volume_discounts'],key=lambda discount: discount['price'])
    
        for vd in sortedDiscounts:
            items_discounted = int(amount/ vd['number'])
            total +=  items_discounted*vd['price']
   
            amount -= items_discounted * vd['number']
            print(total)
        
        total += amount * item['unit_price']

    return total