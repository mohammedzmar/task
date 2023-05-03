import os

class Vcf_task:
    def __init__(self, vcf_file):
        self.input_file = vcf_file
        self.chromosome_variants = {} #dictionary to store the variants

#read the inputs file and group the variants by chromosome
    def vcf_chromosome(self):
        with open(self.input_file, 'r') as vcf_file:
            for line in vcf_file:
                if line.startswith('#'):
                    continue
                fields = line.strip().split('\t')
                chromosome = fields[0]
                if chromosome not in self.chromosome_variants:
                    self.chromosome_variants[chromosome] = []
                self.chromosome_variants[chromosome].append(line)
#create output files
    def generate_chromosome_files(self):
        for chromosome in self.chromosome_variants:
            output_file_path = os.path.splitext(self.input_file)[0] + '_' + chromosome + '.vcf'
            with open(output_file_path, 'w') as output_file:
                output_file.write(''.join(self.chromosome_variants[chromosome]))

    def execute_vcf_file(self):
        self.vcf_chromosome()
        self.generate_chromosome_files()



my_vcf_splitter = Vcf_task('308-23-EIH_hg38.hard-filtered.vcf')
my_vcf_splitter.excute_vcf_file()