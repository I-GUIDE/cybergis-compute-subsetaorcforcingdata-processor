#!/bin/env python3

import yaml
import os
import glob

# check to see if a shapefile is provided, if so, skip the huc12_id option
if 'data_folder' in os.environ:
    # find a shapefile in there, if there are more than one ignore
    glob_pattern = '%s/*.shp' % os.environ['data_folder']
    shapefiles = glob.glob(glob_pattern)

if len(shapefiles) == 1:
    processor_dict = {'$1': {'SubsetAORCForcingData': 
                                  {'shapefile': shapefiles[0],
                                   'start_date': os.environ['param_start_date'], 
                                   'end_date': os.environ['param_end_date'], 
                                   'version': os.environ['param_version'],
                                   'gsl': os.environ['param_gsl'],
                                   'aorc_datapath':'/compute_shared/AORC_Forcing'}}}
else:
    processor_dict = {'$1': {'SubsetAORCForcingData': 
                                  {'huc12_id': os.environ['param_huc12_id'], 
                                   'start_date': os.environ['param_start_date'], 
                                   'end_date': os.environ['param_end_date'], 
                                   'version': os.environ['param_version'],
                                   'gsl': os.environ['param_gsl'],
                                   'aorc_datapath':'/compute_shared/AORC_Forcing'}}}

with open('/job/executable/subsetaorcforcingdata.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
