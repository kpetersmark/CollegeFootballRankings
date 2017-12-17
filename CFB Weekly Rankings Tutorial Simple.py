# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 08:46:04 2017

@author: Kyle
"""

#Import Libraries
import requests
from bs4 import BeautifulSoup
import csv

 

#Open CSV file to start writing
File = open("CFB Weekly Rankings 2005 thru 2016.csv", "w", newline='')        

#Create arrays to store data in
Rankings = []
Headers = ["Year", "Week", "Rank", "Team"]
Rankings.append(Headers)



#Loop through all the URL's
for year in range(2005,2017):
    for week in range(1,16):
        URL = 'http://www.espn.com/college-football/rankings/_/poll/1/week/{}/year/{}/seasontype/2'.format(week,year)
        request = requests.get(URL)
        content = request.content

        #Make the soup
        Soup = BeautifulSoup(content, "html.parser")
        Table = Soup.find("tbody")    
        Rows = Table.find_all("tr")
        
        
        for Row in Rows:
            
            Col = Row.find_all("td")
            Team = Row.find("span", class_="team-names")
            print(year, week, Col[0].text, Team.text)
            Ranking = [year, week, Col[0].text, Team.text]
            Rankings.append(Ranking)
        
            
#Write arrays to CSV file        
with File:
    writer = csv.writer(File)
    writer.writerows(Rankings)        