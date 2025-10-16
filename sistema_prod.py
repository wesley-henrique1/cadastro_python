def validar_erro(e):
    if isinstance(e, KeyError):
        return f"KeyError: A coluna ou chave '{e}' não foi encontrada."
    elif isinstance(e, PermissionError):
        return "PermissionError: O arquivo está sendo usado ou você não tem permissão para acessá-lo. Por favor, feche o arquivo."
    elif isinstance(e, TypeError):
        return f"TypeError: Erro de tipo. Verifique se os dados são do tipo correto. Mensagem original: {e}"
    elif isinstance(e, ValueError):
        return f"ValueError: Erro de valor. Mensagem original: {e}"
    else:
        return f"Ocorreu um erro inesperado: {e}"



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
                print("\nFavor informar os campos abaixo\n")
                desc = input("descrição: ")
                fator = int(input("fator de converção: "))
                emb = input("Embalagem: ")
                end = input("Endereço:")
                vl = float(input("valor do produto:"))

                cadastrar(desc, fator, emb, end, vl)   
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
        try:
            cod_list = []
            count_list = len(cod_list)
            
            for produto in base_dados:
                if count_list != 0:
                    print(f"lista cheia {cod_list}")
                else:
                    cod_list.append(produto["COD"])
                maior_cod = max(cod_list)
                cod = maior_cod + 1

            print("aqui",cod_list)
            print("aqui",cod)

            novo_registro = {
                "COD": cod,
                "DESCRICAO": desc,
                "FATOR": fator,
                "EMBALAGEM": emb,
                "ENDERECO": end,
                "PRECO": vl
            }
        except Exception as e:
            error = validar_erro(e)
            print(f"cadastro: {error}\n")
            
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