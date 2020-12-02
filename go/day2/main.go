package main

import (	
	input "aoc2020/inpututils"

	"fmt"
)

func main(){
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))
	
	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}


func Part1(filename string) int {
	nums := input.ReadNumbers(filename)
	sum := 0 
	for _, i := range(nums){
		sum += i
	}
	return sum
}

func Part2(filename string) string {
	return filename
}

func check(err error) {
	if err != nil {
		panic(err)	
	}
}