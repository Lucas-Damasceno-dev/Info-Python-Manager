def ler_arquivo() -> list:
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
                
            if cont == 2:
                num1 = informacoes[0][2]
                numero_de_empresas = int(num1)
                
            if cont == 8:
                num2 = informacoes[3:9]
                valores_das_propinas = []
                for lista in num2:
                    for valor in lista:
                        valores_das_propinas.append(int(valor.replace(',', '')))
                        
            if cont == 15:
                num3 = informacoes[10:16]
                numero_de_parcelas = []
                for lin in num3:
                    for valo in lin:
                        numero_de_parcelas.append(int(valo.replace(',', '')))
                        
        return [numero_de_politicos, numero_de_empresas, valores_das_propinas, numero_de_parcelas]


ler_arquivo()


def calcula_montante():
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


calcula_montante()
