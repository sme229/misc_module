import os

def calc_gc_content(seq: str) -> float:
    """
    Calculates gc content
    Argument is string
    Returns float in %
    """
    seq_lower = seq.lower()
    length_seq = len(seq_lower)
    gc_count = 0
    for nt in seq_lower:        
        if nt=='g' or nt=='c':
            gc_count+=1
    gc_content = (gc_count/length_seq)*100
    return gc_content


def seq_length(seq: str) -> str:
    """
    Calculates sequence length
    Argument is string
    Returns string    
    """
    return len(seq)


def quality_score(seq: str) -> int:
    """
    Calculates numeric quality score
    Argument is string
    Returns int value
    """
    score_count = 0
    length_q_seq = len(seq)
    for symbol in seq:
        score_num = ord(symbol) - 33
        score_count+=score_num
    mean_qs = (score_count/length_q_seq)
    return mean_qs


def length_filter(seqs: dict, length_bounds=(0,1000)) -> dict:
    """
    Filters fastq reads by length
    Arguments:
    -dictionary
    -sequence length parameters (>= and <=)
    Returns filtered dictionary
    """
    #seqs = {'name': ('sequence', 'quality')}
    output = []
    result = dict()
    for name, (sequence, quality) in seqs.items():
            
        if seq_length(sequence) <= length_bounds[1] and seq_length(sequence) >= length_bounds[0]:
            output.append(name)
            if name in output:
                result[name] = (sequence, quality)
            
    return result


def quality_filter(seqs: dict, quality_threshold=25) -> dict:
    """
    Filters fastq reads by quality score
    Arguments:
    -dictionary
    -quality score threshold (>=)
    Returns filtered dict     
    """
    #seqs = {'name': ('sequence', 'quality')}
    output = []
    result = dict()
    for name, (sequence, quality) in seqs.items():
            
        if quality_score(quality) >= quality_threshold:
            output.append(name)
            if name in output:
                result[name] = (sequence, quality)
            
    return result


def gc_filter(seqs: dict, gc_bounds=(0,100)) -> dict:
    """
    Filters fastq reads by gc content
    Arguments:
    -dict
    -gc content parameters (>= and <=)
    Returns filtered dict
    """
    #seqs = {'name': ('sequence', 'quality')}
    output = []
    result = dict()
    for name, (sequence, quality) in seqs.items():
            
        if calc_gc_content(sequence) >= gc_bounds[0] and calc_gc_content(sequence) <= gc_bounds[1]:
            output.append(name)
            if name in output:
                result[name] = (sequence, quality)
            
    return result


def fastq_filter(seqs: dict, gc_bounds: int, length_bounds: int, quality_threshold: int) -> dict:
    """
    Filters fastq sequence by gc content, length and quality score
    Arguments: dict with fastq sequences, filtering parameters
    Returns filtered dictionary
    """
    resulting_sequences = dict()
    gc_filtered = gc_filter(seqs, gc_bounds = (0,100))
    length_filtered = length_filter(seqs, length_bounds = (0,1000))
    quality_filtered = quality_filter(seqs, quality_threshold = 15)
    intersection = gc_filtered.keys() & length_filtered.keys() & quality_filtered.keys()
    #intersection = {keys: gc_filtered[keys] for keys in gc_filtered.keys() & length_filtered.keys()}
    #for keys, (sequence, quality) in intersection:
    #    resulting_sequences[keys] = (sequence, quality)
    return intersection


############fastq to dict

def file_to_dict_keys(input_path: str) -> list:
    """
    Takes sequence names from a fastq file and creates a list
    """
    names = []
    if os.path.isfile(input_path) == True:
        with open(input_path) as py_file:
            lines = py_file.readlines()
            for line in lines:
                line.split(' 1:N')
                line = line.strip('\n')
                if line.startswith('@S'):
                    names.append(line)
            return names
            
            
def file_to_dict_values(input_path: str) -> list:
    """
    Takes reads and quality sequences and creates a list
    """
    prel_list = []
    sequences_list = []
    quality_list =[]
    values = []
    if os.path.isfile(input_path) == True:
        with open(input_path) as py_file:
            lines = py_file.readlines()
            for line in lines:
                line = line.strip('\n')
                if not (line.startswith('@S') or line.startswith('+S')):
                    prel_list.append(line)
                    quality_list = prel_list[1::2]
                    sequences_list = prel_list[0::2]
                    values = list(zip(sequences_list, quality_list))
            return values

                    
def fastq_to_dict(input_path: str) -> dict:
    """
    combines the two functions above and creates a dictionary
    """
    output_dict = dict()
    names = file_to_dict_keys(input_path)
    values = file_to_dict_values(input_path)    
    output_dict = dict(zip(names, values))
    return output_dict


#######dict to fastq for output

def dict_to_fastq(filtered_dict: dict, output_filename: str) -> list:
    """
    Turns dictionary into a fastq file
    Arguments: dictionary and output file name
    Returns a fastq file in 'fastq_filtrator_results' folder
    """
    str(os.mkdir('fastq_filtrator_results'))
    #path_to_output_file = 'C:\\Users\\sme229\\BIOINF\\python\\HW5\\fastq_filtrator_results'
    current_dir = str(os.getcwd())
    path_to_output_file = os.path.join(current_dir, 'fastq_filtrator_results', output_filename)
    with open(path_to_output_file, mode='w') as file:
        for keys, (val1, val2) in filtered_dict.items():
            file.write(keys + '\n')
            file.write(val1 + '\n')
            file.write(keys + '\n')  
            file.write(val2 + '\n')
        return file



