from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Entrez
eq = Seq.Seq("AGTCGATTA")
dir(IUPAC)  ## too see the available alphabets

## methods
## reverse complement
rc_my_seq = Seq.Seq.reverse_complement(my_seq)

mut_my_seq = my_seq.mutableSeq ## ? method name not sure; returns an object that is like a string but it's mutable;

## .stopcodon .startcodon mrna.translate
## Biopython trabnslates the STOP codons with "*" in the sequence

## SeqRecord module
## SeqRecord class is for a sequence with attached metainfo, e.g. annotation, database id ... 

## Entrez
Entrez.email="alessandro.lussana@protonmail.com"
x=Entrez.esearch(db="pubmed",term="vitexin")
record=Entrez.read(x)   ## record is a dict-like object
record['IdList']        ## returns IDs (first 20 by default)
