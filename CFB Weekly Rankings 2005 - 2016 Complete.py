# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:43:02 2017

@author: Kyle
"""
#Import Libraries
import requests
from bs4 import BeautifulSoup
import csv

#function of making the soup
def MakeSoup(content):
    Soup = BeautifulSoup(content, "html.parser")
        
    Table = Soup.find("tbody")    
           
    Rows = Table.find_all("tr")
        
        
    for Row in Rows:
            
         Col = Row.find_all("td")
         Team = Row.find("span", class_="team-names")
         print(year, week, Col[0].text, Team.text)
         Ranking = [year, week, Col[0].text, Team.text]
         Rankings.append(Ranking)
 

#Open CSV file to start writing
File = open("CFB Weekly Rankings 2005 thru 2016.csv", "w", newline='')        

#Create arrays to store data in
Rankings = []
Headers = ["Year", "Week", "Rank", "Team"]
Rankings.append(Headers)



#Loop through all the URL's
for year in range(2005,2017):
    for week in range(1,18):
        URL = 'http://www.espn.com/college-football/rankings/_/poll/1/week/{}/year/{}/seasontype/2'.format(week,year)
        request = requests.get(URL, allow_redirects=False)
        
        
        #Find out if we've reached the end of the regular season and then change URL to final standings
        if request.status_code >= 300:
            URL = 'http://www.espn.com/college-football/rankings/_/poll/1/week/1/year/{}/seasontype/3'.format(year)
            request = requests.get(URL, allow_redirects=False)
            content = request.content
          
            MakeSoup(content)
          
            break
        content = request.content
        
             
# Run the soup         
        MakeSoup(content)
            
#Write arrays to CSV file        
with File:
    writer = csv.writer(File)
    writer.writerows(Rankings)        


