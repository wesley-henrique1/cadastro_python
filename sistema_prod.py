# variavel para armazenar os dados de exemplo
base_dados = [
    {"COD": 8000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59, "ESTOQUE": 15000, "VENDA": 150},
    {"COD": 8001, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99, "ESTOQUE": 150, "VENDA": 280},
    {"COD": 8002, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59, "ESTOQUE": 3, "VENDA": 200},
    ]

# função auxiliares
def divisor_op():
    return print("-" * 114)

def validar_erro(e):
    if isinstance(e, TypeError):
        return f"TypeError: Operação inválida. Tentativa de usar tipos de dados incompatíveis. Mensagem original: {e}"
    elif isinstance(e, ValueError):
        return f"ValueError: Dado inválido. O valor não pode ser convertido (Ex: vírgula em número ou data errada). Mensagem original: {e}"
    else:
        return f"Ocorreu um erro inesperado: {e}"

def obter_valor(prompt, tipo_dado):
    """Função: vai capturar os dados do usario tratar de acordo com o tipo de dados, se ele e str, int ou float"""
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

            # se passar do 'if vem para essa clausula onde se estiver ',' e não tiver '.'
            elif "," in valor_str and "." not in valor_str:
                valor_str = valor_str.replace(",", ".")

            if tipo_dado == int:
                return int(float(valor_str))
            elif tipo_dado == float:
                return float(valor_str)

        except Exception as e:
            error = validar_erro(e)
            print(f"AUXILIAR OBTER DADOS: {error}\n")

def cadastrar(desc, fator, emb, rua, pr, nvl, apto, vl):
    end = str(rua) + "-" + str(pr) + "-" + str(nvl) + "-" + str(apto)
    end_existe = [produto['ENDERECO'] for produto in base_dados]
    if end in end_existe:
        print(f"\nERRO: Endereço ja cadastrado.")
        return
    
    cod_existe = [produto['COD'] for produto in base_dados]
    if cod_existe:
        cod = max(cod_existe) + 1
    else:
        cod = 8000

    novo_registro = {
        "COD": cod,
        "DESCRICAO": desc,
        "FATOR": fator,
        "EMBALAGEM": emb,
        "ENDERECO": end,
        "PRECO": vl,
        "ESTOQUE": None,
        "VENDA": None
    }
    print("\nCadastro finalizado!!!")  
    print("produto cadastrado:") 

    divisor_op()
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

    divisor_op()
    input("Precione 'enter' para continuar...")
    divisor_op()
    return base_dados.append(novo_registro)

def listar():
    try:
        if not base_dados:
            print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10}")
            divisor_op()
            print("\nsem produtos cadastrados!!\n")
            divisor_op()
            return

        print("\nprodutos cadastrados.\n")
        print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10} {'VENDA':<12} {"ESTOQUE":<12}")
        divisor_op()
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

def buscar(procx):  
    try:
        prod_encotrado = False
        for produto in base_dados:
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
                break

        if not prod_encotrado:
            print(f"aviso: o codigo {procx} não foi encotrado na base de dados")


        divisor_op()
        input("Precione 'enter' para continuar...")
        divisor_op()
    except Exception as e:
        error = validar_erro(e)
        print(f"menu: {error}")

def remover(lista, produto,):
    prod_encotrado = False

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

def atualizar(procx):
    prod_encotrado = False
    for produto in base_dados:
        if procx == produto['COD']:
            prod_encotrado = True
            buscar(procx)
            escolha = menu(2)
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

def lançamento(procx):
    prod_encotrado = False
    for produto in base_dados:
        print("passando aqui 1")
        if produto['COD'] == procx:
            print("passando aqui 2")

            prod_encotrado = True
            buscar(procx)

            escolha = menu(3)

            if escolha == 1:
                estoque = obter_valor("Informe a quantidade recebida: ", int)
                produto['ESTOQUE'] = produto['ESTOQUE'] + estoque
                break
            elif escolha == 2:
                venda = obter_valor("Informe a quantidade vendida: ", int)
                produto['VENDA'] = produto['VENDA'] + venda
                break
    if not prod_encotrado:
        print(f"aviso: o codigo {procx} não foi encotrado na base de dados")
        divisor_op()
        input("Precione 'enter' para continuar...")
        divisor_op()
    else:
        print("Produto alterado com sucesso!!!")
        buscar(procx)

def menu(id):
    try:
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
            
            escolha = int(input("Digite o numero da opção desejada: \n"))
            divisor_op()
            return escolha
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
            
            escolha = int(input("Digite uma das opção acima.\n"))
            return escolha
        elif id == 3:
            print("\n")
            print(
                f"{"LANÇAMENTO DE MERCADORIA":-^36}\n",
                f"{"1 - RECEBIMENTO.":<36}\n",
                f"{"2 - VENDA.":<36}\n",
                f"{"0 - VOLTAR PARA O MENU":<36}")
            
            escolha = int(input("Digite uma das opção acima.\n"))
            return escolha

    except Exception as e:
        error = validar_erro(e)
        print(f"menu: {error}")

def status():
    def prinft(listar,prompt):
        print(f"\nProduto com {prompt} estoque:")
        print(f"{listar['COD']}-{listar['DESCRICAO']} valor estoque: {listar['valor_estoque']:.2f}")

    for produto in base_dados:
        produto['valor_estoque'] = produto['PRECO'] * produto['ESTOQUE']

    list_prod = [prod['COD'] for prod in base_dados]
    qtde_prod = len(list_prod)

    list_vl_st = [vl_st['valor_estoque'] for vl_st in base_dados]
    qtde_vl_st = sum(list_vl_st)
    avg_vl = qtde_vl_st / qtde_prod

    prod_maior_vl = max(base_dados, key=lambda produto: produto['valor_estoque'])
    prod_menor_vl = min(base_dados, key=lambda produto: produto['valor_estoque'])

    divisor_op()
    print(f"{"Demostrativo":-^92}")
    print(f"Total de produto cadastrado: {qtde_prod}")
    print(f"Estoque em R$: R$ {qtde_vl_st:.2f}")
    print(f"Media valor estoque: {avg_vl:.2f}")

    prinft(prod_maior_vl, "maior")
    prinft(prod_menor_vl, "menor")


    divisor_op()

# função principal
def main():
    print(f"{"sistema":-^92}")
    print("\nBem vindo ao sistema\n")

    while True:
        escolha = menu(1)
        try:
            if escolha == 1:
                try:
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
                    
                    if None in [desc, fator, emb, rua, pr, nvl, apto, vl]:
                        print("\nCadastro cancelado devido a uma entrada inválida.")
                    else:
                        cadastrar(desc, fator, emb, rua, pr, nvl, apto, vl) 
                except Exception as e:
                    error = validar_erro(e)
                    print(f"menu-1: {error}\n")

            elif escolha == 2:
                print("\nlistagem de produtos cadastrados\n")
                divisor_op()
                listar()   

            elif escolha == 3:
                print("\n\nConsulta de produtos")
                divisor_op()
                procx = int(input("\nDigite codigo do produto: \n"))
                buscar(procx)

            elif escolha == 4:
                print("\n\nRemoção de produto")
                divisor_op()
                procx = int(input("\nfavor digite o codigo do produto para remoção:\n"))
                remover(lista= base_dados, produto= procx)

            elif escolha == 5:
                print("\n\nAlterar cadastros")
                procx = int(input("Informe o codigo do produto para alteração: \n"))
                atualizar(procx)

            elif escolha == 6:
                print("\n\nestatus de estoque")
                status()

            elif escolha == 7:
                print("\n\nLançamentos")
                procx = int(input("Informe o codigo do produto: \n"))
                lançamento(procx)

            elif escolha == 0:
                print('\n\n')
                divisor_op()
                print("Obrigado por utilizar o sistema!!!!")
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