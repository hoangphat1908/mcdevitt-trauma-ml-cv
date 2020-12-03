# Introduction
This repository implements CV tools for Trauma ML project at McDevitt lab
# Prerequisites
- Python3
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

# Extract tables
Extract tables from PDF documents stored in a S3 bucket using Amazon Textract. 
## 1. Verify documents
Verify PDF documents in the S3 bucket before analyzing. 
  
```
python3 verify_documents.py <BUCKET_NAME> --path <PATH>
```
Parameters:
* ```BUCKET_NAME``` &mdash; bucket name
* ```PATH``` &mdash; folder prefix in the bucket (default: `""`)

## 2. Analyze documents
Analyze the PDF documents in the S3 bucket and store the responses locally.

**IMPORTANT:** You will be charged for running analyze_documents.py as it will call the Amazon Textract API. Make sure to call verify_documents.py first to verify the documents you want to analyze.
```
python3 analyze_documents.py <BUCKET_NAME> --path <PATH> --output_folder <OUTPUT_FOLDER>
```
Parameters:
* ```BUCKET_NAME``` &mdash; bucket name
* ```PATH``` &mdash; folder prefix in the bucket (default: `""`)
* ```OUTPUT_FOLDER``` &mdash; output folder path to store the responses (default: `"output"`)

## 3. Get tables
Get tables from document analysis responses and save them in csv format.
```
python3 get_tables.py <PATH>
```
Parameters:
* ```PATH``` &mdash; folder containing all document analysis responses returned from running analyze_documents.py

# Example
```
python3 verify_documents.py "my-bucket" --path="files/documents"
python3 analyze_documents.py "my-bucket" --path="files/documents" --output_folder="documents/tables"
python3 get_tables.py --path="documents/tables"
```
