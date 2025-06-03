import re

TOKEN_SPECIFICATION = [
	#Palavra-chave
	('KEYWORD',    r'\b(mensagem|botao|fluxo|inicio|fim|ir_para)\b'),
	#Identificadores
	('IDENT',      r'[a-zA-Z_][a-zA-Z0-9_]*'),
	#Texto literal
	('STRING',     r'"([^"\\n]|\\.)*"'),
	#Números inteiros
	('NUMBER',     r'\d+'),
	#Dois pontos
	('COLON',      r':'),
	#Setas
	('ARROW',      r'->'),
	#Delimitadores
	('NEWLINE',    r'\n'),
	#Comentário
	('COMMENT',    r'#.*'),
	#Espaço/tabulação
	('WHITESPACE', r'[ \t]+'),
	#Qualquer coisa inesperada
	('MISMATCH',   r'.'),
]

def lexer(codigo):
	token_regex = '|'.join(f'(?P<{nome}>{regex})' for nome, regex in TOKEN_SPECIFICATION)
	linha = 1
	for match in re.finditer(token_regex, codigo):
		tipo = match.lastgroup
		valor = match.group()

		if tipo == 'NEWLINE':
			linha += 1
			continue
		elif tipo == 'WHITESPACE' or tipo == 'COMMENT':
			continue
		elif tipo == 'MISMATCH':
			raise RuntimeError(f"Caractere inválido {valor!r} na linha {linha}")
		yield (tipo, valor)
