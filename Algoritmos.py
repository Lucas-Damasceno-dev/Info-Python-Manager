import functions


def main():
    a = functions.ler_arquivo()
    b = functions.calcular_montante(a)
    c = functions.calcular_total_gasto_por_empresa(a)
    d = functions.politico_mais_recebeu(a, b)
    e = functions.politico_menos_recebeu(a, b)
    f = functions.empresa_mais_pagou(a, b)
    g = functions.empresa_menos_pagou(a, b)
    h = functions.media_propina_politico(a, b)
    i = functions.media_propina_por_empresa(b)
    functions.salvar_dados_em_arquivo(b, c, d, e, f, g, h, i)


if __name__ == "__main__":
    main()
