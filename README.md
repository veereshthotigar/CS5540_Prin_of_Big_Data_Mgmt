<h2 align="center"> Prin of Big Data Mgmt project</h2>

<h4>Team Details</h4>
<blockquote>
 <p>Veeresha M Thotigar</p>
 </blockquote>
<blockquote>
 <p>Sai Sampath Kumar Raigiri </p>
 </blockquote>
 <blockquote>
 <p>Sai Srinivas Vidiyala</p>
 </blockquote>

# Phase 1

1. Firstly we generated Twitter Access keys from the developers.twitters.com using our twitter accounts.

2. Using tweepy package in python we downloaded data on topic yoga, medetation, etc.,

3. Writing python code again we extracted url and hashtags for downladed tweets and the output is our translated input.

4. We loaded traslated input to hdfs directory using "HDFS DFS -copyFromLocal source path HDFS destination path" command in the terminal.

5. We used the example word count program which is part of haddop installation and produced word count for the large data.

6. simillarly we executed spark word count job for the same input data to process the data. and the out put is in the folder

<hr>

      We Pushed our hadoop log files , output, commands that we used in the terminal in the form of "steps_hadoop_wordcount.txt".

      Hadoop folder conains the output and logs generated for the hadoop word count program.

      tweetcrawler.py file in folder Python_script contains python code for downloading tweets using keys and saving them into a csv file.

      Extract.py file in folder Python_script contains python code for extracting URLs and HashTags from the downloaded tweets into a text file.

      Spark folder contains the output and logs of the job submitted.
