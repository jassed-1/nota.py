import math

pb = int(input("escreva sua nota 1bimestre:"))
sb = int(input("escreva sua nota 2bimestre:"))
tb = int(input("escreva sua nota 3bimestre:"))
qb = int(input("escreva sua nota 4bimestre:"))
f = int(input("escreva suas faltas:"))

media = pb * 1 + sb * 2 + tb * 3 + qb * 4
  
if media >= 50:
      print("voce passou")
  
      print (media)

else:                                                                                      
      print("voce reprovou")

      print (media)

elif f >= 30:
     print("voce reprovou por faltas")



