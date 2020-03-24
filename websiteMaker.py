import csv
import JobBoardScraper as js
from  datetime import datetime

def read1():
    jobs = []
    with open ("JobScrape.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            jobs.append(row)
    write1(jobs)

def write1(jobs):
    f = open("index.html","w+")

    f.write("<html>")
    f.write("<head>")
    adString = "<script data-ad-client=$ca-pub-6400085772945590$ async src=$https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js$></script>"
    f.write(adString.replace("$",'"'))
    AnalyticString = "<!-- Global site tag (gtag.js) - Google Analytics --><script async src=$https://www.googletagmanager.com/gtag/js?id=UA-159854442-1$></script><script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'UA-159854442-1');</script>"
    f.write(AnalyticString.replace("$",'"'))
    f.write("<style>")
    f.write("body{background-color: black;} h1{color: grey} p{color: white}")
    f.write("</style>")
    f.write("</head>")

    f.write("<h1> Job Search Aggregate </h1>")
    f.write("<p> Under Construction: Now Showing Developer Jobs Only </p>")
    datex = datetime.now()
    f.write("<p>"+"Last Updated: "+str(datex)+"</p>")
#body
    f.write("<body>")
    
    for x in jobs:
        f.write("<p>"+"********************"+"</p>"+"<p>"+str(x[0])+"</p>"+"<p>"+str(x[1])+"<p>")

    f.write("</body>")
    
    f.close()


js.main()
read1()
