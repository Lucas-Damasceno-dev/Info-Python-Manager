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
                    if caractere.isdigit():
                        valores_das_propinas.append(int(caractere))

            else:
                for caractere in elementos:
                    if caractere.isdigit():
                        numeros_de_parcelas.append(int(caractere))

    return [taxa_de_juros, numero_de_politicos, numero_de_empresas, valores_das_propinas, numeros_de_parcelas]


ler_arquivo()


'''def calcular_montante():
    numeros_de_politicos_e_empresas, valores_das_propinas, numeros_de_parcelas = ler_arquivo()
    numero_de_politico, numero_de_empresa = numeros_de_politicos_e_empresas
    todas_propinas = []
    todas_parcelas = []
    taxa_juros = 3.9944

    for pos in range(0, len(valores_das_propinas), numero_de_empresa):
        todas_propinas.append(valores_das_propinas[pos:pos + numero_de_empresa])

    for pos in range(0, len(numeros_de_parcelas), numero_de_politico):
        todas_parcelas.append(numeros_de_parcelas[pos:pos + numero_de_politico])

    politicos = []
    for politico in range(1, numero_de_politico + 1):
        propinas_politico = todas_propinas[politico - 1]
        parcelas_politico = todas_parcelas[politico - 1]
        montantes_politico = []

        for parcela in parcelas_politico:
            juros = taxa_juros / 12
            montante_individual = propinas_politico[0] * ((1 + juros) ** parcela - 1) / juros
            montantes_politico.append(montante_individual)

        montante_total = sum(montantes_politico)
        politico = {"Propinas": propinas_politico,
                    "Parcelas": parcelas_politico,
                    "Montante": montante_total}
        politicos.append(politico)

    return politicos


calcular_montante()


def calcular_total_gasto_por_empresa():
    numeros_de_politicos_e_empresas, valores_das_propinas, numeros_de_parcelas = ler_arquivo()
    numero_de_politico, numero_de_empresa = numeros_de_politicos_e_empresas
    total_propina_por_empresa = []

    for i in range(0, len(valores_das_propinas), numero_de_empresa):
        total_propina_por_empresa.append(sum(valores_das_propinas[i:i + numero_de_empresa]))

    return total_propina_por_empresa


calcular_total_gasto_por_empresa()'''


'''Informar qual foi o político que mais recebeu propina, o total de propina recebida (com e sem juros) e o juros 
recebido.'''


'''def analisa_dados_politicos():
    numeros_de_politicos_e_empresas, valores_das_propinas, numeros_de_parcelas = ler_arquivo()
    numero_de_politico, numero_de_empresa = numeros_de_politicos_e_empresas
    tot_propina_empresa = []
    for i in range(numeros_de_politicos_e_empresas[0]):
        propinas_empresa = valores_das_propinas[i*numero_de_empresa:(i+1)*numero_de_empresa]
        tot_propina_empresa.append(sum(propinas_empresa))
    print(tot_propina_empresa)


analisa_dados_politicos()
'''

'''def calcular_total_gasto_por_empresa():
    numeros_de_politicos_e_empresas, valores_das_propinas, numeros_de_parcelas = ler_arquivo()
    numero_de_politico, numero_de_empresa = numeros_de_politicos_e_empresas

    valores_por_empresa = []
    for i in range(numero_de_empresa):
        valores_por_empresa.append(0)

    for i in range(numero_de_politico):
        propinas_politico = valores_das_propinas[i*numero_de_empresa:(i+1)*numero_de_empresa]
        parcelas_politico = numeros_de_parcelas[i*numero_de_empresa:(i+1)*numero_de_empresa]

        for j in range(numero_de_empresa):
            valores_por_empresa[j] += propinas_politico[j] * parcelas_politico[j]

    empresa_mais_propina = valores_por_empresa.index(max(valores_por_empresa))
    print(f"A empresa {empresa_mais_propina+1} pagou o maior valor de propina, que foi de "
          f"R${max(valores_por_empresa):.2f}.")


calcular_total_gasto_por_empresa()'''
