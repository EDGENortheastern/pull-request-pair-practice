def original_price(discounted_price,sale_percentage):
    '''Returns the original price of an item.'''
    original = discounted_price/(1-(sale_percentage/100))
    return round(original, 2)