import document_analysis.utils as utils

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Verify the PDF documents in the S3 bucket before analyzing')
    
    parser.add_argument("bucket_name", help="bucket name",
                        type=str)
    parser.add_argument("--path", help="folder prefix in the bucket",
                        default="", type=str)
    
    args = parser.parse_args()
    return args

def verify_documents(bucket_name, path):
    documents = utils.get_file_names_s3(bucket_name, path)
    if len(documents) > 0:
        print("Detected {} PDF documents:".format(len(documents)))
        for index, file_path in enumerate(documents):
            print("\t {} - {}".format(index+1, file_path)) 
    else:
        print("No PDF document found")

if __name__ == '__main__':
    args = parse_args()
    bucket_name = args.bucket_name
    path = args.path
    verify_documents(bucket_name, path)
    