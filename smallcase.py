import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import csv

baseUrl = 'https://www.smallcase.com'
discoverManagerUrl = 'https://www.smallcase.com/discover/creators?count=121'
elements = BeautifulSoup(requests.get(discoverManagerUrl).text, "html.parser").find_all("a")

def getCompanyName(managerDetail):
    divs = managerDetail.find_all("h3", class_="ManagersBanner__header-text__3DL0o mb8")
    if len(divs) > 0:
        return divs[0].get_text()

def getManagerName(managerDetail):
    paras = managerDetail.find_all("p", class_="font-medium text-16 mb12")
    return paras[0].get_text()

def getManagerInvestorId(managerDetail):
    divs = managerDetail.find_all("div", class_="ManagersBanner__header-sebi__2zcOQ mb12 font-regular")
    if len(divs) > 0:
        return divs[0].get_text()

def getManagerExperience(managerDetail):
    paras = managerDetail.find_all("p", class_="")
    experience = paras[0]
    return experience.get_text()

def getManagerDetails(link):
    managerUrl = baseUrl + link
    managerDetail = BeautifulSoup(requests.get(managerUrl).text, "html.parser")
    companyName = getCompanyName(managerDetail)
    managetName = getManagerName(managerDetail)
    riaId = getManagerInvestorId(managerDetail)
    experience = getManagerExperience(managerDetail)
    return [companyName, managetName, riaId, experience]

i = 1
rows = []
for element in elements:
    href = element.get('href')
    if 'manager' in href:
        data = getManagerDetails(href)
        rows.append(data)
        print(href + " ... done")
        i = i + 1

filename = "managers.csv"
header = ['company_name', 'manager_name', 'ria_id', 'experience']

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(header)
      
    print(rows[0])
    print(type(rows))
    # writing the data rows
    csvwriter.writerows(rows)