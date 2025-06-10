from lexico import lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def match(self, expected_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
            return True
        return False

    def expect(self, expected_type):
        if not self.match(expected_type):
            atual = self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '', -1)
            raise SyntaxError(f"Linha {atual[2]}: Esperado {expected_type}, mas encontrou {atual[0]} ({atual[1]!r})")

    def parse(self):
        while self.pos < len(self.tokens):
            tipo, valor, _ = self.tokens[self.pos]
            if tipo == 'KEYWORD' and valor == 'inicio':
                self.parse_inicio()
            elif tipo == 'KEYWORD' and valor == 'mensagem':
                self.parse_mensagem()
            elif tipo == 'KEYWORD' and valor == 'fluxo':
                self.parse_fluxo()
            elif tipo == 'KEYWORD' and valor == 'fim':
                print("Fim do fluxo.")
                self.pos += 1
            else:
                print(f"Ignorando token inesperado: {tipo}, {valor}")
                self.pos += 1

    def parse_inicio(self):
        """Analisa o bloco 'inicio:'"""
        print("Iniciando fluxo principal")
        self.expect('KEYWORD')
        self.expect('COLON')

    def parse_mensagem(self):
        """Analisa bloco de mensagem e seus botões"""
        print("Detectado bloco de mensagem")
        self.expect('KEYWORD')
        self.expect('COLON')
        if self.match('STRING'):
            print("\u2192 Texto da mensagem detectado.")
        while self.pos < len(self.tokens):
            tipo, valor, _ = self.tokens[self.pos]
            if tipo == 'KEYWORD' and valor == 'botao':
                self.parse_botao()
            else:
                break

    def parse_botao(self):
        """Analisa um botão: botao NUM: "texto" -> identificador"""
        print("\u2192 Botão detectado")
        self.expect('KEYWORD')
        self.expect('NUMBER')
        self.expect('COLON')
        self.expect('STRING')
        self.expect('ARROW')
        self.expect('IDENT')

    def parse_fluxo(self):
        """Analisa a definição de um fluxo nomeado"""
        print("Iniciando novo fluxo")
        self.expect('KEYWORD')
        self.expect('IDENT')
        self.expect('COLON')
