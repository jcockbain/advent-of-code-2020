package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"strconv"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	lines := input.ReadLines(filename)

	direction, x, y := 90, 0, 0
	for _, l := range lines {
		d, v := string(l[0]), toInt(l[1:])

		if d == "R" {
			direction = (direction + v) % 360
		}
		if d == "L" {
			// add 360 to stop becoming negative
			direction = (direction + 360 - v) % 360
		}
		if d == "N" {
			y += v
		}
		if d == "E" {
			x += v
		}
		if d == "S" {
			y -= v
		}
		if d == "W" {
			x -= v
		}
		if d == "F" {
			if direction == 90 {
				x += v
			}
			if direction == 180 {
				y -= v
			}
			if direction == 270 {
				x -= v
			}
			if direction == 0 {
				y += v
			}
		}
	}

	return abs(x) + abs(y)
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)

	wx, wy := 10, 1
	sx, sy := 0, 0

	for _, l := range lines {
		d, v := string(l[0]), toInt(l[1:])

		if d == "R" {
			wx, wy = rotateCoords(wx, wy, v)
		}
		if d == "L" {
			// add 360 to stop becoming negative
			wx, wy = rotateCoords(wx, wy, 360-v)
		}
		if d == "N" {
			wy += v
		}
		if d == "E" {
			wx += v
		}
		if d == "S" {
			wy -= v
		}
		if d == "W" {
			wx -= v
		}
		if d == "F" {
			sx += wx * v
			sy += wy * v
		}
	}

	return abs(sx) + abs(sy)
}

func rotateCoords(x, y, r int) (int, int) {
	if r == 90 {
		return y, -x
	}
	if r == 180 {
		return -x, -y
	}
	if r == 270 {
		return -y, x
	}
	return x, y
}

func abs(x int) int {
	if x >= 0 {
		return x
	}
	return -1 * x
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
