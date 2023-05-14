def ler_arquivo():
    with open('arquivo.txt', 'r') as arquivo:
        taxa_de_juros = 0
        numero_de_politicos = 0
        numero_de_empresas = 0
        valores_das_propinas = []
        numeros_de_parcelas = []
        cont = 0
        for linha in arquivo:
            cont += 1
            elementos = linha.strip().split()

            if cont == 1:
                for caractere in elementos:
                    if caractere.replace('.', '').isdigit():
                        taxa_de_juros = float(caractere)

            elif cont == 2:
                for caractere in elementos:
                    if caractere.isdigit():
                        numero_de_politicos = int(caractere)

            elif cont == 3:
                for caractere in elementos:
                    if caractere.isdigit():
                        numero_de_empresas = int(caractere)

            elif 3 < cont < numero_de_politicos + numero_de_empresas:
                for caractere in elementos:
                    if caractere.replace('.', '').isdigit():
                        valores_das_propinas.append(float(caractere))

            else:
                for caractere in elementos:
                    if caractere.isdigit():
                        numeros_de_parcelas.append(int(caractere))

    return [taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas]


def calcular_montante(a):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    todas_propinas = []
    todas_parcelas = []

    for pos in range(0, len(valores_das_propinas), numero_de_empresas):
        todas_propinas.append(valores_das_propinas[pos:pos + numero_de_empresas])

    for pos in range(0, len(numeros_de_parcelas), numero_de_politicos):
        todas_parcelas.append(numeros_de_parcelas[pos:pos + numero_de_politicos])

    politicos = []
    for politico in range(1, numero_de_politicos + 1):
        propinas_politico = todas_propinas[politico - 1]
        parcelas_politico = todas_parcelas[politico - 1]
        montantes_politico = []

        for parcela in parcelas_politico:
            juros = taxa_de_juros / 12
            montante_individual = propinas_politico[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_politico.append(montante_individual)

        montante_total = sum(montantes_politico)
        politico = {"Propinas": propinas_politico,
                    "Parcelas": parcelas_politico,
                    "Montante": montante_total}
        politicos.append(politico)

    return politicos


def calcular_total_gasto_por_empresa(a):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    total_propina_por_empresa = []

    for i in range(0, len(valores_das_propinas), numero_de_empresas):
        total_propina_por_empresa.append(sum(valores_das_propinas[i:i + numero_de_empresas]))

    return total_propina_por_empresa


def politico_mais_recebeu(a, b):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    info_politicos = b
    maior_montante = 0
    politico_mais_propinas = {}

    for politico in info_politicos:
        propinas_politico = politico['Propinas']
        parcelas_politico = politico['Parcelas']
        montantes_politico = []
        juros_politico = 0

        for parcela in parcelas_politico:
            juros = taxa_de_juros / 12
            montante_individual = propinas_politico[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_politico.append(montante_individual)
            juros_politico += montante_individual - propinas_politico[0]

        montante_total = sum(montantes_politico)

        if montante_total > maior_montante:
            maior_montante = montante_total
            politico_mais_propinas = {
                "Nome": "Político " + str(info_politicos.index(politico) + 1),
                "Propinas Recebidas": sum(propinas_politico),
                "Total com Juros": montante_total,
                "Juros Recebidos": juros_politico
            }

    return politico_mais_propinas


def politico_menos_recebeu(a, b):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    info_politicos = b
    menor_montante = float('inf')
    politico_menos_propinas = {}

    for politico in info_politicos:
        propinas_politico = politico['Propinas']
        parcelas_politico = politico['Parcelas']
        montantes_politico = []
        juros_politico = 0

        for parcela in parcelas_politico:
            juros = taxa_de_juros / 12
            montante_individual = propinas_politico[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_politico.append(montante_individual)
            juros_politico += montante_individual - propinas_politico[0]

        montante_total = sum(montantes_politico)

        if montante_total < menor_montante:
            menor_montante = montante_total
            politico_menos_propinas = {
                "Nome": "Político " + str(info_politicos.index(politico) + 1),
                "Propinas Recebidas": sum(propinas_politico),
                "Total com Juros": montante_total,
                "Juros Recebidos": juros_politico
            }

    return politico_menos_propinas


def empresa_mais_pagou(a, b):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    info_empresas = b
    maior_montante = 0
    empresa_mais_propinas = {}

    for empresa in info_empresas:
        propinas_empresa = empresa['Propinas']
        parcelas_empresa = empresa['Parcelas']
        montantes_empresa = []
        juros_empresa = 0

        for parcela in parcelas_empresa:
            juros = taxa_de_juros / 12
            montante_individual = propinas_empresa[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_empresa.append(montante_individual)
            juros_empresa += montante_individual - propinas_empresa[0]

        montante_total = sum(montantes_empresa)

        if montante_total > maior_montante:
            maior_montante = montante_total
            empresa_mais_propinas = {
                "Nome": "Empresa " + str(info_empresas.index(empresa) + 1),
                "Propinas Pagas": sum(propinas_empresa),
                "Total com Juros": montante_total,
                "Juros Pagos": juros_empresa
            }

    return empresa_mais_propinas


def empresa_menos_pagou(a, b):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    info_empresas = b
    menor_montante = float('inf')
    empresa_menos_propinas = {}

    for empresa in info_empresas:
        propinas_empresa = empresa['Propinas']
        parcelas_empresa = empresa['Parcelas']
        montantes_empresa = []
        juros_empresa = 0

        for parcela in parcelas_empresa:
            juros = taxa_de_juros / 12
            montante_individual = propinas_empresa[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_empresa.append(montante_individual)
            juros_empresa += montante_individual - propinas_empresa[0]

        montante_total = sum(montantes_empresa)

        if montante_total < menor_montante:
            menor_montante = montante_total
            empresa_menos_propinas = {
                "Nome": "Empresa " + str(info_empresas.index(empresa) + 1),
                "Propinas Pagas": sum(propinas_empresa),
                "Total com Juros": montante_total,
                "Juros Pagos": juros_empresa
            }

    return empresa_menos_propinas


def media_propina_politico(a, b):
    taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas = a
    info_politicos = b
    media_propinas = []

    for politico in info_politicos:
        propinas_politico = politico['Propinas']
        parcelas_politico = politico['Parcelas']
        montantes_politico = []
        juros_politico = 0

        for parcela in parcelas_politico:
            juros = taxa_de_juros / 12
            montante_individual = propinas_politico[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_politico.append(montante_individual)
            juros_politico += montante_individual - propinas_politico[0]

        montante_total = sum(montantes_politico)
        media_propinas.append(montante_total / len(info_politicos))

    media_total = sum(media_propinas) / len(media_propinas)

    return media_total


def media_propina_por_empresa(b):
    info_empresas = b
    media_por_empresa = {}

    for empresa in info_empresas:
        propinas_empresa = empresa['Propinas']
        total_propinas = sum(propinas_empresa)
        media = total_propinas / len(propinas_empresa)
        media_por_empresa["Empresa " + str(info_empresas.index(empresa) + 1)] = media

    return media_por_empresa


def salvar_dados_em_arquivo(b, c, d, e, f, g, h, i):
    montantes = b
    total_gasto_empresa = c
    politico_mais = d
    politico_menos = e

    with open("resultados.txt", "w") as arquivo:
        arquivo.write("Montantes dos políticos:\n")
        for idx, politico in enumerate(montantes):
            arquivo.write(f"Político {idx + 1}:\n")
            arquivo.write(f"Propinas: {politico['Propinas']}\n")
            arquivo.write(f"Parcelas: {politico['Parcelas']}\n")
            arquivo.write(f"Montante total: {politico['Montante']:.2f}\n\n")

        arquivo.write("Total gasto por empresa:\n")
        for idx, valor in enumerate(total_gasto_empresa):
            arquivo.write(f"Empresa {idx + 1}: {valor:.2f}\n")
        arquivo.write("\n")

        arquivo.write("Político que mais recebeu:\n")
        arquivo.write(f"Nome: {politico_mais['Nome']}\n")
        arquivo.write(f"Propinas Recebidas: {politico_mais['Propinas Recebidas']:.2f}\n")
        arquivo.write(f"Total com Juros: {politico_mais['Total com Juros']:.2f}\n")
        arquivo.write(f"Juros Recebidos: {politico_mais['Juros Recebidos']:.2f}\n\n")

        arquivo.write("Político que menos recebeu:\n")
        arquivo.write(f"Nome: {politico_menos['Nome']}\n")
        arquivo.write(f"Propinas Recebidas: {politico_menos['Propinas Recebidas']:.2f}\n")
        arquivo.write(f"Total com Juros: {politico_menos['Total com Juros']:.2f}\n")
        arquivo.write(f"Juros Recebidos: {politico_menos['Juros Recebidos']:.2f}\n\n")

        arquivo.write("Empresa que mais pagou:\n")
        arquivo.write(str(f) + "\n\n")

        arquivo.write("Empresa que menos pagou:\n")
        arquivo.write(str(g) + "\n\n")

        arquivo.write("Média de propina por político:\n")
        arquivo.write(str(h) + "\n\n")

        arquivo.write("Média de propina por empresa:\n")
        arquivo.write(str(i) + "\n\n")

    arquivo.close()