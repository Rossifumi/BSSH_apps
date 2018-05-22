FROM jjxu/base_image_dotnet
COPY bssh_native_app-0.9.1.0.tar.gz /bssh_native_app-0.9.1.0.tar.gz
RUN yum install -y ncurses-devel \
    && yum install -y bzip2-devel \
    && yum install -y xz-devel \
    && wget https://github.com/samtools/samtools/releases/download/1.6/samtools-1.6.tar.bz2 -O samtools-1.6.tar.bz2 \
    && tar xvjf samtools-1.6.tar.bz2 \
    && rm -rf samtools-1.6.tar.bz2 \
    && cd samtools-1.6 \
    && ./configure \
    && make \
    && make install \
    && cd /
RUN  wget https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && rm -rf get-pip.py \
    && /usr/bin/pip install simplejson /bssh_native_app-0.9.1.0.tar.gz \
    && /usr/bin/pip install numpy pandas scipy cython pysam future \
    && yum install -y python-devel \
    && /usr/bin/pip install regex matplotlib \
    && /usr/bin/pip install umi_tools \
    && wget https://ayera.dl.sourceforge.net/project/bowtie-bio/bowtie/1.2.2/bowtie-1.2.2-linux-x86_64.zip -O bowtie-1.2.2-linux-x86_64.zip \
    && unzip bowtie-1.2.2-linux-x86_64.zip \
    && rm -rf bowtie-1.2.2-linux-x86_64.zip
COPY umi-tools-app-fastq.py /umi-tools-app-fastq.py