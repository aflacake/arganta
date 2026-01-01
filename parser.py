# parser.py

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", "")

    def eat(self, type_):
        if self.current()[0] == type_:
            self.pos += 1
        else:
            raise SyntaxError(f"Diharapkan {type_}, dapat {self.current()}")

    def parse_program(self):
        statements = []
        while self.current()[0] != "EOF":
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        tok = self.current()[0]

        if tok == "IDENTIFIER":
            return self.parse_assignment()
        elif tok == "PERULANGAN":
            return self.parse_loop()
        elif tok == "BUKTI":
            return self.parse_proof()
        elif tok == "HASIL":
            return self.parse_output()
        else:
            raise SyntaxError(f"Pernyataan tidak dikenal: {tok}")
