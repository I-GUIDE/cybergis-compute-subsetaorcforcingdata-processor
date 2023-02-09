#!/bin/env python3

import yaml
import os
import glob

# check to see if a shapefile is provided, if so, skip the huc12_id option
if 'data_folder' in os.environ:
    # find a shapefile in there, if there are more than one ignore
    glob_pattern = '%s/*.shp' % os.environ['data_folder']
    shapefiles = glob.glob(glob_pattern)
    
# get extents from the CUAHSI subsetter job results
subsetter_jobid = os.environ['param_Domain_Path']
subsetter_result_path = '/compute_shared/%s' % subsetter_jobid
# find a subset text file which has the subsetting command and extents
glob_pattern = '%s/script_forcing_subset.txt' % subsetter_result_path
subset_script_files = glob.glob(glob_pattern)

extents = None
if len(subset_script_files) == 1:
    with open(subset_script_files[0],'r') as script_file:
        for line in script_file:
            if line.startswith('ncks'):
                m = re.search(r'(?<=west_east,)\d+\,\d+', line)
                if m:
                    west_east = m.group(0)
                    m = re.search(r'(?<=south_north,)\d+\,\d+', line)
                    if m:
                        south_north = m.group(0)
                        extents = '%s,%s' % (m1,m2)

if len(shapefiles) == 1:
    processor_dict = {'$1': {'SubsetAORCForcingData': 
                                  {'shapefile': shapefiles[0],
                                   'start_date': os.environ['param_start_date'], 
                                   'end_date': os.environ['param_end_date'],
                                   'version': '1.0',
                                   'gsl': 'True',
                                   'aorc_datapath':'/compute_shared/AORC_Forcing'}}}
elif extents is not None:
    processor_dict = {'$1': {'SubsetAORCForcingData': 
                                  {'start_date': os.environ['param_start_date'], 
                                   'end_date': os.environ['param_end_date'],
                                   'extents': extents,
                                   'version': '1.0',
                                   'gsl': 'True',
                                   'aorc_datapath':'/compute_shared/AORC_Forcing'}}}
else:
    processor_dict = {'$1': {'SubsetAORCForcingData': 
                                  {'huc12_id': os.environ['param_huc12_id'], 
                                   'start_date': os.environ['param_start_date'], 
                                   'end_date': os.environ['param_end_date'], 
                                   'version': '1.0',
                                   'gsl': 'True',
                                   'aorc_datapath':'/compute_shared/AORC_Forcing'}}}

with open('/job/executable/subsetaorcforcingdata.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
