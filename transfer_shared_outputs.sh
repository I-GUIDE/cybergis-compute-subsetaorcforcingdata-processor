#!/bin/bash

if [[ "${param_Standalone}" = "True" ]]; then
  mkdir /compute_shared/${job_id}

  cd ${result_folder}

  mv *LDASIN* /compute_shared/${job_id}/
else
  mkdir /compute_scratch/${job_id}

  cd ${result_folder}

  mv *LDASIN* /compute_scratch/${job_id}/
fi
