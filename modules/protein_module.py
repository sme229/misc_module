from typing import Optional

aa_code_dict = {'C':'Cys', 'c':'Cys', 'D':'Asp', 'd':'Asp', 'S':'Ser', 's':'Ser', 'Q':'Gln', 'q':'Gln', 
                 'K':'Lys', 'k':'Lys', 'I':'Ile', 'i':'Ile', 'P':'Pro', 'p':'Pro', 'T':'Thr', 't':'Thr',
                 'F':'Phe', 'f':'Phe', 'N':'Asn', 'n':'Asn', 'G':'Gly', 'g':'Gly', 'H':'His', 'h':'His',
                 'L':'Leu', 'l':'Leu', 'R':'Arg', 'r':'Arg', 'W':'Trp', 'w':'Trp', 'A':'Ala', 'a':'Ala', 
                 'V':'Val', 'v':'Val', 'E':'Glu', 'e':'Glu', 'Y':'Tyr', 'y':'Tyr', 'M':'Met', 'm':'Met'}

aa_weight_dict = {'G':75, 'g':75, 'A':89, 'a':89, 'R':174, 'r':174, 'N':132, 'n':132, 
                          'D':133, 'd':133, 'C':121, 'c':133, 'E':147, 'e':147, 'Q':146, 'q':146,
                         'H':155, 'h':155, 'I':131, 'i':131, 'L':131, 'l':131, 'K':146, 'k':146, 
                         'M':149, 'm':149, 'F':165, 'f':165, 'P':115, 'p':115, 'S':105, 's':105, 
                         'T':119, 't':119, 'W':204, 'w':204, 'Y':181, 'y':181, 'V':117, 'v':117}
def amino_acid_frequency(seq: str) -> dict:
  """
  Calculates amino acid frequencies
  Arguments:
  -seq (str) input protein sequence
  Return:
  -dictionary with amino acid and its frequency
  """
  freq_dict = {}
  for letter in seq:
    if letter in freq_dict:
      freq_dict[letter] += 1
    else:
      freq_dict[letter] = 1
  for letter in freq_dict:
    freq_dict[letter] = round(freq_dict[letter] / len(seq) * 100, 2)
  return freq_dict
 
    
def find_motifs(seq: str, motif: str):
  """
  Finds a motif of interest in a protein sequence
  Arguments:
  -seq (str) input protein sequence
  -motif (str) motif to be found in sequence
  Return:
  -position(s) of the motif in seq
  """
  positions = []
  for i in range(len(seq) - len(motif) + 1):
    window = seq[i:i+len(motif)]
    if window == motif:
      positions.append(i)
  return positions


def check_protein_seq(seq: str) -> str:
    """
    Checks whether a sequence is written using 1-letter amino acid code
    Arguments:
    -seq (str) input protein sequence
    Return:
    - str, 'single_letter_prot_seq' otherwise 'Invalid Input' error is raised
    """
    unique_chars = set(seq)
    single_letter = set('GALMFWKQESPVICYHRNDTgalmfwkqespvicyhrndt')

    if unique_chars <= single_letter:
        seq = 'single_letter_prot_seq'

    else:
        raise ValueError("Invalid Input")
    return seq


def molecular_weight(seq: str) -> int:
    """
    Calculates molecular weight of a protein
    Arguments:
    - seq (str) 1-letter coded protein sequence
    Return:
    - int, molecular weight (g/mol) rounded to integer   
    """
    list_input_seq = list(seq)
    water_mw = 18
    total_mw = sum(aa_weight_dict[a] for a in seq)
    return total_mw - water_mw * (len(seq) - 1)
    
    
def one_to_three_letter(seq: str) -> str:
    """
    Converts a 1-letter amino acid code sequence into a 3-letter sequence
    Arguments:
    - seq (str) sequence to convert, must be 1-letter coded protein sequence
    Return:
    - str, a 3-letter coded protein sequence without spaces            
    """
    three_letter_aa = ''
    for aa in seq:
        three_letter_aa_seq += aa_code_dict[aa] 
    return three_letter_aa_seq

    
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

