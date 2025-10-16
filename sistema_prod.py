


def main():
    def menu():
        
        pass
    def cadastrar(COD, DESC, FATOR, EMB, END):
        novo_registro = {"COD": COD, "DESCRICAO": DESC, "FATOR": FATOR, "EMBALAGEM": EMB, "ENDERECO": END}
        return base_dados.append(novo_registro)
    def listar():
        pass
    def buscar():
        pass
    def remover():
        pass
    def atualizar():
        pass

    base_dados = [
        {"COD": 101000, "DESCRICAO": "SANDALIA MASC 37/8", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101"},
        {"COD": 100100, "DESCRICAO": "CHOC TALENTO DARCK", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202"},
        {"COD": 987654, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102"}
    ]


    # CADASTRO
    cod_list = []
    tt_cod_list = len(cod_list)
    for produto in base_dados:
        if tt_cod_list != 0:
            print(f"lista cheia {cod_list}")
        else:
            continue
        cod_list.append(produto["COD"])

def validar_erro(e):
    print("=" * 60)
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


if __name__ == "__main__":
    main()  