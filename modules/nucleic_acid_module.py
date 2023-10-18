def transcribe(seq: str) -> str:
    """
    Transcribes DNA->RNA
    Argument is string
    Return is string
    """
    list_input = list(seq)
    for i in range(len(seq)):
        if (list_input[i] == 'T'):
            list_input[i] = 'U'
        elif (list_input[i] == 't'):
            list_input[i]='u'
    return "".join(list_input)


def reverse(seq: str) -> str:
    """
    Returns reversed sequence
    Argument is string
    Return is string
    """
    output = seq[::-1]
    return output


def complement(seq: str) -> str:
    """
    Returns a complementary sequence
    Argument is a string
    Return is a string
    """
    list_input = list(seq)
    for i in range(len(seq)):
        if (list_input[i]=='G'):
            list_input[i]='C'
        elif (list_input[i]== 'g'):
            list_input[i]='c'
        elif (list_input[i]=='C'):
            list_input[i]='G'
        elif (list_input[i]=='c'):
            list_input[i]='g'
        elif (list_input[i] == 'T'):
            list_input[i] = 'A'
        elif (list_input[i] == 't'):
            list_input[i]='a'
        elif (list_input[i] == 'A'):
            list_input[i] = 'T'
        elif (list_input[i]=='a'):
            list_input[i]='t'        

    else:
           
            list_input = list(seq)
            for i in range(len(seq)):
                if (list_input[i]=='G'):
                    list_input[i]='C'
                elif (list_input[i]== 'g'):
                    list_input[i]='c'  
                elif (list_input[i]=='C'):
                    list_input[i]='G'
                elif (list_input[i]=='c'):
                    list_input[i]='g'
                elif (list_input[i] == 'U'):
                    list_input[i] = 'A'
                elif (list_input[i] == 'u'):
                    list_input[i]='a'
                elif (list_input[i] == 'A'):
                    list_input[i] = 'U'
                elif (list_input[i]=='a'):
                    list_input[i]='u'  
    return "".join(list_input)


def check_nucleic_acid(seq: str) -> str:
    """
    This function checks whether input sequence(s) is a nucleic acid
    Argument is str
    Return is str
    """
    unique_chars = set(seq)
    nucleotides_dna = set('ATGCatgc')
    nucleotides_rna = set('AUGCaugc')
    if unique_chars <= nucleotides_dna:
        seq = 'dna'
    elif unique_chars <= nucleotides_rna:
        seq = 'rna'
    else:
        raise ValueError("Invalid Input")
    return seq


def reverse_complement(seq: str) -> str:
    """
    This function returns a reversed complementary sequence
    Argument is str
    Return is str
    """
    complement_seq = complement(seq)
    reverse_compl_seq = reverse(complement_seq)
    return reverse_compl_seq


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
  

