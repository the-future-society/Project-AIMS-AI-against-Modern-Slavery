
<img align="left" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171138-777e6d3d-3442-4872-8ada-e1bd311a49f9.png">

<img align="right" alt="Coding" width="150" src="https://user-images.githubusercontent.com/64998301/143171267-86860e2b-8a25-440e-b778-a860ceac7e99.png">


<img align="center" alt="Coding" width="650" src="https://cdn.dribbble.com/users/2507445/screenshots/5776417/media/8efcb73a124de3b1f6937fb85133aeee.gif">



# Getting the dataset
This directory presents the different data sources of modern slavery statements from the UK and how to extract the text from the statements. 

To date, access to modern slavery statements has been through company websites or the compilation efforts by the Business and Human Rights Resource Centre’s (BHRRC), referred to here as the  [Archive of BHRRC The Modern Slavery Registry]() and [WikiRate](), who has collated and analysed this data.  

Much of this information has been collated manually, with teams of researchers searching for and systematically reviewing available statements. Given that this is costly in terms of person-hours, a more centralised and automated approach is desirable. Promising steps in this direction is the recent launch of [🇬🇧 GOV.UK Modern slavery statement registry](), which will centralise the housing of these statements.

When Project AIMS started, there was no centralised database of statements by the government, so the project’s dataset was built from existing resources. The main data used thought Project AIMS so far are: 
- Archive of BHRRC The Modern Slavery Registry
- The WikiRate data (that we generally call the labelled dataset) 



In this directory, we present the main data sources that could be used in this project and how to extract the text from the statements. 


Bellow, we present the techniques used in the pipeline of Project AIMS. Nonetheless, some elements were developed dependent on AWS services. To avoid needing those services, we also provide in this directory alternatives on how to access those datasets, how to extract the text from the statements and a copy of data available as of November 2021.


They can be found here: 
- [Archive of BHRRC The Modern Slavery Registry]()
- [🇬🇧 GOV.UK Modern slavery statement registry]()
- [The WikiRate data (that we generally call the labelled dataset)]()




### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/release/python-3611/) installed on your system
- If you'd like to use the provided tutorials, you also need access to a [Jupyter notebook](https://jupyter.org/install.html)

### Quickstart

It's recommended that you use a virtual environment such as [virtualenv](https://virtualenv.pypa.io/en/latest/), [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) or similar.




## Text extraction 
Being able to extract the text and assess its quality before using it in building models is of great importance and a key step in ensuring the accuracy of the final tool. For example, if a paragraph of a company’s report is not extracted, the analysis will lead to an incorrect assessment of the company’s compliance with modern slavery regulation. The same issue also arises if the text is fully extracted but not in the intended order (e.g. columns of text are read as a single block).


## An older version of the Project AIMS Pipeline looks like this: 
> This pipeline is dependent on Lambda Functions for extracting text from original files.
<img width="924" alt="Screen Shot 2021-11-30 at 8 43 27 pm" src="https://user-images.githubusercontent.com/64998301/144032949-de2ce1e9-91af-47aa-a7e9-f54ad0d78127.png">

### PDF pipeline (Use Async APIs of Amazon Textract)
<img align="right" alt="Coding" width="500" src="https://cdn.dribbble.com/users/100976/screenshots/3407799/media/46606d8d83079426b1e942444ede9160.gif">

1. A document with a .pdf extension gets uploaded to an Amazon S3 bucket. It sends event to SQS queue named S3Documents.
2. A job scheduler lambda function runs at a certain frequency for example, every 5 minutes, and poll for messages in the SQS queue.
3. For each message in the queue, it submits an Amazon Textract job to process the document and continue submitting these jobs until it reaches the maximum limit of concurrent jobs in your AWS account.
4. As Amazon Textract is finished processing a document, it sends a completion notification to an SNS topic.
5. SNS then triggers the job scheduler lambda function to start the next set of Amazon Textract jobs.
6. SNS also sends a message to an SQS queue named TextractResults, which is then processed by a Lambda function to get results from Amazon Textract and store them in the S3 output bucket.


### HTML pipeline

1. A document with .html extension gets uploaded to an Amazon S3 bucket. It sends event to SQS queue named S3DocumentsDirect.
2. SQS triggers lambda function named DirectExtractTextFunction (function-direct folder) which processes HTML file and store result to S3 output bucket.

This is created with a separate SQS queue because it doesn't need throttling for Textract, as it doesn't use it so that processing could be faster, and lambdas are invoked immediately from SQS.

In a folder, function-direct could be added python files for processing different kinds of text files. When added then, process_direct_function.py should be updated in this part:

```
import extract_html_text_function as html
.....
.....
.....
if(pathlib.Path(objectName).suffix == ".html"):
            result = html.create_txt(request)
```           


### Setup

- `function` - A folder for python scripts to be deployed to AWS
- `template.yml` - An AWS CloudFormation template that creates an application.
- `1-create-bucket.sh`, `2-build-layer.sh`, etc. - Shell scripts that use the AWS CLI to deploy and manage the lambda function.

Use the following instructions to deploy and manage the lambda function.


To create a new bucket for deployment artifacts, run `1-create-bucket.sh`.

    $ ./1-create-bucket.sh
    make_bucket: lambda-artifacts-a5e491dbb5b22e0d

To build a Lambda layer that contains the function's runtime dependencies, run `2-build-layer.sh`. Packaging dependencies in a layer reduces the size of the deployment package that you upload when you modify your code.

    $ ./2-build-layer.sh


To deploy the application, run `3-deploy.sh` (you should specify input and output buckets in the script, as well as e-mail address for notifications).

    $ ./3-deploy.sh
    Uploading to e678bc216e6a0d510d661ca9ae2fd941  9519118 / 9519118.0  (100.00%)
    Successfully packaged artifacts and wrote output template to file out.yml.
    Waiting for changeset to be created..
    Waiting for stack create/update to complete
    Successfully created/updated stack - pdf-extract-stack

This script uses AWS CloudFormation to deploy the Lambda functions and an IAM role. If the AWS CloudFormation stack that contains the resources already exists, the script updates it with any changes to the template or function code.


Set S3 bucket notification to send events to SQS queue where the file is created run `4-s3-sqs-event.sh` script (you should specify input bucket in the script). For PDF files info goes to S3Document SQS queue, and for HTML files it goes to S3DocumentsDirect SQS queue.

    $ ./4-s3-sqs-event.sh


### Automated trigger
At the moment of this design, the `template.yaml` did not configure the automatic triggering of the Lambda function once it's deployed. At that time, the best way to achieve that is to set it manually on the AWS console used.

### Updating the deployment
When you make code updates to the 'meat' of the function without adding any new libraries, you only have to run the 3rd step of the deployment to update the cloud function with new code. If you add new third-party libraries, then the 2nd step of building a layer needs to be rerun as well. The first step needs to be run only the very first time when creating the function, so you don't need to run it when making code updates.

## An updated version of the text extraction pipeline 
<img align="right" alt="Coding" width="600" src="https://cdn.dribbble.com/users/1729935/screenshots/4108239/media/1a4b3d5ebbe44ab8e020793a9960295a.gif">

The first step is to run the ‘prepare’ command that downloads the scrapable list of URLs and sets unique IDs to all of them. 

The next step is the extraction of the text.

Text extraction is composed of three parts:
- HTML extraction (fully-automated)
- Scanned PDF extraction (fully-automated)
- Digital PDF extraction (semi-automated)

The first two steps are automated using a lambda function trigger. As soon as a document is received by the `...-raw` bucket, it will be sent to the extraction pipeline. HTML file extensions are processed using a GPT-based article extractor and scanned PDFs are processed using AWS Textract OCR API.

If all the documents are automatically processed, then it’d be necessary to run the XPDF to extract higher-quality text from the digital PDFs. That notebook will also take care of choosing the best extraction of each PDF file (among the digital extraction and the OCR’d version) and upload the best extractions to AWS S3.

## Analysis and learnings 
### Extracting text from PDFs

[The Portable Document Format (PDF)](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdf_reference_archive/pdf_reference_1-7.pdf) covers a very broad spectrum of different document styles and it can be very complex. For our purposes, there are two types of PDF files that require different approaches to text extraction: native (or digital) and scanned files. The difference between native and scanned PDF files is that the native one is created from text editors such as Microsoft Word, whereas the scanned PDF is created from scanned image files. Even though both contain textual data, the scanned PDF files are not directly readable by computers and require Optical Character Recognition (OCR) technology to convert them into a machine-readable format.

Typical PDF text extraction Python libraries  (such as   PyPDF and PDFMiner) are only able to extract the text from digital PDFs. To extract text from scanned files, one needs to use an  OCR  tool to recognize letters, commonly trained using computer vision methods on vast numbers of files. During the process of data exploration, it was found that approximately one-quarter of the published statements in PDF format were scanned. Hence, our first attempt was to implement an OCR solution for all the files as it would cover both subtypes of the format. 

<img align="right" alt="Coding" width="400" src="https://cdn.dribbble.com/users/656298/screenshots/2895552/media/4e8f0b3f30854b3ae137b30840ea4741.gif">


While some text was extracted from 99% of PDF documents, it was revealed that the extraction of the OCR solution was of low quality, and digital PDF text extractors provided much more coherent sentences and ordered paragraphs. Issues that arose included:
- For multi-column documents, the OCR solution would mix sentence beginnings from both columns resulting in incoherent paragraphs.
- Paragraph titles were extracted separately from the paragraph texts which made the titles unusable for topic detection.
- Incorrect characters were recognized, e.g. the'r n'combination was recognised  as 'm'.

Therefore, a hybrid method was implemented, where the text from native PDFs was extracted using the open-source software [XpdfReader](https://www.xpdfreader.com/), while scanned files were processed using the AWS Textract OCR API.
### Extracting text from HTMLs
Hypertext Markup Language (HTML) is a standardized markup language for documents on the World Wide Web. Most web pages contain HTML (or XHTML) markup descriptions. HTML is interpreted by browsers, and the formatted text obtained as a result of interpretation is displayed on the screen of a computer monitor or mobile device. An HTML document consists of a tree of elements enclosing text data that can be searched, manipulated, and retrieved. Each element is denoted in the original document by a start (opening) and end (closing) tag (with rare exceptions).

Retrieving information from web pages can be difficult as they vary greatly.  Generally, text extraction in Python is carried out using libraries, namely Scrapy, BeautifulSoup and BoilerPy, which facilitate the retrieval of required data from the page.


[BeautifulSoup (BS)]( https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is one of the most commonly used libraries, due to its efficiency and user-friendliness. Furthermore, it is also able to retrieve information from pages with unclosed tags, incorrect and/or nested attributes. Therefore, this is the first library that was tested by Project AIMS for text extraction from the HTML documents. This method is based on the web page structure. It maps a web page to an HTML tree and then retrieves the table nodes of the tree to detect the main content. Nevertheless, this method suffers from only partial extraction of text due to the inconsistent use of tags on different web pages.

The next step was to test [BoilerPy3](https://pypi.org/project/boilerpy3/), providing algorithms to detect and remove the surplus 'clutter' (boilerplate, templates) around the main textual content of a web page, extracting the main content without additional noise (advertisements, search and filtering panels, unwanted images or links). The library comprises several extractors. ArticleExtractor, being tuned towards news articles, is highly suitable for extracting content from modern slavery statements. However, one limitation of ArticleExtractor is its inability to extract additional statements from the same company, which are linked within the HTML document (for example, statements from previous years or statements formatted as PDFs).

## Text extraction quality assessment
Most of our learnings are collected in our publication [Digital AI against Modern Slavery: Digital Insights into Modern Slavery Reporting - Challenges and Opportunities](http://ceur-ws.org/Vol-2884/paper_110.pdf). 


<iimg align="centert" img width="400" alt="Screen Shot 2021-11-30 at 8 16 22 pm" src="https://user-images.githubusercontent.com/64998301/144033314-5ca09cc3-cdc8-44ce-8a7a-e136b033cb15.png">


The scope of this work was to compare the performance of different methods of text extraction from the HTML and PDF files. The methodology was to sample several HTML and PDF files containing modern slavery statements, test different methods of text extraction, and manually compare the quality of the resulting text using [Diffchecker](https://www.diffchecker.com). Diffchecker facilitates the comparison of text by highlighting deletions and additions. For HTML documents, ArticleExtractor and BeautifulSoup were compared, and for PDF documents XPDF Reader  and AWS Textract OCR API were compared.
### Key findings and examples
Retrieval of text data from 120 HTML documents, using Diffchecker to manually compare the results, revealed that in 68% of cases ArticleExtractor (provided by BoilerPy) performs better than BeautifulSoup in terms of the amount of main content information that was extracted.  However, BoilerPy’s ArticleExtractor does not extract URLs on the web page and refers to other statements (e.g. statements of previous years), so a combination of BoilerPy’s ArticleExtractor and BeautifulSoup could be used to further improve text retrieval from HTML documents.

Retrieval of text data from 150 PDF documents, using Diffchecker to manually compare the results, revealed that XPDF always outperformed OCR except for scanned PDFs (for which XPDF produces empty output). Therefore, OCR was used on scanned PDFs and XPDF on all others.

For both HTML and PDF documents, a combination of both methods is more desirable. Having assessed the results of text retrieval from the statements, all of the extracted text was added as a  new column to Project AIMS’ dataset, generally called ‘text’. 

In each notebook of this repository, the data with the text extracted is linked and openly available. 
