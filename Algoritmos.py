def situacao() -> list:
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


situacao()


def montante():
    numero_de_politico = situacao()[0]
    numero_de_empresas = situacao()[1]
    valores_das_propinas = situacao()[2]
    numero_de_parcelas = situacao()[3]
    propinas = []
    parcelas = []
    taxa_juros = 3.9944
    
    for i in range(0, len(valores_das_propinas), numero_de_empresas):
        propinas.append(valores_das_propinas[i:i+numero_de_empresas])
        
    for o in range(0, len(numero_de_parcelas), numero_de_politico):
        parcelas.append(numero_de_parcelas[o:o+numero_de_politico])
    
    politicos = []
    for i in range(1, numero_de_politico + 1):
        propinas_politico = propinas[i-1]
        parcelas_politico = parcelas[i-1]
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


print(montante())
