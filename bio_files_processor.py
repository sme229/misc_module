import os
from typing import Optional
def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: Optional[str]=None) -> str:
    """
    This function converts a multiline fasta file into one line fasta
    Arguments: input file and output file name (optional)
    Returns a file in current working directory
    """
    if output_fasta == None:
        output_fasta = 'output_fasta.fasta'
    current_dir = str(os.getcwd())
    output_file = os.path.join(current_dir, output_fasta)
    with open(input_fasta) as input_file, open(output_fasta, mode='w') as output_file:
        help_list = []
        for line in input_file:
            if line.startswith('>'):
                if len(help_list)!=0:
                    output_file.write(''.join(help_list) + '\n')
                    help_list = []
                output_file.write(line)
            else:
                help_list.append(line.strip())
        if len(help_list)!=0:
            output_file.write(''.join(help_list) + '\n')
        return output_file
