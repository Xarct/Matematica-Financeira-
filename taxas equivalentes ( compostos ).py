i =float (input ( " Digite a taxa anual :"))
pi = (i / 100) + 1
mensal = 1/12
diario= 1/360
semestre= 1/2
trimestre = 1/4
taxamensal =( ( pi) **mensal -1 )* 100
taxadiaria = ((pi) **diario - 1 )* 100
taxasemenstral = ((( pi)**semestre )- 1 )* 100
taxatrimestral = ((( pi)**trimestre)-1)*100
round (taxamensal, 3)
round (taxadiaria, 3)
round (taxasemenstral, 3)

print ( " A taxa diaria é de {} % \n A taxa mensal é de {} % \n A taxa semenstral é de {} % \n A taxa trimestral é de {}". format ( taxadiaria,taxamensal,taxasemenstral, taxatrimestral))