FROM ubuntu:20.04

# Requirements
RUN apt -y update && apt -y install \
      curl

# Python
RUN apt -y update && apt -y install \
      python3 \
      python3-pip \
      python3-dev

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ jupyterlab \
     && jupyter notebook --generate-config

WORKDIR /root/.jupyter
COPY jupyter_notebook_config.py jupyter_notebook_config.py

RUN mkdir /anaconda && cd /anaconda
WORKDIR /anaconda

# Python packages
#RUN pip3 install pycrypto
#RUN pip3 install numpy
#RUN pip3 install sympy


EXPOSE 8888

#CMD ["jupyter","lab"]