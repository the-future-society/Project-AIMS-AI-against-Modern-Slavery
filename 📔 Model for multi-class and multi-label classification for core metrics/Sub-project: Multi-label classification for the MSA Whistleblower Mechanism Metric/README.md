



#Sub-project: Multi-label classification for the MSA Whistleblower Mechanism Metric


For this exercise, please develop a solution for the MSA Whistleblower Mechanism Metric. This solution should be able to detect from each of the modern slavery statements whether the company has a due diligence process in place to monitor these risks through continuous  engagement with suppliers. Please read carefully the description of this metric and methodology  on how the data is labeled here: [MSA whistleblowing mechanism](https://wikirate.org/Walk_Free_Foundation+MSA_whistleblowing_mechanism_revised)
At the end of the test, the solutions you developed should include systems that would: 
● Detect whether a statement contains one or more of the metric’s options:  
Hotline, Email, Contact Form (direct employees)
Hotline, Email, Contact Form (supply chain workers)
Whistleblower protection (direct employees)
Whistleblower protection (supply chain workers)
Focal Point (direct employees)
Focal Point (supply chain workers)
In Development (direct employees)
In Development (supply chain workers)
No

**Assumptions for this metric**
 
| |Hotline, Email, Contact Form (direct employees)| Hotline, Email, Contact Form (supply chain workers)|Whistleblower protection (direct employees)|Whistleblower protection (supply chain workers)|Focal Point (direct employees)|Focal point (supply chain workers)|In Development (direct employees)|No|


|-|--------------------------------------------|---|-|-|-|-|------------------|--------------------------------|











● Explain the prediction by pointing to the part of the text that describes each option of the  metric that was found (could be at the level of sentence or paragraph).  
Steps:  
1. Read and collect the resources 
2. Set up a Google Colab notebook 
3. In your Google Colab notebook provide answers to the following:  
A. What methodology do you propose to assess the quality of text extracted under  column ‘TEXT’? This text is extracted from the URLs in column ‘Answer Link’. ? 
B. Present the code of the solutions developed for this metric and interpret your results.  Ensure that each section of the solution is well described and documented.  
C. How do you assess the quality of your results? What are the challenges? What would  you recommend to do to improve your initial results? 
D. How would you design and deploy the Project API to align your solution with the  WikiRate platform? 
4. Share the link of your Google Colab notebook with Adriana  
(adriana.bora@thefuturesociety.org) by Tuesday, March 2nd, 9 am AEST (Brisbane  time). 
Resources:  
● See attached the labeled dataset to your email.  
● Read carefully the description and methodology about the Walk Free Foundation+MSA  risk management  
● A guiding list of keywords for this metric:  
○ "due diligence" 
○ “human rights due diligence” 
○ "planning to implement" 
○ "continuous improvement programs" 
○ "audit of suppliers"
○ "continuously engaging with suppliers" 
○ “engagement” 
○ “workers” 
○ “trade unions” 
○ "on-site visits" 
○ “visit” 
○ "audits of suppliers" 
○ "Audits" 
○ "Audit" 
○ "Monitor" 
○ "third party" 
○ “independent” 
○ "verification" 
○ “unannounced” 
○ “external” 
● Multi-category Options:  
○ Audits of suppliers (self-reporting) 
○ Audits of suppliers (independent) 
○ On-site visits (self-reporting) 
○ On-site visits (independent) 
○ In Development 
○ No 
○ Unknown: If this label is found, do not include it in the analysis.  
NOTE: One statement can contain multiple options (they are comma ‘,’ separated in column H  called ‘Labels’) 
