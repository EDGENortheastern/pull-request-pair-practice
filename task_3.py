def mystery_func(ss):
    '''Returns the set of words in ss.'''
    words = ss.split(' ')
    seen_words = []
    for word in words:
        if word not in seen_words:
            seen_words.append(word)
    return ' '.join(seen_words)
    