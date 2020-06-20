iap = float ( input ( " Digite a taxa de juros aparente anual : "))
i =float ( input ( " Digite o valor da inflação anual: "))
import math
taxareal = ((1 + ( iap / 100)) / (1 + ( i / 100)) - 1)*100
tp=((( (1 + (taxareal / 100)))**0.08333) - 1) *100

print ( " O valor da taxa real anual é de :%.1f "% taxareal,"%")
print ( " O valor da taxa real mensal é de : %.1f " % tp, "%")