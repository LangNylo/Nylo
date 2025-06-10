from lexico import lexer
from sintatico import Parser

if __name__ == "__main__":
    with open("codigo.nylo", "r") as f:
        codigo = f.read()

    tokens = lexer(codigo)
    parser = Parser(tokens)
    parser.parse()
