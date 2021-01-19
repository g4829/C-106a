import csv
import numpy

def getDataSource(data_path):
    student_marks=[]
    days_present=[]
    
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            student_marks.apend(float(row["Marks In Percentage"]))
            days_present.apend(float(row["\t Days Present"]))
    
    return {"x": student_marks,"y": days_present}

def findCorrelation(datasource):
     correlation = np.corrcoef(datasource["x"], datasource["y"])
     print("Correlation between Marks In Percentage and Days Present :- \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource) 
    
setup()