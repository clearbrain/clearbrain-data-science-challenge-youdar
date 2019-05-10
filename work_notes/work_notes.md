## Task

### Build a model that predicts conversion rate

The company goal is to increase conversion rate: # conversions / total sessions.   
The data contains a single row for each session, there is not time-stamp, so we can't look at evolution of 
the conversion rate. 

Ideally one should look at the data a little, plot and get some basic understanding of what we have   
(I will not do that now)   

Looking at the conversion rates, there are no NULLs in the data and the current value is `3%`   


### model, determine which features are important in predicting conversion.
The basic features in the data are   
- country    
- age                 
- new_user             
- source              
- total_pages_visited   
- converted           


We do not have info on the actual user (such as user account)   
We do not have dates in the data, so we can't look at the change over time   
What I would do is try to predict `converted = 1`   
and see what features are important. Try to understand what drive the conversion, rather than 
directly predict the conversion rate.   
In this way, once there is a model, you can test how changing feature effect conversion and   
then calculate the conversion rate.

I will do several thing (if I were to actually do the work):   
- Just ot get better understanding of the data I will run some clustering algorithm (k-means)   
   Just to see if there is something we can see that can help with creating good features
- I would have like to do couple of models   
1) Try to predict:   
   - converted_at_first_visit (new_user=1 and converted=1)   
   - converted_not_at_first (new_user=0 and converted=1)   
   - did_not_convert (converted=0)   
   so create a target feature `conversion_state` that capture those categories   

2) Use converted as the target, and try to predict `converted = 1` 
3) repeat (1) and (2) but sample down the `converted = 0`


I added an age range feature, such as `age_range`: `< 18`, `18 - 26`, `27 - 36`, ...   
I would do this after the first iteration of modeling, to see (using some x-ray method) if there   
are ranges suggested by the data. (the k-means might contribute some insight regarding this) but I did not do that     

The same for countries, I might create a `region` feature, in order to try and make the model more  
general and perhaps more interpretable. 

#### Models 
In general the tool I use, split the data to 6, 1 holdout and the other 5 for training and cross-validation.

Model with basic target (`converted`)   
`Regularized Logistic Regression (L2)`     

ROC and more:   
![roc](https://github.com/clearbrain/clearbrain-data-science-challenge-youdar/blob/master/images/roc_and_more_-_all_data_-_basic_target.png "ROC and more")   

Features impact:   
The feature `total_pages_visited` dominated the model prediction   
`age_reange` and `age` found to be redundant, I would drop the age feature if I would continue to work on it    
I would also run the model without the `total_pages_visited` to get more insight on the other   
features influence   
![Feature_Impact](https://github.com/clearbrain/clearbrain-data-science-challenge-youdar/blob/master/images/Regularized_Logistic_Regression_Feature_Impact_-_all_data_-_basic_target.png "Feature_Impact")   


Frequencies:   
![age_range Frequency](https://github.com/clearbrain/clearbrain-data-science-challenge-youdar/tree/master/images/Feature_age_range_Frequency_Values_-_all_data_-_basic_target.png "age_range Frequency")   
![pages_visited Histogram](https://github.com/clearbrain/clearbrain-data-science-challenge-youdar/tree/master/images/Feature_total_pages_visited_Histogram_-_all_data_-_basic_target.png "pages_visited Histogram")   


**(I get a little into on this model when it is done processin)**  
Model with new target (`target`, option 1 above)   
  

Model review image   
 


### Come up with some recommendations of experiments you might run or changes you might make to the product team and to the marketing team   
There are several features I would like to have, that to not include knowing the actual customer   
- day of the week   
- weekend / weekday  
- hour of day (local time)
- holiday (yes / know)

Those will allow to add features that capture interaction time line and frequency, and will allow   
making more inform recommendation about when to try and interact with the customer and in what way.   

If it is possible to know info like `user_account_uid`   
it would allow better understanding the effectiveness of the different sources on different users   
and again maybe help understand better when and how to interact with the customers      

### Testing
You have a client who is testing out a new marketing methodology.   
In order to test the new methodology, the client splits their users into two groups.   
In the first group, some users are treated with the new marketing methodology and others are put into a holdout.   
In the second group, some users are treated with the old marketing methodology and others are put into a holdout.   
The client sends you a report on the performance of the two campaigns:   
   (their old methodology vs the new methodology) detailing the overall incremental conversion rate   
   above the holdout of each group as well as "statistical significance" of the incremental conversation rate. 
   "The new methodology shows an incremental conversion rate above its holdout of 3.5% 
   with a statistical significance of 99%. The old methodology shows an incremental conversion rate above 
   its holdout of 2.5% with a statistical significance of 99%". 
The client asks you if we can conclude whether the new marketing methodology will provide an increase in   
incremental conversions over the old methodology? This is all of the data you have to work with.    
You will need to interpret and come up with your conclusions from this data only.

The significance of 99% imply that we reject the null hypothesis with p < 0.01, so the   
conversion rates of 3.5% and 2.5% do reflect data characteristics, and we expect to get those results  
99 times of a 100 such experiments.   
From 2.5% to 3.5% there is about 40% lift, which means that even if we do not get better conversion rate   
1% of the times, we still get value from the new methodology and should probably use it.

(This might change if we knew the margin of error or if the cost of the new methodology is more than the extra benefit)              

### (Bonus) 
If you were going to run the scooter share service, how would you use this data / model in production    
to continuously improve the product?

What I do currently in my models, is automatically checking what actually after the fact and compare   
those results to what we predicted. This help us in several ways, making sure that the model   
does not drift, allow the relevant team to follow up and evaluate how they are utilizing the insights. 
Typically I like to rebuild the model and re-evaluate the main features, so that the teams using this   
info can improve on their methodology.   

### General comments
just to save you and me time when continuing this process, I'll say several thoughts.   
My strength is definitely not memory, while learned and used very many concepts in ML and statistics,   
I tend to forget what I do not frequently ues. I like to focus on the problem on hand, finding best tools or methods     
to deal with each problem, learning or relearning what is relevant, utilizing existing knowledge and tools   
or developing tools that can help the next time I'll have to solve similar challenge.   
It is very important for me to deal with interesting and challenging problems, by I prefer to build and invent on others    
work rather than reinvent.   
