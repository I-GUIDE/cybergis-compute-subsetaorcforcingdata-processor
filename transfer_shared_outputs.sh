#!/bin/bash

mkdir /compute_shared/${job_id}

cd ${result_folder}

mv *LDASIN* /compute_shared/${job_id}/
