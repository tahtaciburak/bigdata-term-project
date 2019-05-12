rm -fr out_directory
hadoop com.sun.tools.javac.Main Year.java && jar cf year-count-job.jar Year*.class && hadoop jar year-count-job.jar Year ../data/ out_directory
