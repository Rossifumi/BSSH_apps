import subprocess
import os
import sys

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


class UMIToolsApp(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)

    def do_work(self, workspace_directory, appsettings, output_builder):
        output_project = appsettings.input["project-id"].content[0]
        bc_pattern = appsettings.input["bc-pattern"].content[0]
        ref_genome_folder = appsettings.input["DATA-GenomeFolder"].content[0]
        #ref_genome_index = "/".join([ref_genome_folder,"genome"])
        ref_genome_fa = "/".join([ref_genome_folder,"genome.fa"])
        
        #build index
        bowtie_index_directory_path = os.path.join(workspace_directory,"Bowtie_index","genome")
        os.makedirs(bowtie_index_directory_path)
        
        print "bowtie_index_directory_path is "+bowtie_index_directory_path
        bowtie_index_command = " ".join(["/bowtie-1.2.1.1/bowtie-build","-f",ref_genome_fa,bowtie_index_directory_path])
        exit_code = os.system(bowtie_index_command)
        
        for sample in appsettings.input["sample-id"].content:
            output_appresult = output_builder.create_output_appresult(output_project,
                                                                      sample.name,
                                                                      "Results for Sample ID: " + sample.id)
            sample_output_directory_path = os.path.join(workspace_directory, sample.id)
            count=0
            read1_fastq_files = []
            read1_fastq_files = list()
            read2_fastq_files = []
            read2_fastq_files = list()
            
            fastq_set_output_directory_path = os.path.join(sample_output_directory_path, "fastq_set")
            os.makedirs(fastq_set_output_directory_path)
            for fastq_set in sample.fastq_sets:
                count += 1
                #fastq_set_output_directory_path = os.path.join(sample_output_directory_path, "fastq_set_" + str(count))
                #os.makedirs(fastq_set_output_directory_path)
                log_file_path = os.path.join(fastq_set_output_directory_path, "fastq_set_" + str(count) + ".log")
                read1_output_file_name = self.__get_output_extracted_fastq_name(fastq_set.read_1_file_path)
                read1_output_file_path = os.path.join(fastq_set_output_directory_path, read1_output_file_name)
                umi_tools_command = ["/usr/local/python2.7.12/bin/umi_tools",
                                     "extract",
                                     "--log="+log_file_path,
                                     "--bc-pattern="+bc_pattern,
                                     "--stdin="+fastq_set.read_1_file_path,
                                     "--stdout="+read1_output_file_path]
                print "read1_output_file_path is "+read1_output_file_path
                print "read1_output_file_name is "+read1_output_file_name
                #global read1_fastq_files
                read1_fastq_files.append(str(read1_output_file_path))
                if fastq_set.is_paired:
                    read2_output_file_name = self.__get_output_extracted_fastq_name(fastq_set.read_2_file_path)
                    read2_output_file_path = os.path.join(fastq_set_output_directory_path, read2_output_file_name)
                    umi_tools_command.extend(["--read2-in="+fastq_set.read_2_file_path,
                                              "--read2-out="+read2_output_file_path])
                    #global read2_fastq_files
                    read2_fastq_files.append(str(read2_output_file_path))
                
                print "umi_tools_command is "+" ".join(umi_tools_command)
                exit_code = subprocess.call(umi_tools_command)
                if exit_code == 0:
                    #appresult_subfolder_name = "FastqSet_" + str(count)
                    appresult_subfolder_name = "FastqSet"
                    output_appresult.add_file(log_file_path, None, appresult_subfolder_name)
                    output_appresult.add_file(read1_output_file_path, None, appresult_subfolder_name)
                    if fastq_set.is_paired:
                        output_appresult.add_file(read2_output_file_path, None, appresult_subfolder_name)
            
            
            print "read1_fastq_files is "+" ".join(read1_fastq_files)
            print type(read1_fastq_files)
            print type(fastq_set_output_directory_path)
            
            #For all fastq output, do bowtie mapping
            bowtie_output_directory_path = os.path.join(sample_output_directory_path, "Bowtie_Alignment")
            os.makedirs(bowtie_output_directory_path)
            mapped_sam_path = os.path.join(bowtie_output_directory_path, sample.name + ".mapped.sam")
            
            if fastq_set.is_paired:
                read1_files = ",".join(read1_fastq_files)
                read2_files = ",".join(read2_fastq_files)
                bowtie_command = " ".join(["/bowtie-1.2.1.1/bowtie","--threads 4 -v 2 -m 10 -a",str(bowtie_index_directory_path),"-1",read1_files,"-2",read2_files,"--sam >",mapped_sam_path])
            else:
                read1_files = ",".join(read1_fastq_files)
                print "read1_files is "+read1_files
                bowtie_command = " ".join(["/bowtie-1.2.1.1/bowtie","--threads 4 -v 2 -m 10 -a",str(bowtie_index_directory_path),read1_files,"--sam >",mapped_sam_path])
           
            print "bowtie_command is "+bowtie_command
            #os.chdir(sample_output_directory_path)
            exit_code = os.system(bowtie_command)
            
            if exit_code == 0:
                appresult_subfolder_name = "Bowtie_Alignment"
                output_appresult.add_file(mapped_sam_path, None, appresult_subfolder_name)
                
            
            
            #For mapped sam, samtools 
            samtools_output_directory_path = os.path.join(sample_output_directory_path, "Samtools_Output")
            os.makedirs(samtools_output_directory_path)
            mapped_bam_path = os.path.join(samtools_output_directory_path, sample.name +".mapped.bam")
            sorted_bam_path = os.path.join(samtools_output_directory_path, sample.name +".sorted.bam")
            
            samtools_command = " ".join(["/usr/local/bin/samtools","import",ref_genome_fa,mapped_sam_path,mapped_bam_path])
            print "samtools_command is "+samtools_command
            exit_code = os.system(samtools_command)
            if exit_code == 0:
                appresult_subfolder_name = "Samtools_Output"
                output_appresult.add_file(mapped_bam_path, None, appresult_subfolder_name)
            
            samtools_command = " ".join(["/usr/local/bin/samtools","sort",mapped_bam_path,"-o",sorted_bam_path])
            print "samtools_command is "+samtools_command
            exit_code = os.system(samtools_command)
            if exit_code == 0:
                output_appresult.add_file(sorted_bam_path, None, appresult_subfolder_name)
            
            samtools_command = " ".join(["/usr/local/bin/samtools","index",sorted_bam_path])
            print "samtools_command is "+samtools_command
            exit_code = os.system(samtools_command)
            if exit_code == 0:
                output_appresult.add_file(".".join([sorted_bam_path,"bai"]), None, appresult_subfolder_name)
            
            #For example bam, dedup
            dedup_output_directory_path = os.path.join(sample_output_directory_path, "Dedup_Output")
            os.makedirs(dedup_output_directory_path)
            dedup_bam_path = os.path.join(dedup_output_directory_path, sample.name +".dedup.bam")
            
            dedup_command = " ".join(["/usr/local/python2.7.12/bin/umi_tools","dedup","-I",sorted_bam_path,"--output-stats=deduplicated -S",dedup_bam_path])
            print "dedup_command is "+dedup_command
            exit_code = os.system(dedup_command)
            if exit_code == 0:
                appresult_subfolder_name = "Dedup_Output"
                output_appresult.add_file(dedup_bam_path, None, appresult_subfolder_name)
                
            
            

    def __get_output_extracted_fastq_name(self, source_fastq_file_path):
        source_fastq_file_name = os.path.basename(source_fastq_file_path)
        split = source_fastq_file_name.split(".", 1)
        return ".".join([split[0], "extracted", split[1]])


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = UMIToolsApp(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()
