c = int ( input ( " Digite a primeira aplicação: "))
i = float ( input ( " Digite a porcentagem mensal : "))
print ( " Se tu tiver o valor futuro e quer descobrir o tempo que foi \n preciso, digita 0 a seguir. Se não, digita o valor conhecido.")
n = int ( input ( " Digite o tempo em meses :"))

pi = i / 100

round ( pi, 2)

if n == 0 : 
       ms = int ( input ( " Digite o valor futuro : "))
       nss = ( ms - c) / ( c * pi )
       round ( ms, 2)
       round ( nss, 2)
       print ( " O valor do tempo em meses é {}" .format (nss))
else :
       m = c + (c * pi * n)
       js = c * pi * n
       round ( m, 2)
       round ( js, 2)
       print ( " O valor futuro em juros simples será de : {} \n O valor dos juros é : {} ".format  (m,js))
