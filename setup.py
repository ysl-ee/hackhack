from datetime import datetime
import os
import csv

def setup():
    mytime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    mypath = "./%s" % mytime
    os.mkdir(mypath)

    csvpath = os.path.join(mypath, "transcribed.csv")
    header = ['Word', 'start_time', 'end_time']
    
    with open(csvpath, 'w') as f:
        writer = csv.writer(f)

        writer.writerow(header)

    print(mypath)

setup()