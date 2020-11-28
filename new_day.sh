#! /bin/bash

DAY=$1

echo "Creating Boilerplate for day ${DAY}"

# python

PYTHON_ROOT=python/src/day${DAY}
PYTHON_TEST_ROOT=python/test/day${DAY}

cp -r python/src/template $PYTHON_ROOT

cp -r python/test/template $PYTHON_TEST_ROOT

# go

GOROOT=golang/day${DAY}

cp -r golang/template golang/day${DAY}

mv golang/day${DAY}/example.go ${GOROOT}/day${DAY}.go
mv golang/day${DAY}/example_test.go ${GOROOT}/day${DAY}_test.go

# copy input

INPUT_URL="https://adventofcode.com/2020/day/${DAY}/input"
TEMP_INPUT="temp-input.txt"

# curl "${INPUT_URL}" -H "cookie: session=${AOC_COOKIE}" -o "${TEMP_INPUT}" 2>/dev/null

cp ${TEMP_INPUT} ${GOROOT}/input.txt
cp ${TEMP_INPUT} ${PYTHON_TEST_ROOT}/input.txt

# clean up

rm ${TEMP_INPUT}