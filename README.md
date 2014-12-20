# Reddit Top 2.5 Million

## What is this?

This is a dataset of top posts from [reddit](http://www.reddit.com). It contains the top 1,000 all-time posts from the top 2,500 subreddits, so 2.5 million posts in total. The top subreddits were determined by subscriber count and are located in the manifest file within.

Ths data was pulled between August 15-20 of August 2013.

Each file is a CSV with the related subreddit as its filename. Each CSV file contains a header line.

[A good example of the structure of this data is here.](https://github.com/umbrae/reddit-top-2.5-million/blob/master/data/serendipity.csv)


### RESEARCH QUESTION
How is corporate media reflected on social media?  How do world events published
in mainstream media reflect sentiment of social media posts?

### NLP
For NLP We will be using nltk.  Install with pip:
sudo pip install -U nltk

### SCI KIT LEARN
Install with pip:
pip install -U scikit-learn

### Where we got the data from
https://github.com/umbrae/reddit-top-2.5-million

### News articles

####Newtown school shooting
http://www.endmemo.com/events/evt/2012gunmanassaults.php

####NSA Prism program leaked
http://www.endmemo.com/events/evt/2013usnsa.php

####Boston marathon bombed
http://www.endmemo.com/events/evt/2013bostonmarathon.php

####Facebook IPO
http://www.endmemo.com/events/evt/2012facebookipo.php

We have 3 news articles from NYT, Fox, and CNN for each event.  These are stored as text files under /articles. 


####Useful links
* https://pypi.python.org/pypi/textblob
* https://textblob.readthedocs.org/en/dev/quickstart.html#sentiment-analysis
* http://textblob.readthedocs.org/en/latest/advanced_usage.html
* http://scikit-learn.org/stable/user_guide.html
* http://scikit-learn.org/stable/install.html

#####Hypothesis
* Foreseen events such as the facebook IPO will show less disparity between sentiment before and after the event.  What we predict is that random events like the Newton massacre will show a huge disparity between before/after the event.

* High profile traumatic news events might inititally decrease subjectivity but weeks after, when the event degenerates to a commentary about gun laws or something like that, will increase subjectivity.  Also, polarity will probably be negative following the events because of the impact people feel from the events.

* News articles will fit into the densest cluster of sentiment.  They will not represent extreme opinion but rather a more neutral ideology.

* Different news sources will maintain different average sentiments.  This may be based on political leaning

#####METHODS
We will use positivity, negativity, objectivity, and polarity as predictors.  

##### Results
These are the clusters that we were able to render through our Sentiment Analysis.

A week Before Sandy Hook:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/TotalWeekCluster.png)

A week After Sandy Hook:
![alt tag](https://github.com/swam92/datasetsProject/blob/master/FinalResults/weekAfterSandy.png)

A week before Boston Marathon Bombing:
![alt tag](https://raw.githubusercontent.com/Stefaney/datasetsProject/master/FinalResults/BostonBefore.png)

A week After Boston Marathon Bombing:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/BostonAfter.png)

A week before Facebook IPO:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/FacebookBefore.png)

A week after Facebook IPO:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/FacebookAfter.png)

A week before NSA Prism Leak:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/NSABefore.png)

A week after NSA Prism Leak:
![alt tag](https://raw.githubusercontent.com/swam92/datasetsProject/master/FinalResults/NSAafter.png)



