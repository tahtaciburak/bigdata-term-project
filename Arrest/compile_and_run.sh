rm -fr out_directory
hadoop com.sun.tools.javac.Main Arrest.java && jar cf arrest-type-count-job.jar Arrest*.class && hadoop jar arrest-type-count-job.jar Arrest ../data/ out_directory
