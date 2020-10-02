#DNA toolset test file
from DNAToolkit import *
from utilities import colored
import random
#creating a random DNA sequence for testing:

randDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])
DNAStr = validateSeq(randDNAStr)
#print(validateSeq(randDNAStr))
#print(countNucFrequency(DNAStr))
#print(transcription(DNAStr))
print(f'\nSequence: {(DNAStr)}\n')
print(f'[1]  Sequence Length: {len(DNAStr)}\n')
print(f'[2]  Nucleotide Frequency:{countNucFrequency(DNAStr)}\n')
print(f'[3]  DNA/RNA Transcription:{transcription(DNAStr)}\n')
print(f'[4]  Reverse Complement:{reverse_complement(DNAStr)}\n')

print(f"DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5' \n")
