<h1>Tweet Classifier</h1>
<h2>Project board link:</h2>
https://github.com/TempleS19CIS3296-01/project-tweetneurelnetwork/projects/1

<h2>Part 1:</h2>
<h3><Team Members:</h3>
<ul>
  <li>John Mancini</li>
  <li>Qunchao Zhou</li>
</ul>
<br>
<h2>Project Relevance:</h2>
<p>This project is relevant to the class because it involves object oriented programming, utilizing API's, doing software development  with agile, potentially utilizing a database, and potentially adding parallelism (although cloud computing will abstract all of this most likely). John's experience is in the python programming language and a high level understanding of neural networks. Qunchao's experience is in databases. Both team members will be new to the TensorFlow library and cloud computing with Google Collaboration. The project is a tweet classifier. We will implement various machine learning models to approximate tweet sentiment classifications and then allow users to scrape tweets from others and run those tweets through our model.</p><br>

<h2>Sprints</h2>
<h4>Sprint 1</h4>
<p>During the first sprint, we gathered resources for our project. Both John and Qunchao downloaded the relevant packages to set up our respective environments. We also started gathering information about the various machine learning models we wanted to implement. We started reading documentation from tensor flow and sklearn and implementing small projects with those APIs to get more comftorable with them.</p>
<h4>Sprint 2</h4>
<p>During the second spring John and Qunchao split off and started exploring various machine learning models. John read multiple research papers about naive bayes and implemented that on his local device. He was able to tweak parameters sufficiently to achieve 70% approximations. Qunchao explored neural networks. He continued reading the tensorflow API and started to implement small neural networks with it. The size of the data set was also a problem. The original dataset file was too large and therefore needed to be fragmented into smaller files. John wrote some python3 code, using the csv library, to fragment the original file of 800k positive followed by 800k negative tweets to 16 files of 50k positive followed by 50k negative tweets. The way this was tested was every single tweet was iterated over in a nested for loop (so each tweet was compared to every other tweet with the exception of itself), and if the unique tweet id matched another tweet then the test failed. Also, if any of the 16 csv files had a different number of rows than 100k, or if they had a different number of positive and negative tweets than 50k, the tests were failed. All the tests were completed successfully.</p>
<h4>Sprint 3</h4>
<p> During the third spring, John and Qunchao continued to work seprately on their respective tasks. John continued with the naive bayes model but was now working in a different environment. John started to learn the google colab environment, a cloud computing service that was vitial to this project. After the google colab environment was successfully learned, the code then needed to be fragmented because it was only viable on a local device. This was not difficult but was tedious, as the whole data parsing method had to be changed which is the most tedious part of this project. Qunchao continued learning tensorflow in the attempt to learn how to utilize a neural network. During our scrum meeting, this was where we decided to abandon the neural network model and instead focus on UI.</p>
<h4>Sprint 4</h4>
<p> During the forth spring John and Qunchao combined their code to develop a final project. Qunchao worked on scraping tweets from the user and John continued improving the naive bayes model as well as implementing a new model called decision trees. John and Qunchao worked on refactoring the code in such a way that it could run on google colab in a ram efficient manner as well as allowing the user a good, non-annoying experience when running this code. </p>
<h2>MILESTONES:</h2>
<h4>Sprint 1</h4>
<ul>
  <li>Set up environment: This took under an hour (John, Qunchao). It simply involved downloading python3, the data set we are working with, and a few libraries with pip.</li>
</ul>
<h4> Sprint 2</h4>
<ul>
  <li>Implement Naive Bayes Method on the data (John): This took 6-8 hours. First I had to learn what naive bayes was, which is a stochastic method for classifying things using Baye's theorem. Then I had to learn how to clean my data. Surprisingly, this was quite difficult because my data set is just one massive csv file with 800k postively rated tweets followed by 800k negatively rated tweets. After the data was "cleaned", cleaned here means that I was able to feed it properly to the sklearn library, and I trained a gaussian distribution based model with sklearn, I received 64% approximation. I was happy with anything over 50%. After tweaking the parameters I got up to 70% approximation, well above the 50% baseline.
  <br>
    <p>Results:</p>
    <img src="https://github.com/TempleS19CIS3296-01/project-tweetclassifier/blob/readmebranch/70percent.png" class="inline">
    <img src="https://github.com/TempleS19CIS3296-01/project-tweetclassifier/blob/readmebranch/paramaters.png" class="inline"></li>

  <li>Fragment data into 16 seperate files (John): This took about 2 hours. The first part was making sure I properly fragmented the data into 16 files. That means putting 50k positive then 50k negative tweets into 16 seperate files. The longest part was testing. Firstly, I tested to make sure the length of each file was 100k. Then I made sure each file had 50k positive and 50k negative tweets. Lastly, I made sure the tweet id, which is a unique id assigned to a tweet, was different across all files, therefore confirming that each tweet in each file is unique. From all of that I was able to conclude that the file was fragmented properly and I was finally ale to upload the data set to github.</li>
</ul>
<h4>Sprint 3</h4>
<ul>
  <li>Learn google colab environment (John): This took about 4 hours. Google colab was a decently tricky environment to get comftorable with. Firstly, I had to figure out how to actually get the code I wanted into google colab. This was the hardest part that required a good amount of research. Then I had to get accustomed to the environment. Ultimately, it came down to simply cloning the repo I want to work with into the virtual machine and navigating to the right directory.</li>
  <li>Refactoring naive bayes code to work with google colab (John): This took about 2 hours. The previous version of the code was written to work on my local device and was confined to my local devices hardware constraints. Therefore, I had to do certain things with the train and test data as to not over use my ram. On google colab, I have more ram and computational power. So the code had to be refactored to take that into consideration. It was ultimately not difficult, and debugging in the google colab environment is straightforward. But editing code is annoying as it has to be done on a local device, pushed to github, and then pulled from github in google colab. </li>
</ul>
<h4>Sprint 4</h4>
<ul>
  <li>
    Implement decision trees (John): This took about 5 hours. Simply utilizing the code was not very time consuming, but reading the documentation and some online sources on decision trees to learn how they work took a few hours. Then the code needed to be refactored because the data parsing for naive bayes was not precisely the type of data parsing necessary for decision trees. The final implementation of decision trees garnered 65% approximations.
  </li>
  <li>
    Imporve naive bayes (John): This took a about 2 hours. I was experimenting with various distributions, as well as various parameters within those distributions. Doing so on google colab is time consuming because it requires one to edit code in a seperate environment, push it to github, pull it from github on google colab, and then rerun the code on google colab. This must be done every time a paramater is changed. The final distribution was multinomial and the final parameters were 3500 words in our vocabulary, 300k train tweets, 100k test tweets.
  </li>
  <li>
    Create user interface (Qunchao): This took about 4 hours. I had to first learn the twitter API and understand how it works, then I had to use it to fulfill the purposes of our project. I was able to successfully develop our requirements through a python library that accesses twitter called tweepy. With this library I was able to allow a user to enter a twitter handle and then parse their tweets. Then those tweets get written to a csv file in the same format as our training and testing data so those tweets can be run through the model
  </li>
  <li>
    Merging it all together (John and Qunchao): This took about 3 hours. With Qunchao's twitter scraping code and John's machine learning model code, it was time to put it all together. Putting it together meant developing the control flow in such a way as to minimize RAM usage and allow the user the most options when testing the project.
  </li>
    
</ul>

<h2>Things we did not do</h2>
<ul>
  <li>Neural Network: We ultimately did not end up implementing the neural network. While John continued working on various machine learning algorithms, Qunchao was learning the tensorflow API and attempting to implement the neural network. As time constraints grew more concerning, we decided to abandon the neural network. We felt confident in doing to because in the research papers we read many researchers did not use neural networks, instead implementing models that we ultimitely used like naive bayes and decision trees. Also, we achieved 74% accurate approximations with naive bayes, which we felt was strong.</li>
  <li>>80% accurate approximations: We ultimately could not get our models to greater than 80% approximations. This was a goal of ours because a research team at Stanford that utilized our data set got about 80% accurate approximations. We felt that was a good goal to strive for. Unfortunately we did not make it, ending at 74%. We still feel confident about this because we had no knowledge of machine learning before this and were able to do enough research to implement strong models that did an incredible thing, namely sentiment classification of tweets.</li>
</ul>
  
