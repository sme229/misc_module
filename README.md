# misc_module #

This module includes tools that can work with fastq, protein and nucleic acid sequences.

# fastq_filter # 

The function takes a path to fastq sequences as input as well as the output file name and filtering parameters (GC content, sequence length and quality score).  

`
fastq_filter('C:/Users/sme229/BIOINF/python/HW5/example_fastq.fastq', output_filename='file1', gc_bounds=(0,80), length_bounds=(100,200), quality_threshold=20)
`

In this example, the GC content filter is set up as >= 0 and <= 80, the length filter removes sequences that are outside of >= 100 and <= 200 length and the quality score cut off is set to >= 20. A new folder ('fastq_filtrator_results') with a file ('file1') containing sequences that passed all 3 filters is returned.

# run_protein_tool #

Includes a set of commands that perform various operations with protein or peptide sequences of any length. The input sequence(s) must be written using 1-letter amino acid code and can contain any of the standard 20 amino acids.

The following functions are implemented:

```
molecular_weight

```

this function takes 1-letter coded protein sequence(s) (string) and calculates molecular weight rounded to integer in g/mol. The function is not case-sensitive.

`
run_protein_tool('peptide', function='molecular_weight')
`
`
799
`

```
one_to_three_letter
```

this function takes 1-letter coded protein sequence(s) (string) and returns a 3-letter coded sequence(s) without spaces (string).

`
run_protein_tool('PEPTIDE', function='one_to_three_letter')
`
`
'ProGluProThrIleAspGlu'
`
`
run_protein_tool('p', 'peptide', function='one_to_three_letter')
`
`
['Pro', 'ProGluProThrIleAspGlu']
`
```
amino_acid_frequency
```

this function takes 1-letter coded protein sequence(s) (string), calculates frequency for each unique amino acid and creates a dictionary with amino acids as keys and corresponding frequencies as values.

`
run_protein_tool('MADSEQNQEEAGGGEQREH', function='amino_acid_frequency')
`
`
{'M': 5.26, 'A': 10.53, 'D': 5.26, 'S': 5.26, 'E': 26.32, 'Q': 15.79, 'N': 5.26, 'G': 15.79, 'R': 5.26, 'H': 5.26}
`
```
find_motifs
```

this function takes two string arguments: 1-letter coded protein sequence(s) and a motif of interest, where motif is any sequence which occurence will be searched for in the input protein sequence(s). The function returns position(s) of the motif.

`
find_motifs('MADSEQNQEEAGGGEQREH', function='find_motifs', motif='GG')
`
`
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
`

`
'aaagggcccuuu'
`
```
complement
```

This function works with either DNA or RNA sequences and returns a complementary sequence

```
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='complement')
```

`
['tttcccgggaaa', 'uaccgg']
`

```
reverse
```

This function returns a reversed sequence
`
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='reverse')
`
`
['tttcccgggaaa', 'ccggua']
`

```
reverse_complement
```

This function returns a reversed complementary sequence

`
run_dna_rna_tools('aaagggcccttt', 'auggcc', function='reverse_complement')
`
`
['aaagggcccttt', 'ggccau']
`

# bio_file_processor #

This script contains a function that converts multiple line fasta file into a single line fasta. It takes a fasta file and an output file name (optional) as input returning a new fasta file in the current working directory. If the output file name is not specified, a default name 'output_fasta.fasta' is used.

```
convert_multiline_fasta_to_oneline
```

Example:

`
convert_multiline_fasta_to_oneline(input_fasta='example_multiline_fasta.fasta')
`

Input file example:

![before](https://github.com/sme229/misc_module/assets/104040609/65e68a7a-a47c-4335-8d10-a88387fa3bdd)

After conversion to a single line:

![after](https://github.com/sme229/misc_module/assets/104040609/c85e4283-295e-4689-a156-5c464cec2164)






