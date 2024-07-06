symbol_to_name = {
    '%': 'percent',
    '$': 'dollar',
    '&': 'ampersand',
    '@': 'at',
    '#': 'hashtag',
    '!': 'exclamation mark',
    '?': 'question mark',
    '*': 'asterisk',
    '(': 'left parenthesis',
    ')': 'right parenthesis'
}

def get_name(symbol):
    return symbol_to_name.get(symbol, 'unknown symbol')