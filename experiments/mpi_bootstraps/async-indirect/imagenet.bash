#!/usr/bin/env bash

export DEVICE=${DEVICE}/r${OMPI_COMM_WORLD_RANK}
export OUTPUT_PATH=results/async-indirect
export OUTPUT_FILE=results/async-indirect/imagenet.json.r${OMPI_COMM_WORLD_RANK}

mkdir -p ${DEVICE}
mkdir -p ${OUTPUT_PATH}

echo ----Running async-indirect/imagenet[r${OMPI_COMM_WORLD_RANK}]
${FIO:=fio} --output-format=json --output=${OUTPUT_FILE} experiments/async-indirect/imagenet.fio
echo ----Done async-indirect/imagenet[r${OMPI_COMM_WORLD_RANK}]
