from lexer import Lexer, Token
from version import Version

class CPException(Exception):
    def __init__(self, message: str) -> str:
        super().__init__(message)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def adv(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        # Entry point for parsing
        return self.parse_statements()

    def parse_statements(self):
        statements = []
        while self.current_token is not None:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements

    def parse_statement(self):
        # Example starting point
        if self.current_token.type == 'IF':
            return self.parse_if_statement()
        if self.current_token.type == 'ALT':
            return self.parse_alt_statement()
        else:
            self.advance()  # Skip unknown tokens for now
            return None

    def parse_if_statement(self):
        # Assume current_token is IF
        self.advance()  # Move past IF

        # Expect '('
        if self.current_token.type != 'LPAREN':
            raise CPException("ERROR!\nMissing '(' before statement condition.\nError code MS-LPAREN")
        self.advance()

        # Parse condition (simplified for now)
        condition = self.parse_expression()

        # Expect ')'
        if self.current_token.type != 'RPAREN':
            raise CPException("ERROR!\nMissing ')' after statement condition.\nError code MS-RPAREN")
        self.advance()

        # Expect '{'
        if self.current_token.type != 'LBRACE':
            raise CPException("ERROR!\nMissing '{' before statement body.\nError code MS-LBRACE")
        self.advance()

        # Parse body (simplified: list of statements)
        body = self.parse_statements()

        # Expect '}'
        if self.current_token.type != 'RBRACE':
            raise CPException("ERROR!\nMissing '}' after statement body.\nError code MS-RBRACE")
        self.advance()

        return {'type': 'if_statement', 'condition': condition, 'body': body}
    
    def parse_alt_statement(self):
        # Assume current token is ALT
        self.advance()  # Move past ALT

        # Expect '{'
        if self.current_token.type != 'LBRACE':
            raise CPException("ERROR!\nMissing '{' before statement body.\nError code MS-LBRACE")
        self.advance()

        # Parse the statements inside the alt block
        body = self.parse_statements()

        # Expect '}'
        if self.current_token.type != 'RBRACE':
            raise CPException("ERROR!\nMissing '}' after statement body.\nError code MS-RBRACE")
        self.advance()

        return {'type': 'alt_statement', 'body': body}
    
    def parse_as_loop(self):
        #Assume current token is ALT
        self.advance() #Move past ALT

        #Expect '('
        if self.current_token.type != 'LPAREN':
            raise CPException("ERROR!\nMissing '(' before statement condition.\nError code MS-LPAREN")
        self.advance()

        #Parse condition(simplified for now)
        condition = self.parse_expression()

        if self.current_token.type != "RPAREN":
			raise CPException("ERROR!\nMissing ')' after statement condition.\nError code MS-RPAREN")
		self.advance()

		if self.current_token.type != "LBRACE":
			raise CPException("ERROR!\nMissing ')' after statement condition.\nError code MS-LBRACE")
		self.advance()

		#Parse statements inside body
		body = self.parse_statements()

		if self.current_token.type != "RBRACE":
			raise CPException("ERROR!\nMissing ')' after statement condition.\nError code MS-RBRACE")
		self.advance()

		return {'type': 'as_loop', 'condition': condition, 'body': body}

	def parse_for_loop(self):
		
          
    def parse_expression(self):
        # Simplify: just parse an identifier or number for now
        token = self.current_token
        if token.type in ('IDENTIFIER', 'INT', 'FLOAT'):
            self.advance()
            return token
        else:
            raise Exception("Expected expression")


