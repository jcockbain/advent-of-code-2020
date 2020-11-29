#! /bin/bash

YEAR=$1
DAY=$2

echo "Creating Boilerplate for year ${YEAR} day ${DAY}"

# python

PYTHON_ROOT=python/src/day${DAY}
PYTHON_TEST_ROOT=python/test/day${DAY}

cp -TR python/src/template $PYTHON_ROOT
cp -TR python/test/template $PYTHON_TEST_ROOT

# go

GOROOT=go/day${DAY}

cp -TR golang/template golang/day${DAY}

mv {GOROOT}/example.go ${GOROOT}/day${DAY}.go
mv ${GOROOT}/example_test.go ${GOROOT}/day${DAY}_test.go

# copy input

INPUT_URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"
TEMP_INPUT="temp-input.txt"

curl "${INPUT_URL}" -H "cookie: session=${AOC_COOKIE}" -o "${TEMP_INPUT}" 2>/dev/null

cp ${TEMP_INPUT} ${GOROOT}/input.txt
cp ${TEMP_INPUT} ${PYTHON_ROOT}/input.txt

# clean up

rm ${TEMP_INPUT}