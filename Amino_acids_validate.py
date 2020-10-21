import collections
from sequences import *
import random


#function for validating if DNA or not
def validateAA(aa_seq):
    tmpseq = aa_seq.upper()
    for aa in tmpseq:
        if aa not in Amino_Acids:
            return False
    return tmpseq
# randAA = ''.join([random.choice(Amino_Acids)
#                     for aa in range(100)])
# AAStr = validateAA(randAA)
# print(validateAA(randAA))

randAA = "AKFVAAWTLKAAAEAAAKGKDGSKSDSGTPIKDKKHSKGPGPGQSGGDSNNNEGNNGDST\
GSSGPGPGDDSSSSETSQQPQQPPDQPVGPGPGPPSAPNGTATGPAGTQPEGGGPGPGEK\
IVVPPKTPELEEAFEAIEGPGPGSAVSSSDVSTTIPTPVSEENGPGPGGLKVPGVGVPGA\
VSPQGGQSGPGPGDQVPSNGSDSEEEDNKSTSSGPGPGTSTLQTQTEEVPAASGSDSYAA\
YFIAQVRNSLAAYAQVRNSLRMAAYNVVKGFSSLAAYFLFEELESLAAYVVPPKTPELAA\
YSLVNTLIELAAYRMVPHQMNLAAYIEFGFKIAYAAYFIAQVRNSLAAYEVADGIWKLAA\
YRMVPHQMNLAAYAKAVRSFIFAAYFLFEELESL"

print(validateAA(randAA))
print(f'Amino Acid Length: {len(randAA)}')
