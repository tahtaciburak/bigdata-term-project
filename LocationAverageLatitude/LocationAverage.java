import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LocationAverage {

public static class MapperClass extends Mapper<LongWritable, Text, Text, FloatWritable> {
    private Text word = new Text();
    
    public void map(LongWritable key, Text value, Context con) throws IOException, InterruptedException {

        StringTokenizer itr = new StringTokenizer(value.toString(),",");
        int i = 0;
        String flg = " ";
        while (itr.hasMoreTokens()) {
            word.set(itr.nextToken(","));
            if (i==20){
                try {
                    Float sayi = Float.parseFloat(word.toString());
                    con.write(new Text(flg), new FloatWritable(sayi));
                } catch (Exception e) {
                    //e.printStackTrace();
                }
            }
            i = i+1;
        }
    }
}

public static class ReducerClass extends
        Reducer<Text, FloatWritable, Text, Text> {
    public void reduce(Text key, Iterable<FloatWritable> valueList, Context con) throws IOException, InterruptedException {
        try {
            Double total = (double) 0;
            int count = 0;
            for (FloatWritable var : valueList) {
                total += var.get();

                count++;
            }
            Double avg = (double) total / count;
            String out = avg.toString();//"Total: " + total + " :: " + "Average: " + avg;
            con.write(key, new Text(out));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

public static void main(String[] args) {
    Configuration conf = new Configuration();
    try {
        Job job = Job.getInstance(conf, "Average Location");
        job.setJarByClass(LocationAverage.class);
        job.setMapperClass(MapperClass.class);
        job.setReducerClass(ReducerClass.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    } catch (IOException e) {
        e.printStackTrace();
    } catch (ClassNotFoundException e) {
        e.printStackTrace();
    } catch (InterruptedException e) {
        e.printStackTrace();
    }

}
}