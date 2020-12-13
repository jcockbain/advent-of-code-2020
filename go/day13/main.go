package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	lines := input.ReadLines(filename)

	earliestTime := toInt(lines[0])
	buses := lines[1]

	shortestWait, currentBusId := int(^uint(0)>>1), 0

	for _, bus := range strings.Split(buses, ",") {
		if bus == "x" {
			continue
		}
		b := toInt(bus)
		wait := (((earliestTime / b) * b) + b - earliestTime)
		if wait < shortestWait {
			shortestWait = wait
			currentBusId = b
		}
	}
	return shortestWait * currentBusId
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)

	buses := strings.Split(lines[1], ",")
	runningProduct, earliestBus := 1, 0

	for idx, bus := range buses {
		if bus == "x" {
			continue
		}
		for (earliestBus+idx)%toInt(bus) != 0 {
			earliestBus += runningProduct
		}
		runningProduct *= toInt(bus)
	}
	return earliestBus
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func toInt(s string) int {
	i, err := strconv.Atoi(s)
	check(err)
	return i
}
