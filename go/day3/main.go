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

type treeCounter struct {
	lines []string
	h, w int
}

func newTreeCounter(lines []string) treeCounter {
	return treeCounter {
		lines: lines,
		w: len(lines[0]),
		h: len(lines),
	}
} 

func (tc treeCounter) count (dx int, dy int) int {
	x, y, trees := 0, 0, 0
	for y < tc.h {
		if string(tc.lines[y][x % tc.w]) == "#" {
			trees += 1
		}
		x += dx
		y += dy
	}
	return trees
}

func Part1(filename string) int {
	lines := input.ReadLines(filename)
	tc := newTreeCounter(lines)
	return tc.count(3, 1)
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	tc := newTreeCounter(lines)
	return tc.count(1, 1) * tc.count(3, 1) * tc.count(5, 1) * tc.count(7, 1) * tc.count(1, 2)
}