from lexico import lexer
from sintatico import Parser

def testar_lexer():
    print("Testando lexer...")
    codigo = 'mensagem: "Oi!"'
    tokens = list(lexer(codigo))
    assert tokens[0][0] == 'KEYWORD'
    assert tokens[1][0] == 'COLON'
    assert tokens[2][0] == 'STRING'
    print("Lexer OK")

def testar_parser():
    print("Testando parser...")
    codigo = '''
    inicio:
    mensagem:
        "Olá!"
        botao 1: "Ir" -> destino
    fim
    '''
    tokens = lexer(codigo)
    parser = Parser(tokens)
    parser.parse()
    print("Parser OK")

if __name__ == "__main__":
    testar_lexer()
    testar_parser()
