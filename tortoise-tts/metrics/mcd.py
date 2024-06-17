# Please read this page carefully. https://github.com/MattShannon/mcd
# Please follow the instructions on this page to make independent conda environment only for calculating MCD

from pymcd.mcd import Calculate_MCD

# Instance of MCD class
# There are three different modes "plain", "dtw" and "dtw_sl" for the above three MCD metrics 
mcd_toolbox = Calculate_MCD(MCD_mode="dtw")

# Input the path of the reference speech and generated speech
reference  = input("reference speech path: ")
generated = input("generated speech path: ")

mcd_value  = mcd_toolbox.calculate_mcd(reference, generated)
print(mcd_value)
