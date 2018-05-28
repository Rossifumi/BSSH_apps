import os
import sys

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


class DNAApmliconOutputParser(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)


    def do_work(self, workspace_directory, appsettings, output_builder):
        output_project = appsettings.input["project-id"].content[0]

        for sample in appsettings.input["app-result-id"].content:
            appresult_list = os.listdir(sample.directory_path)
            for appresult_file in appresult_list:
                file_ext = '.'.join(appresult_file.split(".")[1:])
                sample_id = appresult_file.split(".")[0]
                if file_ext == 'annotations.json.gz':
                    input_json_path = os.path.join(sample.directory_path,appresult_file)
                    
                    output_appresult = output_builder.create_output_appresult(output_project,
                                                                      sample_id,
                                                                      "Results for Sample ID: " + sample_id)
                    sample_output_directory_path = os.path.join(workspace_directory, sample_id)
                    os.makedirs(sample_output_directory_path)
                    
                    # parse json
                    command_1 = " ".join(["cp", input_json_path, sample_output_directory_path])
                    os.system(command_1)
                    
                    compressed_json_path = os.path.join(sample_output_directory_path,appresult_file)
                    command_2 = " ".join(["gunzip",compressed_json_path])
                    os.system(command_2)
                    
                    uncompressed_json_path = os.path.join(sample_output_directory_path,".".join([sample_id,"annotations.json"]))
                    output_csv_path = os.path.join(sample_output_directory_path,".".join([sample_id,"annotations.csv"]))
                    command_3 = " ".join(["python","/json_to_csv.py","header",uncompressed_json_path,output_csv_path])
                    os.system(command_3)

                    # upload output
                    output_appresult.add_file(output_csv_path, None)
            
            
if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = DNAApmliconOutputParser(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()

