rm -fr out_directory
hadoop com.sun.tools.javac.Main CrimeType.java && jar cf crime-type-count-job.jar CrimeType*.class && hadoop jar crime-type-count-job.jar CrimeType ../data/ out_directory
