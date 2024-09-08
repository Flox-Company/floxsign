# floxsign/get_name_of_symbol.py
no_space = {
    ' ': 'space',
    '-': 'minus',
    '=': 'equal',
    '{': 'leftbrace',
    '}': 'rightbrace',
    '\\': 'backslash',
    ';': 'semicolon',
    '\'': 'apostrophe',
    '~': 'grave',
    ',': 'comma',
    '.': 'dot',
    '/': 'slash',
    '%': 'percent',
    '$': 'dollar',
    '&': 'ampersand',
    '@': 'at',
    '#': 'hashtag',
    '!': 'exclamationmark',
    '?': 'questionmark',
    '*': 'asterisk',
    '(': 'leftparenthesis',
    ')': 'rightparenthesis',
    '^': 'caret',
    '_': 'underscore',
    '+': 'plus',
    '[': 'leftbracket',
    ']': 'rightbracket',
    '|': 'pipe',
    ':': 'colon',
    '"': 'quote',
    '<': 'lessthan',
    '>': 'greaterthan'
}

with_space = {
    ' ': 'space',
    '-': 'minus',
    '=': 'equal',
    '{': 'left brace',
    '}': 'right brace',
    '\\': 'backslash',
    ';': 'semicolon',
    '\'': 'apostrophe',
    '~': 'grave',
    ',': 'comma',
    '.': 'dot',
    '/': 'slash',
    '%': 'percent',
    '$': 'dollar',
    '&': 'ampersand',
    '@': 'at',
    '#': 'hashtag',
    '!': 'exclamation mark',
    '?': 'question mark',
    '*': 'asterisk',
    '(': 'left parenthesis',
    ')': 'right parenthesis',
    '^': 'caret',
    '_': 'underscore',
    '+': 'plus',
    '[': 'left bracket',
    ']': 'right bracket',
    '|': 'pipe',
    ':': 'colon',
    '"': 'quote',
    '<': 'less than',
    '>': 'greater than'
}

def with_space(symbol):
    if with_space.get(symbol, 'unknown symbol') == 'unknown symbol':
        print("error: unknown symbol")
    return with_space.get(symbol, 'unknown symbol')
        

def with_no_space(symbol):
    if no_space.get(symbol, 'unknown symbol') == 'unknown symbol':
        print("error: unknown symbol")
    return no_space.get(symbol, 'unknown symbol')
