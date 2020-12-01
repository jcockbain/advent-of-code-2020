#! /bin/bash

YEAR=$1
DAY=$2

echo "Creating Boilerplate for year ${YEAR} day ${DAY}"

# python

PYTHON_ROOT=python/src/day${DAY}
PYTHON_TEST_ROOT=python/test/day${DAY}

cp -n -TR python/src/template $PYTHON_ROOT
cp -n -TR python/test/template $PYTHON_TEST_ROOT

# go

GOROOT=go/day${DAY}
cp -n -TR go/template go/day${DAY}

# copy input

INPUT_URL="https://adventofcode.com/${YEAR}/day/${DAY}/input"
TEMP_INPUT="temp-input.txt"

# "session cookie" must be given as input is per-user...
# this can be grabbed from the URL of any input page online e.g https://adventofcode.com/2019/day/2/input
# I have this set as an environment variable here

curl "${INPUT_URL}" -H "cookie: session=${AOC_COOKIE}" -o "${TEMP_INPUT}" 2>/dev/null

cp ${TEMP_INPUT} ${GOROOT}/input.txt
cp ${TEMP_INPUT} ${PYTHON_ROOT}/input.txt

# clean up

rm ${TEMP_INPUT}