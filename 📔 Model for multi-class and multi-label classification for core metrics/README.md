 
 
<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">
 
<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">
 
<img align="center" alt="Coding" width="550" src="https://cdn.dribbble.com/users/917530/screenshots/2879128/media/6008ce6d81787b9aa0ed9c0101b75567.gif">
 
 
 
 
 
The [📔 Initial Metrics Exploration](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Initial%20Metrics%20Exploration)  was followed by a second semantic workshop with the project partners. Based on all the accumulated knowledge, the decision was made to prioritize four of the metrics to explore multi-class and multi-label classification models.  Those four metrics are: 
 
- Approval
- Training
- Whistleblowing mechanism
- Incidents remediation
 
## Improve the annotation for the four selected metrics
 
For these four initial metrics, the modern slavery experts designed a clear set of assumptions that were used not only to label more data but also to clean the existing ground truth data on the WikiRate platform. 
 
Clear rules for labelling were designed, allowing to make the most of the labelled dataset. This includes, for instance, improvements of the collection of 'Commnets', ensuring that for each label there was an associated comment, in a format of exact copy-paste from the statement text. Based on the assumptions and the labelling rules, the WikiRate team and Walk Free Foundation labelled new documents for each of the four metrics while undergoing extensive cleaning and validation of the existing data on the WikiRate platform. 
 
## Using the example of the  MSA Approval metric example, join us in building solutions for the other three subprojects: 

- [Multi-lebel classification for the training metric](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Sub-project:%20Multi-label%20classification%20for%20the%20MSA%20Training%20Metric)
- [Multi-lebel classification for the whistleblowing mechanism metric](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Sub-project:%20Multi-label%20classification%20for%20the%20MSA%20Whistleblower%20Mechanism%20Metric)
- Multi-lebel classification for the incidents remediation metric
 
### Example: Multi class classification for the approval metric
 
In this directory you can access the [Multi_class_classification_for_the_approval_metric.ipynb](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/blob/1fe5bbcf0eef6b0997eef6e14337d92096525175/%F0%9F%93%94%20Model%20for%20multi-class%20and%20multi-label%20classification%20for%20core%20metrics/Multi_class_classification_for_the_approval_metric.ipynb) notebook, where we present an example of a multi-class classification model for the Aproval matrix. 
 
🗄️ You can access the data used in this notebook [here](https://drive.google.com/file/d/1xThQSWn501Jlxfay-c7u-EjTu-3R1FAg/view?usp=sharing). We recommend you re-run this research with an updated version of this data which can be downloaded following these [instructions](https://github.com/the-future-society/Project-AIMS-AI-against-Modern-Slavery/tree/main/%F0%9F%97%84%EF%B8%8F%20Data%20and%20text%20extraction/WikiRate).

 
**Assumptions for the approval metric**
 
| |Approval not explicit in statement| Approved by Board| Approved - not by Board
|-|--------------------------------------------|---------------------------|--------------------------------|
|Description| Approval by board is not explicit.| Approval by board is explicit in the statement.| Approval is explicit in statement, but by an person/entity other than the board|
|Assumption for meeting answer|No mention of any sort of approval in the statement.|Statement explicitly mentions that the statement has received approval from the company's board. It must be explicit that it has been "been approved by the board" or "on behalf of the board", NOT that a board member has signed the statement. This is usually found at the end of the statement or first page.|Statement mentions that it was approved but the entity is not a representative of the Board or the Board itself.|
|Example| | "This Statement was approved by the Board of Netwealth Group Limited" | Eurizon SLJ Capital Limited's 2019 statement, p1:"This statement has been approved by the Chief Operating Officer of ESLJ." |
 
 
 
**🙏 Special thanks to the WikiRate team for leading the work on annotating new documents and validating the existing ones.**
<img align="left" width="200" src="https://user-images.githubusercontent.com/64998301/143174086-aebdf1ed-fe4a-400f-95b2-0269cd10498b.png">
 
 
 
 
 
