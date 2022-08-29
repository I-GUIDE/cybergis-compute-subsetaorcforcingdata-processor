#!/bin/bash

mkdir /compute_shared/${job_id}

cd ${result_folder}

cp *LDASIN* /compute_shared/${job_id}/
