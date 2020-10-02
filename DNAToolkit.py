import collections
from sequences import *
#function for validating if DNA or not
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#function for counting DNA seq length
def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C":0, "T":0, "G":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    #return dict(collections.Counter(seq))

#DNA -> RNA
def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine(T) with Uracil(U)"""
    return seq.replace("T", "U")
#reverse complimentation:
def reverse_complement(seq):
    """Reverse Complement converts a DNA sequence into its reverse"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
