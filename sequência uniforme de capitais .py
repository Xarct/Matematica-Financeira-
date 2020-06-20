va = float ( input ( " Digite o valor do financiamento, sem os juros : "))
i =float ( input ( " Digite a porcentagem  - em juros compostos - mensal : "))
n = float ( input ( " Digite a quantidade de parcelas que será dividido :"))
pi = (i / 100) + 1
import math
x = pi**n * ( pi - 1)
y = pi**n - 1
p = va * x / y
print ( " Cada prestação será de : %2.f" % p)

