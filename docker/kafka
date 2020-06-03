一.镜像拉取
docker pull wurstmeister/zookeeper
docker pull wurstmeister/kafka

二.定义docker-compose.yml
version: '2'

services:
  zoo1:
    image: wurstmeister/zookeeper
    restart: unless-stopped
    hostname: zoo1
    ports:
      - "2181:2181"
    container_name: zookeeper

  # kafka version: 1.1.0
  # scala version: 2.12
  kafka1:
    image: wurstmeister/kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: localhost
      KAFKA_ZOOKEEPER_CONNECT: "zoo1:2181"
      KAFKA_BROKER_ID: 1
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_CREATE_TOPICS: "stream-in:1:1,stream-out:1:1"
    depends_on:
      - zoo1
    container_name: kafka
 

 ZooKeeper 2 Kafka

ZooKeeper的部分与上个例子一样，需要调整的是Kafka部分。

这里将第一个Kafka broker命名为kafka1，KAFKA_ADVERTISED_HOST_NAME参数设为kafka1，KAFKA_ADVERTISED_PORT设为9092。

对于第二个broker，相较第一个broker所有kakfka1的部分改为kafka2，包括service name和coontainer name。同时KAFKA_BROKER_ID设为2，KAFKA_ADVERTISED_PORT设为9093。

需要注意的是，当有不止一个kafka broker时，这里的hostname不能再设为localhost。建议设为本机IP地址。以Mac为例，使用ipconfig getifaddr en0指令来获取。

具体的docker-compose.yml文件内容如下：

  # ZooKeeper部分不变

  kafka1:
    image: wurstmeister/kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 192.168.1.2
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_ZOOKEEPER_CONNECT: "zoo1:2181"
      KAFKA_BROKER_ID: 1
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_CREATE_TOPICS: "stream-in:2:1,stream-out:2:1"
    depends_on:
      - zoo1
    container_name: kafka1


  kafka2:
    image: wurstmeister/kafka
    ports:
      - "9093:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: {ipconfig getifaddr en0指令的结果}
      // KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.204.128:9092
      KAFKA_ADVERTISED_PORT: 9093
      KAFKA_ZOOKEEPER_CONNECT: "zoo1:2181"
      // KAFKA_ZOOKEEPER_CONNECT=192.168.204.128:2181 改为宿主机器的IP地址，如果不这么设置，可能会导致在别的机器上访问不到
      KAFKA_BROKER_ID: 2
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      // KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092
    depends_on:
      - zoo1
    container_name: kafka2



docker-compose build  打包
docker-compose up -d 后台启动

docker exec -it kafka1 /bin/bash
在其中一个窗口里创建topic并运行producer:

kafka-topics.sh --zookeeper zookeeper:2181 --create --replication-factor 1 --partitions 1 --topic kafkatest
kafka-console-producer.sh --broker-list localhost:9092 --topic kafkatest
在另一个窗口里运行consumer:
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafkatest --from-beginning
保持上面的生产者和消费者在运行状态，在生产者命令行上输入文本回车后，消费者可以看到输出 。

查看主题：

kafka-topics.sh -list --bootstrap-server 127.0.0.1:9092

列出所有Kafka brokers
$ docker exec zookeeper bin/zkCli.sh ls /brokers/ids











version: '2'
services:
  zookeeper:
    image: wurstmeister/zookeeper   ## 镜像
    ports:
      - "2181:2181"                 ## 对外暴露的端口号
  kafka:
    image: wurstmeister/kafka       ## 镜像
    volumes: 
        - /etc/localtime:/etc/localtime ## 挂载位置（kafka镜像和宿主机器之间时间保持一直）
        - ./kafka-logs:/kafka
        - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "9092:9092"
    environment:
      KAFKA_ADVERTISED_HOST_NAME: 192.168.150.130   ## 修改:宿主机IP
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181       ## 卡夫卡运行是基于zookeeper的
  kafka-manager:  
    image: sheepkiller/kafka-manager                ## 镜像：开源的web管理kafka集群的界面
    environment:
        ZK_HOSTS: 192.168.150.130                   ## 修改:宿主机IP
    ports:  
      - "9000:9000"                                 ## 暴露端口

3. 运行

/* 运行单机版kafka */
docker-compose up -d

/*  运行kafka集群模式*/
/*  由于指定了kafka对外暴露的端口号，增加集群节点会报端口冲突的错误，请将kafka暴露的端口号删掉后再执行如下命令*/
/*  自己指定kafka的节点数量 */
docker-compose scale kafka=3    
