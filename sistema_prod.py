# variavel para armazenar os dados de exemplo
base_dados = [
    {"COD": 8000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59},
    {"COD": 8001, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99},
    {"COD": 8002, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59}
    ]

# função auxiliares
def divisor_op():
    return print("-" * 92)
def validar_erro(e):
    if isinstance(e, TypeError):
        return f"TypeError: Operação inválida. Tentativa de usar tipos de dados incompatíveis. Mensagem original: {e}"
    elif isinstance(e, ValueError):
        return f"ValueError: Dado inválido. O valor não pode ser convertido (Ex: vírgula em número ou data errada). Mensagem original: {e}"
    else:
        return f"Ocorreu um erro inesperado: {e}"
def obter_valor(prompt, tipo_dado):
    while True:
        try:
            valor_str = input(prompt).strip()
            
            if tipo_dado == str:
                return valor_str.upper()
            
            if "," in valor_str and "." in valor_str:
                valor_str = valor_str.replace(".", "")
                valor_str = valor_str.replace(",", ".")

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
        "PRECO": vl
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
        f"R$ {vl:<12.2f}\n"
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
        print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10}")
        divisor_op()
        for produto in base_dados:
            print(
                f"{produto['COD']:<7}",
                f"{produto['DESCRICAO']:<35}",
                f"{produto['FATOR']:<8}",
                f"{produto['EMBALAGEM']:<12}"
                f"{produto['ENDERECO']:<15}",
                f"R$ {produto['PRECO']:<10.2f}\n"
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
                print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10}")
                divisor_op()
                print(
                    f"{produto['COD']:<7}",
                    f"{produto['DESCRICAO']:<35}",
                    f"{produto['FATOR']:<8}",
                    f"{produto['EMBALAGEM']:<12}"
                    f"{produto['ENDERECO']:<15}",
                    f"R$ {produto['PRECO']:<10.2f}\n"
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

def menu(id):
    try:
        if id == 1:
            print("\n")
            print(f"{"-" * 16 + "MENU" + "-" * 16}\n",
                  f"{"1 - cadastrar produto":<36}\n",
                  f"{"2 - listagem base de dados":<36}\n",
                  f"{"3 - consulta":<36}\n",
                  f"{"4 - Remover produto":<36}\n",
                  f"{"5 - alterar produto":<36}\n",
                  f"{"0 - sair":<36}")
            
            escolha = int(input("Digite o numero da opção desejada: \n"))
            divisor_op()
            return escolha
        elif id == 2:
            print("\n")
            print(f"{"-" * 7 + "OPÇÕES DE ATUALIZAÇÃO" + "-" * 7}\n",
                  f"{"1 - DESCRIÇÃO.":<36}\n",
                  f"{"2 - FATOR.":<36}\n",
                  f"{"3 - EMBALAGEM.":<36}\n",
                  f"{"4 - ENDEREÇO.":<36}\n",
                  f"{"5 - PREÇO.":<36}\n",
                  f"{"0 - VOLTAR PARA O MENU":<36}")
            
            escolha = int(input("Digite uma das opção acima.\n"))
            return escolha

    except Exception as e:
        error = validar_erro(e)
        print(f"menu: {error}")

# função principal
def main():
    print("=" *42 + "sistema" + "=" *42)
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
                prod = int(input("\nfavor digite o codigo do produto para remoção:\n"))
                remover(lista= base_dados, produto= prod)

            elif escolha == 5:
                print("\n\nAlterar cadastros")
                procurar = int(input("Informe o codigo do produto para alteração: \n"))
                atualizar(procurar)

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