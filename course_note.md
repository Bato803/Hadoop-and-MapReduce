# Hapdoop and MapReduce Notes

## Core Hadoop
1. Store data in HDFS (Hapdoop distributed file system), and process data in MapReduce. 
2. Key of the Core Hadoop system work: 
  - We split the data, and store it across a collection of machines, known as a cluster. And we process it where it was stored, rather than retrieving data from central server. So it's processed in place. 
  - More machine can be added to the cluster as the amount of data grows. 
3. Hadoop ecosystem:
  - Hive(turns SQL into MapReduce code, and then run it in the cluster), Pig; (These two might need more time because it's still running MapReduce code.)
  - Impala: Write SQL to directly access HDFS, it's optimized for low latency query. (No need to translated to MapReduce.) Hive is optimzied for long, batched processing job. 
  - Sqoop: Takes data from traditional relational database, and put it in HDFS files. 
  - Flume: Put external generated data into HDFS. 
  - HBase/Hue/Oozie/mahout....
  - CDH: Package all of them...Far easier to install CDH to have everything. 
  

## Hadoop Distributed File System
1. One file is split into different blocks, such as blk_1, blk_2, blk_3. 
2. Each block is store in one node of the cluster, separately. Namenode store the metadata about which block is stored in which node. 
3. To make the system more safe, Hadoop doesn't just store the block in one node. But in three nodes instead. This takes care of the problem that if one of the data nodes fail. 
4. To solve the problem if the meta node fails, people doesn't just store the namenode in its own harddrive, but also somewhere in the network system (NFS); There is an alternative solution as well, active namenode and standby namenode. 
5. Mapper and Reducer. 
  - Each mapper deals with a small amount of data and works in parallel, the output is called intermedimate records. (The record is dealt with in the form of (key, value))
  - Once the mappers have finished, a phase called shuffle and sort take place. Shuffle: the movement of intermediate record from mappers to reducers; Sort: the reducer would organize the records. 
6. When we run a map reduce job, we submit the job to what's called job tracker. That splits the job into mappers and reducers. 
  - There is a task tracker in each of the data node. The task tracker and the data node run at the same machine, the Hadoop framework would be able to have the map task tracker work directly on the pieces of data that are stored on the machine. That save a lot of traffics. 
  - Each mapper processes a portion of the input data, that's known as the input split. And by default, Hadoop would use a HDFS block as the input split for each mapper. It makes sure each mapper works on data on the same machine. 
  - If the task tracker could already been busy, in this case a different node would be chosen, and it would be streamed over the network.
  - Then the mapper passes the output to the reducer, then the reducer pass the final result back to HDFS. 
