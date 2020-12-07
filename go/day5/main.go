package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"sort"
	"strconv"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	lines := input.ReadLines(filename)
	maxSeatId := 0
	for _, line := range lines {
		maxSeatId = max(maxSeatId, getSeatId(line))
	}
	return maxSeatId
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	seatIds := []int{}
	for _, line := range lines {
		seatIds = append(seatIds, getSeatId(line))
	}

	sort.Ints(seatIds)
	missing := seatIds[0]
	for _, id := range seatIds {
		missing ^= id
	}
	return missing
}

func getSeatId(code string) int {
	row, mask := 0, 64
	for _, r := range code[0:7] {
		if string(r) == "B" {
			row += mask
		}
		mask >>= 1
	}

	col, mask := 0, 4
	for _, r := range code[7:10] {
		if string(r) == "R" {
			col += mask
		}
		mask >>= 1

	}
	return (8 * row) + col
}

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func toInt(s string) int {
	i, err := strconv.Atoi(s)
	check(err)
	return i
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

