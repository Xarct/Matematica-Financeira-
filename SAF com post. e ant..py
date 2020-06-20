va = float ( input ( " Digite o valor do financiamento, sem os juros : "))
i =float ( input ( " Digite a porcentagem  - em juros compostos - mensal : "))
n = float ( input ( " Digite a quantidade de parcelas que será dividido :"))
t = float ( input (" Você irá postecipar quantos meses ? "))
ta = float ( input (" Você irá antecipar quantos meses ? "))
taa = (( i /100) + 1) **ta
ti =( ( i/ 100 ) + 1 ) **t
pi = (i / 100) + 1
import math
x = pi**n * ( pi - 1)
y = pi**n - 1
p = (va * (x / y)) 
ppos =  va * ((x / y)*ti)
pposs =  va * ((x / y) /taa)

print ( " Cada prestação sem variação será de : %2.f" % p)
print ( " Cada prestação com postecipação : %2.f" % ppos )
print ( " Cada prestação com antecipação : %2.f" % pposs )
