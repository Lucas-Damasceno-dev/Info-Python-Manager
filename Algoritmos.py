def situacao(quantos_envolvidos: int) -> dict:
    PROPINAS = {0 : [1000.00, 100000.00, 90.00, 0.00],
                1 : [100.00, 300.00, 5500.00, 10000.00],
                2 : [15.00, 20.00, 400.00, 1000.00],
                3 : [1200.00, 3500.00, 0.00, 0.00]}
    PARCELAS = {0 : [36, 36, 0, 0], 
                1 : [1, 3, 24, 10],
                2 : [1, 1, 4, 10],
                3 : [12, 5, 0, 0]}
    politicos = []
    for i in range(quantos_envolvidos):
        politico = {"Quanto recebeu": PROPINAS[i],
                    "Quantas parcelas": PARCELAS[i]}
        politicos.append(politico)
    return politicos

meus_tiriricas = situacao(4)

def montante(meus_tiriricas: list) -> list:
    montantes_totais = []
    for pos, politico in enumerate(meus_tiriricas):
        recebidos = list(politico.values())[0]
        montantes = []
        for valor, parcelas in zip(recebidos, politico["Quantas parcelas"]):
            juros = 0.039944 / 12
            montante = valor * ((1 + juros) ** parcelas - 1) / juros
            montantes.append(montante)
        montantes_totais.append(montantes)
    return montantes_totais


valores = montante(meus_tiriricas)

def total_recebido(valores):
    valores_totais = []
    for montante in valores:
        total_propina_recebido = sum(montante)
        valores_totais.append(total_propina_recebido)
    return valores_totais


soma_das_propinas_por_politico = total_recebido(valores)

def total_gasto_por_empresa():
    GASTOS_POR_EMPRESA = {0 : [[1000.00, 100.00, 15.00, 1200.00], [36, 1, 1, 12]],
                          1 : [[100000.00, 300.00, 20.00, 3500.00], [36, 3, 1, 5]],
                          2 : [[90.00, 5500.00, 400.00, 0.00],[0, 24, 4, 0]],
                          3 : [[0.00, 10000.00, 1000.00, 0.00],[0, 10, 10, 0]],}
    tot_por_empresa = []
    for chave in GASTOS_POR_EMPRESA:
        tot_gasto = 0
        for pos in range(0, 4):
            tot_gasto += GASTOS_POR_EMPRESA[chave][0][pos] * GASTOS_POR_EMPRESA[chave][1][pos]
        tot_por_empresa.append(tot_gasto)
    return tot_por_empresa

        
tanto_que_pagaro = total_gasto_por_empresa()
print(tanto_que_pagaro)
