Trabalho de Iniciação à Programação em Python
Trabalho de Iniciação à Programação em Python
Tema: Sistema de Cadastro com Funções (tema livre)
1) Objetivos de aprendizagem
Praticar entrada e saída de dados (input/print).
Utilizar listas e dicionários como estruturas de dados.
Projetar e reutilizar funções (com parâmetros, retorno e escopo).
Aplicar validação de dados e tratamento simples de erros.
Organizar o código em módulo principal (main) e funções auxiliares.
2) Descrição geral
Cada aluno deverá escolher um tema livre e implementar um sistema básico baseado em funções. O tema pode ser, por exemplo:
Sistema escolar (cadastro de alunos, notas e disciplinas)
Sistema de supermercado (cadastro de produtos e controle de estoque)
Sistema de biblioteca (cadastro de livros e empréstimos)
Sistema de oficina (cadastro de veículos e serviços)
Sistema de clínica (cadastro de pacientes e consultas)
O sistema deve ser baseado em funções e permitir cadastrar, listar, buscar, atualizar e remover registros, conforme o contexto do tema escolhido.
3) Requisitos obrigatórios (MVP – 70%)
Estrutura de dados: use uma lista de dicionários, ex.: registros = [{"nome": "Ana", "idade": 21}, ...].
Funções mínimas:
<menu()> → exibe opções e retorna a escolha do usuário.
<cadastrar()> → adiciona novo registro.
<listar()> → imprime todos os registros cadastrados.
<buscar()> → busca um registro pelo nome ou outro campo.
<remover()> → remove um registro.
<atualizar()> → atualiza campos de um registro.
<main()> → laço principal que organiza o fluxo do programa.
Validação de dados:
Evitar campos vazios.
Verificar tipos (ex: idade deve ser número inteiro, preço deve ser float, etc.).
Mensagens claras de sucesso, erro e orientações de entrada.
Prevenção de duplicatas (não permitir dois registros idênticos) ou uso de ID auto-incremental.
Busca parcial e listagem ordenada (por nome, preço, idade, etc.)
Estatísticas (total de registros, média, máximo e mínimo).
Docstrings e comentários explicativos em cada função.
EXEMPLO DE MENU DO SISTEMA

=== MENU ===
1 - Cadastrar item
2 - Listar registros
3 - Buscar
4 - Atualizar
5 - Remover
6 - Salvar em arquivo
7 - Carregar de arquivo
0 - Sair
Escolha uma opção: _
 
Entrega
Arquivo único: QUALQUER_NOME.py.
Incluir no topo: nome completo, tema, turma e data.
O programa deve executar sem erros.
 
Dicas e boas práticas
Use strip(), lower() para padronizar texto.
Quebre o problema em funções pequenas.
Escreva docstrings curtas em cada função.
Teste o código passo a passo.
Escolha um tema criativo e explore diferentes tipos de dados.
Posso usar classes? Não, o foco é funções.
Preciso tratar exceções? Simples validações com isdigit() ou try/except são suficientes.
Posso usar bibliotecas externas? Não. Apenas biblioteca padrão do Python.
 