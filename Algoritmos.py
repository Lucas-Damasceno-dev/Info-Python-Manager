def ler_arquivo():
    with open('arquivo.txt', 'r') as arquivo:
        numeros_de_politicos_e_empresas = []
        numeros_de_propinas = []
        numeros_de_parcelas = []
        cont = 0
        for linha in arquivo:
            cont += 1
            elementos = linha.split()

            if cont < 3:
                for caractere in elementos:
                    if caractere.isdigit():
                        numeros_de_politicos_e_empresas.append(int(caractere))

            elif 2 < cont < sum(numeros_de_politicos_e_empresas):
                for caractere in elementos:
                    if caractere.isdigit():
                        numeros_de_propinas.append(int(caractere))

            else:
                for caractere in elementos:
                    if caractere.isdigit():
                        numeros_de_parcelas.append(caractere)

    return [numeros_de_politicos_e_empresas, numeros_de_propinas, numeros_de_parcelas]


ler_arquivo()


def calcular_montante():
    numero_de_politico = ler_arquivo()[0]
    numero_de_empresas = ler_arquivo()[1]
    valores_das_propinas = ler_arquivo()[2]
    numero_de_parcelas = ler_arquivo()[3]
    todas_propinas = []
    todas_parcelas = []
    taxa_juros = 3.9944
    
    for pos in range(0, len(valores_das_propinas), numero_de_empresas):
        todas_propinas.append(valores_das_propinas[pos:pos+numero_de_empresas])
        
    for pos in range(0, len(numero_de_parcelas), numero_de_politico):
        todas_parcelas.append(numero_de_parcelas[pos:pos+numero_de_politico])
    
    politicos = []
    for politico in range(1, numero_de_politico + 1):
        propinas_politico = todas_propinas[politico-1]
        parcelas_politico = todas_parcelas[politico-1]
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
