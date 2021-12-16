<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/146298024-e50a9c98-fa50-4189-9c95-73a218f8cc9a.png">
 
<img align="center" alt="Coding" width="650" src="https://cdn.dribbble.com/users/2046015/screenshots/4841937/media/3a17ba6103821f4374cb2c9791ddff38.png?compress=1&resize=800x600">



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



| |Hotline, Email, Contact Form (direct employees)| Hotline, Email, Contact Form (supply chain workers)|Whistleblower protection (direct employees)| Whistleblower protection (supply chain workers)| Focal Point (direct employees)| Focal point (supply chain workers)| In Development (direct employees)| In Development (supply chain workers)|No|
|-|---------------------------|-----------------|-----------------------------|----------------------|--------------|------------------|------|-----|---|
|Description| A reporting line or hotline that workers can call ( reporting managed by third parties fall in this category too). A direct employee is someone who is working directly for the company either in the company head office or in regional offices| A reporting line or hotline that workers can call (reporting managed by third parties fall in this category too). A supply chain worker is someone who is employed by contractors or sub-contractors further down the supply chain| Whistleblower protections for employees so they will not be penalised if they report modern slavery cases (mention of any kind of protection is sufficient e.g. "we ensure that anyone raising such concern will not suffer dismissal, disciplinary action, threats or other unfavourable treatment as a result"). A direct employee is someone who is working directly for the company either in the company head office or in regional offices| Whistleblower protections for employees so they will not be penalised if they report modern slavery cases (mention of any kind of protection is sufficient e.g. "we ensure that anyone raising such concern will not suffer dismissal, disciplinary action, threats or other unfavourable treatment as a result"). A supply chain worker is someone who is employed by contractors or sub-contractors further down the supply chain| An employee or independent focal point to whom reports can be made. A direct employee is someone who is working directly for the company either in the company head office or in regional offices |An employee or independent focal point to whom reports can be made. A supply chain worker is someone who is employed by contractors or sub-contractors further down the supply chain| If the business indicates it is developing a whistleblowing or grievance mechanism or planning to implement one in the future, please indicate “In Development'' and again give details in the comments section.A direct employee is someone who is working directly for the company either in the company head office or in regional offices | If the business indicates it is developing a whistleblowing or grievance mechanism or planning to implement one in the future, please indicate “In Development'' and again give details in the comments section.A supply chain worker is someone who is employed by contractors or sub-contractors further down the supply chain | |
|Assumption for meeting answer| Needs to mention a hotline OR an email OR a contact form OR other grievance mechanism AND this is available for direct employees. If no information mentions who this is for, then assume it's for direct employees only | Needs to mention a hotline OR an email OR a contact form OR other grievance mechanism AND this is available for supply chain workers OR available to "third parties"| Needs to mention having whistleblowing protection OR a policy/protection with the same aim AND this is available for direct employees. If no information mentions who this is for, then assume it's for direct employees only. Synonyms for offering protection include protect from 'retaliation' or from 'fear of reprisals' | Needs to mention having whistleblowing protection OR a policy/protection with the same aim AND this is available for supply chain workers OR available to "third parties". Synonyms for offering protection include protect from "retaliation" or from "fear of reprisals"|  Needs to mention a focal point for reporting incidents/grievances such as a line manager, HR officer, or other AND this is available for direct employees. If no information mentions who this is for, then assume it's for direct employees only| Needs to mention a focal point for reporting incidents/grievances such as a line manager, HR officer, or other AND this is available for supply chain workers or available to "third parties" | A specific whistleblowing channel /mechanism is being planned or will be implemented in the future AND can be met simultaneously with other answers AND this is aimed at direct employees. If no information mentions who this is for, then assume it's for direct employees only | A specific whistleblowing channel /mechanism is being planned or will be implemented in the future AND can be met simultaneously with other answers AND this is aimed at supply chain workers or aimed at "third parties"| No information is found regarding the company’s whistleblowing mechanisms. The metric is also marked as "No" if the statement indicates they have whistleblowing mechanisms in place but they don't specifically mention them. For example, any mention that "We have a Whistleblowing policy' is not sufficient to meet this metric and would be coded as No|

 

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
3. Read carefully the description and methodology about the  [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
4. Check out our initial exploration on the [Whistleblowing_mechanism.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/a5f8610f2bbbdc69552108d049cde083f0bf9b83/%F0%9F%93%94%20Initial%20Metrics%20Exploration/Whistleblowing_mechanism.ipynb)

Please do not hesitate to get in touch if you have any questions. 



