![image](https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png)
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">


![MasterHead](https://cdn.walkfree.org/content/uploads/2020/10/07102204/16-Akash-woman-panning-etched.png)

# Project-AIMS-AI-against-Modern-Slavery
GitHub README - Main Page


README 

# Hi 👋  welcome to Project AIMS (AI against Modern Slavery) 

This repository contains the work developed so far under Porject AIMS under an open source licence. It contains a collection of experiments and analyses performed on the Modern Slavery statements, as well as a set of sub-projects designed to encourage the community to apply data science and AI skills in analysising those stamtents. 


## Introduction

#### The challenge
[The UN Sustainable Development Goal 8.7](https://sustainabledevelopment.un.org/sdg8) states:
“Take immediate and effective measures to eradicate forced labour, end modern slavery and human trafficking and secure the prohibition and elimination of the worst forms of child labour, including recruitment and use of child soldiers, and by 2025 end child labour in all its forms.”

Slavery is a multi-billion-dollar transnational crime, and according to the 2018, [the Global Slavery Index](https://www.globalslaveryindex.org/2018/findings/highlights/) it affects more than 40.3 M peopleworldwide - 1 in 4 of whom are children. Of these, 16 million are in forced labor in the private sector, meaning they form part of the supply chains of international corporations supplying our goods and services.

#### Modern slavery legislation

In response to those shoking statistics, the UK introduced the first national legal framework for combatting modern slavery, the Modern Slavey Act of 2015. California, Australia, the EU, France and the Netherlands have similar legislation, with many more countries expected to follow in the coming years. 

An estimated 12,000 - 17,000 modern slavery statements are published each year by UK businesses, with thousands more expected from other countries.

#### The need for a scalable solution

Manually assessing statements is labor intensive and time consuming. Currently it takes approximately 1 hour for volunteers to manually assess one statement and for the researchers to validate their results.

[The Future Society](https://thefuturesociety.org/), an independent nonprofit think-and-do tank [launched a partnership](https://thefuturesociety.org/2020/06/23/project-aims-artificial-intelligence-against-modern-slavery/) with the [Walk Free Initiative](https://www.minderoo.org/walk-free/) to automate the analysis of modern slavery statements produced by businesses to boost compliance and help combat and eradicate modern slavery. 

The analysis of the statements takes into account a list of “metrics”, adapted from requirements set by the UK Modern Slavery Act. Each metric is a question about the quality of a company’s modern slavery statement. For example, is the statement signed? Is it approved by the Board of Directors? Does the company have a mechanism to facilitate whistle-blowing or the reporting of suspected incidents of slavery?



#### Objectives

Build an AI tool to decrease the time required to benchmark Modern Slavery Act-compliant statements.
Provide policymakers and legislators with a greater understanding of these new methods of analysis, fostering their use in other contexts, such as other non-financial reporting initiatives.
Encourage software developers, data scientists, and social scientists to apply their domain expertise to AI for social good projects and combat modern slavery.



[The team](https://thefuturesociety.org/our-team/) at The Future Society is now making the work developed between April 2020 to June 2021 open source, for the wider community to contribute to the fight against modern slavery.

By sharing your analysis and contributing to this repository you help the global community to hold multi-national corporations accountable for how they are addressing modern slavery in their supply chains. 

“This tool will be an innovative way to hold companies to account. It means our teams can speed up the analysis of company statements and it will allow us to focus on the investigation of different sectors and highlight areas that require improvement. Going forward, this will lead to better disclosure of company action to tackle modern slavery in global supply chains.” 

- Katharine Bryant,
European Engagement Lead
Walk Free Initiative 






### 🤝 Collaborators

Special thanks to our closest collaborators and their teams: 


    


### Strucutre

This GitHub contains the following resources: 

The notebooks developed under Project AIMS from April 2020 to June 2021, clearly documented , ideally for anyone who would like to reproduce our project to be able to get similar results. Those notebooks are organsied in the following format
Data and text extraction
🔭 Exploration for labeling functions and binary classification for core metrics
Model for multi-class and multi-label classification for core metrics 

Sub-projects for multi-class and multi-label classification for core metrics designed for the community to pick up and develop further. Those include a clear scope, questions, expected outcomes, a proposed methodology and resources.
Details on engagement 

<img align="right" alt="Coding" width="400" src="https://cdn.dribbble.com/users/2646423/screenshots/5507196/computer.gif">




### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/release/python-3611/) installed on your system
- If you'd like to use the provided tutorials, you also need access to a [Jupyter notebook](https://jupyter.org/install.html)

### Quickstart

It's recommended that you use a virtual environment such as [virtualenv](https://virtualenv.pypa.io/en/latest/), [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) or similar.




## Get Help
If you'd like to get help with domain expertise or technical requirements and implementations then get in touch with [Adriana](mailto:adriana.bora@thefuturesociety.org).


## Citation

If you intend to share any form of public research and analysis based on the data from this repository and the `modern-slavery-dataset` bucket in AWS S3, then please include the following citation to your publication:


The Future Society. (2020) Project AIMS (AI against Modern Slavery). Retrieved from https://github.com/the-future-society/modern-slavery-statements-research.


## Contributions

If you'd like to contribute to the research then take a look at any of the [issues](https://github.com/the-future-society/modern-slavery-statements-research/issues) or get in touch with [Adriana](mailto:adriana.bora@thefuturesociety.org)


Take a look at colab notebooks based on the modern slavery corpus:

- Rey Farhan's initial exploration [Modern Slavery Statements NLP (rey farhan) v1.0.ipynb](https://colab.research.google.com/drive/1Xk3TZ-30CfNmUxxiDRrWh9S3nR74pZlj?usp=sharing).
- Parth Shah's [exploration of knowledge graphs based on subject-object syntactic relations](https://colab.research.google.com/drive/1Nig3YyHy8MEx5a1gmw_Hj95uYDAO30DV?usp=sharing)
- Darin Plutchok's [Clustering Analysis of Modern Slavery data](https://colab.research.google.com/drive/1J1m1Yoy93d5nyfEHCVcBGv-fFH7l9sfG?usp=sharing)
- Goutham Venkatesh's  [Clustering Analysis of Modern Slavery data](https://colab.research.google.com/drive/1bkM7WEe0_nPCCUCnvDC05g9xxGNtbcmM?usp=sharing)
- Rey Farhan's [Modern Slavery Statements NLP - Word2Vec w/ Bigrams (rey farhan) v1.2.ipynb](https://colab.research.google.com/drive/1S0EM1LFJ0KppuENMxiALe7ZikYjNhTLP#scrollTo=aWUYZx9KZbKL)
- Daniel Hilgart's [Exploratory Data Analysis of the hackathon dataset](https://github.com/the-future-society/modern-slavery-statements-research/blob/master/notebooks/EDA.ipynb)


