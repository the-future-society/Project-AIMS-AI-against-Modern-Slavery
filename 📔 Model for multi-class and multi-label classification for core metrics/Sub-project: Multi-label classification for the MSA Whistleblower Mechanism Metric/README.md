<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">
 
<img align="center" alt="Coding" width="550" src="https://cdn.dribbble.com/users/2046015/screenshots/4899533/media/778aee3233f01428ee90bb1df20a60d9.png?compress=1&resize=800x600">



# Sub-project: Multi-label classification for the MSA Whistleblower Mechanism Metric


For this exercise, please develop a solution for the MSA Whistleblower Mechanism Metric. This solution should be able to detect from each of the modern slavery statements if the company provide a hotline or reporting mechanism where grievances or suspected incidents of slavery or trafficking can be reported for direct employees and/or supply chains workers. 
Please read carefully the description of this metric and methodology  on how the data is labelled here: [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
At the end of the test, the solutions you developed should include systems that would: 
Detect whether a statement contains one or more of the metric’s options:  
- Hotline, Email, Contact Form (direct employees)
- Hotline, Email, Contact Form (supply chain workers)
- Whistleblower protection (direct employees)
- Whistleblower protection (supply chain workers)
- Focal Point (direct employees)
- Focal Point (supply chain workers)
- In Development (direct employees)
- In Development (supply chain workers)
- No
> Note: Unknown: If this label is found, do not include it in the analysis.  
> NOTE: One statement can contain multiple options (they are comma ‘,’ separated) 

Also, please explain the prediction by pointing to the part of the text that describes each option of the metric that was found (could be at the level of sentence or paragraph). 



### Assumptions for the Whistleblowing metric
![Screen Shot 2021-11-30 at 3 23 23 pm](https://user-images.githubusercontent.com/64998301/143990347-1611f99c-c822-424b-a62b-29905a31f000.png)




 

## Steps:  
1. Access the [Multi_class_classification_for_the_approval_metric.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/1fe5bbcf0eef6b0997eef6e14337d92096525175/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Multi_class_classification_for_the_approval_metric.ipynb) notebook, where we present an example of a multi-class classification model for the Aproval matric. 

2. Read and collect the resources 
3. Set up a Google Colab notebook (you can also run this locally)
4. In your Google Colab notebook or .jpynb, provide answers to the following:  
   - What methodology do you propose to assess the quality of text extracted? 
   - Present the code of the solutions developed for this metric and interpret your results.  Ensure that each section of the solution is well described and documented.  
   - How do you assess the quality of your results? What are the challenges? What would  you recommend to do to improve your initial results? 

Share the link of your Google Colab notebook or or .jpynb with Adriana or present it during our next meeting. 

## Resources:  
1. See attached the labelled dataset to this directory. We recommend you to access and extract the text from an updated version of this data which can be downloaded following these [instructions](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate). 
2. Read carefully the description and methodology about the  [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
3. Check out our initial exploration on the [Whistleblowing_mechanism.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/a5f8610f2bbbdc69552108d049cde083f0bf9b83/%F0%9F%93%94%20Initial%20Metrics%20Exploration/Whistleblowing_mechanism.ipynb)

Please do not hesitate to get in touch if you have any questions. 



