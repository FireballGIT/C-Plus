from version import Version

version = Version()
version.setVersion(1.1, 1)

class Lexer:
    SINGLE_CHAR_TOKENS = {
        '(': 'LPAREN',
        ')': 'RPAREN',
        '{': 'LBRACE',
        '}': 'RBRACE',
        '+': 'PLUS',
        '-': 'MINUS',
        '*': 'MULTIPLY',
        '/': 'DIVIDE',
        '=': 'EQUALS',
        ';': 'SEMICOLON',
        ',': 'COMMA',
        '[': 'LBRACKET',
        ']': 'RBRACKET'
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def generate_tokens(self):
        tokens = []

        while self.current_char is not None:
            # Skip whitespace
            if self.current_char.isspace():
                self.advance()

            # Identifiers & keywords
            elif self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self._generate_identifier())

            # Numbers
            elif self.current_char.isdigit():
                tokens.append(self._generate_number())

            # Multi-char tokens like '==' or '!='
            elif self.current_char == '=':
                tokens.append(self._generate_equals())

            # Single-char tokens
            elif self.current_char in self.SINGLE_CHAR_TOKENS:
                token_type = self.SINGLE_CHAR_TOKENS[self.current_char]
                tokens.append(Token(token_type, self.current_char))
                self.advance()

            else:
                raise Exception(f"Illegal character '{self.current_char}'")

        return tokens

    def _generate_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        token_type = KEYWORDS.get(result, 'IDENTIFIER')
        return Token(token_type, result)

    def _generate_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if dot_count == 1:  # Only one dot allowed in float
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token('INT', int(num_str))
        else:
            return Token('FLOAT', float(num_str))

    def _generate_equals(self):
        self.advance()
        if self.current_char == '=':
            self.advance()
            return Token('EQUALS_EQUALS', '==')
        else:
            return Token('EQUALS', '=')

# Token class for completeness
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

KEYWORDS = {
    'if': 'IF',
    'alt': 'ALT',
    'altoption': 'ALT_OPTION',
    'as': 'AS',
    'pass': 'PASS',
    'without': 'WITHOUT',
    'all': 'ALL',
    'return': 'RETURN',
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'bool': 'BOOL_TYPE',
    'string': 'STRING_TYPE',
    'nvp': 'NVP',
    'ratio': 'RATIO',
    'const': 'CONST',
    'let': 'LET',
}
