import matplotlib
import matplotlib.pyplot as plt
plt.axhline(y=.10,xmin=0.25,xmax=0.9)
plt.axhline(y=10,color ='b',linestyle = ':')
plt.axhline(y=70,color='y',linestyle=':')
plt.axhline(y=50,color='r',linestyle = 'dashed')

plt.xlabel('x -- axis')
plt.xlabel('y -- axis')
plt.show()
