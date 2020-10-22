# Predicting cardiovascular risk

Source : https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

### Contexte
•	Leading cause of death worldwide
•	Second in France (just after cancers)
•	First cause of death for women


### Aim 
=> identify factors that may influence the occurrence of cardiovascular risk for prevention purposes

### Task
=> predict the presence or absence of CVD using patient exam results.

### Advantage
=> large volume of data

 

### EDA
Target : Balanced (50% CVD)
Features : categorical features are Unbalanced : smoke, alco, gluc, active, chol
It is important to update of the dataset with more patients : more smoking data,  more drinking alcohol…
Strong correlation between features : gluc / chol / age /  height …

### Preprocessing
Choice of variables for prediction: Forward selection, Feature selection
Normalisation
Data cleaning: outliers, ...

### Modelling
I developed some Machine Learning models for a binary classification problem but also deep learning algorithms with libraries as tensorflow and fastAI which is recommended if the available data size is large (70 000 patients).

Machine Learning : Random forest, Gradient Boosting, SVM, KNN
=> Best score : Gradient Boosting Classifier

Deep Learning with libraries Tensorflow and FastAI
=> Score : 74% (on average)
Deep Learning sometimes applies well to the datasets we are used to processing. Their real advantage is to save us a lot of preprocessing
 


### Conclusion
From a scientific point of view is that ap_hi, age, cholesterol, weight, ap-lo etc, already allow to predict the risk effectively.
But for example, the fact that smoke and alcohol have low coefficients does not mean that these are not risk factors... It just means they don’t bring more information than we already have. My hypothesis is that ap_hi and cholesterol are correlated with these variables, and so the information about someone smoking is already implicitly contained in these variables. In short: in fact, you can unfortunately not conclude on the risk factors, this is why epidemiological studies are very complicated to carry out: because all the variables are correlated with each other



### Web App.
Create a webApp with Flask in order to predict wether MCV from the Gradient Boosting model which offers the best score.

