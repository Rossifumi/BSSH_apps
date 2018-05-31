import subprocess
import os
import sys

from bssh_native_app.BaseSpaceNativeApp import BaseSpaceNativeApp


def run_fastqc(fastq_file_path, kmer, workspace_directory):
    def get_unique_directory_path(candidate_directory_path):
        count = 0
        directory_path = candidate_directory_path
        while os.path.isdir(directory_path):
            count = count + 1
            directory_path = os.path.dirname(candidate_directory_path) + "_" + str(count) + "/"
        return directory_path

    candidate_output_directory = os.path.join(workspace_directory, os.path.basename(fastq_file_path) + "/")
    output_directory_path = get_unique_directory_path(candidate_output_directory)
    os.makedirs(output_directory_path)
    fastqc_command = ["fastqc", "--outdir", output_directory_path, "--kmers", kmer, "--extract", fastq_file_path]
    exit_code = subprocess.call(fastqc_command)
    return exit_code, output_directory_path


class FASTQCApp(BaseSpaceNativeApp):
    def __init__(self, input_directory_path, output_directory_path, scratch_directory_path, log_directory_path,
                 appsession_id=None):
        BaseSpaceNativeApp.__init__(self, input_directory_path, output_directory_path, scratch_directory_path,
                                    log_directory_path, appsession_id)

    def do_work(self, workspace_directory, appsettings, output_builder):
        # parse input properties
        output_project = appsettings.input["project-id"].content[0]
        sample = appsettings.input["sample-id"].content[0]
        kmer = appsettings.input["kmer-size"].content

        for fastq_set in sample.fastq_sets:
            # Analyze read 1 fastq file
            read_1_fastq_filename = os.path.basename(fastq_set.read_1_file_path)
            exit_code, output_directory_path_1 = run_fastqc(fastq_set.read_1_file_path, kmer, workspace_directory)

            if exit_code == 0:
                # create output AppResult for read 1
                output_appresult_1 = output_builder.create_output_appresult(output_project,
                                                                          read_1_fastq_filename,
                                                                          "Results for " + read_1_fastq_filename)
                output_appresult_1.add_directory(output_directory_path_1, "Files")

            if fastq_set.is_paired:
                # Analyze read 2 fastq file
                read_2_fastq_filename = os.path.basename(fastq_set.read_2_file_path)
                exit_code, output_directory_path_2 = run_fastqc(fastq_set.read_2_file_path, kmer, workspace_directory)

                if exit_code == 0:
                    # create output AppResult for read 2
                    output_appresult_2 = output_builder.create_output_appresult(output_project,
                                                                              read_2_fastq_filename,
                                                                              "Results for " + read_2_fastq_filename)
                    output_appresult_2.add_directory(output_directory_path_2, "Files")


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    scratch_dir = sys.argv[3]
    logs_dir = sys.argv[4]

    app = FASTQCApp(input_dir, output_dir, scratch_dir, logs_dir)

    app.start()

