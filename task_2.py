def return_middle(triplet: list):
    '''Returns the index of the median element of a triplet.'''
    assert len(triplet) == 3 
    return triplet.index(sorted(triplet)[1])