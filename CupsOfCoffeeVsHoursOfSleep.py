import csv
import numpy

def getDataSource(data_path):
    cup_of_coffees=[]
    hours_of_sleep=[]
    
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            cup_of_coffees.apend(float(row["Coffee in ml"]))
            hours_of_sleep.apend(float(row["\t sleep in hours"]))
    
    return {"x": cup_of_coffees,"y": hours_of_sleep}

def findCorrelation(datasource):
     correlation = np.corrcoef(datasource["x"], datasource["y"])
     print("Correlation between Coffee in ml and sleep in hours :- \n--->",correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource) 
    
setup()