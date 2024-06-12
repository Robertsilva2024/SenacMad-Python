import matplotlib.pyplot as plt  #biblioteca matplotlib
salariomaior = float(input('salario:'))
salariomenor = float(input('Salario menor'))
y = salariomenor
plt.axhline(y=salariomaior,xmin = 0.25,xmax = salariomaior)
plt.axhline(y=salariomaior, color='b', linestyle= ':')
plt.axhline(y=salariomaior, color = 'y',linestyle=':')
plt.axhline(y=salariomaior,color='r', linestyle='dashed')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
