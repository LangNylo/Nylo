# 🌊 | Nylo
### DOCUMENTAÇÃO COMPLETA
#### 📌 Atualizada toda semana

### INTEGRANTES DO GRUPO
#### 1️⃣ ‣ Breno Marcelo de Oliveira Barbosa
#### 2️⃣ ‣ Danilo de Sousa Gonçalves
#### 3️⃣ ‣ Guilherme Lima Fontana
#### 4️⃣ ‣ Lucas Araujo Silva
#### 5️⃣ ‣ Pedro Ferreira Gomes
#### 6️⃣ ‣ Welinton Thiago Fechi Sandrin

### DESCRIÇÃO DA LINGUAGEM
#### 🤖 - A proposta consiste no desenvolvimento de uma linguagem própria voltada à criação de conversas automáticas, semelhantes a um chatbot, mas com foco em mensagens padronizadas, amigáveis e organizadas em fluxos pré-definidos, guiados por decisões do usuário por meio de botões interativos.

#### 🔗 - A ideia central é permitir que, ao final da construção do fluxo conversacional, seja gerado um link exclusivo que redireciona o usuário para a versão final do chatbot. Esse link poderá ser compartilhado livremente, permitindo que diferentes pessoas utilizem o sistema de forma direta, sem necessidade de instalação ou configuração adicional.

#### 🖥️ - Para facilitar o uso, especialmente por pessoas com conhecimentos básicos em tecnologia, pretende-se disponibilizar uma plataforma web onde os fluxos possam ser montados de forma intuitiva, acessível e compatível com qualquer navegador, eliminando a necessidade de configurações locais complexas.

#### 💼 - Essa solução é pensada especialmente para micro e pequenas empresas que não desejam investir em sistemas robustos e caros de atendimento ao cliente. A linguagem será projetada com simplicidade e objetividade, permitindo que o próprio empreendedor ou um colaborador com noções básicas de programação seja capaz de estruturar o atendimento de maneira funcional e eficaz.

##### Obs.: (A iniciativa surgiu a partir de uma necessidade prática observada em um negócio próprio de um integrante, o que reforça o potencial real de aplicabilidade da ferramenta no dia a dia de empresas de pequeno porte.)

### TOKENS DA LINGUAGEM
| Tipo de Token         | Nome Técnico | Exemplo                                              | Regex (versão ajustada)                             |
|-----------------------|--------------|------------------------------------------------------|-----------------------------------------------------|
| **Palavra-chave**     | `KEYWORD`    | `mensagem`, `botao`, `fluxo`, `inicio`, `fim`, `ir_para` | `\b(mensagem ou botao ou fluxo ou inicio ou fim ou ir_para)\b`      |
| **Identificadores**   | `IDENT`      | `inicio_atendimento`, `duvida_produto`              | `[a-zA-Z_] ou [a-zA-Z0-9_]*`                             |
| **Texto literal**     | `STRING`     | `"Olá! Como posso te ajudar?"`                      | `"([^"\\\n]\\.)*"`                                  |
| **Números inteiros**  | `NUMBER`     | `1`, `2`                                             | `\d+`                                               |
| **Dois pontos**       | `COLON`      | `:`                                                  | `:`                                                 |
| **Setas**             | `ARROW`      | `->`                                                 | `->`                                                |
| **Delimitadores**     | `NEWLINE`    | (quebra de linha)                                   | `\n`                                                |
| **Comentário**        | `COMMENT`    | `# isso é um comentário`                            | `#.*`                                               |
| **Espaço/tabulação**  | `WHITESPACE` | ` `, `\t`                                            | `[ \t]+` (ignorar ou usar para indentação)          |

##### EXEMPLO DE CÓDIGO
  `inicio:`
  
    mensagem: "Olá! Bem-vindo ao nosso atendimento."
    
    botao: "Quero saber mais" -> mais_info
    
    botao: "Falar com atendente" -> atendimento_humano
  
  `fluxo mais_info:`
  
      mensagem: "Nosso produto é top, veja só!"
      
      botao: "Voltar" -> inicio
  
  `fluxo atendimento_humano:`
  
      mensagem: "Ok! Vamos te redirecionar para um atendente humano."
      
      fim
