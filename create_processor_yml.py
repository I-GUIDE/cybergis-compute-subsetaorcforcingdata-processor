#!/bin/env python3

import yaml
import os

processor_dict = {'$1': {'SubsetAORCForcingData': 
                              {'huc12_id': os.environ['param_huc12_id'], 
                               'start_date': os.environ['param_start_date'], 
                               'end_date': os.environ['param_end_date'], 
                               'aorc_datapath':'/compute_shared/AORC_Forcing'}}}

with open('/job/executable/subsetaorcforcingdata.yml','w') as procfile:
    yaml.dump(processor_dict,procfile)
