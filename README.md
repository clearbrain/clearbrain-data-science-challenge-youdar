# ClearBrain data science challenge

#### Overview

This is an open ended, data science / product / statistics challenge.  Please read through the entire exercise first, 
then proceed with the parts you feel most comfortable with.  Due to limited time, 
it’s not expected that you’ll necessarily have time to expansively respond to each prompt, 
so be selective and feel free to move on to other parts as needed.

#### Scenario

Your potential company, Scootfinity, is going to become the latest Scooter Ride Share service — the “Uber for Scooters”. 
You have built a basic landing page to collect and measure interest in the product, 
and have data about potential riders who sign up: 
   whether they signed up or not as well as some of their characteristics such as their country, 
   the marketing channel, 
   their age, 
   whether they are repeat visitors 
   and the number of pages visited during that session (as a proxy for site activity/time spent on site).

Your project is 
   to understand the potential rider base, 
   and build a model that predicts conversion rate, 
   and based on the model, come up with ideas to best go after the opportunity in the new Scooter Ride Share market.

Come up with recommendations for the product team and the marketing team to scoop up some potential riders! 

#### Data

The rider hit data is available for download in this repsitory at [data/conversion_data.csv](data/conversion_data.csv):


The table has information about visitors during one session. Each row is a visitor session.

#### Columns

 - **country** : user country based on the IP address
 - **age** : user age. Self-reported at sign-up step
 - **new_user** : whether the user created the account during this session 
                  or had already an account and simply came back to the site
 - **source** : marketing channel source<br/>
   Ads: came to the site by clicking on an advertisement<br/>
   Seo: came to the site by clicking on search results<br/>
   Direct: came to the site by directly typing the URL on the browser 
 - **total_pages_visited**: number of total pages visited during the session.    
                            This is a proxy for time spent on site and engagement during the session.
 - **converted**: this is our label. 1 means they converted within the session,    
                                     0 means they left without buying anything.   
                                     
 The company goal is to increase conversion rate: # conversions / total sessions. 

#### Example
Here are the characteristics of the user in the first row.

|Field               |Value |Description
|--------------------|------|-----------
|country             | UK   | the user is based in the UK 
|age                 | 25   | the user is 25 yr old 
|new_user            | 1    | she created her account during this session 
|source              | Ads  | she came to the site by clicking on an ad 
|total_pages_visited | 1    | she visited just 1 page during that session 
|converted           | 0    | this user did not buy during this session
 
#### Challenges

Please respond to these challenges as fully as possible within the time frame, 
and write a brief description of your analysis for each.

1. Build a model that predicts conversion rate.

2. Using the model, determine which features are important in predicting conversion.

3. Come up with some recommendations of experiments you might run or changes you might make to the product team and to the marketing team

4. You have a client who is testing out a new marketing methodology. In order to test the new methodology, the client splits their users into two groups. In the first group, some users are treated with the new marketing methodology and others are put into a holdout. In the second group, some users are treated with the old marketing methodology and others are put into a holdout. The client sends you a report on the performance of the two campaigns: (their old methodology vs the new methodology) detailing the overall incremental conversion rate above the holdout of each group as well as "statistical significance" of the incremental conversation rate. "The new methedology shows an incremental conversion rate above its holdout of 3.5% with a statistical significance of 99%. The old methodology shows an incremental conversion rate above its holdout of 2.5% with a statistical significance of 99%". The client asks you if we can conclude whether the new marketing methedology will provide an increase in incremental conversions over the old methedology? This is all of the data you have to work with. You will need to interpret and come up with your conclusions from this data only.

5. (Bonus) If you were going to run the scooter share service, how would you use this data / model in production to continuously improve the product?

#### What you should submit
 - Any code / queries written for the exercise, (esp. #1 and #2): an ipython notebook would work well, for example.
 - A short writeup of experiments you might run or changes you might make to the product and marketing teams (#3)
 - A short writeup of analysis on the campaign outcome scenario (#4)
 - (Bonus) A short writeup of how you’d incorporate the modeling into a production workflow (#5).
