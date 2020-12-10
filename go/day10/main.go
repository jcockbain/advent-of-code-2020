package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"sort"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	nums := input.ReadNumbers(filename)
	sort.Ints(nums)

	ones, threes, v := 0, 0, 0

	for _, x := range nums {
		if (x - v) == 1 {
			ones += 1
		} else if (x - v) == 3 {
			threes += 1
		}
		v = x
	}
	return ones * (threes + 1)
}

func Part2(filename string) int {
	nums := input.ReadNumbers(filename)

	numSet := map[int]struct{}{}
	for _, n := range nums {
		numSet[n] = struct{}{}
	}

	maxV := max(nums)
	cache := make([]int, maxV)
	for i := range cache {
		cache[i] = -1
	}

	var numberOfWays func(int) int

	numberOfWays = func(v int) int {
		if _, ok := numSet[v]; !ok {
			return 0
		}
		if v == maxV {
			return 1
		}
		if cache[v] == -1 {
			s := 0
			for _, x := range []int{1, 2, 3} {
				s += numberOfWays(v + x)
			}
			cache[v] = s
		}
		return cache[v]
	}
	return numberOfWays(1) + numberOfWays(2) + numberOfWays(3)
}

func max(s []int) int {
	m := s[0]
	for _, v := range s {
		if v > m {
			m = v
		}
	}
	return m
}
