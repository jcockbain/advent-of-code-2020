package main

import (
	"fmt"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1([]int{7, 14, 0, 17, 11, 1, 2}))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2([]int{7, 14, 0, 17, 11, 1, 2}))
}

func Part1(nums []int) int {
	return playGame(nums, 2020)
}

func Part2(nums []int) int {
	return playGame(nums, 30000000)
}

func playGame(nums []int, turns int) int {
	a := make([]int, turns)
	seen := make(map[int]int)

	for i, n := range nums {
		a[i] = n
		seen[n] = i
	}

	for n := len(nums); n < turns-1; n++ {
		if m, ok := seen[a[n]]; ok {
			a[n+1] = n - m
		}
		seen[a[n]] = n
	}

	return a[turns-1]
}
