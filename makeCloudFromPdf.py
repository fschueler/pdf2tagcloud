'''
Created on Jan 19, 2014

@author: felix
'''
import sys
from PyPDF2 import PdfFileReader
from pytagcloud import create_tag_image, make_tags, LAYOUT_HORIZONTAL
from pytagcloud.lang.counter import get_tag_counts

def main():
    for i in range(0, len(sys.argv)):
        if (sys.argv[i] == '-f'):
            try:
                content = getPDFContent(sys.argv[i+1])
            except:
                raise RuntimeError('Something went wrong! Usage: makeCloudFromPdf -f inputfile.pdf')  
    tags = make_tags(get_tag_counts(content)[1:100], maxsize=100)
    create_tag_image(tags, 'cloud_large2.png', size=(1920, 1080), background=(0, 0, 0, 255), layout=LAYOUT_HORIZONTAL, fontname='Vollkorn')
            
def getPDFContent(path):
    content = ""
    p = file(path, "rb")
    pdf = PdfFileReader(p)
    numPages = pdf.getNumPages()
    print 'pages:', numPages
    for i in range(0, numPages-1):
        try:
            content += pdf.getPage(i).extractText() + "\n"
        except:
            content += ""
    #content = " ".join(content.replace(u"\xa0", " ").strip().split()) 
    return content 
        
if __name__ == "__main__":
    main()