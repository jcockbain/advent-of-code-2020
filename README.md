# 🎄 advent-of-code-2020 🎄

## Summary

Solutions to the Christmas themed Advent-of-Code challenges. 

My aim this year is to do as many as I can in Python, and then in Go. 

For now the repo contains a few things that I hope will save me repeating boring stuff each day.

## Running the code

How I run the code, works on my machine (until I start trying to solve the problems 🥴).

### Helpers

```bash
# creates dirs at go/day{day}, python/src/day{day}, python/test/day{day}
# from the templates in each of those repos
# then fetches input and sticks it where I want it (next to the solutions)
./helpers/new_day.sh 2020 {day}

# attempt to destroy anything created above ;)
./helpers/cleanup.sh {day}

# run all tests 
./helpers/test.sh

```

### Go

These need to be run from inside `/go`.

```golang
// get answers - from the days dir (e.g go/day1/)
go run main.go

// run tests - also from the dir of the day
go test

// run tests - run all tests recursively
go test ./...

```

### Python

I use a Miniconda Python env.
Setting up with the local module imports can be a bit awkward. 
This [answer](https://stackoverflow.com/questions/37006114/anaconda-permanently-include-external-packages-like-in-pythonpath) was helpful for me getting past pesky `ModuleNotFound` errors!


These commands should be able to run from anywhere inside the repo. 🤞

```python
# get answers
python python/src/day{day}/main.py

# run tests (individual day)
python python/test/day{day}/test_main.py

# run tests (whole suite)
pytest

```

## Days 

- Template

    - [Python](python/src/template)
    - [Go](go/template)

- [Day 1 - Report Repair](https://adventofcode.com/2020/day/1)

    - [Python](python/src/day1/main.py)
    - [Go](go/day1/main.go)

- [Day 2 - Password Philosophy](https://adventofcode.com/2020/day/2)

    - [Python](python/src/day2/main.py)
    - [Go](go/day2/main.go)

- [Day 3 - Toboggan Trajectory](https://adventofcode.com/2020/day/3)

    - [Python](python/src/day3/main.py)
    - [Go](go/day3/main.go)

- [Day 4 - Passport Processing](https://adventofcode.com/2020/day/4)

    - [Python](python/src/day4/main.py)
    - [Go](go/day4/main.go)

- [Day 5 - Binary Boarding](https://adventofcode.com/2020/day/5)

    - [Python](python/src/day5/main.py)