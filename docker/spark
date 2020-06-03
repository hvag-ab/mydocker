## 安装单机Spark-Hadoop集群

1 创建目录
mkdir spark
cd spark
vi docker-compose.yml

2 编写docker-compose.yml:
version: "2.2"
services:
  namenode:
    image: bde2020/hadoop-namenode:2.0.0-hadoop3.1.3-java8
    container_name: namenode
    volumes:
      - ./hadoop/namenode:/hadoop/dfs/name
      - ./input_files:/input_files
    environment:
      - CLUSTER_NAME=test
    env_file:
      - ./hadoop.env
    ports:
      - 50070:9870
      - 8020:8020
  
  resourcemanager:
    image: bde2020/hadoop-resourcemanager:2.0.0-hadoop3.1.3-java8
    container_name: resourcemanager
    depends_on:
      - namenode
      - datanode1
      - datanode2
    env_file:
      - ./hadoop.env
  
  historyserver:
    image: bde2020/hadoop-historyserver:2.0.0-hadoop3.1.3-java8
    container_name: historyserver
    depends_on:
      - namenode
      - datanode1
      - datanode2
    volumes:
      - ./hadoop/historyserver:/hadoop/yarn/timeline
    env_file:
      - ./hadoop.env
  
  nodemanager1:
    image: bde2020/hadoop-nodemanager:2.0.0-hadoop3.1.3-java8
    container_name: nodemanager1
    depends_on:
      - namenode
      - datanode1
      - datanode2
    env_file:
      - ./hadoop.env
  
  datanode1:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.1.3-java8
    container_name: datanode1
    depends_on:
      - namenode
    volumes:
      - ./hadoop/datanode1:/hadoop/dfs/data
    env_file:
      - ./hadoop.env
  
  datanode2:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.1.3-java8
    container_name: datanode2
    depends_on:
      - namenode
    volumes:
      - ./hadoop/datanode2:/hadoop/dfs/data
    env_file:
      - ./hadoop.env
  
  datanode3:
    image: bde2020/hadoop-datanode:2.0.0-hadoop3.1.3-java8
    container_name: datanode3
    depends_on:
      - namenode
    volumes:
      - ./hadoop/datanode3:/hadoop/dfs/data
    env_file:
      - ./hadoop.env

  master:
    image: gettyimages/spark:2.4.1-hadoop-3.0
    container_name: master
    command: bin/spark-class org.apache.spark.deploy.master.Master -h master
    hostname: master
    environment:
      MASTER: spark://master:7077
      SPARK_CONF_DIR: /conf
      SPARK_PUBLIC_DNS: 127.0.0.1
    links:
      - namenode
    expose:
      - 4040
      - 7001
      - 7002
      - 7003
      - 7004
      - 7005
      - 7077
      - 6066
    ports:
      - "49100:22"
      - 4040:4040
      - 6066:6066
      - 7077:7077
      - 8080:8080
    volumes:
      - ./conf/master:/conf
      - ./data:/tmp/data
      - ./jars:/root/jars

  worker1:
    image: gettyimages/spark:2.4.1-hadoop-3.0
    container_name: worker1
    command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
    hostname: worker1
    environment:
      SPARK_CONF_DIR: /conf
      SPARK_WORKER_CORES: 2
      SPARK_WORKER_MEMORY: 2g
      SPARK_WORKER_PORT: 8881
      SPARK_WORKER_WEBUI_PORT: 8081
      SPARK_PUBLIC_DNS: 127.0.0.1
    links:
      - master
    expose:
      - 7012
      - 7013
      - 7014
      - 7015
      - 8881
      - 8081
    ports:
      - 8081:8081
    volumes:
      - ./conf/worker1:/conf
      - ./data/worker1:/tmp/data

  worker2:
    image: gettyimages/spark:2.4.1-hadoop-3.0
    container_name: worker2
    command: bin/spark-class org.apache.spark.deploy.worker.Worker spark://master:7077
    hostname: worker2
    environment:
      SPARK_CONF_DIR: /conf
      SPARK_WORKER_CORES: 2
      SPARK_WORKER_MEMORY: 2g
      SPARK_WORKER_PORT: 8881
      SPARK_WORKER_WEBUI_PORT: 8082
      SPARK_PUBLIC_DNS: 127.0.0.1
    links:
      - master
    expose:
      - 7012
      - 7013
      - 7014
      - 7015
      - 8881
      - 8082
    ports:
      - 8082:8082
    volumes:
      - ./conf/worker2:/conf
      - ./data/worker2:/tmp/data


注意：

将SPARK_PUBLIC_DNS这个配置的ip换成你自己想暴露的机器ip  默认是本地
对于master，我们额外暴露了49100映射内部ssh的22端口，因为我们想远程调试。

3 编写hadoop配置：

vi hadoop.env
文件内容：
CORE_CONF_fs_defaultFS=hdfs://namenode:8020
CORE_CONF_hadoop_http_staticuser_user=root
CORE_CONF_hadoop_proxyuser_hue_hosts=*
CORE_CONF_hadoop_proxyuser_hue_groups=*

HDFS_CONF_dfs_webhdfs_enabled=true
HDFS_CONF_dfs_permissions_enabled=false

YARN_CONF_yarn_log___aggregation___enable=true
YARN_CONF_yarn_resourcemanager_recovery_enabled=true
YARN_CONF_yarn_resourcemanager_store_class=org.apache.hadoop.yarn.server.resourcemanager.recovery.FileSystemRMStateStore
YARN_CONF_yarn_resourcemanager_fs_state___store_uri=/rmstate
YARN_CONF_yarn_nodemanager_remote___app___log___dir=/app-logs
YARN_CONF_yarn_log_server_url=http://historyserver:8188/applicationhistory/logs/
YARN_CONF_yarn_timeline___service_enabled=true
YARN_CONF_yarn_timeline___service_generic___application___history_enabled=true
YARN_CONF_yarn_resourcemanager_system___metrics___publisher_enabled=true
YARN_CONF_yarn_resourcemanager_hostname=resourcemanager
YARN_CONF_yarn_timeline___service_hostname=historyserver
YARN_CONF_yarn_resourcemanager_address=resourcemanager:8032
YARN_CONF_yarn_resourcemanager_scheduler_address=resourcemanager:8030
YARN_CONF_yarn_resourcemanager_resource___tracker_address=resourcemanager:8031

然后，我们就能启动啦：

cat docker-compose.yml && cat hadoop.env && docker-compose up -d

全都是up之后，部署就是成功了，如果哪个没有成功，通过

docker logs 名称（例如master）

注意当前目录下的文件不能删除或者自行修改与修改权限，是镜像里面的文件出来的，如果操作不当会导致集群重启不成功。

访问下spark：http://localhost:8080
访问下hdfs：http://localhost:50070


docker exec -it master /bin/bash
pip install wheel
pip  install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com  pyspark==2.4.1
pip  install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com  jupyter


jupyter notebook --no-browser --port 6066 --ip=172.25.0.6 --allow-root
这里的ip 地址 是 docker inspect master 查看容器的虚拟ip  也就是其中 "IPAddress": "172.25.0.6", 
port 是 映射端口 就是容器映射到主机的端口 我选择的6066

启动了后 运行的日志中 复制
例如 http://172.25.0.6:6066/?token=d450139123190d0efb5ba77bfc61a3172aa37cc38072211c
然后吧IP 换成 本机ip  http://localhost:6066/?token=d450139123190d0efb5ba77bfc61a3172aa37cc38072211c

from pyspark.sql import SparkSession, Row

<!-- spark = SparkSession.builder.appName("Hash")\
    .config("spark.num.executors", "1") \
    .config("spark.executor.cores", "2") \
    .config("spark.executor.memory", "600m") \
    .config("spark.driver.memory", "600m") \
    .getOrCreate()

sc = spark.sparkContext -->

from pyspark import SparkContext
sc = SparkContext("local[*]", "count app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])
counts = words.count()
print("Number of elements in RDD -> %i" % counts)
