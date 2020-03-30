import csv 
import urllib.request
import matplotlib.pyplot as plt

url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
urlRecovery = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"
urlDeaths = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv"

try:
    #reading the confirmed cases file
    downloadOpen = urllib.request.urlopen(url)
    decodedDownload = downloadOpen.read()
    decodedDownloadDecoded = decodedDownload.decode('utf-8')

    readCsv = csv.reader(decodedDownloadDecoded.splitlines(),delimiter=',')
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

    #reading the deaths file 
    downloadDeathsOpen = urllib.request.urlopen(urlDeaths)
    decodedDeathsDownload = downloadDeathsOpen.read()
    decodedDeathsDownloadDecoded = decodedDeathsDownload.decode('utf-8')

    readDeathsCsv = csv.reader(decodedDeathsDownloadDecoded.splitlines(),delimiter=',')
    deathsCsvList = list(readDeathsCsv)

    for row in deathsCsvList:
        if row[1] == 'New Zealand':
            deathsYAxisString = row[4:]
            deathsYAxisInt = []
            for numDeathsCases in deathsYAxisString:
                deathsYAxisInt.append(int(numDeathsCases))



    plt.plot(xAxis,confirmedYInt, color = 'green', label = "Confirmed")
    plt.plot(xAxis,recoveryYAxisInt, color='purple' ,label = "Recovered")
    plt.plot(xAxis,deathsYAxisInt, color = 'red', label = "Deaths")
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