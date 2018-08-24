# get_ecmwf_loop.py
# 
# Program to download ERA-Interim data to generate ROMS forcing files.
#
# Joseph B. Zambon
# jbzambon@ncsu.edu
# 19 August 2018

# ! conda install -y -c conda-forge ecmwf-api-client 

from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

dest_dir = '/raid0/datasets/hindcast/ecmwf/era-interim/attempt3/'
syyyy=1979; eyyyy=2017;

def get_ecmwf(yyyy,dest_dir):
    dateline = str(str(yyyy) + "-01-01/to/" + str(yyyy) + "-12-31")
    target = str(dest_dir + "useast_ecmwf_" + str(yyyy) + ".nc")
    print(dateline, target)
    server = ECMWFDataServer()
    server.retrieve({
                    "class": "ei",
                    "dataset": "interim",
                    "date": dateline,
                    "expver": "1",
                    "grid": "0.125/0.125",
                    "levtype": "sfc",
                    "param": "58.128/146.128/147.128/151.128/164.128/165.128/166.128/167.128/168.128/175.128/176.128/177.128/180.128/181.128/182.128/195.128/196.128/205.128/228.128",
                    "step": "3/6/9/12",
                    "stream": "oper",
                    "time": "00:00:00/12:00:00",
                    "type": "fc",
                    'area': "48/260/7/301",
                    'format': "netcdf",
                    "target": target,
                    })

for yyyy in range (syyyy,eyyyy+1):
    dateline = str(str(yyyy) + "-01-01/to/" + str(yyyy) + "-12-31")
    target = str(dest_dir + "useast_ecmwf_" + str(yyyy) + ".nc")
    get_ecmwf(yyyy,dest_dir)


