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
	_, acc := runCode(lines)
	return acc
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	
	for i, line := range(lines){
		split := strings.Split(line, " ")
		code, val := split[0], split[1]
		copy := copySlice(lines)

		if code == "nop" {
			newSlice := append(append(copy[:i], fmt.Sprintf("%s %s", "jmp", val)), copy[i+1:]...)
			completed, acc := runCode(newSlice)
			if completed {
				return acc
			}
		}
		
		if code == "jmp" {
			newSlice := append(append(copy[:i], fmt.Sprintf("%s %s", "nop", val)), copy[i+1:]...)
			completed, acc := runCode(newSlice)
			if completed {
				return acc
			}
		}

	}
	return -1
}

func runCode(lines []string) (bool, int) {
	acc, idx := 0, 0
	visited := map[int]bool{}

	for idx < len(lines) && !visited[idx] {
		visited[idx] = true

		split := strings.Split(lines[idx], " ")
		code, val := split[0], split[1]

		if code == "acc" {
			acc += getValueFromString(val)
			idx += 1
		} else if code == "jmp" {
			idx += getValueFromString(val)
		} else if code == "nop" {
			idx += 1
		}
	
	}
	return idx >= len(lines), acc
}

func copySlice(a []string) []string{
	return append(a[:0:0], a...)
}

func getValueFromString(s string) int {
	if string(s[0]) == "-" {
		return -1 * toInt(s[1:])
	}
	return toInt(s[1:])
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
