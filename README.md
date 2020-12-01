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
# then fetches input and places in place for each repo
./helpers/new_day 2020 {day}

# attempt to destroy anything created above ;)
./helpers/cleanup.sh {day}

# run all tests 
./helpers/test.sh

```

### Go

These need to be run from inside `/go`.

```golang
// get answers - from the days dir (e.g go/day1/)
go run day{day}.go

// run tests - also from the dir of the day
go test

// run tests - run all tests recursively
go test ./...

```

### Python

I use Miniconda Python env.
Setting up with the local module imports can be a bit awakward. 
This [answer](https://stackoverflow.com/questions/37006114/anaconda-permanently-include-external-packages-like-in-pythonpath) was helpful for me getting past pesky `ModuleNotFound` errors!


These commands should be able to run from anywhere inside the repo. 🤞

```python
# get answers
python python/src/day{day}/solution.py

# run tests (individual day)
python python/test/day{day}/test_solution.py

# run tests (whole suite)
pytest

```

## Days 

- Template

    - [Python](python/src/template)
    - [Go](go/template)

- Day 1

    - [Python](python/src/day1/solution.py)
