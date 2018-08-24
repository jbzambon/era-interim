# era-interim

Program to download ERA-Interim files and generate ROMS forcing files.  Requires account and settings in ~/.ecmwfapirc, see https://confluence.ecmwf.int/display/WEBAPI/Access+ECMWF+Public+Datasets for instructions.  

Requires Matlab arango packages...  
https://github.com/dcherian/tools/tree/master/ROMS/arango  
with modified roms_metadata.m script  

get_ecmwf_loop.py: downloads the ERA-Interim datasets  
d_ecmwf2roms_useast_jbz.m: converts ERA-Interim fields for ROMS forcing files  
roms_metadata.m: adds PAR data for ROMS forcing files, which aren't actually used but nice anyways.  See: https://www.myroms.org/forum/viewtopic.php?f=14&t=4959  

Joseph B. Zambon  
jbzambon@ncsu.edu  
21 August 2018  

