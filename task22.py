im = Image.open( 'myBike.png' )

#Display image
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )

#Saving the filtered image to a new file
im_sharp.save( 'another_Bike.jpg', 'JPEG' )



#!/usr/bin/env python
import sys
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    from pyPdf import PdfFileReader, PdfFileWriter

def pdf_cat(input_files, output_stream):
    input_streams = []
    try:
        # First open all the files, then produce the output file, and
        # finally close the input files. This is necessary because
        # the data isn't read from the input files until the write
        # operation. Thanks to
        # https://stackoverflow.com/questions/6773631/problem-with-closing-python-pypdf-writing-getting-a-valueerror-i-o-operation/6773733#6773733
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(output_stream)
    finally:
        for f in input_streams:
            f.close()
        output_stream.close()

if __name__ == '__main__':
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    pdf_cat(sys.argv[1:], sys.stdout)
    
    
    import requests
import MySQLdb
from bs4 import BeautifulSoup

#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "scraping_user"
PASSWORD = ""
DATABASE = "scraping_sample"

#URL to be scraped
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)
#parse the data
soup = BeautifulSoup(plain_html_text.text, 


# importing pandas package 

import pandas as pd 

  
# making data frame from csv file  

data = pd.read_csv("employees.csv") 

  
# replacing blank spaces with '_'  

data.columns =[column.replace(" ", "_") for column in data.columns] 

  
# filtering with query method 

data.query('Senior_Management == True 

            and Gender =="Male" and Team =="Marketing" 

            and First_Name =="Johnny"', inplace = True) 

  
# display 
data 