#
import bs4
import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#################Templates#################
#https://www.indeed.com/jobs?q=Developer+remote&l=il
#https://www.indeed.com/jobs?q=Developer+remote&l=il&start=10 page 2

######################## SCRAPE INDEED #############################
def ScrapeIndeed():
    
    indeedSoupBowl = []
    indeed    = "https://www.indeed.com/jobs?q=Developer+remote&l="
    indeedcli = uReq(indeed)
    pageco    = indeedcli.read()
    indeedcli.close()
    indeedSoup= soup(pageco, "html.parser")
    ###########counts pages of jobs#############
    jobcnt    = indeedSoup.findAll("div",{"id":"searchCountPages"})
    numbOfJobs= jobcnt[0].text
    stringCL  = str(numbOfJobs)
    stringCX  = stringCL[28:]
    IntVar    = int("".join(filter(str.isdigit, stringCX)))
    print(numbOfJobs)
    numReal   = IntVar * 15
    print(str(numReal)+ " jobs")
    ############################################
    numberOfPages = round(IntVar)
    print(str(numberOfPages) + " pages")

    
    i=int(0)
    count = 0
    while(i<numberOfPages):
        print("scraping page: "+str(i))
        if(i==0):
            pageToScrape = str("https://www.indeed.com/jobs?q=Developer+remote&l=")
            pCLI         = uReq(pageToScrape)
            pCO          = pCLI.read()
            pCLI.close()
            paToScSoup   = soup(pCO, "html.parser")
            indeedSoupBowl.append(paToScSoup)
        elif(i>0):
            pageExpander = str("&start="+str(count))
            pageToScrape = str("https://www.indeed.com/jobs?q=Developer+remote&l="+pageExpander)
            pCLI         = uReq(pageToScrape)
            pCO          = pCLI.read()
            pCLI.close()
            paToScSoup   = soup(pCO, "html.parser")
            indeedSoupBowl.append(paToScSoup)
        count += 10
        i+=1
        
    AnalyzeIndeed(indeedSoupBowl)
    
def AnalyzeIndeed(indeedSoupBowl):
    numberOfPages = len(indeedSoupBowl)
    print(str(numberOfPages)+" pages")
    print("Analyzing pages")

    #filename = "JobScrape.csv"
    #f        = open(filename, "w")
    #headers  = "Title, Company"
    #f.write(headers)
    passtoFileWriter = []
    i=0
    while(i<numberOfPages):
        print("page:        "+str(i))
        listings = indeedSoupBowl[i].findAll("div",{"class":"jobsearch-SerpJobCard"})
        x=0
        while(x<len(listings)):
            newSet = []
            print("* * * * * *")
            #jobTitle = listings[x].div.a["title"]
            jobTitlex = listings[x].div.a.text
            jobTitle = jobTitlex.replace("\n","")
            print("Title:   "+str(jobTitle))

            company  = listings[x].findAll("span",{"class":"company"})
            company2 = company[0].text
            company4 = str(company2)[1:]
            company3 = company4.replace("\n","")
            print("Company: "+company3)

            #f.write(str(jobTitle).replace(",",":")+","+company3.replace(",",":")+"\n")
            newSet.append(str(jobTitle))
            newSet.append(company3)
            passtoFileWriter.append(newSet)
            x+=1
        i+=1
    with open("jobScrape.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(passtoFileWriter)
    #f.close()
    
    
            
###################################################################

#indeedSoupBowl = []
#indeed    = "https://www.indeed.com/jobs?q=Developer+remote&l=il"
#indeedcli = uReq(indeed)
#pageco    = indeedcli.read()
#indeedcli.close()
#indeedSoup= soup(pageco, "html.parser")
#indeedSoupBowl.append(indeedSoup)
#AnalyzeIndeed(indeedSoupBowl)
def main():
    ScrapeIndeed()

