import random
abc = ['a', 'b','c','d','e','e','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x','z']
matrizAbc = [None] * (26)

#palabra1 = #['p','i','l','a','r']
#palabra2= #['a', 'r','d', 'i', 'l', 'a']
palabra3=['h','o','l'] 
#['s','c','h','a','r','i','f','k','e','r']

for i in range(0, 10):
    matrizAbc[i] = [None] * 10

for i in range(10):
    for j in range(10):
        matrizAbc[i][j] = abc [random.randint(0,25)]

#for i in range(5):
#    matrizAbc[i][0] = palabra1 [i];
#for i in range(6):
#    matrizAbc[7][i] = palabra2 [i];
for i in range(3):
    matrizAbc[i][0] = palabra3 [i];

print (f'''
{matrizAbc}
''').split('[]')[0]


