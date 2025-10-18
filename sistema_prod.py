# variavel para armazenar os dados de exemplo
base_dados = [
    {"COD": 8000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59},
    {"COD": 8001, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99},
    {"COD": 8002, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59}
    ]


# função auxiliares
def validar_erro(e):
    if isinstance(e, TypeError):
        return f"TypeError: Erro de tipo. Verifique se os dados são do tipo correto. Mensagem original: {e}"
    elif isinstance(e, ValueError):
        return f"ValueError: Erro de valor. Verifique se os dados são do tipo correto.. Mensagem original: {e}"
    else:
        return f"Ocorreu um erro inesperado: {e}"

def obter_valor(prompt, tipo_dado):
    while True:
        try:
            valor_str = input(prompt)
            
            valor_str_limpo = valor_str.replace(".", "")
            valor_str_limpo = valor_str_limpo.replace(",", ".")
            
            if tipo_dado == int:
                return int(float(valor_str_limpo))
            elif tipo_dado == float:
                return float(valor_str_limpo)
            else:
                valor_str = valor_str.upper()
                return valor_str
                
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
    print(f"{cod}-{desc}")
    print(f"Endereço: {end}")
    print(f"fator de converção: {fator}, embalagem: {emb}, preço pra venda: R$ {vl:.2f}, ") 
    return base_dados.append(novo_registro)

def listar():
    if not base_dados:
        print("sem produtos cadastrados!!")
        return
    
    print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'ENDEREÇO':<15} {'PREÇO':<10}")
    print("-" * 75)
def buscar():
    pass
def remover():
    pass
def atualizar():
    pass

def menu():
    print("MENU")
    print("1 - cadastro")
    print("2 - lista")
    print("0 - sair")
    try:
        escolha = int(input("Digite o numero da opção desejada: \n"))
        return escolha
    except Exception as e:
        error = validar_erro(e)
        print(f"escolhas: {e}")

        return -1
        
# função principal
def main():
    print("=" *60 + "sistema" + "=" *60)
    print("\nBem vindo ao sistema\n")

    while True:
        escolha = menu()
        try:

            if escolha == 1:
                try:
                    print("#"*120)
                    print("\nFavor informar os campos abaixo\n")
                    desc = obter_valor("descrição: ", str)
                    fator = obter_valor("fator de converção: ", int)
                    emb = obter_valor("Embalagem: ", str)
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
                listar()   

            elif escolha == 0:
                print("\n\nObrigado por utilizar o sistema")
                break

            else:
                print("Numero invalido valor digitar o numero correspodente a opção desejada") 
        except Exception as e:
            error = validar_erro(e)
            print(f"escolhas: {e}")
            break
            

if __name__ == "__main__":
    main()  