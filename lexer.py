# lexer.py

import re

TOKENS = [
    ("NUMBER", r"\d+"),
    ("IDENTIFIER", r"[a-zA-Z_]\w*"),
    ("STRING", r"\".*?\""),
    ("OP", r"[+\-*/%]"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COLON", r":"),
    ("EQUALS", r"="),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
]

KEYWORDS = {
    "perulangan", "dari", "sampai",
    "jika", "selain", "itu",
    "bukti", "berhenti:",
    "hasil", "jelaskan:"
}

def lex(code):
    tokens = []
    pos = 0

    while pos < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                text = match.group(0)
                if token_type == "IDENTIFIER" and text in KEYWORDS:
                    tokens.append((text.upper(), text))
                elif token_type != "SKIP":
                    tokens.append((token_type, text))
                pos = match.end(0)
                break
        if not match:
            raise SyntaxError(f"Token tidak dikenal: {code[pos]}")
    return tokens
