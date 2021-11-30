
<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">

<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">


<img align="center" alt="Coding" width="650" src="https://cdn.dribbble.com/users/916515/screenshots/5807370/media/717687e26cc7421464a5bd283bb02a92.gif">




# Initial Metrics Exploration
## Proof of concept for extracting supporting text and conducting binary classifications for 16 metrics 

After extracting the text and understanding the corpus, the project moved to its second phase, focusing on creating the understanding needed to prepare for the training of the machine learning solutions. This project phase analyses the sixteen metrics used to benchmark the statements and identifies and extract their associated supporting text (quotes, context, meaning, claims, or facts) from the statements. 

> Note: This process should be a continuous one, and once it reaches a high level of accuracy, the supporting text could become part of the ground truth data, just as the 'Comments' from [WikiRate](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/b0571d0b34f1ee68856b5b18468d8d3b7d540c19/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate/README.md) labelled data.  The 'Comments' are text imputed by annotators to explain the exact part of the text that describes their decision to choose the specific label. In the future, the supporting text could be used to facilitate the creation of a more extensive, cleaner labelled dataset. Also, the supporting text could aid to achieve better performance for the multi-class and multi-label classifications.

This directory will introduce the different qualitative and quantitative methods used in the supporting text extraction procedure. It explains the steps taken during this phase to understand each of the sixteen metrics and their unique challenges and opportunities. 
Alongside this documentation, this work could be used in later phases to label more data and guide the verification of the existing ground truth data. 
The sixteen metrics used in this project are designed by Walk Free, WikiRate and Business and Human Rights Resource Center in line with the UK Government guidance. Each metric questions the quality of a company’s modern slavery statement, indicating good reporting. 

<img align="right" alt="Coding" width="400" src="https://cdn.dribbble.com/users/1501052/screenshots/4545496/media/13e279b5c3bd2e8f79067239da3d8633.gif">



The metrics explored are: 
1. **MSA Statement Signed** - Was the company’s Modern Slavery Act statement signed by an appropriate person?
2. **MSA whistleblowing mechanism**  - Does the company have a grievance mechanism in place to facilitate whistle-blowing or the reporting of suspected incidents of slavery or trafficking?
3. **MSA Business Performance Indicators** - Has the company reviewed business key performance indicators (KPIs) to ensure they are not increasing the risk of modern slavery?
4. **MSA incidents remediation** - Did the company explain the corrective steps it has taken (or would take) in response to modern slavery incidents in its own operations and/or supply chain?
5. **MSA Performance Indicators** - Does the company define performance indicators that measure the effectiveness of its actions to combat slavery and trafficking? 
6. **MSA Ownership Disclosure** - Does the company disclose the ownership structure(s) and/or business model(s) of each of its brands, subsidiaries, and other businesses covered by its Modern Slavery statement?
7. **MSA Training**  - Does the statement describe training for staff that is specifically geared towards detecting signs of slavery or trafficking?
8. **MSA Historical Record** -Does the company provide a historic record of their modern slavery statements (either on their website or in their current statement)?
9. **MSA incidents identified** - Did the company identify any specific incidents related to modern slavery that require(d) remediation?
10. **MSA Statement Approval** - Was the company's Modern Slavery Act statement explicitly approved by the board of directors (or equivalent management body)?
11. **MSA impact on company behaviour**
Does the company’s statement describe a change in their policy that occurred as a direct result of the UK Modern Slavery Act 2015?
12. **MSA supply chain disclosure** - Does the company’s statement identify the suppliers in their supply chain and/or the geographic regions where their supply chain operates?
13. **MSA policy**  - Does the company’s statement detail specific organisational policies or actions to combat slavery in their direct (tier 1) and/or indirect (beyond tier 1) supply chain?
14. **MSA Identification of risks** - Does the company’s statement identify specific geographic regions, industries, resources or types of workforce where the risk of modern slavery is the greatest?
15. **MSA risk management** - Does the company continuously monitor suppliers to ensure that they comply with its policies and local laws?
16. **MSA risk assessment** - How does the company assess the risks of modern slavery and trafficking in their supply chain?

## Methodology 
### Semantic workshop 
Before starting to use any computational techniques to explore the statements, the process started with a semantic workshop to collect and imbed the domain knowledge of the specialists in modern slavery reporting. 

This workshop looked at creating a set of guiding methodologies and keywords that will facilitate the identification and exploration of the metrics in the corpus. It brought together modern slavery research experts who have designed and worked with the metrics for the last few years. Based on their advice, a list of keywords was formed for each of the metrics to search for it in the document. Those keywords informed the computational methods to identify the metrics’ associated supporting text in the statements. 

### The supporting text extraction procedure 

Supporting text extraction is the process of defining a set of text characteristics that will most efficiently or meaningfully represent the information that is important for analysis and classification. In the case of Project AIMS, the most important supporting text to extract are the sentences indicating the presence of each metric in the businesses’ statements. Supporting text, in this case, is defined as the sentences that include quotes, context, meaning, claims, or facts that correspond to each metric. 

Supporting text extraction is a process of reducing the dimensions of the representation of a document. Generally, large data sets require a lot of computing resources to process.  Supporting text extraction is the method that selects and/or combines segments of the data (in this case, sentences) into supporting text, effectively reducing the amount of data that must be processed while still accurately and completely describing the original data set. The supporting text is intended to be informative and non-redundant, facilitating the subsequent learning and generalisation steps, and in some cases leading to better human interpretations. 
<img align="right" alt="Coding" width="400" src="https://cdn.dribbble.com/users/672882/screenshots/2314038/media/d0c59fa60407d5123a5e5da6be6f2a06.gif">
> Note: Machine learning algorithms learn from a predefined set of supporting text from the training data to produce output for the test data. Yet, the main problem in language processing is that machine learning algorithms cannot directly work on the raw text. Some supporting text extraction techniques are needed to convert text into a matrix (or vector) of supporting text. Some of the most popular methods of supporting text extraction are Bag-of-Words and term frequency-inverse document frequency (TF-IDF).

Some exploratory tests were executed using diverse computational methods to understand the complexity of identifying the metrics and their associated supporting text in the statements. On top of this, those tests allowed preliminary classifications of the statements.  

Those methods are:
-Labelling functions using Snorkel framework
-Rule-based and Random Forest approach
-Hierarchical Attention Network
-Transformer-based approach (using the 'Comments' from WikiRate dataset) 


## A. Labeling functions using the Snorkel framework 
The first method explored is based on labelling functions that use the Snorkel framework. Snorkel is a system for programmatically building and managing training datasets without manual labelling. 


Snorkel currently exposes three key programmatic operations: 
Labelling data, e.g., using heuristic rules or distant supervision techniques
Transforming data, e.g., rotating or stretching images to perform data augmentation
Slicing data into different critical subsets for monitoring or targeted improvement

This exploratory test aimed to work through various metrics to understand their vocabulary and their presence in the text data. Also, it aimed to develop, based on the domain expert knowledge extracted from our semantic workshop, more labelled data through keywords and regular expression matching. Based on the keywords, this method enables the extraction of the relevant supporting text associated with the metrics from the statements. 

> Note: These supporting texts can be used as training data for the machine learning model in a later phase of the project. 

In Snorkel, users can develop large training datasets in hours or days rather than hand-labelling them over weeks or months. Labelling functions are designed to be weak heuristic functions that predict a label given unlabeled data. The method explored is based on labelling functions that use the Snorkel framework to process, build and manage training datasets without manual labelling.

When applied to each of the metrics, the output of the system is a prediction about whether a sentence for the statement could be classified as containing relevant information about that metric or not.

For this exploratory task, we used the ground truth data from the WikRate platform as available between October 2020 and January 2021. **We recommend you to re-run this research with an updated version of this data which can be downloaded following the instructions from [WikiRate directory](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/b0571d0b34f1ee68856b5b18468d8d3b7d540c19/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate/README.md).**

The methodology across those metrics consisted of the main four steps (some containing supplementary steps): 
Lemmatize - the process of reducing the different forms of a word to one single form, for example, reducing 'builds', 'building', or 'built' to the lemma 'build' - the keywords provided by the experts
Lemmatize the input text, remove stopwords, punctuation and space tokens
Search for lemmatized keywords in the lemmatized text
If matches are found among lemmatized text, save the original sentences containing the processed lemmas as extracted output.


### 💡 Key findings using this method: 

While conducting this work, key lessons were drawn. Firstly, the results indicated the need to verify the quality of the labelled dataset. Without this clear benchmark, the results are not strong enough to allow with confidence the integration of the supporting text as part of the ground truth data.  In some cases, manual validation was conducted, following the labels and the comment sections of the ground truth data provided by WikiRate. The 'Comments' from the WikiRate dataset are useful for understanding the context that generates the label. Yet, at this stage, the data was unclear and unstructured. Not all documents included 'Comments’, and when they existed, many were just free text added by the annotators, without directly linking the exact text from the statement, justifying the label’s selection.  To correct this, improvement in the annotation process is required moving forward. 

What is more, this method based on keywords is useful, but in many cases, the lack of context is taken into account can generate noise. For instance, in many cases, some of the keywords appeared in multiple places on the statement but did not always refer to the metric in question. Being able to correct this is key to avoiding false positives or false negatives. 

> Note: The next three methods were applied only for the following metrics:
- MSA Risk Assessment
- MSA Risk Management
- MSA Risk Identification

## B. Rule-based and Random Forest approach
The second method used in the project was to explore a combination of rule-based and random forest approaches for classifying the statements informed by the keywords of the semantic workshop. 

The rule-based classifier is a simpler method than Snorkel that uses a set of IF-THEN rules for classification. 

![Screen Shot 2021-11-30 at 11 29 10 am](https://user-images.githubusercontent.com/64998301/143969195-e9c1346a-7af3-4bfb-8398-e6c836811329.png)

>_Figure explaining the rule-base method_

The basic concept behind the Random Forest (or random decision forest) approach is that a group of 'weak learners' may come together to build a 'strong learner'. What is more, Random Forest is designed to overcome the 'overfitting' problem of decision trees. [Random Forest](https://www.semanticscholar.org/paper/Combining-Machine-Learning-and-Natural-Language-to-Balyan-McCarthy/24bef0ea2cdc76616c7c0da087f0da4c6b9033cc) constructs a multitude of decision trees in the training phase and uses majority voting for classification. A Random Forest algorithm is [arguably one of the best algorithms for classification](https://www.sciencedirect.com/topics/engineering/random-forest).


![Screen Shot 2021-11-30 at 11 31 31 am](https://user-images.githubusercontent.com/64998301/143969500-5535a467-f1f2-4be7-b3cc-15115ea359ba.png)

>_[Figure](https://corporatefinanceinstitute.com/resources/knowledge/other/random-forest/) explaining the Random Forest method_

This method aims to use heuristics and the domain knowledge gathered via the semantic workshop to classify part of the statements. This method indicates which supporting text   n this case, sentences) contributed to the classification decision.

### Methodology:
In order to build an easily interpretable pipeline, experts' knowledge and feedback were leveraged. Using the list of keywords from the semantic workshop, this method allowed for the extraction of sentences that potentially indicate the presence of the metrics. If a sufficient number of the sentences containing the keywords were found, the statement was classified as positive, meaning it contains the metrics, or else, a random forest model was trained to classify the statement. For this exercise, the list of keywords associated with the metrics from the semantic workshop was used. Those words were enlarged to incorporate more 'business knowledge', for instance, by including a list of synonyms (e.g. for assessment, we added evaluation, rating, etc.).

Based on this list, all the sentences containing these keywords were extracted. All statements for which at least six sentences containing keywords were extracted were classified as positive. 

Based on the assessment of the application of this methodology for the metric ‘Risk Assessment’, by using a simple rule, some statements were classified with rather high accuracy. Using six sentences as the threshold, 38% of the statements were classified with an 83% accuracy.


![Screen Shot 2021-11-30 at 11 33 44 am](https://user-images.githubusercontent.com/64998301/143969615-76cecc2c-744c-4c64-acd3-2b74507a1d4b.png)


>_Figure explaining the accuracy of rule-based sentence classification based on the ‘Risk Approval’ metric keywords._

However, using the six sentences as a threshold leaves 62% of statements to classify. For this, Random Forests were used. For the 62% remaining statements, the sentences containing at least one predefined keyword were kept. 

Each document was represented using a TF IDF vectorization (with n-gram- meaning a sequence of N words- ranging from 1 to 3) from these sentences. Then, a Random Forest model was trained. 


### 💡 Key findings using this method: 
This method seems to best perform for the Risk Assessment metric. Using this system shows an average of 74% accuracy. Yet, this frequency-based method does not incorporate much context, which needs to be addressed as it is very important to classify if the statement describes risk assessment. What is more, for some documents, the sentences predicted seem to indicate a positive metric, even if labelled negative. This justifies the need to recheck the quality of the labelled dataset. 

## C. Hierarchical Attention Network (HAN)

Hierarchical Attention Network (HAN) was proposed by [Yang et al. in 2016]( https://www.cs.cmu.edu/~./hovy/papers/16HLT-hierarchical-attention-networks.pdf) for document classiﬁcation. Their model, has two distinctive characteristics: (i) it has a hierarchical structure that mirrors the hierarchical structure of documents; (ii) it has two levels of attention mechanisms applied at the word and sentence level, enabling it to attend differentially to more and less important content when constructing the document representation. Experiments conducted on six large scale text classiﬁcation tasks demonstrate that the proposed architecture outperforms previous methods by a substantial margin. Visualization of the attention layers illustrates that the model selects qualitatively informative words and sentences. 

![Screen Shot 2021-11-30 at 11 34 55 am](https://user-images.githubusercontent.com/64998301/143969732-9c030ed9-93ac-4103-ba56-3d921e10dc49.png)


>_[Figure](https://www.cs.cmu.edu/~./hovy/papers/16HLT-hierarchical-attention-networks.pdf) Explaining the Hierarchical Attention Network method_ 


HAN was trained to predict their presence for three risk metrics and identify their associated supporting text from the statements. This method allowed us to use the hierarchical structure of statements and drive attention to incorporating context. 

The advantages of this method are that the attention weights are unique, which facilitate the interpretation of predictions. Also, this model provides a clear view of the part of the text the model is looking at, and thus the supporting text that is helping make the predictions. Thanks to the two levels of attention, the model also highlights sentences and words which are important for prediction. The HAN model predicts if the overall statement contains or not the metric analysed. 

![Screen Shot 2021-11-30 at 11 35 29 am](https://user-images.githubusercontent.com/64998301/143969796-a0a02e89-0286-4235-a153-da944a9e9047.png)

_Figure visualising the Hierarchical Attention Network method_  


### 💡 Key findings using this method: 
Based on this initial exploration, this method produces similar results as the rule-based and Random Forest methods. 

>Note: For future exploration, pre-training word embeddings on this projects’ specific corpus would probably improve performance (e.g. using S-BERT). Another possible improvement on this method would be to use transformers instead of bi-GRU RNN for words and sentence encoders.

In this case as well, for some statements, the sentences predicted seem to justify a positive metric (indicating the metric is present in the statement) even if labelled given by the annotators in the original ground truth data was negative (indicating the metric is not present in the statement). This indicated that the quality of the ground truth data used at this stage needs assessment. This was informed by a manual evaluation of the list of documents where the model was conflicting, as well as the words and sentences important for the prediction.

## D. Transformer Based approach 
This method uses a pre-trained transformer model to identify which segments of which supporting text  (as segments of the statements) would require an annotator’s attention to be labelled. This method classified statements identified supporting text, and scored statements based on their complexity. The latter purpose allowed for creating a list of priority statements that were sent to WikiRate, for manual annotation to augment the ground truth data. 

### Methodology
The data was split into paragraphs using the TextTilingTokenizer from the NLTK package. If no paragraphs were detected using this method (due to extraction irregularities), then a paragraph was defined as eight continuous sentences counting from the beginning of the document.

Positive class labels were created using manually validated ground truth data related to the text inputted by the annotators when justifying their label choice (WikiRate data column 'Comments'). Positive classifications indicate the metric is present in the statement, while negative classification indicates it is not. Regex-based text cleaning functions were applied to eliminate 'Comments' noise, such as the reviewer name and page numbers.

Negative class labels were created by sampling random sentences from texts that were not part of the positive class. The negative cases were amplified to generate more data for those instances in order to make the classification problem closer to real life and to teach the transformer more examples. In some cases, a class imbalance of up to 8x was created. 

[A pre-trained Roberta model](saibo/legal-roberta-base) from the Hugging Face model hub was used to fine-tune the classification models on the data. The Roberta architecture has shown good performance at inference and the advantage is that this model was trained on legal language, which tends to be better suited for this project’s dataset.

For scoring the statements, after the statement was segmented into paragraphs as described above, every segment of every document was scored with the model. Then, the difference between the positive class prediction (probability) and negative class prediction (probability) for every segment was calculated. The statements with the lowest difference were considered to be the most difficult to label and, thus, prioritised to be sent to WikiRate for manual labelling. 


This method used a contextual method, leveraging the 'Comments' given by annotators, to predict if a sentence could be retrieved as a comment or not. If a sentence can be a comment, it would mean it justifies the presence of the metric in the statement analysed.

Using the training set, for each of the three metrics, positive and negative classes were created. The positive classes were created by using the sentences extracted from 'Comments', where the statement was labelled positively. The negative samples contained sentences randomly sampled from statements, except the sentences present in 'Comments'.
The ALBERT-based model for classifying sentences was trained in two categories, 'in Comment' and 'not in Comment'. This model scores each sentence in the statements. If a sentence gets a probability greater than 0.5, it was predicted as coming from a comment. Then, if a statement had at least one of its sentences being predicted as coming from a comment, it was classified as containing the metric analysed.  

Compared to the previous method, this method outputs the sentence justifying the prediction. 

![Screen Shot 2021-11-30 at 11 36 33 am](https://user-images.githubusercontent.com/64998301/143969853-2aa712c0-d144-4297-94ed-57f718283b8d.png)


_Visualisation of Transformers Based Approach Method Using the 'Comments'_  

### 💡 Key findings using this method:
When analysing the three risk-associated metrics, overall, this system is the worst at predicting if a metric is contained in a statement. Nevertheless, considering that it does not use the label at all (just use the comment section), the results are encouraging. However, as this model is trained on very few data points, overall, this system was considered overconfident in predicting a risk metric in the statement. A way of improvement could be to use this task as a pre-training for a BERT backbone that could be then used in HAN. This way, the information contained in the Comment section and the real labels could be used. 

As for the previous approaches, for some documents, the sentences predicted seem to justify a positive metric, even if labelled negative. This indicates the need to clean and verify the ground truth data. 


## Results Validation and Evaluation Methodology
This section describes the validation methodology to be used in training our algorithms. **Identifying all the metrics in those exploratory tests was treated as binary (Yes/No, 1/0, True/False). All the subcategories of the labels were merged into two categories.**

Each metric is treated separately when creating labelling functions with Snorkel, with individual labelling functions being created for it. If a labelling function finds a pattern for the positive cases (Yes/1/True), the label is Yes(1). If the labelling function does not find the pattern then the result is ABSTAIN(-1). If all labelling functions abstain, then the label is No(0).

A group of labelling functions with a voting mechanism is a classification algorithm. 

A classification algorithm can be 
- Rule-based, for example, using if-else statements, e.g. if the document contains the word 'training' then ‘Yes’. Snorkel’s pattern and keyword matching techniques are rule-based systems.
- Learned (from the data), for example, using numeric supporting text  to predict an outcome probabilistically
- Combined using both methods above

In the case of rule-based models, ground truth labelled data is required only for testing the results. In the case of learned and combined models, ground truth data needs to be used to train and test the model.

This means that for rule-based approaches, we can use the entire WikiRate corpus (the ground truth data of the project) for validation. At the same time, for the other two cases, we need to use, for instance, ⅔ of the labelled statements for training and ⅓ for testing.

<img align="right" alt="Coding" width="400" src="https://cdn.dribbble.com/users/38569/screenshots/7131533/media/1b8aeec115fb064688de4ef74620fae3.png">

Required evaluation measurements for rules-based systems include:
- Accuracy - the fraction of correctly predicted labels 
- Precision - the number of true positive results divided by the number of all positive results, including those not identified correctly (i.e. true positives plus false positives)
- Recall - the number of true positive results divided by the number of all samples that should have been identified as positive (true positives plus false negatives).
- F1 score -  the harmonic mean of precision and recall, which can serve as a measure for accuracy

Required evaluation measurements for learned and combined systems include:
- Log loss - the negative average of the log of corrected predicted probabilities for each instance.
- ROC-AUC curve - a graphical plot that illustrates the diagnostic ability of a binary classifier system as its discrimination threshold is varied.
Since accuracy, precision, recall and F1 score are threshold measurements, it is important to plot the ROC-AUC and precision-recall curves to decide on the right threshold before reporting on final metric results per evaluation cycle.

When using Snorkel,  utilities from the Snorkel library like LFAnalysis are used to evaluate these labelling tasks. LFAnalysis is used to understand the different statistics like polarity, coverage, overlaps, and conflicts. Polarity shows the set of unique labels that LF outputs (excluding abstains). Coverage depicts the fraction of the dataset of the LF labels, while overlaps demonstrate the fraction of the dataset where this LF and at least one other LF label, and conflicts show the fraction of the dataset where this LF and at least one other LF label disagree. After collecting statistics using LFAnalysis, MajorityLabelVoter is used to perform the classification task to predict the label. The predicted variables are evaluated against their respective ground-truth value.


**Cross-Validation**
When developing learned and combined systems, a stratified repeated 5-fold cross-validation is used. Each fold should be drawn three times. This means that we train and test it 15 times for every classification algorithm and report the average results of the 15 runs. Initially, stratification should be based on document length in tokens based on a simple whitespace tokenizer (short/medium/long) and industry group.

When using cross-validation, every test fold’s ground truth values alongside predicted values,  metric results per each fold, and report the mean (+/- error based on standard deviation) as a final metric result shall be stored. Since this project has very limited data, it was separated into train and test sets. Further validation will be done using future, improved labelled data as our validation data.

## 💡 Key findings 
This phase of the project was built upon domain knowledge on modern slavery disclosure and proposed four first methods to extract the metrics’ associated supporting text and classify modern slavery statements preliminarily. The methods display about the same accuracy (approximately 70.5% average, with the lowest model performing at 33% accuracy and the highest performance at 91%). All methods can bring insightful supporting text and predictions. **The notebooks attached to this directory explain the exploratory tests done for each of the metrics.**

The best use of those supporting texts will be to suggest part of the statements indicating the metrics’ presence to make the manual labelling quicker or to guide the cleaning of the existing labelled dataset. For instance, in the future, leveraging the help of the volunteers who are now annotating statements on the WikiRate platform, a tagging process can be created to label and validate the quality of the supporting text and their attribution to each metric. This process should be continuously improved in later stages to continue developing and iterating the machine learning models.  

Based on the exploratory tests, certain learnings were derived. First of all, the quality of the initially labelled dataset needs to be improved. In many cases, when trying to validate the results, it was unclear whether the classified result was correct or not since the label itself was uncertain. When manually validating the results of the different computation methods employed by comparing with the ground truth data, the researchers concluded that the results tend to be wrong or conflicting, not only because of the models but rather because the labelled data needs improvements. 

Yet, some of our models show that based on the structure of the labelled database, there is a great potential to use the 'Comments’ for creating the positive class data where possible since the 'Comments’ are already extracted relevant text by the original reviewer. Yet, until the labelled dataset is entirely cleaned and validated, only internally validated 'Comments’ were used to ensure clean labelled data. In this case, negative class data can be sampled randomly from the texts while ensuring no intersection between the data of positive and negative classes. This method was useful in identifying supporting text without relying on the labels.

The exploratory tests indicate that analysis at a paragraph or sentence level rather than document-level would be more feasible and accurate. This would require a reliable paragraph or sentence extractor. During this exploratory phase, difficulties were faced cutting the text into sentences. Moreover, the quality of the text extracted needs improvement as in many cases, the text was not fully extracted, and inconsistencies were found in the text field (words without spaces, of “l” written as “1”, etc.). 


## 🙏 Special thanks to the BNPP team for their support with this analysis. 
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174131-743f4dc5-c5b3-4b3f-ba2d-83e0fc413a13.png">



