from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)

#nomeia cada posicao
for label, friend_count,minute_count in zip(labels,friends,minutes):
        plt.annotate(label,
                     xy=(friend_count,minute_count), #coloca cada rotulo com >
                     xytext=(5,-5),                   #mas compensa um pouco
                     textcoords='offset points' )

plt.title('Minutos Diarios vs. Numero de Amigos')
plt.xlabel('# de amigos')
plt.ylabel('# minutos diarios passados no site')
plt.show()

