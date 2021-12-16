​​
<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">

<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/146294338-7999acb1-e781-46be-82b5-2e5f89d0da58.png">


![MasterHead](http://www.endslaverynow.org/media/3705/informal-garment-industry-2015-6a.jpg?width=660&height=440&bgcolor=fff)

                                             © Claudio Montesano Casillas

# Hi 👋  welcome to Project AIMS (AI against Modern Slavery) 

This repository presents the work developed so far in Project AIMS under an ©️ open source licence. It contains a collection of experiments and analyses performed on the Modern Slavery statements, as well as a set of sub-projects designed to encourage the community to apply data science and AI skills in analysing those statements and fighting against modern slavery. 


## Structure

This GitHub contains the following resources: 

1. The notebooks developed under Project AIMS from April 2020 to June 2021, clearly documented, ideally for anyone who would like to reproduce our project to be able to get similar results. Those notebooks are organised in the following format: 
   - 🗄️ [Data and text extraction](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction)
   - 📔 [Initial Metrics Exploration](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration)
   - 📔 [Model for **multi-class** and **multi-label classification** for core metrics](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics)
     - 💡 Sub-projects for multi-class and multi-label classification for core metrics designed for the community to pick up and develop further. Those include a clear scope, questions, expected outcomes, a proposed methodology and resources.
         - [Sub-project Multi-label classification for the Incidents Remediation Metric](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Sub-project%20Multi-label%20classification%20for%20the%20Incidents%20Remediation%20Metric)
         - [Sub-project: Multi-label classification for the MSA Training Metric](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Sub-project:%20Multi-label%20classification%20for%20the%20MSA%20Training%20Metric)
         - [Sub-project: Multi-label classification for the MSA Whistleblower Mechanism Metric](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Sub-project:%20Multi-label%20classification%20for%20the%20MSA%20Whistleblower%20Mechanism%20Metric)
   - 🔎 [Other explorations on the modern slavery corpus](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%94%8E%20Other%20explorations%20on%20the%20modern%20slavery%20corpus)


## Introduction


#### The challenge
[The UN Sustainable Development Goal 8.7](https://sustainabledevelopment.un.org/sdg8) states:
“Take immediate and effective measures to eradicate forced labour, end modern slavery and human trafficking and secure the prohibition and elimination of the worst forms of child labour, including recruitment and use of child soldiers, and by 2025 end child labour in all its forms.”

Slavery is a multi-billion-dollar transnational crime, and according to 2018, [Global Slavery Index](https://www.globalslaveryindex.org/2018/findings/highlights/), it affects more than 40.3 M people worldwide - 1 in 4 of whom are children. Of these, 16 million are in forced labour in the private sector, meaning they form part of the supply chains of international corporations supplying our goods and services.

In response to those shocking statistics, the UK introduced the first national legal framework for combatting modern slavery, the Modern Slavery Act of 2015. California, Australia, the EU, France and the Netherlands have similar legislation, with many more countries expected to follow in the coming years. 

#### The need for a scalable solution

<img align="right" width="400" src="https://cdn.dribbble.com/users/458522/screenshots/16034588/media/f2e9bcf8eed4d50c909863e9c51f0f21.png?compress=1&resize=1600x1200">

An estimated 12,000 - 17,000 modern slavery statements are published each year by UK businesses, with thousands more expected from other countries.

Manually assessing statements is labour intensive and time-consuming. Currently, it takes approximately [1 hour for volunteers to evaluate manually one statement and for the researchers to validate their results](https://wikirate.org/uk_modern_slavery_act_research).


[The Future Society](https://thefuturesociety.org/), an independent nonprofit think-and-do tank [launched a partnership](https://thefuturesociety.org/2020/06/23/project-aims-artificial-intelligence-against-modern-slavery/) with the [Walk Free Initiative](https://www.minderoo.org/walk-free/) to automate the analysis of modern slavery statements produced by businesses to boost compliance and help combat and eradicate modern slavery. 

The analysis of the statements takes into account a list of “metrics”, adapted from requirements set by the UK Modern Slavery Act. Each metric is a question about the quality of a company’s modern slavery statement. For example, is the statement signed? Is it approved by the Board of Directors? Does the company have a mechanism to facilitate whistle-blowing or the reporting of suspected incidents of slavery?

>_*"Project AIMS seeks to capture the potential of artificial intelligence to help solve pressing social issues in new ways, to ultimately uphold human dignity. With this innovative machine learning tool, our goal is two-fold: empower civil society and legislators to hold businesses and governments to account; and pave the way for a new type of public policy and legislation, which embraces the full power of data mining and processing" – Nicolas Miailhe, co-founder and president of The Future Society*_
 
#### Objectives

1. Build an AI tool to decrease the time required to benchmark Modern Slavery Act-compliant statements.
2. Provide policymakers and legislators with a greater understanding of these new analysis methods,, fostering their use in other contexts, such as other non-financial reporting initiatives.
3. Encourage software developers, data scientists, and social scientists to apply their domain expertise to AI for social good projects and combat modern slavery.



### Project AIMS in the media and more:
- The [prototype](https://github.com/adrianaeufrosinabora/Adriana-Bora-Master-Thesis-AI-against-Modern-Slavery) built by Adriana in her Master thesis as part of the [médialab Sciences Po](https://medialab.sciencespo.fr/) 
- Walk Free Foundation [Press Release](https://www.minderoo.org/walk-free/news/artificial-intelligence-to-assist-in-the-fight-against-modern-slavery/)
- DATA FOR FUTURE podcast episode [#17: AI AGAINST MODERN SLAVERY](https://dataforfuture.org/episodes/ai-against-modern-slavery/) – with Adriana Bora talking about AI the conceptualisation of Project AIMS
- Project AIMS being presented at the UN World Data Forum [2020](https://youtu.be/1iDmSXJwClA) and [2021](https://www.youtube.com/watch?v=nSGiXbe6gLg&list=PLBc4lThqX-WMnXI1gt95r_hJ4IgZP8tWY&index=42)
- Project AIMS was selected to be presented as a promising use-case of responsible AI for Social Good at the [Global Partnership on AI (GPAI) Montreal Summit 2020](https://youtu.be/k9-2JMvLJg)
- Project AIMS at the UNESCO and the World Economic Forum [Girl Trouble: Breaking Through The Bias in AI](https://youtu.be/cgpye788P9Q)

## JOIN US 

<img align="right" width="450" src="https://cdn.dribbble.com/users/472667/screenshots/15669289/media/d18929f9db262c8c118740dd65d8a395.gif">


The work developed by [The Future Society](https://thefuturesociety.org/our-team/) between April 2020 to June 2021 is now ©️ open source, allowing the wider community to contribute to the fight against modern slavery.

By sharing your analysis and contributing to this repository, you help the global community to hold multi-national corporations accountable for how they are addressing modern slavery in their supply chains. 

Join our community on [Slack](https://join.slack.com/t/projectaimsai-fqt6125/shared_invite/zt-zqrmnzh2-KezsPrxFMpW_DGL6ko4ytw) and [Trello](https://trello.com/invite/b/TmP0XgcU/304d196df1e8edbf06066e222f9f3eed/project-aims-github-2022) and join our regular meetings where we discuss recent research and development on the project. 
- 🗓️  **Next meeting _February 2022**_

### Get in touch 💬
If you have any questions or you would like to get help with domain expertise or technical requirements, please get in touch with [Adriana](mailto:adriana.bora@thefuturesociety.org).

>_“This tool will be an innovative way to hold companies to account. It means our teams can speed up the analysis of company statements and it will allow us to focus on the investigation of different sectors and highlight areas that require improvement. Going forward, this will lead to better disclosure of company action to tackle modern slavery in global supply chains.”  -  Katharine Bryant, European Engagement Lead Walk Free Initiative_



### Citation 📝 

If you intend to share any form of public research and analysis based on this repository’s data or code, please include the following citation to your publication: _The Future Society. (2020) Project AIMS (AI against Modern Slavery). Retrieved from https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery _ 

### Main contributors to the GitHub:
- [Adriana Eufrosina Bora](https://www.linkedin.com/in/adriana-eufrosina-bora-2965a19a/) 
- [Karyna Bikziantieieva](https://www.linkedin.com/in/karyna-bikziantieieva-48aba1197/)
- [Rui Wang](https://www.linkedin.com/in/rui-wang-07774221/)
- [Rodney Phillips](https://www.linkedin.com/in/rodney-levon-phillips/)
- [Badrul Chowdhury](https://www.linkedin.com/in/badrul-c-301b1473/)

### Special thanks to:

- [Nicolas Miailhe](http://thefuturesociety.org/people/nicolas-miailhe/), [Yolanda Lannquist](http://thefuturesociety.org/people/yolanda-lannquist/) and [Katharine Bryant](https://www.linkedin.com/in/katharine-bryant-0779b151/) who oversaw the project
- [Clement Baccar](https://www.linkedin.com/in/clement-baccar-a23b6768/), [Brian Ulicny](https://www.linkedin.com/in/bulicny/), [Hermès Martinez](https://www.linkedin.com/in/hermes-martinez-7a057bb7/), [Mathis Linger](https://www.linkedin.com/in/lingermathis/) and [Sahan Bulathwela](https://www.linkedin.com/in/in4maniac/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAZgenABan_BCFNehPhF0m1Ld0KMdSVj62E) who advised on the project 
- [Roberto Espinoza](https://www.linkedin.com/in/robeespi/)
- [Pranamya Korde](https://www.linkedin.com/in/pranmayakorde17/)
- [Li He](https://www.linkedin.com/in/li-he-94a514194/)
- [Edgar Rootalu](https://www.linkedin.com/in/edgarrootalu/)
- [Samuel Clarke](https://www.linkedin.com/in/samckclarke/)
- [Nicolas Guetta-Jeanrenaud](https://www.linkedin.com/in/nicolas-guetta-jeanrenaud/)
- [Francisca Sassetti](https://www.linkedin.com/in/franciscasassetti/)
- [Lewis Hammond](https://www.linkedin.com/in/lrhammond/)







## 🤝 Collaborators

Special thanks to our closest collaborators and their teams: 

<br />

<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174086-aebdf1ed-fe4a-400f-95b2-0269cd10498b.png">
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174037-d110437c-b89c-45c7-85ab-392d983813e0.png">
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174131-743f4dc5-c5b3-4b3f-ba2d-83e0fc413a13.png">
<img align="left" width="300" src="https://www.rethinkingvaluechains.com/wp-content/uploads/2021/02/RVC-WEbiste-logo-6.png">
<br />
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174259-eb005a57-f97f-4fc2-9026-ffd70d0d5da5.png">
<br />
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174301-f5b0459e-f16b-4e9b-8cad-09649a561232.png"> 
<br />
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174322-d354b5a2-5d86-493e-bc55-fd104bc331fb.png">

<img align="left" width="200" src="https://namr.com/wp-content/uploads/2021/07/logo-namR-2021.png">






