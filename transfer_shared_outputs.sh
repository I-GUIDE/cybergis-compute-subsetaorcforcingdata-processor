#!/bin/bash

mkdir /compute_scratch/${job_id}

cd ${result_folder}

mv *LDASIN* /compute_scratch/${job_id}/
