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
    result = dict()
    gc_filtered = gc_filter(seqs, gc_bounds)
    length_filtered = length_filter(seqs, length_bounds)
    quality_filtered = quality_filter(seqs, quality_threshold)
    intersection = gc_filtered.keys() & length_filtered.keys() & quality_filtered.keys()

    for keys, (sequence, quality) in seqs.items():
        if keys in intersection:
            result[keys] = (sequence, quality)
    return result

