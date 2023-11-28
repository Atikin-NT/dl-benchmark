#!/bin/bash

. ./utils.sh

omz_downloader --output_dir working_dir_smoke --cache_dir cache_dir_smoke --name=googlenet-v1

result_file="results_benchmark_caffe.csv"
[ -f $result_file ] && rm $result_file
smoke_config_file="smoke_config_caffe.xml"
smoke_tests_count=$(grep -io '<Test>' "$smoke_config_file" | wc -l)

python3 ../../src/benchmark/inference_benchmark.py -r $result_file --executor_type host_machine -c $smoke_config_file
check_exit_code inference_benchmark
check_results_file $result_file $smoke_tests_count

exit $return_value
