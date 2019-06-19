#! /usr/bin/env python -u
# coding=utf-8

__author__ = 'Sayed Hadi Hashemi'

total_size = "256g"
global_configurations = {
    "directory": "${DEVICE}",
    "filename": "data.bin",
    "thread": "1",
    "time_based": "1",
    "runtime": "30s",
    "invalidate": "1",
    "filesize": "256g",
    "fadvise_hint": "1",
    "ramp_time": "5",
    "disk_util": "1",
    "bssplit": "128k/1",
    "rw": "randread"
}

sync_configurations = {
    "ioengine": "sync",
    "group_reporting": "1",
    "thread": "1",
    "norandommap": 1,
    "numjobs": 1,
    "direct": 1
}

async_configurations = {
    "ioengine": "libaio",
    "direct": 1,
    "iodepth": 1
}

depths = [1, 8, 32, 128]
sizes = [64, 256, 1024, 4096, 32768, 262144, 2 ** 32]
apis = ["sync", "async", "sync-direct", "async-indirect"]

sequence_sizes = [1, 32, 256]

run_all_script_path = "experiments/run-all.bash"
run_mpi_script_path = "experiments/run-mpi.bash"

mpi_bootstrap_script_body = """
export DEVICE=${{DEVICE}}/r${{OMPI_COMM_WORLD_RANK}}
export OUTPUT_PATH=mpi_results/r${{OMPI_COMM_WORLD_RANK}}/{result_path}
export OUTPUT_FILE=mpi_results/r${{OMPI_COMM_WORLD_RANK}}/{result_file_name}

mkdir -p ${{DEVICE}}
mkdir -p ${{OUTPUT_PATH}}

${{FIO:=fio}} --output-format=json --output=${{OUTPUT_FILE}} {test_file_name}
"""

run_all_script_body = """
echo
echo Running {test_name}
mkdir -p {result_path}
${{FIO:=fio}} --output-format=json --output={result_file_name} {test_file_name}
"""
