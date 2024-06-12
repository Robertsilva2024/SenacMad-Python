import matplotlib.pyplot as plt  #biblioteca matplotlib
plt.axhline(y=.10,xmin = 0.25,xmax = 0.9)
plt.axhline(y=70, color='b', linestyle= ':')
plt.axhline(y=50, color = 'y',linestyle=':')
plt.axhline(y=30,color='r', linestyle='dashed')

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.show()
