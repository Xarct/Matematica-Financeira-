ta= float ( input ( " Digite a taxa da taxa aparente anual : "))
ir =float ( input ( " Digite o valor da taxa real anual: "))
import math
infl =(((( ir/ 100 ) + 1 )/(( ta/ 100 ) + 1)) - 1) * 100
inflmensal = (infl  ) **0.08333

print ( " O valor da inflação anual é de :%.1f "% infl,"%")
print ( " O valor da inflação mensal é de : %.1f " % inflmensal, "%")
