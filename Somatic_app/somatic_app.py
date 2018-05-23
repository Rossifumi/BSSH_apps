import os
import sys
#from glob import glob

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


class SomaticApp(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)


    def do_work(self, workspace_directory, appsettings, output_builder):
        output_project = appsettings.input["project-id"].content[0]
        #otherParams = appsettings.input["other-params"].content[0]
        hygeaParams = appsettings.input["hygea-params"].content[0]
        stitcherParams = appsettings.input["stitcher-params"].content[0]
        piscesParams = appsettings.input["pisces-params"].content[0]

        for sample in appsettings.input["app-result-id"].content:
            print "sample.file_path is "+sample.file_path
            input_bam_path = sample.file_path
            print "input_bam_path is "+input_bam_path
            sample_id = str(input_bam_path).split('/')[-1].split('.')[0]
            print "sample_id is "+sample_id
            
            output_appresult = output_builder.create_output_appresult(output_project,sample_id,"Results for Sample ID: " + sample_id)
            
            sample_output_directory_path = os.path.join(workspace_directory, sample_id)
            os.makedirs(sample_output_directory_path)
            
            # run re-header
            reheader_output_path = os.path.join(sample_output_directory_path,"CollapsedReads")
            os.makedirs(reheader_output_path)
            
            reheader_bam_tmp_name = ".".join([sample_id,"reheader_tmp","bam"])
            reheader_bam_tmp_path = os.path.join(sample_output_directory_path,reheader_bam_tmp_name)
            reheader_command_1 = " ".join(["/usr/local/bin/samtools","view","-H",input_bam_path,"|","cat","-","/resources/header","|","/usr/local/bin/samtools","reheader","-P","-",input_bam_path,">",reheader_bam_tmp_path])
            print "reheader_command_1 is "+reheader_command_1
            os.system(reheader_command_1)
            
            reheader_bam_name = ".".join([sample_id,"reheader","bam"])
            reheader_bam_path = os.path.join(reheader_output_path,reheader_bam_name)
            reheader_command_2 = " ".join(["/usr/bin/python","/resources/UMItag_add.py","--bam",reheader_bam_tmp_path,"--outbam",reheader_bam_path])
            print "reheader_command_2 is "+reheader_command_2
            os.system(reheader_command_2)
            
            reheader_command_3 = " ".join(["/usr/local/bin/samtools","index",reheader_bam_path])
            print "reheader_command_3 is "+reheader_command_3
            os.system(reheader_command_3)
            
            output_appresult.add_directory(reheader_output_path)
            
            # run hygea
            hygea_output_path = os.path.join(sample_output_directory_path,"IndelRealigned")
            os.makedirs(hygea_output_path)
            
            hygea_command = " ".join(["/usr/local/bin/dotnet","/Hygea_5.2.7.47/Hygea.dll","-b",reheader_output_path,"-outFolder",hygea_output_path,"-genomeFolders","/genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta",hygeaParams])
            print "hygea_command is "+hygea_command
            os.system(hygea_command)
            
            output_appresult.add_directory(hygea_output_path)
            
            # run stitcher
            stitcher_output_path = os.path.join(sample_output_directory_path,"IndelRealignedStitched")
            os.makedirs(stitcher_output_path)
            
            hygea_bam_path = "".join([hygea_output_path,"/",sample_id,".reheader.bam"])
            stitcher_command_1 = " ".join(["/usr/local/bin/dotnet","/Stitcher_5.2.7.47/Stitcher.dll","-Bam",hygea_bam_path,"-OutFolder",stitcher_output_path,stitcherParams])
            print "stitcher_command_1 is "+stitcher_command_1
            os.system(stitcher_command_1)
            
            stitcher_bam_path = "".join([stitcher_output_path,"/",sample_id,".reheader.stitched.bam"]) 
            stitcher_bam_tmp_path = "".join([stitcher_output_path,"/",sample_id,".reheader.stitched.bam_tmp"])
            stitcher_command_2 = " ".join(["/usr/local/bin/samtools","sort","-@ 4",stitcher_bam_path,"-o",stitcher_bam_tmp_path])
            print "stitcher_command_2 is "+stitcher_command_2
            os.system(stitcher_command_2)
            
            stitcher_command_3 = " ".join(["mv -f",stitcher_bam_tmp_path,stitcher_bam_path])
            print "stitcher_command_3 is "+stitcher_command_3
            os.system(stitcher_command_3)
            
            stitcher_command_4 = " ".join(["/usr/local/bin/samtools","index",stitcher_bam_path])
            print "stitcher_command_4 is "+stitcher_command_4
            os.system(stitcher_command_4)
            
            output_appresult.add_directory(stitcher_output_path)
            
            # run pisces
            pisces_output_path = os.path.join(sample_output_directory_path,"Pisces")
            os.makedirs(pisces_output_path)
            
            pisces_command = " ".join(["/usr/local/bin/dotnet","/Pisces_5.2.7.47/Pisces.dll","-b",stitcher_output_path,"-G","/genomes/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta","-OutFolder",pisces_output_path,piscesParams])
            print "pisces_command is "+pisces_command
            os.system(pisces_command)
            
            output_appresult.add_directory(pisces_output_path)
                    
            # run pepe
            
            
            
if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = SomaticApp(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()

