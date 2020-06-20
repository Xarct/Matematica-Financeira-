d = float ( input ( " Digite o primeiro depósito : "))
i =float ( input ( " Digite a porcentagem  - em juros compostos - mensal : "))
valorfuturo = float ( input ( " Digite a quantidade que você deseja ter  :"))
pi = (i / 100) + 1
import math
x = ((valorfuturo * ( i / 100)) / d )+ 1 
qd = math.log( x, 10)/ math.log (pi, 10)
round ( qd, 2)
print ( " Você vai precisar depositar : {} vezes  ".format  (qd))

