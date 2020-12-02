package main

import (	
	input "aoc2020/inpututils"

	"fmt"
	"regexp"
	"strings"
	"strconv"
)

func main(){
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))
	
	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}


func Part1(filename string) int {
	lines := input.ReadLines(filename)
	validPasswords := 0
	for _, line := range(lines){
		re := regexp.MustCompile(`(\d+)-(\d+) ([a-z]): ([a-z]+)`)
		parts := re.FindStringSubmatch(line)
		min, max, letter, pword := parts[1], parts[2], parts[3], parts[4]
		letterCount := strings.Count(pword, letter)
		if toInt(min) <= letterCount && letterCount <= toInt(max) {
			validPasswords += 1
		}
	}
	return validPasswords
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	validPasswords := 0
	for _, line := range(lines){
		re := regexp.MustCompile(`(\d+)-(\d+) ([a-z]): ([a-z]+)`)
		parts := re.FindStringSubmatch(line)
		pos1, pos2, letter, pword := parts[1], parts[2], parts[3], parts[4]
		
		// XOR - for booleans equivalent to !=
		X := string(pword[toInt(pos1) - 1]) == letter
		Y := string(pword[toInt(pos2) - 1]) == letter
		if X != Y {
			validPasswords += 1
		}
	}
	return validPasswords
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