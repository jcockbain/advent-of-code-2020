package main

import (	
	input "aoc2020/inpututils"

	"fmt"
	"errors"
)

func main(){
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))
	
	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

type set map[int]struct{}

func (s set) add(n int){
	s[n] = struct{}{}
}

func (s set) has(n int) bool{
	_, ok := s[n]
	return ok
}

func Part1(filename string) int {
	nums := input.ReadNumbers(filename)
	multiplied, err := twoSum(nums, 2020)
	if err != nil {
		return -1
	}
	return multiplied
}

func Part2(filename string) int {
	nums := input.ReadNumbers(filename)
	for i := 0; i < len(nums) - 2; i += 1 {
		num := nums[i]
		multiplier, err := twoSum(nums[i+1:], 2020 - num)
		if err == nil {
			return multiplier * num
		}
	}
	return -1
}

func twoSum(ints []int, target int) (int, error) {
	seen := set{}
	for _, i := range(ints){
		if seen.has(target - i){
			return (target - i) * i, nil
		}
		seen.add(i)
	}
	return -1, errors.New("No solution")
}

func check(err error) {
	if err != nil {
		panic(err)	
	}
}