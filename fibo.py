b_n = 0
b1 = 0
b2 = 1
f_zahl = int(input("Welche Fibonacci Zahl wollen Sie wirklich haben?"))

f_list = []

for i in range(f_zahl+1):
    f_list.append(b1)
    b_n = b1+b2
    b1 = b2
    b2 = b_n

print("Die "+str(f_zahl)+". Zahl in der Fibonacci Folge ist:", f_list[f_zahl])
