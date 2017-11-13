#Problem Statement 1
#write a python script to scrape https://www.babynamesdirect.com to get
#all baby names for boys and girls both. Store names in a comma-separated format 
#in names.csv with two fields: name, gender. The first column will contain all
#names and second column will contain either boy or girl.


import bs4                             # bs4 contain beautifulsoup package 
from urllib.request import urlopen as uReq    # import urlopen to load the contents and I used urlopen as uReq
from bs4 import BeautifulSoup as soup         # BeautifulSoup is used for parsing the html page and I used BeautifulSoup as soup

my_url = "https://www.babynamesdirect.com/"      # link of the website

uClient = uReq(my_url)       # Upload the contents in variable

page_html = uClient.read()

uClient.close()              # Close the Client

page_soup = soup(page_html, "html.parser")     #parsing the html-page

containers = page_soup.findAll("div",{"class":"wcontent"})   #find all the div whose class name is wcontent

filename = "names.csv"                        # csv_file store in filename

f = open(filename, "w")                      # open the names.csv file to write all data

headers = "Name, Gender \n"                  # In first row Assigning name and gender 

f.write(headers)                             # write the name and gender in file of first row

for link in containers[:-1]:                # total content is 9 but name contain in only 8 'wcontent' so I remove the last 'wcontent'
    
    tag = link.findAll('a')                 #In 'wcontent' name is associted in the <a> tag so I find all the <a> 
    
    for val in tag[:-1]:                    # in 'wcontent' there is 10 name so first I find the first name 
        #print(val)
        gender = val.get('class')           # In <a> tag class name for gender boy is 'boy' and for gender girl is 'girl' so I get the class name.
        
        name = val.text                     # text in <a> tag is name 
        
        print(name + "," + str(gender)[2:-2].capitalize())  # gender name is in list and contain "[' ']" so I remove first two char from starting and ending gender is in list format and name is in string format so it can't contanate.So, I convert the list in string.
        
        f.write(name + "," + str(gender)[2:-2].capitalize() + "\n")  # Samething is written in file and comma is used for partition.
        
f.close()     #close the file