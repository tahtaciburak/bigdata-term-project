hadoop com.sun.tools.javac.Main FBICode.java && jar cf fbicode-count-job.jar FBICode*.class && hadoop jar fbicode-count-job.jar FBICode ../data/ out_directory
