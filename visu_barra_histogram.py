from matplotlib import pyplot as plt 
from collections import Counter

grades =[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade:grade//100

histogram = Counter(decile(grade) for grade in grades)


plt.bar([x-4 for x in histogram.keys()], #move cada barra para a esquerda
         histogram.values(),            #da para cada barra sua altura correta
         8)                             #largura de 8 p cada barra

plt.axis([-5,105,0,5])  #eixo(x,y) x(-5,105) e y (0,5)

plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decil')
plt.ylabel('# de Alunos')
plt.title('Distribuicao das notas no teste 1')
plt.show()
