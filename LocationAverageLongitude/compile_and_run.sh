rm -fr out_directory
hadoop com.sun.tools.javac.Main LocationAverage.java && jar cf loc-avg-lon-job.jar LocationAverage*.class && hadoop jar loc-avg-lon-job.jar LocationAverage ../data/ out_directory
