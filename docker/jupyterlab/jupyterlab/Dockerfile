FROM python:3.8

RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com jupyterlab \
     && jupyter notebook --generate-config

WORKDIR /root/.jupyter
COPY jupyter_notebook_config.py jupyter_notebook_config.py

RUN mkdir /anaconda && cd /anaconda
WORKDIR /anaconda

# Python packages
#RUN pip3 install pandas -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install scipy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install matplotlib -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install numpy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
#RUN pip3 install sympy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com


EXPOSE 8888

#CMD ["jupyter","lab"]
