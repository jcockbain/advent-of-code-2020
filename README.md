# 🎄 advent-of-code-2020 🎄

![Go Solutions](https://github.com/jcockbain/advent-of-code-2020/workflows/Go/badge.svg)

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

- [Day 9 - Encoding Error](https://adventofcode.com/2020/day/9)

    - [Python](python/src/day9/main.py)
    - [Go](go/day9/main.go)

- [Day 10 - Adapter Array](https://adventofcode.com/2020/day/10)

    - [Python](python/src/day10/main.py)
    - [Go](go/day10/main.go)

- [Day 11 - Seating System](https://adventofcode.com/2020/day/11)

    - [Python](python/src/day11/main.py)
    - [Go](go/day11/main.go)

- [Day 12 - Rain Risk](https://adventofcode.com/2020/day/12)

    - [Python](python/src/day12/main.py)
    - [Go](go/day12/main.go)

- [Day 13 - Shuttle Search](https://adventofcode.com/2020/day/13)

    - [Python](python/src/day13/main.py)
    - [Go](go/day13/main.go)

- [Day 14 - Docking Data](https://adventofcode.com/2020/day/14)

    - [Python](python/src/day14/main.py)
    - [Go](go/day14/main.go)

- [Day 15 - Rambunctious Recitation](https://adventofcode.com/2020/day/15)

    - [Python](python/src/day15/main.py)
    - [Go](go/day15/main.go)

- [Day 16 - Ticket Translation](https://adventofcode.com/2020/day/16)

   - [Python](python/src/day16/main.py)

- [Day 17 - Conway Cubes](https://adventofcode.com/2020/day/17)

   - [Python](python/src/day17/main.py)

- [Day 18 - Operation Order](https://adventofcode.com/2020/day/18)

   - [Python](python/src/day18/main.py)

- [Day 19 - Monster Messages](https://adventofcode.com/2020/day/19)

    - [Python](python/src/day19/main.py)

- [Day 20 - Jurassic Jigsaw](https://adventofcode.com/2020/day/20)

   - [Python](python/src/day20/main.py)

- [Day 21 - Allergen Assessment](https://adventofcode.com/2020/day/21)

   - [Python](python/src/day21/main.py)

- [Day 22 - Crab Combat](https://adventofcode.com/2020/day/22)

   - [Python](python/src/day22/main.py)

- [Day 23 - Crab Cups](https://adventofcode.com/2020/day/23)

   - [Python](python/src/day23/main.py)

- [Day 24 - Lobby Layout](https://adventofcode.com/2020/day/24)

   - [Python](python/src/day24/main.py)
