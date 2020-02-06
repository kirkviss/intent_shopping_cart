from db.item import getItem


def get_total(cartItems: dict):
    total = 0
    for itemId, amount in cartItems.items():
        item = getItem(itemId)

        ''' sort by the lowest price ratio, guaranting that the discount with 
        the lowest price is first in the array '''
        sortedDiscounts = sorted(item['volume_discounts'],key=lambda discount: discount['number']/discount['price'])
    
        '''loop through each discount '''
        for vd in sortedDiscounts:
            items_discounted = int(amount/ vd['number'])

            # add the amount of item discounted to
            total +=  items_discounted*vd['price']
   
            amount -= items_discounted * vd['number']
        
        total += amount * item['unit_price']

    return round(total, 2) 