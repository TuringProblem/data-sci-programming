#*******************#
# Author: Andrew W. #
#*******************#
#   @09/17/2024     #
#*******************#
tfc = float(input("Please enter the Total Fixed Costs: "))
sppu = float(input("Please enter the Sales Price: "))
vcpu = float(input("Please enter the Variable "))

bep_units = (tfc / (sppu - vcpu))
cmpu = sppu - vcpu
cmrpu = cmpu / sppu
bep_sdollars = tfc / cmrpu

print(f"BEP Units: {bep_units}")
print(f"Contribution Margin Per Unit: {cmpu}")
print(f"Contribution Margin Ratio Per Unit: {cmrpu}")
print(f"BEP Sales Dollars: {bep_sdollars}")
