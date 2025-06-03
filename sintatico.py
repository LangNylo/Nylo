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
			atual = self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '')
			raise SyntaxError(f"Esperado {expected_type}, mas encontrou {atual}")

	def parse(self):
		while self.pos < len(self.tokens):
			tipo, valor = self.tokens[self.pos]
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
		print("Iniciando fluxo principal")
		self.expect('KEYWORD')
		self.expect('COLON')

	def parse_mensagem(self):
		print("Detectado bloco de mensagem")
		self.expect('KEYWORD')
		self.expect('COLON')
		if self.match('STRING'):
			print("→ Texto da mensagem detectado.")
		while self.pos < len(self.tokens):
			if self.tokens[self.pos][0] == 'KEYWORD' and self.tokens[self.pos][1] == 'botao':
				self.parse_botao()
			else:
				break

	def parse_botao(self):
		print("→ Botão detectado")
		self.expect('KEYWORD')  # botao
		self.expect('NUMBER')   # número
		self.expect('COLON')
		self.expect('STRING')
		self.expect('ARROW')
		self.expect('IDENT')

	def parse_fluxo(self):
		print("Iniciando novo fluxo")
		self.expect('KEYWORD')  # fluxo
		self.expect('IDENT')    # nome do fluxo
		self.expect('COLON')

if __name__ == "__main__":
	codigo = '''

	inicio:

	mensagem:
		"Olá! Que bom ver você por aqui."
			botao 1:
				"Quero saber mais" -> mais_info
			botao 2:
				"Falar com alguém" -> atendimento_humano

	fluxo mais_info:
		mensagem:
			"Nosso produto é top. Veja só!"

	fluxo atendimento_humano:
		mensagem:
			"Já vou chamar alguém para você..."

	fim

	'''

	tokens = lexer(codigo)
	parser = Parser(tokens)
	parser.parse()
