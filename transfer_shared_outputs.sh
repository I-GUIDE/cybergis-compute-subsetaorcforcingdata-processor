#!/bin/bash

if [[ "${param_Retrieve_Output}" = "True" ]]; then

  mkdir /compute_shared/${job_id}/forcingdata

  cd ${result_folder}

  mv *LDASIN* /compute_shared/${job_id}/forcingdata
else
  mkdir /compute_scratch/${job_id}

  cd ${result_folder}

  mv *LDASIN* /compute_scratch/${job_id}/
fi  
