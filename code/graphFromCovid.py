import csv 
import requests
import urllib.request
import matplotlib.pyplot as plt

url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
urlRecovery = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"

try:
    #reading the confirmed cases file
    with requests.Session() as S:
        download = S.get(url)
        
    decodedDownload = download.content.decode('utf-8')

    readCsv = csv.reader(decodedDownload.splitlines(),delimiter=',')
    csvList = list(readCsv)

    for row in csvList:
        if row[2] == 'Lat':
            xAxis = row[4:]

        if row[1] == 'New Zealand':
            yAxisString = row[4:]
            confirmedYInt =[] 
            for numConfirmedCases in yAxisString:
                confirmedYInt.append(int(numConfirmedCases))

    #reading the recovery file
    downloadRecoveryOpen = urllib.request.urlopen(urlRecovery)
    decodedRecoveryDownload = downloadRecoveryOpen.read()
    decodedRecoveryDownloadDecoded = decodedRecoveryDownload.decode('utf-8')

    readRecoveryCsv = csv.reader(decodedRecoveryDownloadDecoded.splitlines(), delimiter = ',')
    recoveryCsvList = list(readRecoveryCsv)

    for row in recoveryCsvList:
        if row[1] == 'New Zealand':
            recoveryYAxisString = row[4:]
            recoveryYAxisInt = []
            for numCases in recoveryYAxisString:
                recoveryYAxisInt.append(int(numCases))


    plt.plot(xAxis,confirmedYInt, color = 'red', label = "Confirmed")
    plt.plot(xAxis,recoveryYAxisInt, color='purple' ,label = "Recovered")
    plt.legend(loc="upper left")
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('Covid19 New Zealand Cases')
    plt.xticks(rotation = 90)
    plt.show()

        

except Exception as e:
    print("Something went wrong " + str(e))

finally:
    print("no im ramona")