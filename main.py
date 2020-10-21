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
print(f'[3]  DNA/RNA Transcription(mRNA):{transcription(DNAStr)}\n')

print(f"[4] Sense Strand + Complement + Reverse Complement:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement] \n")

print(f'[5] GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] GC Content in sub-sequence K=5: {gc_content_subsec(DNAStr, k=5)}\n')

print(f'[7] Aminoacid Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

print(f'[8] Codon frequency (L): {codon_usage(DNAStr, "L")}\n')
print(f'[9] Reading frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)

print('\n[10] All proteins in 6 ORFS:')
for prot in all_proteins_from_orfs(DNAStr, 0, 0, True):
    print(f'{prot}')
