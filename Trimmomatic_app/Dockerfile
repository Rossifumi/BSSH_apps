FROM jjxu/base_image_dotnet
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz && \
tar -zxf jdk-8u151-linux-x64.tar.gz && \
update-alternatives --install /usr/bin/java java /jdk1.8.0_151/bin/java 100 && \
update-alternatives --install /usr/bin/javac javac /jdk1.8.0_151/bin/javac 100
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip && \
unzip Trimmomatic-0.36.zip
COPY bssh_native_app-0.9.0.0.tar.gz /bssh_native_app-0.9.0.0.tar.gz
RUN yum -y install python-pip && \
pip install simplejson /bssh_native_app-0.9.0.0.tar.gz
COPY run_trimmomatic.py /run_trimmomatic.py
