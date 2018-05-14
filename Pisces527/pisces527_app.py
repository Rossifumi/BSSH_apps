import os
import sys

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


class Pisces527(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)


    def do_work(self, workspace_directory, appsettings, output_builder):
        output_project = appsettings.input["project-id"].content[0]
        otherParams = appsettings.input["other-params"].content[0]

        for sample in appsettings.input["app-result-id"].content:
            input_bam_path = sample.file_path
            sample_id = str(input_bam_path).split('/')[-1].split('.')[0]
            
            output_appresult = output_builder.create_output_appresult(output_project,sample_id,"Results for Sample ID: " + sample_id)
            
            sample_output_directory_path = os.path.join(workspace_directory, sample_id)
            os.makedirs(sample_output_directory_path)
                    
            # run pisces
            pisces_command = " ".join(["/usr/local/bin/dotnet","/Pisces_5.2.7.47/Pisces.dll","-bam",input_bam_path,"-g","/genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta","-o",sample_output_directory_path,otherParams])
            os.system(pisces_command)
            print "pisces_command is "+pisces_command
                    
            # upload output
            output_appresult.add_directory(sample_output_directory_path,sample_id)
            
            
if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = Pisces527(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()

