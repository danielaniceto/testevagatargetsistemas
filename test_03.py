"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça
um programa, na linguagem que desejar, que calcule e retorne: • O menor valor de
faturamento ocorrido em um dia do mês;

• O maior valor de faturamento ocorrido em
um dia do mês;

• Número de dias no mês em que o valor de faturamento diário foi
superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento
mensal;

b) Podem existir dias sem faturamento, como nos finais de semana e
feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

json_file_path = "C:/Users/Daniel/Desktop/PASTAS/testevagatargetsistemas/dados_faturamentos.json"

with open(json_file_path, 'r', encoding="utf-8") as json_file:
    json_dates = json.load(json_file)

invoicing = json_dates

billing_invoicing = [day['valor'] for day in invoicing if day['valor'] > 0]

minor_invoice = min(billing_invoicing)
major_invoice = max(billing_invoicing)

monthly_average = sum(billing_invoicing) / len(billing_invoicing)

days_above_average = sum(1 for value in billing_invoicing if value > monthly_average)

print(f'O menor valor de faturamento ocorrido em um dia do mês foi de R${minor_invoice:,.2f}.')
print(f'O maior valor de faturamento ocorrido em um dia do mês foi de R${major_invoice:,.2f}.')
print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {days_above_average}.')