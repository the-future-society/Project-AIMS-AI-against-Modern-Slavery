<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/146298024-e50a9c98-fa50-4189-9c95-73a218f8cc9a.png">
 
<img align="center" alt="Coding" width="650" src="https://cdn.dribbble.com/users/2046015/screenshots/15331473/media/a4c5a1de94fd671207981baf686b9058.gif">




# Sub-project: Multi-label classification for the MSA Training Metric


For this exercise, please develop a solution for the MSA Training Metric. This solution should be able to detect from each of the modern slavery statements if the company provide training specifically to address modern slavery and human trafficking.
Please read carefully the description of this metric and methodology on how the data is labelled here: [MSA training (revised)](https://wikirate.org/Walk_Free_Foundation+MSA_training_revised)
At the end of the test, the solutions you developed should include systems that would: 
Detect whether a statement contains one or more of the metric’s options:  
- Employees (all)
- Procurement / purchasing
- Recruitment / HR
- Leadership
- Suppliers
- Training provided - not specified to who
 - In Development
- No modern slavery training provided

> Note: Unknown: If this label is found, do not include it in the analysis.  
> NOTE: One statement can contain multiple options (they are comma ‘,’ separated) 

Also, please explain the prediction by pointing to the part of the text that describes each option of the metric that was found (could be at the level of sentence or paragraph). 



### Assumptions for the training metric

| |Employees (all)| Procurement| Recruitment/HR| Leadership| Suppliers| Training provided - not specified to who| In Development| No modern slavery training provided|
|-|---------------------------|-----------------|-----------------------------|----------------------|--------------|------------------|------|-----|
|Description| If all employees in the company are receiving training, please select the "Employees (all)" value.| Where the intended recipients of the training are those who work in procurement or purchasing, please select the “Procurement/ purchasing” value.|If the training is targeting those who work in recruitment or human resources, please select the “Recruitment/ HR” value.| If the leadership or management of the company receive training, please select the “Leadership” value.| If the training is provided to suppliers and/or contractors, please select the "Suppliers" value.| Where the recipients of the training are not specified, please select the “Training provided - not specified” value.| If the business indicates it is developing a training programme, or plans to implement one in the future, please indicate “In Development” and please include a comment if the company is planning on including elements of modern slavery to existing trainings, or developing training specific to modern slavery and human trafficking.|Please select "No" if no training is described in the statement.|
|Assumption for meeting answer| Must mention MS training for all employees NOT MS training available to employees or new starters| Must mention MS training specifically for procurment/purchasing|Must mention MS training specifically for recruitment/HR|Must mention MS training specifically for leadership, which includes Managers, Directors, Board|Must mention MS training provided specifically to suppliers|MS training is provided but it doesn't meet any of the other categories OR training recipient not identified in the statement. Training described for just "employees' or 'new employees' would be captured under this metric|A modern slavery training is being developed, implemented or will be implemented in the future AND can be met simultaneously with other answers|No information is found regarding the company’s modern slavery training. The metric is also marked as "No" if the statement indicates they have training in place but it doesn't specifically target/cover modern slavery.Where a statement says they provide training on their Human Rights Policy, or are training xyz on the content of their Code of Conduct, and in an earlier section of the statement, they have explained that these policies/documents cover modern slavery they would meet the training metric. This metric requires reading two components of the statement in conjunction.|


## Steps:  

1. Read and collect the resources 
2. Set up a Google Colab notebook (you can also run this locally)
3. In your Google Colab notebook or .jpynb, provide answers to the following:  
   - What methodology do you propose to assess the quality of text extracted? 
   - Present the code of the solutions developed for this metric and interpret your results.  Ensure that each section of the solution is well described and documented.  
   - How do you assess the quality of your results? What are the challenges? What would  you recommend to do to improve your initial results? 

4. Share the link of your Google Colab notebook or your .jpynb with Adriana or present it during our next meeting. 

## Resources:  
1. Access the [Multi_class_classification_for_the_approval_metric.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/1fe5bbcf0eef6b0997eef6e14337d92096525175/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Multi_class_classification_for_the_approval_metric.ipynb) notebook, where we present an example of a multi-class classification model for the Aproval matric. 
2. See attached the labelled dataset to this directory. We recommend you to access and extract the text from an updated version of this data which can be downloaded following these [instructions](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate). 
3. Read carefully the description and methodology about the  [MSA training (revised)](https://wikirate.org/Walk_Free_Foundation+MSA_training_revised)
4. Check out our initial exploration on the [Training.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration/Training.ipynb)

Please do not hesitate to get in touch if you have any questions. 






