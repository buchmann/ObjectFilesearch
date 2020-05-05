# my first test with Elastic Search 
# read some pdf content and index it 
# search for words 
# example Indexing many PDF files for full-text search using Elasticsearch
# from : https://www.youtube.com/watch?v=vziwQjHk1Bk
# created by Fisseha Berhane , thank you !!!
# 
from elasticsearch import Elasticsearch 
import os
import glob
import PyPDF2
import pandas as pd

os.chdir("/tmp/pdf")
files = glob.glob("*.*")

len(files)

for book in files:
    print (book)

def extractPdfFiles(files):
    this_loc = 1
    df = pd.DataFrame(columns = ("name","content"))

    for file in files:
        pdfFileObj = open(file,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        n_pages = pdfReader.numPages
        this_doc = ''
        for i in range(n_pages):
            pageObj = pdfReader.getPage(i)
            this_text = pageObj.extractText()
            this_doc +=this_text
        df.loc[this_loc] = file, this_doc
        this_loc = this_loc +1 
    return df

df = extractPdfFiles(files)
print(df.head())

es = Elasticsearch(hosts=["localhost:9200"])

#es.indices.delete(index='data_science')

col_names = df.columns
for row_number in range(df.shape[0]):
    body = dict([(name, str(df.iloc[row_number][name]))for name in col_names])
    print (body)
    es.index(index= 'data_science', doc_type='books', body=body)
search_results = es.search(index = 'data_science', doc_type = 'books',
        body = {"_source": "name",
            'query':{
                'match_phrase':{"content": "Elastic"},
                }
        })

print (search_results['hits']['total'])
print (search_results['hits'])
