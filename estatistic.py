def quantile(x,p):
        ###retorna o valor percentual p-ésimo em x
        p_index = int(p*len(x))
        return sorted(x)[p_index]
def mode(x):
        counts = Counter(x)
        max_count = max(counts.values())
        return [x_i for x_i, count in counts.iteritems() if count == max_coun>

### dispersao ###

#amplitude
def data_range(x):
        return max(x)-min(x)

###varianc

def de_mean(x):
        x_bar = mean(x)
        return [x_i - x_bar for x_i in x]
        #unitario - media
#3
from collections import Counter
from matplotlib import pyplot as plt
from math import sqrt

num_friends = [100,49,41,40,25]

friends_counts = Counter(num_friends)

xs = range(101) #o maior valor da nossa amostra é 100
ys = [friends_counts[x] for x in xs]

##### estatistica basica #####
def mean(x):
        return sum(x)/len(x)

def median(v):
        n = len(v)
        sorted_v = sorted(v) #coloca em ordem crescente
        midpoint = n//2
        if  n % 2 == 1:
                # se for impar, retorna o valor do meio
                return sorted_v[midpoint]
        else:
                lo = midpoint-1
                hi = midpoint
                return ((sorted_v[lo] + sorted[hi])/2)
                #[1,2,((3,4)),5,6]
     ###varianc

def de_mean(x):
        x_bar = mean(x)
        return [x_i - x_bar for x_i in x]
        #unitario - media
#3
def sum_of_squares(x): # x=deviations
        s = x
        ss=[]
        for i in s:
                ss.append(i*i)
        sum_of_squares_final = sum(ss)          
        return sum_of_squares_final

def variance(x):
        n = len(x)
        deviations = de_mean(x)
        return (sum_of_squares(deviations)/(n-1))

def standart_deviation(x):
        return sqrt(variance(x))

"""
plt.bar(xs,ys)

plt.axis([0,101,0,25])
plt.title('Histograma de COntagem de Amigos')
plt.xlabel('n de amigos')
plt.ylabel('n de pessoas')
plt.show()
"""


