"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de
representação que cada estado teve dentro do valor total mensal da distribuidora. """


billing_by_state = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_billing = sum(billing_by_state.values())

print("Percentual de representação por estado:\n")
for state, value in billing_by_state.items():
    percentage = (value / total_billing) * 100
    print(f"{state}: {percentage:.2f}%")

#output:SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.03%
# Outros: 10.98%
