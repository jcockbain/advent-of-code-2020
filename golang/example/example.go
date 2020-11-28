package example

import (
	"aoc2020/input"
)

// Part1 returns sum on ints
func Part1(filename string) int {
	nums := input.ReadNumbers(filename)
	sum := 0 
	for _, i := range(nums){
		sum += i
	}
	return sum
}