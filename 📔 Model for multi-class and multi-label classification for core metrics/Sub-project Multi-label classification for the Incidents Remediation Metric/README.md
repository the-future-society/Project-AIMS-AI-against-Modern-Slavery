
<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/146298024-e50a9c98-fa50-4189-9c95-73a218f8cc9a.png">
 
<img align="center" alt="Coding" width="650" src="https://cdn.dribbble.com/users/2046015/screenshots/4971991/media/85a583891a0bb4b0c2a45df0340c66b7.gif">




#  Sub-project: Multi-label classification for the Incidents Remediation Metric


For this exercise, please develop a solution for the MSA Incidents Remediation Metric. This solution should be able to detect from each of the modern slavery statements ifhe company disclosed the steps it would take if a supplier or internal department is found to be engaging in any activities related to modern slavery or human trafficking.
Please read carefully the description of this metric and methodology on how the data is labelled here: [MSA incidents remediation (revised)](https://wikirate.org/Walk_Free_Foundation+MSA_incidents_remediation_revised)
At the end of the test, the solutions you developed should include systems that would: 
Detect whether a statement contains one or more of the metric’s options:  
- Worker remediation
- Corrective action plan
- Senior management
- Cancel contracts
- In Development
- No


> Note: Unknown: If this label is found, do not include it in the analysis.  
> NOTE: One statement can contain multiple options (they are comma ‘,’ separated) 

Also, please explain the prediction by pointing to the part of the text that describes each option of the metric that was found (could be at the level of sentence or paragraph). 

### Assumptions for the Incidents Remediation Metric

![Screen Shot 2021-11-30 at 4 50 19 pm](https://user-images.githubusercontent.com/64998301/143999514-193a18c6-8ef1-4d0e-8d00-d217043f11df.png)


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
3. Read carefully the description and methodology about the [MSA incidents remediation (revised)](https://wikirate.org/Walk_Free_Foundation+MSA_incidents_remediation_revised)
4. Check out our initial exploration on the [Incidents_remediation.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration/Incidents_remediation.ipynb)


Please do not hesitate to get in touch if you have any questions. 



| |
|Worker remediation
|Corrective action plan
|Senior management
|Cancel contracts
|In Development
|No|
_
Description|
_If the company specifies the remediation available for individual workers affected by modern slavery, such as backpayment of wages or support to pursue a claim, please select the “Worker remediation” value.|
_If the company supports the supplier to respond to instances of modern slavery, please select the “Corrective action plan” value.|
_If the company specifies that senior management will be informed if instances of modern slavery have been identified, please select the “Senior management” value.|
_If the company identifies punitive action, by cancelling the contracts of suppliers, please select the “Cancel contracts” value.|
_If the business indicates it is developing a remediation policy or planning to implement one in the future, please indicate “In Development” and again provide details in the comment.|
_If no such information exists in the statement, then please select “No”.|


| |Worker remediation| Corrective action plan| Senior management| Cancel contracts| In Development| No|
|-|---------------------------|-----------------------------|-----------------------------|----------------------|--------------------------------|------|
|Description| If the company specifies the remediation available for individual workers affected by modern slavery, such as backpayment of wages or support to pursue a claim, please select the “Worker remediation” value | If the company supports the supplier to respond to instances of modern slavery, please select the “Corrective action plan” value| If the company specifies that senior management will be informed if instances of modern slavery have been identified, please select the “Senior management” value| If the company identifies punitive action, by cancelling the contracts of suppliers, please select the “Cancel contracts'' value| If the business indicates it is developing a remediation policy or planning to implement one in the future, please indicate “In Development'' and again provide details in the comment| If no such information exists in the statement, then please select “No”|
|Assumption for meeting answer|Must mention worker remediation or worker involvement in remediation policy or mechanisms NOT The statement mentions general remediation| Must mention the existance of an action plan / corrective action plan for remediating incidents of modern slavery OR for remediating risks or red flags related to modern slavery (including health and safety violations) | NOT vague statement of actions to address modern slavery / incidents found | Must mention that cases or incidents are reported to senior management which includes but not limited to: managers, directors, the Board | Must mention contract / relationship cancellation/ termination / cease if a modern slavery case or incident is found. Often this is referred as a last resort | A specific remediation channel /mechanism is being implemented or will be implemented in the future AND can be met simultaneously with other answers | No information is found regarding the company’s incidents remediation. The metric is also marked as "No" is the statement indicates they have remediation practices in place but they don't specifically mention them| 
|Example| | Next's 2020 statement, p.6:"Occasionally we identify the issue of wage retention in a supplier ’s factory and our priority is to ensure that the workers receive all wages that they are owed. In all cases of wage retention we take the following steps:
· Discuss and agree with the factory a plan for paying the workers all monies owed
· Confirm via documentation review and worker interviews that the agreed plans have been actioned" | Cato Corp's 2020 statement:"In the event that Cato becomes aware of any actions or conditions not in compliance with our Code of Conduct, Cato reserves the right to demand corrective measures." | Advent International's 2020 statement, p.1:


"If any issues are identified in relation to the MSA, these will be reported to our Board of Directors (the “Board”) and, if necessary, to the appropriate authorities." - taken to mean escalating to senior management. | Bensons for Beds's 2020 statement: "In the event we suspect a failure by a supplier to comply with our Modern Slavery Policy or SLA we will investigate and require, where appropriate immediate corrective action which may include if appropriate terminating the supplier relationship." | Legal & General Group's 2019 statement, p.10: "we are developing a Human Rights Escalation and Remediation Policy, detailing actions required in the event of uncovering instances of modern slavery and other human rights issues." | |

