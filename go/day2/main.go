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
		min, max, letter, pword := getParts(line)		
		letterCount := strings.Count(pword, letter)
		if min <= letterCount && letterCount <= max {
			validPasswords += 1
		}
	}
	return validPasswords
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	validPasswords := 0
	for _, line := range(lines){
		pos1, pos2, letter, pword := getParts(line)
		if (string(pword[pos1 - 1]) == letter) != (string(pword[pos2 - 1]) == letter) {
			validPasswords += 1
		}
	}
	return validPasswords
}

func getParts(line string) (int, int, string, string) {
	re := regexp.MustCompile(`(\d+)-(\d+) ([a-z]): ([a-z]+)`)
	parts := re.FindStringSubmatch(line)
	return toInt(parts[1]), toInt(parts[2]), parts[3], parts[4]
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