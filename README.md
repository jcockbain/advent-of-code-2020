# 🎄 advent-of-code-2020 🎄

## Summary

Solutions to the Christmas themed Advent-of-Code challenges. 

My aim this year is to do as many as I can in Python, and then in Go. 

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
    - [Go](go/day5/main.go)

- [Day 6 - Custom Customs](https://adventofcode.com/2020/day/6)

    - [Python](python/src/day6/main.py)
    - [Go](go/day6/main.go)

- [Day 7 - Handy Haversacks](https://adventofcode.com/2020/day/7)

    - [Python](python/src/day7/main.py)
    - [Go](go/day7/main.go)

- [Day 8 - Handheld Halting](https://adventofcode.com/2020/day/8)

    - [Python](python/src/day8/main.py)
    - [Go](go/day8/main.go)

- [Day 8 - Encoding Error](https://adventofcode.com/2020/day/9)

    - [Python](python/src/day9/main.py)
