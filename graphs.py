from cProfile import label
import matplotlib.pyplot as plt


x = []
y = []
with open('C1_indice.txt') as archivo: #Cambiar el nombre del archivo correspondiente
    for linea in archivo:
        punto = [int(i) for i in linea.split(',')]
        x.append(punto[0])
        y.append(punto[1])
plt.plot(x, y, "o--", label="Indice")
plt.legend(loc="best" )

x = []
y = []
with open('sin_indice.txt') as archivo:  # Cambiar el nombre del archivo correspondiente
    for linea in archivo:
        punto = [int(i) for i in linea.split(',')]
        x.append(punto[0])
        y.append(punto[1])
plt.plot(x, y, "o--", label="C1_sin indice")
plt.legend(loc="best" )



# plt.xscale("log") 
# plt.yscale("log")
# # plt.ylim(0, 123000)
# plt.ylabel("Tiempo en ms")
# plt.xlabel("Cantidad de vertices")
# plt.title("Kruskal: HashGraph")
# plt.savefig("HashGraph.jpg")
# plt.show()


# plt.xscale("log")
# plt.yscale("log")
# # plt.ylim(0, 123000)
# plt.ylabel("Tiempo en ms")
# plt.xlabel("Cantidad de vertices")
# plt.title("Kruskal: ListGraph")
# plt.savefig("ListGraph.jpg")
# plt.show()



plt.xscale("log")
plt.yscale("log")
# plt.ylim(0, 123000)
plt.ylabel("Tiempo en ms")
plt.xlabel("Cantidad de datos")
plt.title("Consulta 1: Sin indice vs indice")
plt.savefig("Consulta1.jpg")
plt.show()

#Cambiar los respectivos nombre de acuerdo a la conveniencia