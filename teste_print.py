# variavel para armazenar os dados de exemplo
base_dados = [
    {"COD": 8000, "DESCRICAO": "SANDALIA MASC 45/6", "FATOR": 12, "EMBALAGEM": "UN/001/UN", "ENDERECO": "30-10-1-101", "PRECO": 39.59},
    {"COD": 8001, "DESCRICAO": "CHOC TALENTO DARCK WHITE", "FATOR": 6, "EMBALAGEM": "DP/012/UN", "ENDERECO": "11-50-1-202", "PRECO": 56.99},
    {"COD": 8002, "DESCRICAO": "TV AOC 32", "FATOR": 1, "EMBALAGEM": "UN/001/UN", "ENDERECO": "01-64-1-102", "PRECO": 1578.59}
    ]

try:
    procx = int(input("Digite codigo do produto: "))

    prod_encotrado = False
    for produto in base_dados:
        if procx == produto['COD']:
            prod_encotrado = True

            print("\nprodutos cadastrados.\n")
            print(f"{'CÓD':<7} {'DESCRIÇÃO':<35} {'FATOR':<8} {'EMBALAGEM':<12} {'ENDEREÇO':<15} {'PREÇO':<10}")
            print("-" * 84)
            print(
                f"{produto['COD']:<7}",
                f"{produto['DESCRICAO']:<35}",
                f"{produto['FATOR']:<8}",
                f"{produto['EMBALAGEM']:<12}"
                f"{produto['ENDERECO']:<15}",
                f"R$ {produto['PRECO']:<10.2f}\n"
            )
            print("-" * 84)
            break
        if not prod_encotrado:
            print(f"aviso: o codigo {procx} não foi encotrado na base de dados")
except Exception as e:
    print(f"valor não encotrado {e}")
