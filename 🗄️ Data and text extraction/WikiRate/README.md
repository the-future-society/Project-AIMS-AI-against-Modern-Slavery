
[<img align="center"  src="https://media-exp1.licdn.com/dms/image/C4D1BAQG_U9F1oAbg4g/company-background_10000/0/1557326103523?e=1637892000&v=beta&t=HHRTu6Y5KkEz5t3v5SiMomoKrqnezkalWLPSE-NTOlM">](https://wikirate.org/uk_modern_slavery_act_research)









# WikiRate dataset - in Project AIMS we generally refer to it as the labelled dataset

[WikiRate’s UK Modern Slavery Act research]( Modern Slavery Research by WikiRate details: https://WikiRate.org/UK_Modern_Slavery_Act_Research) aims to 'evaluate the quality of Modern Slavery Statements that are produced by companies following the Modern Slavery Act. To do so, over the previous six years they have been evaluating modern slavery statements according to a set of core metrics, each of which represents a desirable property of a modern slavery statement. For example:
- Is the statement signed and/or approved by a managing body of the organization?
- Does the statement describe a whistleblowing mechanism to facilitate the reporting of suspected cases of modern slavery?

Learn more about those metrics, by check out our [📔 Initial Metrics Explorationon](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration) the core 16 metrics. 

Labelling statements with these metrics is repetitive labour, and currently, only approximately 2,400 statements have been labelled. One of the goals of Project AIMS is to augment this manual effort using NLP techniques, to obtain a fully labelled dataset. Thus, the WikiRate dataset is effectively the training dataset ('ground truth data', ‘labelled dataset’) that will be used to train machine learning models. The trained models then can be used to label the remaining statements in the [Archive of BHRRC The Modern Slavery Registry](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/Archive%20of%20BHRRC%20The%20Modern%20Slavery%20Registry). Once all statements are labelled, it will be much easier to identify companies that need to make greater efforts to meet the minimum requirements of the legislation and to go beyond compliance. 

In this directory, we present a notebook on how to extract the text from the statements. WikiRate stores both the links to the original PDFs, as well as a PDF copy of the statement. This ensures that all the historical versions of the statements are being stored, and not lost due to frequent issues met when scraping URLs. 

<img align="right" width="400"   src="https://user-images.githubusercontent.com/64998301/144046036-391f451f-a464-4a13-bbae-5cfdc21d8518.gif">


Therefore, this text extraction is proposing a simple, open solution to extracting the text from PDFs only files. 

## The steps are as follows:
- Accesses and downloads the latest version of the .CSV, by accessing  ‘Export: csv / json’ from the WikiRUK Modern Slavery Act Research [page](https://wikirate.org/uk_modern_slavery_act_research)
https://wikirate.org/UK_Modern_Slavery_Act_Research+Answer.csv
- Once the data is downloaded, access the Source Page column (for instance, https://wikirate.org/~7613712 
- For each document, access the Download link (looks something like <a href="https://dq06ugkuram52.cloudfront.net/files/7613713/25352410.pdf" target="_blank" class="source-color"><i class="fa fa-download"></i> Download</a>), and fetch the PDF
- Once you have the PDF, extract the text with the best tool you can find, and append the text as a column to the dataset
- Save the dataset

### A proposed version of this workflow and the data as available in November 2021 is attached to this directory.




Rights reserved to WikiRate is a registered trademark of The WikiRate Project e.V., a nonprofit organization based in Berlin, Germany.

