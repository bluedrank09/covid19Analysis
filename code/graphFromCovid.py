import csv 
import requests
import matplotlib.pyplot as plt

url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"

try:
    with requests.Session() as S:
        download = S.get(url)
        
    decodedDownload = download.content.decode('utf-8')

    readCsv = csv.reader(decodedDownload.splitlines(),delimiter=',')
    csvList = list(readCsv)

    for row in csvList:
        if row[2] == 'Lat':
            xAxis = row[4:]

        if row[1] == 'New Zealand':
            yAxis = row[4:]
    
    plt.plot(xAxis,yAxis, label = "From John Hopkins")
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('Covid19 New Zealand Cases')
    plt.xticks(rotation = 90)
    plt.show()

        

except Exception as e:
    print("Something went wrong " + str(e))

finally:
    print("no im ramona")