n=int(input('ingrese cantidad de notas'))
ac=float(0)
for i in range(n):
   nota=float(input('ingrese una nota'))
   ac=ac+nota
prom=ac/n
print('promedio es ',prom) 
if prom>=6:
   print('MB')
elif prom>=5:
   print('B')
elif prom>=4:
   print('S')
else:
   print('I')
