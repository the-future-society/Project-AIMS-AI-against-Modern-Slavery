<img align="left" width="300" src="https://www.rethinkingvaluechains.com/wp-content/uploads/2021/02/RVC-WEbiste-logo-6.png">
<br />


[![Screen Shot 2021-11-25 at 11 08 22 am](https://user-images.githubusercontent.com/64998301/143334156-979f2f75-67d3-4213-bd6c-340746ee3b3a.png)](https://www.business-humanrights.org/en/from-us/modern-slavery-statements/)



## The History

As mentioned in the introduction, the UK Modern Slavery Act (Act) was enacted in 2015. A landmark piece of legislation, the transparency in supply chains provision (TISC) requires commercial organisations that operate in the UK and have an annual turnover above £36m to produce a statement setting out the steps they are taking to address and prevent the risk of modern slavery in their operations and supply chains. Thousands of companies are required to report under the TISC provision every year but there was no government-run registry established under the Act where stakeholders could efficiently access statements by all entities that are required to report.

The Modern Slavery Registry, operated by Business & Human Rights Resource Centre, was created to fill this gap. The Registry has provided an invaluable resource that has helped promote transparency and increase accountability by enabling thousands of users worldwide the access to scrutinise over 16,000 modern slavery statements side by side. 

In doing so, BHRRC have played a central role in monitoring compliance with the UK Modern Slavery Act. They also have collected over 1,700 statements published under the California Transparency in Supply Chain Act, which is considered the predecessor to the UK Act. Several key contributors to the introduction of this legislation also advocated for the UK Government to create a central registry for these statements. Whilst the Government was planning to establish this registry, the Modern Slavery Registry provided this resource. It is intended to enable stakeholders to assess the quality of statements and their compliance with the legislation. 


In 2021, the [🇬🇧 GOV.UK Modern slavery statement registry](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/%F0%9F%87%AC%F0%9F%87%A7%20GOV.UK%20Modern%20slavery%20statement%20registry) was launched,  a central public registry of modern slavery statements. BHRRC fully supports this step forward and hopes that the new government-run registry will result in improved monitoring and enforcement against companies that fail to comply with their obligations under the Act. 


The Modern Slavery Registry was guided and supported by a dedicated governance comittee and officially recommended as the central registry for UK modern slavery statements by ICCR (Interfaith Center on Corporate Responsibility), The Law Society, and Business Social Compliance Initiative.

This Archive is the only openly available source, holisting all the historical statements published by the businesses from 2016-2020. 

In this directory, we present a notebook on how to extract the text from the statements. This dataset stores the statements in multiple formats. However, we only provide solutions for PDFs and HTMLs. For other formats such as PNGs, we hope the community will propose solutions.


Therefore, this notebook is proposing a simple, open solution to extracting the text from PDFs and HTMLs only files. 

## The steps are as follows:
- Accesses and downloads the latest version of the .CSV, by accessing  ‘Download company response documents comparison data’ from the Business & Human Rights Resource Centre [page](https://www.business-humanrights.org/en/from-us/modern-slavery-statements/)

- Once the data is downloaded, access the 'Document Cached URL'  column 
- Access each document and fetch the PDF or HTMLs
- Once you have the PDF and HTMLs, extract the text with the best tool you can find, and append the text as a column to the dataset
- Save the dataset


### A proposed version of [this workflow](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/Archive%20of%20BHRRC%20The%20Modern%20Slavery%20Registry/Archive_BHRRC%20The%20Modern%20Slavery%20Registry__text%20extraction.ipynb) and the [data](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/Archive%20of%20BHRRC%20The%20Modern%20Slavery%20Registry/Archive_BHRRC%20The%20Modern%20Slavery%20Registry_data.xlsx) as available in November 2021 is attached to this directory.


Credits reserved to [Business & Human Rights Resource Centre Registered Charity in England & Wales no. 1096664 501(c)(3) non-profit organization in USA](https://www.business-humanrights.org/en/from-us/modern-slavery-statements/)
