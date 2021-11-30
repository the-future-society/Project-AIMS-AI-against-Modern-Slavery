<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">
 
<img align="center" alt="Coding" width="550" src="https://cdn.dribbble.com/users/1581085/screenshots/3984307/media/826088ba21447e50a7e525eb592774a3.gif">




#Sub-project: Multi-label classification for the MSA Whistleblower Mechanism Metric


For this exercise, please develop a solution for the MSA Whistleblower Mechanism Metric. This solution should be able to detect from each of the modern slavery statements the company provide a hotline or reporting mechanism where grievances or suspected incidents of slavery or trafficking can be reported for direct employees and/or supply chains workers. 
Please read carefully the description of this metric and methodology  on how the data is labeled here: [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
At the end of the test, the solutions you developed should include systems that would: 
Detect whether a statement contains one or more of the metric’s options:  
- Hotline, Email, Contact Form (direct employees)
-Hotline, Email, Contact Form (supply chain workers)
-Whistleblower protection (direct employees)
-Whistleblower protection (supply chain workers)
-Focal Point (direct employees)
-Focal Point (supply chain workers)
-In Development (direct employees)
-In Development (supply chain workers)
-No
> Note: Unknown: If this label is found, do not include it in the analysis.  
> NOTE: One statement can contain multiple options (they are comma ‘,’ separated in column H  called ‘Labels’) 




### Assumptions for the Whistleblowing metric
![Screen Shot 2021-11-30 at 3 23 23 pm](https://user-images.githubusercontent.com/64998301/143990347-1611f99c-c822-424b-a62b-29905a31f000.png)








Explain the prediction by pointing to the part of the text that describes each option of the  metric that was found (could be at the level of sentence or paragraph).  

##Steps:  
Access the [Multi_class_classification_for_the_approval_metric.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/1fe5bbcf0eef6b0997eef6e14337d92096525175/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Multi_class_classification_for_the_approval_metric.ipynb) notebook, where we present an example of a multi-class classification model for the Aproval matric. 

Read and collect the resources 
Set up a Google Colab notebook 
In your Google Colab notebook provide answers to the following:  
What methodology do you propose to assess the quality of text extracted? 
Present the code of the solutions developed for this metric and interpret your results.  Ensure that each section of the solution is well described and documented.  
How do you assess the quality of your results? What are the challenges? What would  you recommend to do to improve your initial results? 

Share the link of your Google Colab notebook with Adriana or present it during our next meeting. 

##Resources:  
See attached the labeled dataset to this directory. We recommend you to access and extract the text from an updated version of this data which can be downloaded following these [instructions](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate). 
Read carefully the description and methodology about the  [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
A guiding list of keywords for this metric:  
 "due diligence" 
 “human rights due diligence” 
 "planning to implement" 
 "continuous improvement programs" 
 "audit of suppliers"
 "continuously engaging with suppliers" 
“engagement” 
 “workers” 
 “trade unions” 
 "on-site visits" 
 “visit” 
 "audits of suppliers" 
 "Audits" 
"Audit" 
 "Monitor" 
 "third party" 
 “independent” 
 "verification" 
 “unannounced” 
 “external” 


