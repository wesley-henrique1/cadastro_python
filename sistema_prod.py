
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
                return valor_str
                
        except Exception as e:
            error = validar_erro(e)
            print(f"AUXILIAR OBTER DADOS: {error}\n")

# função principal
def main():
    base_dados = [
        {"COD": 80000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59},
        {"COD": 80002, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99},
        {"COD": 80001, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59}
        ]

    def menu():
        
        print("=" *60 + "sistema" + "=" *60)
        print("\nBem vindo ao sistema\n")
    try:
        while True:
            print("MENU")
            print("1 - cadastro")
            print("2 - lista")
            print("0 - sair")

            escolha = int(input("\nDigite o numero da opção desejada: \n"))

            if escolha == 1:
                try:
                    print("#"*120)
                    print("\nFavor informar os campos abaixo\n")
                    desc = obter_valor("descrição: ", str)
                    fator = obter_valor("fator de converção: ", int)
                    emb = obter_valor("Embalagem: ", str)
                    end = obter_valor("Endereço:", str)
                    vl = obter_valor("valor do produto (000,00):", float)
                    
                    if None in [desc, fator, emb, end, vl]:
                        print("\nCadastro cancelado devido a uma entrada inválida.")
                    else:
                        cadastrar(desc, fator, emb, end, vl) 
                except Exception as e:
                    error = validar_erro(e)
                    print(f"menu-1: {error}\n")
                    continue
            elif escolha == 2:
                listar()   
            elif escolha == 0:
                print("\n\nObrigado por utilizar o sistema")
                break
            else:
                print("Numero invalido valor digitar o numero correspodente a opção desejada")          
    except Exception as e:
        error = validar_erro(e)
        print(f"cadastro: {error}\n")
        



    def cadastrar(desc, fator, emb, end, vl):
        end_existe = [produto['ENDERECO'] for produto in base_dados]
        if end in end_existe:
            print(f"ERRO: Endereço ja cadastrado.")
            return
        
        cod_existe = [produto['COD'] for produto in base_dados]
        if cod_existe:
            cod = max(cod_existe) + 1
        else:
            cod = 80000
            
        novo_registro = {
            "COD": cod,
            "DESCRICAO": desc,
            "FATOR": fator,
            "EMBALAGEM": emb,
            "ENDERECO": end,
            "PRECO": vl
        }    
        return base_dados.append(novo_registro)
    def listar():
        pass
    def buscar():
        pass
    def remover():
        pass
    def atualizar():
        pass

    menu()


if __name__ == "__main__":
    main()  