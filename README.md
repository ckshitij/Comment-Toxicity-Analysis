# Comment-Toxicity-Analysis (BE Project)

## Index 

  + **Dataset**
  + **Initial Stage**
     + **About Files**
     + **Fault**
  + **Final Engine**
  + **How to Configure Final Engine**
  + **Improvement Scope**
  + **Helpful Refrenceses**

## Dataset
+ [DataSet Download Site](https://figshare.com/articles/Wikipedia_Talk_Corpus/4264973)
+ [Engine Notebook Kaggle](https://www.kaggle.com/ckshitij/toxic-comment-classifier)


## Initial Stage 

+ This Initial Model is just for Comparing or for starting Without Preprocessing and Ensembling techniques.
+ It tells toxicity after Analysing the Comment.
  + If a comment is Toxic or Bad then it will return Toxic else it will return toxic.
  
 ![img](https://github.com/ckshitij/Comment-Toxicity-Analysis/blob/master/front_view.png)
  
  ### About Files

  + **ToxityAnalysis.ipynb** -> For building model
  + **finalized_model.pkl** -> Saved ML model
  + **RunModel.py** -> For Reloading model and analysing Comment
  + **app.js** -> For Running nodejs app
  
  ### Fault 
 
   + It take **more time** because it reload python script evertime on pressing Submitting the Comment. 
 
## Final Engine 

+ Here is the **engine** of the model which is hosted using **Flask**.
+ It **Resolved the Fault** of *Initial Stage Model*.
+ It Only takes time on **first time loading**.
+ It **Returns the Percentage** instead of Class. 
+ you Can See the **Jupyter-notebook** https://github.com/ckshitij/Comment-Toxicity-Analysis/blob/master/engine/Models/notebook.ipynb 

  + Here its gives the **Toxicity Percentage of the Comment**. 
  
  ![img1](https://github.com/ckshitij/Comment-Toxicity-Analysis/blob/master/1.png)
  
  + You Can see the **Difference between the Percentage** of the comment
  
  ![img2](https://github.com/ckshitij/Comment-Toxicity-Analysis/blob/master/2.png)
  
 ## How to Configure Final Engine
  
  + First Download the code directly from here in zip or clone through git.
  + Then go to the **engine folder**.
  + Click On the above **[Engine Notebook Kaggle](https://www.kaggle.com/ckshitij/toxic-comment-classifier)** and download all the .pkl file in **Models** folder.
  + Then to to the **Terminal** and run **app.py** file.
  + Then open your **Web Browser** and type **http://localhost:5000/**.
  
    ```sh
    
    git clone https://github.com/ckshitij/Comment-Toxicity-Analysis.git
    cd Comment-Toxicity-Analysis
    cd engine
    python3 app.py
    
    ```
    
 ## Improvement Scope
   
   + You Can improve this Code by *Increasing the n-gram range (1,3or4)* for **Word-Level** and *n-gram range (1,10)* for **Char-Level**.
   + You can use **Deeplearning RNN (LSTM)**.

## Helpful Refrenceses

+ [google Perspective](https://www.perspectiveapi.com/)
+ [kaggle Competition on Toxicity](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
+ [githu mediawiki-utilities](https://github.com/mediawiki-utilities/python-mwdiffs)
+ [Detecting Insults in Social Commentary Kaggle](https://www.kaggle.com/c/detecting-insults-in-social-commentary)
+ [Content Analysis](https://us.sagepub.com/en-us/nam/content-analysis/book234903)
+ [Abusive Language Detection in Online User Content](http://dl.acm.org/citation.cfm?id=2883062)
+ [Beware of Publicity! Perceived Distress of Negative Cyber Incidents and Implications for Defining Cyberbullying](http://www.tandfonline.com/doi/abs/10.1080/15388220.2014.971363?src=recsys&journalCode=wjsv20)
+ [Learning part-of-speech taggers with inter-annotator agreement loss](http://lowlands.ku.dk/employees/?pure=en%2Fpublications%2Flearning-partofspeech-taggers-with-interannotator-agreement-loss(ac7d9186-4f4e-4298-94bb-e10e96b46b49)%2Fexport.html)
