ir = float ( input ( " Digite a taxa de juros real anual : "))
i =float ( input ( " Digite o valor da inflação anual: "))
import math
x =(( ir / 100 ) * ( (i /100 )+ 1) )
taxaaparente =(( x + ( i /100 + 1 )) - 1) 
taxamensal =((( 1 + taxaaparente )**0.08333) - 1) 
tp = taxaaparente * 100
tm =(( taxamensal ) ) * 100
print ( " O valor da taxa aparente anual é de :%.1f "% tp,"%")
print ( " O valor da taxa aparente mensal é de : %.1f " % tm, "%")