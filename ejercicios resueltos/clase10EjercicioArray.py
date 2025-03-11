import array as arr
import random

# num= arr.array('i',range(0,1001,1))
# num_eli=int(input("ingrese el numero que desea eliminar del 0 a 1000: "))

# if num_eli in num:
#     print("eliminando numero: ",num_eli)
#     num.remove(num_eli)
#     print(num[num_eli-2:num_eli+2])
# else:
#     print("el numero no existe")

# num_eli2 =random.randint(0,1001)

# if num_eli2 in num:
#     print("eliminando posicion: ",num_eli2,"con el numero ",num[num_eli2])
#     num.pop(num_eli2)
#     print(num[num_eli2-2:num_eli2+2])
# else:
#     ("el numero no existe")


# vector= arr.array('i',[1002,1050,1001,1095,1885,1452,1362,1741,1997,1775])

# for p,v in enumerate(vector):
#     print(p,v)

# print()

# for i in range(10):
#     print(i,vector[i])

# vector = arr.array('i',range(100,201,1))
# print(vector)

# for i in range(len(vector)):
#     print(vector[i])



# vector2= arr.array ('i',[])

# i =100
# while i <= 200:
#     vector2.append (i)
#     i+=1

# print(*vector2)
# print()

# for i in vector2:
#     print(i,end=' ')


# vector= arr.array ('i',[])

# for i in range(10):
#     num=int(input(f"ingrese el {i+1} valor:"))
#     vector.append(int(num))
# print(vector)

# for i in vector:
#     if (i % 10) in (3,8,4,9):
#         print('*',i)
#     else:
#         print(i)

# vector= arr.array('i',[])
# for i in range(100):
#     vector.append(random.randint(1990,2022))

# for i in vector:
#     if (i % 10) in (5,8,4,0):
#         vector.remove(i)

# print(*vector, '\nelementos',len(vector))


# se deberia realizar las operaciones de atras hacia delante, desde el fin hacia el inicio.
# asi, de esta manera no alteraria el orden de los valores.

## 1

# vector= arr.array('i',[])
# for i in range(100):
#     vector.append(random.randint(1990,2022))

# for i in reversed(vector):
#     if (i % 10) in (5,8,4,0):
#         vector.remove(i)

# print(*vector, '\nelementos',len(vector))

## 2

# vector= arr.array('i',[])
# for i in range(100):
#     vector.append(random.randint(1990,2022))

# for i in range(len(vector)-1,-1,-1):
#     if (i % 10) in (5,8,4,0):
#         vector.remove(i)

# print(*vector, '\nelementos',len(vector))

## 3

vector= arr.array('i',[])
for i in range(100):
    vector.append(random.randint(1990,2022))

for i in vector[::-1]:
    if (i % 10) in (5,8,4,0):
        vector.remove(i)

print(*vector, '\nelementos',len(vector))