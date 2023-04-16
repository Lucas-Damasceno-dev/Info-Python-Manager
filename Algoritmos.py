def situacao() -> int | list[int]:
    with open('arquivo.txt', 'r') as arquivo:
        dados = arquivo.readlines()
        cont = 0
        informacoes = []
        for linha in dados:
            informacoes.append(linha.split())
            cont += 1
            if cont == 1:
                num = informacoes[0][2]
                numero_de_politicos = int(num)
                return numero_de_politicos
            if cont == 2:
                num1 = informacoes[0][2]
                numero_de_empresas = int(num1)
                return numero_de_empresas
            if cont == 8:
                num2 = informacoes[3:9]
                valores_das_propinas = []
                for lista in num2:
                    for valor in lista:
                        valores_das_propinas.append(int(valor.replace(',', '')))
                return valores_das_propinas
            if cont == 15:
                num3 = informacoes[10:16]
                numero_de_parcelas = []
                for lin in num3:
                    for valo in lin:
                        numero_de_parcelas.append(int(valo.replace(',', '')))
                return numero_de_parcelas


situacao()


def montante():
    n = 'n'

# juros = 0.039944 / 12
# montante = valor * ((1 + juros) ** parcelas - 1) / juros
