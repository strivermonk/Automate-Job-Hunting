from asyncore import write
from bs4 import BeautifulSoup
import requests
def find_jobs():
    
    html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup= BeautifulSoup(html_text,'lxml')
    jobs= soup.find_all('li',class_ ='clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span',class_='sim-posted').span.text
        if('few' in published_date):
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            with open("C:\Scrape\Jobs\myJobs.txt",'a') as f:
                f.write(f"Company Name : {company_name.strip()} \n")
                f.write(f"Required Skills :{skills.strip()} \n")
                f.write(f"More Info :{more_info}\n\n")

if __name__=='__main__':
    find_jobs()

