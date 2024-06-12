import numpy as np
import matplotlib.pyplot as plt
faixaEtaria = ['18-25', '26-35', '36-45', '46-55', '55+']
renda = [1800, 2000, 3500, 4300, 4600]
plt.bar(faixaEtaria, renda, color='blue')

plt.xticks(faixaEtaria)
plt.ylabel('Renda')
plt.xlabel('Faixa etária (anos)')

plt.title('Renda x Faixa Etária no Brasil')
plt.show()