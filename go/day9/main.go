package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"strconv"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt", 25))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt", 25))
}

func Part1(filename string, preamble int) int {
	nums := input.ReadNumbers(filename)
	for i := preamble; i < len(nums); i++ {
		if !canSum(nums[i-preamble:i], nums[i]) {
			return nums[i]
		}
	}
	return -1
}

func canSum(ints []int, target int) bool {
	seen := map[int]struct{}{}
	for _, i := range ints {
		if _, ok := seen[target-i]; ok {
			return true
		}
		seen[i] = struct{}{}
	}
	return false
}

func Part2(filename string, preamble int) int {
	n := Part1(filename, preamble)
	ints := input.ReadNumbers(filename)
	start, end := contiguousSumEquals(n, ints)
	if start == -1 {
		return -1
	}
	return min(ints[start:end]) + max(ints[start:end])
}

func contiguousSumEquals(target int, ints []int) (int, int) {
	currSum, start := 0, 0

	for end, val := range ints {
		currSum += val
		for currSum > target {
			currSum -= ints[start]
			start += 1
		}
		if currSum == target {
			return start, end
		}
	}
	return -1, -1
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

func min(a []int) int {
	m := a[0]
	for _, v := range a {
		if v < m {
			m = v
		}
	}
	return m
}

func max(a []int) int {
	m := a[0]
	for _, v := range a {
		if v > m {
			m = v
		}
	}
	return m
}
