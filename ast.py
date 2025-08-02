class Expr:
    pass

class Binary(Expr):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator  # this is usually a Token
        self.right = right

class Unary(Expr):
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

class Literal(Expr):
    def __init__(self, value):
        self.value = value

class Grouping(Expr):
    def __init__(self, expression):
        self.expression = expression

class Variable(Expr):
    def __init__(self, token):
        self.name = token
