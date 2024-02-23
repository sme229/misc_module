from Bio import SeqIO
from Bio.SeqUtils import GC

def filter_fastq(input_path: str, quality_threshold: int, output_filename="final_filtered.fastq",  gc_bounds=(40, 60), length_bounds=(50, 350)):
    filename = input_path
    records = SeqIO.parse(filename, "fastq")
    ###quality filter
    good_reads = (rec for rec in records if min(rec.letter_annotations["phred_quality"]) >= quality_threshold)
    result_quality = SeqIO.write(good_reads, "good_quality.fastq", "fastq")
    result_quality_GC = SeqIO.parse("good_quality.fastq", "fastq")
    ###GC content filter
    min_gc_content = gc_bounds[0]
    max_gc_content = gc_bounds[1]
    GC_quality_filt = []
    
    for sequence in result_quality_GC:
        if min_gc_content <= GC(sequence.seq) <= max_gc_content:
            GC_quality_filt.append(sequence)
            
    result_quality = SeqIO.write(GC_quality_filt, "good_quality_GC.fastq", "fastq")
    result_quality_GC_length = SeqIO.parse("good_quality_GC.fastq", "fastq")
    
    ##length filter
    filtered_GC_quality_length = []
    
    for sequence in result_quality_GC_length:
        if len(sequence.seq) >= length_bounds[0] and len(sequence.seq) <= length_bounds[1]:
            filtered_GC_quality_length.append(sequence)
            
    result_quality = SeqIO.write(filtered_GC_quality_length, output_filename, "fastq")
    
    print(result_quality)

#filter_fastq("example_fastq.fastq", 15)
