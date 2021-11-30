

<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">

<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">

<img align="center" alt="Coding" width="550" src="https://cdn.dribbble.com/users/917530/screenshots/2879128/media/6008ce6d81787b9aa0ed9c0101b75567.gif">





The [📔 Initial Metrics Exploration](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration)  was followed by a second semantic workshop with the project partners. Based on all the accumulated knowledge, the decision was made to prioritize four of the metrics to explore multi-class and multi-label classification models.  Those four metrics are: 

-MSA Statement Approval
-MSA Training
-MSA whistleblowing mechanism
-MSA incidents remediation

For these four initial metrics, the modern slavery experts designed a clear set of assumptions that were used not only to label more data but also to clean the existing ground truth data on the WikiRate platform. What is more, clear rules for labelling were designed, allowing us to make the most of the labelled dataset. This includes, for instance, improvements of the collection of 'Commnets', ensuring that for each label there was an associated comment, in a format of exact copy-paste from the statement text. Based on the assumptions and the labelling rules, the WikiRate team and Walk Free Foundation will label new documents for each of the metrics while undergoing extensive cleaning and validation of the existing data on the WikiRate platform. Once the solution will be built for those four metrics, this entire process will be scaled for the remaining 12 metrics. 

With the new clean labelled dataset, we will rerun the initial models and improvement in the results is expected. On top of this, the tests will be further analysed and different methods will be developed to improve the results. Possible avenues to explore include extending further the HAN model by using transformers as backbone models or pre-training embeddings using the 'Comments section (with an S-BERT model computing embeddings for metrics justification) to improve prediction. For each of the metrics, expectations on performance will be considered and a specific feasible threshold will be decided depending on the appropriate goal set (e.g., favouring high precision for positive classes, for instance).

In parallel, the project will focus on the improvement of text extraction. Special attention will be paid to the text extraction from PDFs, especially scanned PDFs. For this, a few different methods and tools will be used in order to observe the differences and improve the existing model. For a start, the PDFs will be passed through the internal machine developed by our partners from BNP Paribas and identify areas of improvement. 

Finally, the pipeline of the project will be augmented with the possibility to explore the integration of the newly launched UK and Australian Registry. The project will build an API designed based on the needs of the WikiRate platform to be easily accessible and directly populate the platform with the classification of the new statements based on the metrics. 


MSA Approval metric example

In this directory you can access the notebook where we present an example of a multi-class classification model for the Aproval matrix. 

| |Approval not explicit in statement| Approved by Board| Approved - not by Board
|-|--------------------------------------------|---------------------------|--------------------------------|
|Description| Approval by board is not explicit.| Approval by board is explicit in the statement.| Approval is explicit in statement, but by an person/entity other than the board|
