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
def gc_content(seq):
    """ Calculating GC Content in DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)

def gc_content_subsec(seq, k=20):
    """GC content in DNA/RNA sub-sequence length k"""
    res = []
    for i in range(0, len(seq) -k + 1, k):
        subseq = seq[i:i +k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an Aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos +3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    """provides the frequency of each codon encoding a given aminoacid in a DNA sequnce"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i +3]] == aminoacid:
            tmpList.append(seq[i:i + 3])
    
    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames

def protein_from_rf(aa_seq):
    """Compute all possible proteins in an Aminoacid sequence and return a list of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == '_':
            #STOP accumulating aminoacids if _ -STOP was found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            #START accumulating aminoacids if M -START was found
            if aa == 'M':
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins

#Generate RFs
#Extract all proteins
#Return a list of proteins (un)sorted
def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos:endReadPos])
    else:
        rfs = gen_reading_frames(seq)
    
    res = []
    for rf in rfs:
        prots = protein_from_rf(rf)
        for p in prots:
            res.append(p)
    if ordered:
        return sorted(res, key=len, reverse=True)
    return res
    
