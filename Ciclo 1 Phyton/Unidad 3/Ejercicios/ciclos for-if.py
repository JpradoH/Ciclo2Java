num_inv = ''
num = str(1235321)
l = list(num)
l.reverse()
for j in l:
    num_inv += j
print(num, num_inv)
if num == num_inv:
    print('es un # palindromo')
else: 
    print('no es # palindromo')