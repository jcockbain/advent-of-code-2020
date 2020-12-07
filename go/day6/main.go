package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"strings"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	lines := input.ReadRaw(filename)
	splitLines := strings.Split(lines, "\n\n")
	sum := 0
	for _, line := range splitLines {
		allLetters := strings.ReplaceAll(line, "\n", "")
		sum += countDistinctLetters(allLetters)
	}
	return sum
}

func Part2(filename string) int {
	lines := input.ReadRaw(filename)
	splitLines := strings.Split(lines, "\n\n")
	sum := 0
	for _, line := range splitLines {
		strings := strings.Split(line, "\n")
		sum += countCommonLetters(strings)
	}
	return sum
}

func countDistinctLetters(s string) int {
	seen := set{}
	for _, c := range s {
		seen.add(int(c))
	}
	return seen.len()
}

func countCommonLetters(strings []string) int {
	seen := set{}
	for _, c := range strings[0] {
		seen.add(int(c))
	}
	for _, a := range strings[1:] {
		for key, _ := range seen {
			if !in(stringToIntArray(a), key) {
				seen.delete(key)
			}
		}
	}
	return seen.len()
}

// create set type as Go doesn't have one
type set map[int]struct{}

func (s set) add(n int) {
	s[n] = struct{}{}
}

func (s set) has(n int) bool {
	_, ok := s[n]
	return ok
}

func (s set) delete(n int) {
	_, ok := s[n]
	if ok {
		delete(s, n)
	}
}

func (s set) len() int {
	var l int
	for _, _ = range s {
		l += 1
	}
	return l
}

func stringToIntArray(s string) []int {
	vsm := make([]int, len(s))
	for i, v := range s {
		vsm[i] = int(v)
	}
	return vsm
}

func in(a []int, e int) bool {
	for _, i := range a {
		if i == e {
			return true
		}
	}
	return false
}

