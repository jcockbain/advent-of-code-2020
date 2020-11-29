# 🎄 advent-of-code-2020 🎄

## Summary

Solutions to the Christmas themed Advent-of-Code challenges. 

My aim this year is to do as many as I can in Python, and then in Go. 

For now the repo contains a few things that I hope will save me repeating boring stuff each day.

## Running the code

How I run the code, works on my machine!

### Helpers

This is the script I run each day to generate boilerplate.

```bash
# creates dirs at go/day{day}, python/src/day{day}, python/test/day{day}
# from the templates in each of those repos
# then fetches input and places into each of those dirs (e.g go/day{day}/input.txt)
./new_day 2020 {day}

```

### Go

```golang
// (from /go dir)

// get answers
go run day{day}/day{day}.go

// run tests (individual day)
go test day{day}

// run tests (whole suite)
go test ./...

```

### Python

```Python

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