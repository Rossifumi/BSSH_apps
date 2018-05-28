FROM centos:centos7
RUN yum install -y which wget tar unzip git make gcc bzip2 \
&& wget https://bootstrap.pypa.io/get-pip.py \
&& python get-pip.py \
&& rm -rf get-pip.py
COPY bssh_native_app-0.9.1.0.tar.gz /bssh_native_app-0.9.1.0.tar.gz
RUN /usr/bin/pip install simplejson /bssh_native_app-0.9.1.0.tar.gz
COPY dna-amplicon-output-parser.py /dna-amplicon-output-parser.py
COPY json_to_csv.py /json_to_csv.py
USER root
WORKDIR /
