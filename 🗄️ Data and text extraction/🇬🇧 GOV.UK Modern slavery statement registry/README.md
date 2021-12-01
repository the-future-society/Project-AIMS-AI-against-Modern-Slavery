
<img align="left" img width="200" alt="Screen Shot 2021-11-25 at 11 16 09 am" src="https://miro.medium.com/max/1400/1*QnjAps-qJwGEXw5st670OA.png">


[<img width="1415" alt="Screen Shot 2021-11-25 at 11 21 21 am" src="https://user-images.githubusercontent.com/64998301/143337270-94599fdb-6745-4bb6-8b08-355676c6b482.png">](https://modern-slavery-statement-registry.service.gov.uk/)


#🇬🇧 GOV.UK Modern slavery statement registry




In this directory, we present a notebook on how to extract the text from the statements. The UK Mondern Slavery regsitry stores the statemetns in both HTMLs an PDFs. 
<img align="right" width="400"   src="https://user-images.githubusercontent.com/64998301/144046036-391f451f-a464-4a13-bbae-5cfdc21d8518.gif">


Therefore, [this notebook](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/%F0%9F%87%AC%F0%9F%87%A7%20GOV.UK%20Modern%20slavery%20statement%20registry/GOV.UK%20Modern%20slavery%20statement%20registry.ipynb) is proposing a simple, open solution to extracting the text from PDFs and HTMLs. 

## The steps are as follows:
- Accesses and downloads the latest version of the .CSV, by accessing  ‘Modern slavery statement summaries (202x)’ from the  GOV.UK Modern slavery statement registry [page](https://modern-slavery-statement-registry.service.gov.uk/download)
- Once the data is downloaded, access the StatementURL column 
- For each document, access the fetch the PDF or HTML
- Once you have the PDFs and HTMLs, extract the text with the best tool you can find, and append the text as a column to the dataset
- Save the dataset

### A proposed version of [this workflow](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate/WikiRate_labeled_data.ipynb) is attached to this directory. A version of the data as available in November 2021 will be available soon. 


<img align="right" img width="200" alt="Screen Shot 2021-11-25 at 11 16 09 am" src="https://user-images.githubusercontent.com/64998301/143334956-8aba1868-8ad6-4e10-967d-d38999f1f5cf.png">


