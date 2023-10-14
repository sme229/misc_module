import modules.fastq_filter_functions.py
import modules.nucleic_acid_module.py
import modules.protein_module.py
import os

def fastq_filter(input_path: str, output_filename: str, gc_bounds: int, length_bounds: int, quality_threshold: int) -> list:
    """
    Filters fastq sequences by gc content, length and quality score
    Arguments: path to fastq file, name for the output file, filtering parameters
    Returns filtered fastq file in a new directory
    """
    seqs = fastq_to_dict(input_path)     
    result = dict()
    gc_filtered = gc_filter(seqs, gc_bounds)
    length_filtered = length_filter(seqs, length_bounds)
    quality_filtered = quality_filter(seqs, quality_threshold)
    intersection = gc_filtered.keys() & length_filtered.keys() & quality_filtered.keys()

    for keys, (sequence, quality) in seqs.items():
        if keys in intersection:
            result[keys] = (sequence, quality)
    output_filename = dict_to_fastq(result, output_filename)
    return output_filename


def run_dna_rna_tools(*args: str, function: str) -> str:
    """
    This function combines the functions above
    Arguments: *args are input sequences, function is a function of choice
    Returns: str, processed seqeunces depending on the function chosen
    """
    results = []
    for seq in args:
        check_nucleic_acid(seq)
        if function == 'transcribe':
            results.append(transcribe(seq))
        if function == 'complement':
            results.append(complement(seq))
        if function == 'reverse':
            results.append(reverse(seq))
        if function == 'reverse_complement':
            results.append(reverse_complement(seq))
    if len(results) == 1:
        results = results[0]
    return results


def run_protein_tool(*args: str, function: str,  motif: Optional[str]=None):
    """
    This is the main function
    Arguments:
    -seq(str) protein sequence(s)
    -function(str) specify the function
    -motif(str), optional argument for find_motifs function
    Return:
    -result of the specified function
    """
    results = []
    for seq in args:
            if check_protein_seq(seq) == 'single_letter_prot_seq':
                if function == 'check_protein_seq':
                    for seq in args:
                        results.append(check_protein_seq(seq))
                elif function == 'molecular_weight':
                    for seq in args:
                        results.append(molecular_weight(seq))
                elif function == 'one_to_three_letter':
                    for seq in args:
                        results.append(one_to_three_letter(seq))
                elif function == 'amino_acid_frequency':
                    for seq in args:
                        results.append(amino_acid_frequency(seq))
                elif function == 'find_motifs':
                    for seq in args:
                        results.append(find_motifs(seq, motif))
            if len(results) == 1:
                results = results[0]
            return results
