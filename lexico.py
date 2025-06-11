import re  # Importa o módulo de expressões regulares

# Lista com as definições de tokens (tipo e padrão de correspondência)
TOKEN_SPECIFICATION = [
    ('KEYWORD',    r'\b(mensagem|botao|fluxo|inicio|fim|ir_para)\b'),  # Palavras-chave da linguagem
    ('IDENT',      r'[a-zA-Z_][a-zA-Z0-9_]*'),                         # Identificadores (nomes de variáveis, fluxos etc.)
    ('STRING',     r'"([^"\\n]|\\.)*"'),                               # Cadeias de texto (entre aspas)
    ('NUMBER',     r'\d+'),                                            # Números inteiros
    ('COLON',      r':'),                                              # Dois-pontos
    ('ARROW',      r'->'),                                             # Seta para indicar transição
    ('NEWLINE',    r'\n'),                                             # Quebra de linha
    ('COMMENT',    r'#.*'),                                            # Comentário (linha iniciada com #)
    ('WHITESPACE', r'[ \t]+'),                                         # Espaços e tabulações
    ('MISMATCH',   r'.'),                                              # Qualquer outro caractere (erro)
]

# Função para fazer a análise léxica (tokenização)
def lexer(codigo):
    # Combina todos os padrões de token em uma única expressão regular
    token_regex = '|'.join(f'(?P<{nome}>{regex})' for nome, regex in TOKEN_SPECIFICATION)
    linha = 1  # Contador de linha para mensagens de erro
    for match in re.finditer(token_regex, codigo):  # Itera sobre cada correspondência no código
        tipo = match.lastgroup  # Tipo de token identificado
        valor = match.group()   # Valor literal do token

        if tipo == 'NEWLINE':
            linha += 1  # Incrementa linha ao encontrar quebra
            continue
        elif tipo in ('WHITESPACE', 'COMMENT'):
            continue  # Ignora espaços em branco e comentários
        elif tipo == 'MISMATCH':
            # Gera erro se caractere não reconhecido
            raise RuntimeError(f"Linha {linha}: Caractere inválido {valor!r}")
        yield (tipo, valor, linha)  # Retorna o token como uma tupla (tipo, valor, linha)
