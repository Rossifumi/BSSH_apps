import os
import sys

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


class TrimmomaticApp(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)

    def do_work(self, workspace_directory, appsettings, output_builder):
        output_project = appsettings.input["project-id"].content[0]
        
        # Setting parameters
        selectPhred = appsettings.input["select-phred"].content[0]
        selectAdapter = appsettings.input["select-adapter"].content[0]
        seedMismatches = appsettings.input["seedMismatches"].content[0]
        palindromeClipThreshold = appsettings.input["palindromeClipThreshold"].content[0]
        simpleClipThreshold = appsettings.input["simpleClipThreshold"].content[0]
        leading = appsettings.input["leading"].content[0]
        trailing = appsettings.input["trailing"].content[0]
        windowSize = appsettings.input["windowSize"].content[0]
        requiredQuality = appsettings.input["requiredQuality"].content[0]
        min_len = appsettings.input["min_len"].content[0]
        
        # for each sample
        for sample in appsettings.input["sample-id"].content:
            output_appresult = output_builder.create_output_appresult(output_project,
                                                                      sample.name,
                                                                      "Results for Sample ID: " + sample.id)
            sample_output_directory_path = os.path.join(workspace_directory, sample.id)
            count=0

            # set output directory
            paired_fastq_set_output_directory_path = os.path.join(sample_output_directory_path, "paired")
            unpaired_fastq_set_output_directory_path = os.path.join(sample_output_directory_path, "unpaired")
          
            os.makedirs(paired_fastq_set_output_directory_path)
            os.makedirs(unpaired_fastq_set_output_directory_path)
            
            # for each fastq dataset
            for fastq_set in sample.fastq_sets:
                count += 1
                
                # set outout for read1
                read1_paired_output_file_name = self.__get_output_paired_fastq_name(fastq_set.read_1_file_path)
                read1_unpaired_output_file_name = self.__get_output_unpaired_fastq_name(fastq_set.read_1_file_path)
                
                read1_paired_output_file_path = os.path.join(paired_fastq_set_output_directory_path, read1_paired_output_file_name)
                read1_unpaired_output_file_path = os.path.join(unpaired_fastq_set_output_directory_path, read1_unpaired_output_file_name)
                
                
                if fastq_set.is_paired:
                    # set output for read2
                    read2_paired_output_file_name = self.__get_output_paired_fastq_name(fastq_set.read_2_file_path)
                    read2_unpaired_output_file_name = self.__get_output_unpaired_fastq_name(fastq_set.read_2_file_path)
                    read2_paired_output_file_path = os.path.join(paired_fastq_set_output_directory_path, read2_paired_output_file_name)
                    read2_unpaired_output_file_path = os.path.join(unpaired_fastq_set_output_directory_path, read2_unpaired_output_file_name)
                    
                    # command line
                    trimmomatic_command = " ".join(["/usr/bin/java -jar /Trimmomatic-0.36/trimmomatic-0.36.jar PE",
                                                    selectPhred,
                                                    fastq_set.read_1_file_path,
                                                    fastq_set.read_2_file_path,
                                                    read1_paired_output_file_path,
                                                    read1_unpaired_output_file_path,
                                                    read2_paired_output_file_path,
                                                    read2_unpaired_output_file_path,
                                                    ":".join(["ILLUMINACLIP",selectAdapter,seedMismatches,palindromeClipThreshold,simpleClipThreshold]),
                                                    ":".join(["LEADING",leading]),
                                                    ":".join(["TRAILING",trailing]),
                                                    ":".join(["SLIDINGWINDOW",windowSize,requiredQuality]),
                                                    ":".join(["MINLEN",min_len])])
                    exit_code = os.system(trimmomatic_command)
                    if exit_code == 0:
                        appresult_subfolder_name = "Paired_Fastq_Output"
                        output_appresult.add_file(read1_paired_output_file_path, None, appresult_subfolder_name)
                        output_appresult.add_file(read2_paired_output_file_path, None, appresult_subfolder_name)
                        appresult_subfolder_name = "Unpaired_Fastq_Output"
                        output_appresult.add_file(read1_unpaired_output_file_path, None, appresult_subfolder_name)
                        output_appresult.add_file(read2_unpaired_output_file_path, None, appresult_subfolder_name)
                else:
                    trimmomatic_command = " ".join(["/usr/bin/java -jar /Trimmomatic-0.36/trimmomatic-0.36.jar SE",
                                                    selectPhred,
                                                    fastq_set.read_1_file_path,
                                                    read1_unpaired_output_file_path,
                                                    ":".join(["ILLUMINACLIP",selectAdapter,seedMismatches,palindromeClipThreshold,simpleClipThreshold]),
                                                    ":".join(["LEADING",leading]),
                                                    ":".join(["TRAILING",trailing]),
                                                    ":".join(["SLIDINGWINDOW",windowSize,requiredQuality]),
                                                    ":".join(["MINLEN",min_len])])
                    exit_code = os.system(trimmomatic_command)
                    if exit_code == 0:
                        appresult_subfolder_name = "Fastq_Output"
                        output_appresult.add_file(read1_unpaired_output_file_path, None, appresult_subfolder_name)

                
    def __get_output_paired_fastq_name(self, source_fastq_file_path):
        source_fastq_file_name = os.path.basename(source_fastq_file_path)
        split = source_fastq_file_name.split(".", 1)
        return ".".join([split[0], "paired", split[1]])

    def __get_output_unpaired_fastq_name(self, source_fastq_file_path):
        source_fastq_file_name = os.path.basename(source_fastq_file_path)
        split = source_fastq_file_name.split(".", 1)
        return ".".join([split[0], "unpaired", split[1]])

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = TrimmomaticApp(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()
