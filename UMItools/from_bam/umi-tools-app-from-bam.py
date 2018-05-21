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
        #bc_pattern = appsettings.input["bc-pattern"].content[0]
        #for sample in appsettings.input["sample-id"].content:
        for sample in appsettings.input["app-result-id"].content:
            
            #print type(sample)
            #sample_directory_path = os.path.basename(sample.directory_path)
            print "sample.directory_path is "+sample.directory_path
            
            appresult_list = os.listdir(sample.directory_path)
            for appresult_file in appresult_list:
                if os.path.splitext(appresult_file)[1] == '.bam':
                    input_bam_path = os.path.join(sample.directory_path,appresult_file)
                    print "input_bam_path is "+input_bam_path
                    sample_id = os.path.splitext(appresult_file)[0]
                    print "sample_id is "+sample_id
                    
                    # for each bam file
                    output_appresult = output_builder.create_output_appresult(output_project,
                                                                      sample_id,
                                                                      "Results for Sample ID: " + sample_id)
                    sample_output_directory_path = os.path.join(workspace_directory, sample_id)
            
                    print "sample_output_directory_path is "+sample_output_directory_path
            
                    dedup_output_directory_path = os.path.join(sample_output_directory_path, "dedup_output")
                    os.makedirs(dedup_output_directory_path)
            
                    debup_bam_file_path = os.path.join(dedup_output_directory_path, sample_id + ".dedup.bam")
                    log_file_path = os.path.join(dedup_output_directory_path, sample_id + ".log")
            
                    umi_tools_command = " ".join(["/usr/local/python2.7.12/bin/umi_tools","dedup","-I",input_bam_path,"--umi-separator=':'","-S",debup_bam_file_path,"-L",log_file_path,"--paired"])
            
                    exit_code = os.system(umi_tools_command)
                    if exit_code == 0:
                        appresult_subfolder_name = "Dedup_bam"
                        output_appresult.add_file(debup_bam_file_path, None, appresult_subfolder_name)
                        output_appresult.add_file(log_file_path, None, appresult_subfolder_name)
            
                    sorted_bam_path = os.path.join(dedup_output_directory_path, sample_id + ".dedup.sorted.bam")
                     
                    samtools_command = " ".join(["/usr/local/bin/samtools","sort",debup_bam_file_path,"-o",sorted_bam_path])
            
                    exit_code = os.system(samtools_command)
                    if exit_code == 0:
                        appresult_subfolder_name = "Dedup_bam"
                        output_appresult.add_file(sorted_bam_path, None, appresult_subfolder_name)
                
                    samtools_command = " ".join(["/usr/local/bin/samtools","index",sorted_bam_path])
                    exit_code = os.system(samtools_command)
                    if exit_code == 0:
                        appresult_subfolder_name = "Dedup_bam"
                        output_appresult.add_file(".".join([sorted_bam_path,"bai"]), None, appresult_subfolder_name)
            

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = UMIToolsApp(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()
