#!/bin/bash

if [[ "${param_Retrieve_Output}" = "False" ]]; then
  mkdir /compute_scratch/${job_id}

  cd ${result_folder}

  mv *LDASIN* /compute_scratch/${job_id}/
fi
