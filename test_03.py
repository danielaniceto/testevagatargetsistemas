"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça
um programa, na linguagem que desejar, que calcule e retorne: • O menor valor de
faturamento ocorrido em um dia do mês; • O maior valor de faturamento ocorrido em
um dia do mês; • Número de dias no mês em que o valor de faturamento diário foi
superior à média mensal.
IMPORTANTE: a) Usar o json ou xml disponível como fonte dos dados do faturamento
mensal; b) Podem existir dias sem faturamento, como nos finais de semana e
feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

json_dates = """
{
"faturamento_diario": [0, 220, 300, 0, 150, 500, 0, 0, 800, 100, 50, 400, 0, 700, 200, 300, 0, 0, 600, 900, 0, 0, 50, 100, 0, 0, 750, 200, 0, 400]
}
"""

json_date = json.loads(json_dates)

invoicing = json_date['faturamento_diario']

billing_invoicing = [value for value in invoicing if value > 0]

minor_invoice = min(billing_invoicing)
major_invoice = max(billing_invoicing)

monthly_average = sum(billing_invoicing) / len(billing_invoicing)

days_above_average = sum(1 for value in billing_invoicing if value > monthly_average)

print(f'O menor valor de faturamento ocorrido em um dia do mês foi de R${minor_invoice}.') #output: 50
print(f'O maior valor de faturamento ocorrido em um dia do mês foi de R${major_invoice}.') #output: 900
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {days_above_average}.')#output: 8