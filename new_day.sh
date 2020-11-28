#! /bin/bash

DAY=$1

# python

cp -r python/src/template python/src/day${DAY}

cp -r python/test/template python/test/day${DAY}

# go

cp -r golang/template golang/day${DAY}

mv golang/day${DAY}/example.go golang/day${DAY}/day${DAY}.go
mv golang/day${DAY}/example_test.go golang/day${DAY}/day${DAY}_test.go