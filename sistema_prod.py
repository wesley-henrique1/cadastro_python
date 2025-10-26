"""
nome: Wesley Henrique Ferreira de Oliveira
Universidade: Estácio
Matricula: 202502189801
Turma: PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON (VIV0160/13758617 / 2025.2 AO VIVO) 3009
tema: Gerenciamento logistico

"""



# variavel para armazenar os dados de exemplo
base_dados = [
    {"COD": 8000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59, "ESTOQUE": 15000, "VENDA": 150},
    {"COD": 8001, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99, "ESTOQUE": 150, "VENDA": 280},
    {"COD": 8002, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59, "ESTOQUE": 3, "VENDA": 200},
    ]

# função auxiliares
"""Função para padronizar a facilitar as divisão"""
def divisor_op():
    print("-" * 114)

"""Função para auxiliar a validação de erros do try-except"""
def validar_erro(e):
    if isinstance(e, TypeError):
        return f"TypeError: Operação inválida. Tentativa de usar tipos de dados incompatíveis. Mensagem original: {e}"
    elif isinstance(e, ValueError):
        return f"ValueError: Dado inválido. O valor não pode ser convertido (Ex: vírgula em número ou data errada). Mensagem original: {e}"
    else:
        return f"Ocorreu um erro inesperado: {e}"

"""Função: vai capturar os dados do usario tratar de acordo com o tipo de dados, se ele e str, int ou float"""
def obter_valor(prompt, tipo_dado):
    while True:
        try:
            # solicitação dos dados e armazenando em variavel para comparação
            valor_str = input(prompt).strip()

            # verificando se o tipo de dado e 'str' se for igual transforma todas as letras em maiusculo
            if tipo_dado == str:
                return valor_str.upper()

            """
            antes de passar para segunda verificação fiz o tratamento de dados para numeros e valores afim de evitar erros de converção por exemplo 4.890,00 onde vai travar se tentar converter para int ou float
            """
            # vai validar se existe ',' e '.' no argumento 
            if "," in valor_str and "." in valor_str:
                valor_str = valor_str.replace(".", "")
                valor_str = valor_str.replace(",", ".")
                # retira os '.' e logo depois troca os ',' para '.' ficando o valor em 4890.00

            # se a condição anterior for falsa então vai validar se tem ',' e não tiver '.'
            elif "," in valor_str and "." not in valor_str:
                valor_str = valor_str.replace(",", ".")

            # aqui vai continua a comparação nos tipo de dados 
            if tipo_dado == int:
                # para evitar qualquer quebra de valor convertir para float depois para inteiro
                return int(float(valor_str))
            elif tipo_dado == float:
                return float(valor_str)

        except Exception as e:
            error = validar_erro(e)
            print(f"Obter valores: {error}\n")

"""Função: com os dados tratado no obter_valor() vai adicionar os registro na base de dados"""
def cadastrar(desc, fator, emb, rua, pr, nvl, apto, vl):
    # com os argumentos passados no paramentros vai fazer as validação abaixo
    # aqui vai fazer as concatenação para forma o endereço, logo em seguida vai validar se o endereço ja foi cadastrado
    end = str(rua) + "-" + str(pr) + "-" + str(nvl) + "-" + str(apto)
    end_existe = [produto['ENDERECO'] for produto in base_dados]
    if end in end_existe:
        print(f"\nERRO: Endereço ja cadastrado.")
        return
    
    # aqui vai extrair todos os codigos da base e passar paras condições
    cod_existe = [produto['COD'] for produto in base_dados]
    # se existir registro na lista vai pegar o maior codigo cadastrado e somar com + 1 criando um indentificador, se não vai iniciar com 8000
    if cod_existe:
        cod = max(cod_existe) + 1
    else:
        cod = 8000
    
    # nessa parte aqui estou criando um dicionario com os argumentos passados. coloquei None nas colunas 'ESTOQUE' e 'VENDA' para ficar vazio
    novo_registro = {
        "COD": cod,
        "DESCRICAO": desc,
        "FATOR": fator,
        "EMBALAGEM": emb,
        "ENDERECO": end,
        "PRECO": vl,
        "ESTOQUE": 0,
        "VENDA": 0
    }

    # depois de ter criado o dicionario fiz uma apresentação para informar os valores cadastrado na horas
    print("\nCadastro finalizado!!!")  
    print("produto cadastrado:") 

    divisor_op()
    # aqui utilizei o f-string para fazer uma apresentação mais organizada, alinhando os texto na esquerda e dando espaçamento
    print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<12}")
    print(
        f"{cod:<7}",
        f"{desc:<35}",
        f"{fator:<8}",
        f"{emb:<12}"
        f"{end:<15}",
        f"R$ {vl:<12.2f}"
    )
    divisor_op()

    # aqui utilizei um input para pausar o loop e  da tempo pro usuario validar as informação, e adicionando os registro na lista(base  de dados)
    divisor_op()
    input("Precione 'enter' para continuar...")
    divisor_op()
    return base_dados.append(novo_registro)

"""Função: vai listar todos os dados cadastrados na base"""
def listar():
    try:
        # valida se a base de dados esta vazio e mostra a as colunas pro usuario
        if not base_dados:
            print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10} {'VENDA':<12} {"ESTOQUE":<12}")
            divisor_op()
            print("\nsem produtos cadastrados!!\n")
            divisor_op()
            return

        print("\nprodutos cadastrados.\n")
        print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10} {'VENDA':<12} {"ESTOQUE":<12}")
        divisor_op()
        # cria um lop pegando os produtos e passando pro print
        for produto in base_dados:
            print(
                f"{produto['COD']:<7}",
                f"{produto['DESCRICAO']:<35}",
                f"{produto['FATOR']:<8}",
                f"{produto['EMBALAGEM']:<12}"
                f"{produto['ENDERECO']:<15}",
                f"R$ {produto['PRECO']:<10.2f}",
                f"{produto['VENDA']:<12}",
                f"{produto['ESTOQUE']:<12}\n",
            )
        divisor_op()
    

        divisor_op()
        input("Precione 'enter' para continuar...")
        divisor_op()
    except Exception as e:
        error = validar_erro(e)
        print(f"escolhas: {error}")

"""Função: vai buscar o argumento passado no paramentro"""
def buscar(procx):
    # aqui criei uma variavel de validação para iniciar o loop
    prod_encotrado = False
    for produto in base_dados:
        # com o os dicionario passado para a variavel 'produto' valida se o argumento passado no parametro esteja na base de dados
        if procx == produto['COD']:
            prod_encotrado = True
            print("\nprodutos cadastrados.\n")
            print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10} {'VENDA':<12} {"ESTOQUE":<12}")
            divisor_op()
            print(
                f"{produto['COD']:<7}",
                f"{produto['DESCRICAO']:<35}",
                f"{produto['FATOR']:<8}",
                f"{produto['EMBALAGEM']:<12}"
                f"{produto['ENDERECO']:<15}",
                f"R$ {produto['PRECO']:<10.2f}",
                f"{produto['VENDA']:<12}",
                f"{produto['ESTOQUE']:<12}\n",
            )
            divisor_op()
            return
    
    # Se o produto não foi encontrado (flag False), exibe uma mensagem de aviso        
    if not prod_encotrado:
        print(f"aviso: o codigo {procx} não foi encotrado na base de dados")

    divisor_op()
    input("Precione 'enter' para continuar...")
    divisor_op()

"""Função: vai remover o argumento passado no paramentro"""
def remover(lista, produto):
    prod_encotrado = False
    # iniciando um for onde extrair cada dicionario da lista principal e valida que existe o valor passado no parametro 'produto' depois excluir da lista
    for i, dic in enumerate(lista):
        if dic['COD'] == produto:
            prod_encotrado = True
            lista.pop(i)
            print("\nProduto removido com sucesso!")
            listar()
            return  lista

    if not prod_encotrado:
        print("\nProduto não encotrado...")
        listar()

    divisor_op()

"""Função: vai atualizar qualquer registro definido"""
def atualizar(procx):
    prod_encotrado = False
    for produto in base_dados:
        # inicia o loop validando se o produto exite no dicionario
        if procx == produto['COD']:
            prod_encotrado = True
            # utliza a função buscar() para mostrar o produto para alteração e da inicio a outra função.
            buscar(procx)
            escolha = menu(2)
            # nas condição valida qual função esta correta e faz a atualização 
            if escolha == 1:
                produto['DESCRICAO'] = obter_valor("descrição: ", str)
                
            elif escolha == 2:
                produto['FATOR'] = obter_valor("fator de converção: ", int)

            elif escolha == 3:
                produto['EMBALAGEM'] = obter_valor("Embalagem ex: CX/024/PT, UN/001/UN: ", str)

            elif escolha == 4:
                rua = obter_valor("Rua: ", int)
                pr = obter_valor("Predio: ", int)
                nvl = obter_valor("Nivel: ", int)
                apto = obter_valor("Apartamento: ", int)

                end = str(rua) + "-" + str(pr) + "-" + str(nvl) + "-" + str(apto)
                end_existe = [produto['ENDERECO'] for produto in base_dados]

                if end in end_existe:
                    print(f"\nERRO: Endereço ja cadastrado.")
                    return
                    
                produto['ENDERECO'] = end

            elif escolha == 5:
                produto['PRECO'] = obter_valor("Preço para venda: ", float)
            elif escolha == 0:
                print("Retornando para o menu.\n\n")
                return
            else:
                print("\nNumero invalido valor digitar o numero correspodente a opção desejada.\n") 


    if not prod_encotrado:
        print(f"aviso: o codigo {procx} não foi encotrado na base de dados")
        divisor_op()
        input("Precione 'enter' para continuar...")
        divisor_op()
    else:
        print("Produto alterado com sucesso!!!")
        buscar(procx)

"""Função: vai atualiza os campos 'ESTOQUE' e 'VENDA' """
def lançamento(procx):
    prod_encotrado = False
    for produto in base_dados:
        if produto['COD'] == procx:
            prod_encotrado = True
            buscar(procx)

            escolha = menu(3)

            if escolha == 1:
                # aqui simula um recebimento de mercadoria
                estoque = obter_valor("Informe a quantidade recebida: ", int)
                produto['ESTOQUE'] = produto['ESTOQUE'] + estoque

                print("Lançamento finalizado com sucesso!!!")
                buscar(procx)
                divisor_op()
                input("Precione 'enter' para continuar...")
                divisor_op()
                break

            elif escolha == 2:
                # aqui simulei uma venda de mercadoria onde cada venda da saida do estoque
                if produto["ESTOQUE"] > 0:
                    venda = obter_valor("Informe a quantidade vendida: ", int)
                    produto['VENDA'] = produto['VENDA'] + venda
                    produto['ESTOQUE'] = produto['ESTOQUE'] - venda

                    print("Lançamento finalizado com sucesso!!!")
                    buscar(procx)
                    divisor_op()
                    input("Precione 'enter' para continuar...")
                    break
                else:
                    print("produto sem estoque favor alimente o estoque...")
                    divisor_op()
                    input("Precione 'enter' para continuar...")
                    divisor_op()


    if not prod_encotrado:
        print(f"aviso: o codigo {procx} não foi encotrado na base de dados")
        divisor_op()
        input("Precione 'enter' para continuar...")
        divisor_op()

"""Função: armazena os menus do script"""
def menu(id):
    """nessa função armazenei todos os menu utilizado no scripts """
    try:
        # menu principal
        if id == 1:
            print("\n")
            print(
                f"{"MENU":-^36}\n",
                f"{"1 - Cadastrar produto":<36}\n",
                f"{"2 - listagem base de dados":<36}\n",
                f"{"3 - Consulta":<36}\n",
                f"{"4 - Remover produto":<36}\n",
                f"{"5 - Alterar produto":<36}\n",
                f"{"6 - Estatus estoque":<36}\n",
                f"{"7 - Lançamentos":<36}\n",

                f"{"0 - Sair":<36}")
            
            escolha = obter_valor("Digite o numero da opção desejada: \n", int)
            divisor_op()
            return escolha
        
        # menu da função atualizar()
        elif id == 2:
            print("\n")
            print(
                f"{"OPÇÕES DE ATUALIZAÇÃO":-^36}\n",
                f"{"1 - DESCRIÇÃO.":<36}\n",
                f"{"2 - FATOR.":<36}\n",
                f"{"3 - EMBALAGEM.":<36}\n",
                f"{"4 - ENDEREÇO.":<36}\n",
                f"{"5 - PREÇO.":<36}\n",
                f"{"0 - VOLTAR PARA O MENU":<36}")
            
            escolha = obter_valor("Digite o numero da opção desejada: \n", int)
            return escolha
        
        # menu da função lançamento()
        elif id == 3:
            print("\n")
            print(
                f"{"LANÇAMENTO DE MERCADORIA":-^36}\n",
                f"{"1 - RECEBIMENTO.":<36}\n",
                f"{"2 - VENDA.":<36}\n",
                f"{"0 - VOLTAR PARA O MENU":<36}")
            
            escolha = obter_valor("Digite o numero da opção desejada: \n", int)
            return escolha

    except Exception as e:
        error = validar_erro(e)
        print(f"menu: {error}")

"""Função: mostra o status do estoque: valor de estoque, media e etc"""
def status():
    # criando uma função para auxiliar na apresentação
    def prinft(listar,prompt):
        print(f"\nProduto com {prompt} estoque:")
        print(f"{listar['COD']}-{listar['DESCRICAO']} valor estoque: R$ {listar['valor_estoque']:.2f}")

    # aqui valida se existe registro na base de dados, para não travar nas aplicação abaixo
    if not base_dados:
        print("Base de dados vazia...")
        return
    for produto in base_dados:
        # inicia a extração dos dicionario e cria uma coluna para apresentação
        produto['valor_estoque'] = produto['PRECO'] * produto['ESTOQUE']

    # faz a contagem dos registros
    list_prod = [prod['COD'] for prod in base_dados]
    qtde_prod = len(list_prod)

    # faz a soma dos valores e depois cria uma media 
    list_vl_st = [vl_st['valor_estoque'] for vl_st in base_dados]
    qtde_vl_st = sum(list_vl_st)
    avg_vl = qtde_vl_st / qtde_prod

    # puxa os valores com maior e o menor valor estoque
    prod_maior_vl = max(base_dados, key=lambda produto: produto['valor_estoque'])
    prod_menor_vl = min(base_dados, key=lambda produto: produto['valor_estoque'])

    # inicia a demostração 
    divisor_op()
    print(f"{"Demostrativo":-^92}")
    print(f"Total de produto cadastrado: {qtde_prod}")
    print(f"Estoque em R$: R$ {qtde_vl_st:.2f}")
    print(f"Media valor estoque: R$ {avg_vl:.2f}")

    prinft(prod_maior_vl, "maior")
    prinft(prod_menor_vl, "menor")
    divisor_op()

    divisor_op()
    input("Precione 'enter' para continuar...")
    divisor_op()

"""Função principal onde faz a chamada das função auxiliar"""
def main():
    print("\n" *4)
    print(f"{"sistema logistico":-^92}")
    print("\nBem vindo ao sistema logistico\n")


    # iniciando com um loop com o menu principal 
    while True:
        escolha = menu(1)
        try:
            if escolha == 1:
                try:
                    # aqui estou solicitando os paramentros para função cadastro
                    print("\n\ncadastro de produtos")
                    print("\nFavor informar os campos abaixo\n")
                    desc = obter_valor("descrição: ", str)
                    fator = obter_valor("fator de converção: ", int)
                    emb = obter_valor("Embalagem ex: CX/024/PT, UN/001/UN: ", str)
                    rua = obter_valor("Rua: ", int)
                    pr = obter_valor("Predio: ", int)
                    nvl = obter_valor("Nivel: ", int)
                    apto = obter_valor("Apartamento: ", int)
                    vl = obter_valor("Preço para venda: ", float)
                    
                    # verifica se algum parametro esta vazio
                    if None in [desc, fator, emb, rua, pr, nvl, apto, vl]:
                        print("\nCadastro cancelado devido a uma entrada inválida.")
                    else:
                        # inicia a função cadastro
                        cadastrar(desc, fator, emb, rua, pr, nvl, apto, vl) 
                except Exception as e:
                    error = validar_erro(e)
                    print(f"menu-1: {error}\n")

            elif escolha == 2:
                print("\nlistagem de produtos cadastrados\n")
                # chamada da função listar
                divisor_op()
                listar()   

            elif escolha == 3:
                print("\n\nConsulta de produtos")
                divisor_op()
                # solicita o codigo para fazer a busca e chama a função buscar
                procx = obter_valor("\nInforme codigo do produto: \n", int)
                buscar(procx)

            elif escolha == 4:
                print("\n\nRemoção de produto")
                divisor_op()
                procx = obter_valor("\nfavor digite o codigo do produto para remoção:\n", int)
                # aqui eu eu queria mostrar que da para informar diretamente os parametros passando em outras ordem 
                remover(produto= procx, lista= base_dados)

            elif escolha == 5:
                print("\n\nAlterar cadastros")
                # chamada da função atualizar
                procx = obter_valor("\nInforme o codigo do produto para alteração: \n", int)
                atualizar(procx)

            elif escolha == 6:
                print("\n\nestatus de estoque")
                # chamada da função status
                status()

            elif escolha == 7:
                print("\n\nLançamentos")
                # chamada da função lançamento
                procx = obter_valor("\nInforme codigo do produto: \n", int)
                lançamento(procx)

            elif escolha == 0:
                print('\n\n')
                divisor_op()
                # finaliza o loop
                print("Obrigado por utilizar o sistema logistico!!!!")
                print('\n')
                break

            else:
                print("\nNumero invalido valor digitar o numero correspodente a opção desejada.\n") 

        except Exception as e:
            error = validar_erro(e)
            print(f"escolhas: {error}")
            break

if __name__ == "__main__":
    main()
    input("Selecione entre para sair...")  