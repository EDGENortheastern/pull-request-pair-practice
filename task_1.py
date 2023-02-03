def original_price(discounted_price,sale_percentage):
    """ Returns original price"""
    original = discounted_price/(1-(sale_percentage/100))
    return round(original, 2)
    