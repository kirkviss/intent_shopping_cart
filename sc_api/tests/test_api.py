import sys, os
# sys.path.append('/home/kirk/Code/intent_assignment/api')
# sys.path.append('../'+ os.path.dirname(os.path.abspath(__file__))

print (sys.path)
import pytest
#from api.shopping_chart_trolly import Shopping_Chart_Trolly
from bin.shopping_cart_trolly import Shopping_Cart_Trolly

# test the instantiation of a shopping_cart
def test_create_shopping_cart_trolly():
    test_sc_trolly = Shopping_Cart_Trolly()

    assert test_sc_trolly
