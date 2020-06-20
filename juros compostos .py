c = int ( input ( " Digite a primeira aplicação: "))
i =float ( input ( "Digite a porcentagem mensal : "))
print ( " Se tu tiver o valor futuro e quer descobrir o tempo que foi \n preciso em meses , digita 0 a seguir. Se não, digita o valor conhecido.")
n = int ( input ( " Digite o tempo em meses :"))
pi = (i / 100) + 1
import math 
if n == 0 : 
	 ms = float ( input ( " Digite o valor futuro : "))
	 nss =(math.log(ms / c , 10) )/ math.log ( pi, 10)
	 round ( nss, 2)
	 print ( " O valor do tempo em meses é {}" .format (nss))
else :
		m = c * ( pi )**n
		jc = m - c
		round ( m, 2)
		round ( jc, 2)
		print ( " O valor futuro em juros compostos será de : {} \n O valor dos juros é de : {} ".format  (m,jc))




	
