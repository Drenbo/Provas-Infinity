culturas = [
    {"produtora": "Fazenda A", "producao": "Milho", "anos": {"2021": [10, 2, 3], "2022": [10, 9, 5], "2023": [5, 3, 7]}},
    {"produtora": "Fazenda B", "producao": "Soja", "anos": {"2021": [7, 2, 5], "2022": [10, 6, 1], "2023": [7, 3, 7]}},
    {"produtora": "Fazenda C", "producao": "Trigo", "anos": {"2021": [1, 3, 3], "2022": [10, 9, 8], "2023": [5, 8, 7]}}
]

def prod_total(anos):
    total = 0
    for ano, producao in anos.items():
        total += sum(producao)
    return total

def ano_com_producao_total_maxima_minima():
    producao_por_ano = {}

    for cultura in culturas:
        for ano, producoes in cultura["anos"].items():
            if ano not in producao_por_ano:
                producao_por_ano[ano] = 0
            producao_por_ano[ano] += sum(producoes)
    
    ano_max = max(producao_por_ano, key=producao_por_ano.get)
    ano_min = min(producao_por_ano, key=producao_por_ano.get)
    
    return {"Ano máximo": (ano_max, producao_por_ano[ano_max]), "Ano mínimo": (ano_min, producao_por_ano[ano_min])}

def cultura_com_producao_total_maxima_minima():
    producao_por_cultura = {}

    for cultura in culturas:
        total = prod_total(cultura["anos"])
        producao_por_cultura[cultura["producao"]] = total
    
    cultura_max = max(producao_por_cultura, key=producao_por_cultura.get)
    cultura_min = min(producao_por_cultura, key=producao_por_cultura.get)
    
    return {"Maior cultura": (cultura_max, producao_por_cultura[cultura_max]), 
            "Menor cultura": (cultura_min, producao_por_cultura[cultura_min])}

def fazenda_com_producao_maxima_minima_em_ano(ano_especifico):
    producao_por_fazenda = []

    for cultura in culturas:
        if ano_especifico in cultura["anos"]:
            total = sum(cultura["anos"][ano_especifico])
            producao_por_fazenda.append({"produtora": cultura["produtora"], "producao_total": total})
    
    if not producao_por_fazenda:
        return "Ano não encontrado nos dados."

    fazenda_max = max(producao_por_fazenda, key=lambda x: x["producao_total"])
    fazenda_min = min(producao_por_fazenda, key=lambda x: x["producao_total"])
    
    return {"Maior produção": fazenda_max, "Menor produção": fazenda_min}

print("Ano com produção total máxima e mínima:\n", ano_com_producao_total_maxima_minima())
print("Cultura com produção total máxima e mínima:\n", cultura_com_producao_total_maxima_minima())
print("Fazenda com produção máxima e mínima em 2022:\n", fazenda_com_producao_maxima_minima_em_ano("2021"))
