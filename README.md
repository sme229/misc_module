## misc_module ##

This module includes tools that can work with fastq, protein and nucleic acid sequences.

# fastq_filter #

   The function takes fastq sequences organised as a dictinary for input: {'seq_name': ('sequence', 'quality')}, for example:
   
`  
{'@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'), '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D')}
`

This function filters fastq sequences by GC content, sequence length and quality score. These parameters can be specified in the function call:

`
fastq_filter({'@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD')}, gc_bounds=(0,80), length_bounds=(100,200), quality_threshold=20)
`

In this example, the GC content filter is set up as >= 0 and <= 80, the length filter filters out sequences that are outside of >= 100 and <= 200 length and the quality score cut off is set to >= 20. 
A filtered dictionary with sequences that passed all 3 filters is returned. 

# run_protein_tool #

Includes a set of commands that perform various operations with protein or peptide sequences of any length. The input sequence(s) must be written 
using _1-letter_ amino acid code and can contain any of the standard 20 amino acids.

The following functions are implemented:
```
molecular_weight

```
this function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive.
`
run_protein_tool('peptide', function='molecular_weight')
799
`

```
one_to_three_letter
```
this function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string).
`
run_protein_tool('PEPTIDE', function='one_to_three_letter')
'ProGluProThrIleAspGlu'
`
`
run_protein_tool('p', 'peptide', function='one_to_three_letter')
['Pro', 'ProGluProThrIleAspGlu']
`

```
amino_acid_frequency
```
this function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary
with amino acids as keys and corresponding frequencies as values.
`
run_protein_tool('MADSEQNQEEAGGGEQREH', function='amino_acid_frequency')
{'M': 5.26,
'A': 10.53,
'D': 5.26,
'S': 5.26,
'E': 26.32,
'Q': 15.79,
'N': 5.26,
'G': 15.79,
'R': 5.26,
'H': 5.26}
`

```
find_motifs
```
this function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence 
will be searched for in the input protein sequence(s). The function returns position(s) of the motif.
`
find_motifs('MADSEQNQEEAGGGEQREH', function='find_motifs', motif='GG')
[12, 13]
`

# run_dna_rna_tools #

This function takes DNA or RNA sequences as input and includes the following operations:

```
transcribe
```
takes a DNA sequence as input and returns the result of transcription (RNA)

`
run_dna_rna_tools('aaagggcccttt', function='transcribe')
'aaagggcccuuu'
`

```
complement
```
This function works with either DNA or RNA sequences and returns a complementary sequence

`
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='complement')
['tttcccgggaaa', 'uaccgg']
`

```
reverse
```
This function returns a reversed sequence

`
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='reverse')
['tttcccgggaaa', 'ccggua']
`

```
reverse_complement
```
This function returns a reversed complementary sequence

`
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='reverse_complement')
['aaagggcccttt', 'ggccau']
`










 
