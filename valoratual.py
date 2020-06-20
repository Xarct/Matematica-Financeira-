p = float ( input ( " Digite a primeira prestação : "))
i =float ( input ( " Digite a porcentagem mensal : "))
n = int ( input ( " Digite a quantidade de  parcelas mensais :"))
pi = (i / 100) + 1
va =(p * ( ( 1 - ( pi)**(-n)))) / ( i / 100)
round ( va, 2)
print ( " O valor atual  será de : {}  ".format  (va))





	
