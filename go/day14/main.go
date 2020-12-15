package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"regexp"
	"strconv"
	"strings"
)

var (
	bits = 36
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	lines := input.ReadLines(filename)
	memory := make(map[int]int)
	mask := ""

	for _, line := range lines {
		splitted := strings.Split(line, "=")
		key, val := strings.TrimSpace(splitted[0]), strings.TrimSpace(splitted[1])

		if key == "mask" {
			mask = val
			continue
		}

		r := regexp.MustCompile(`mem\[(\d+)]`)
		address := toInt(r.FindStringSubmatch(key)[1])

		binaryVal := parseBinaryStringFromDecimalString(val)
		paddedBinaryVal := leftPadString(binaryVal, bits)
		binarySlice := strings.Split(paddedBinaryVal, "")

		for idx, c := range mask {
			if string(c) != "X" {
				binarySlice[idx] = string(c)
			}
		}

		memory[address] = parseDecimalFromBinarySlice(binarySlice)
	}

	return sumVals(memory)
}

func Part2(filename string) int {
	return 12
}

func leftPadString(s string, n int) string {
	return fmt.Sprintf("%0*s", n, s)
}

func parseBinaryStringFromDecimalString(i string) string {
	decimal, _ := strconv.ParseInt(i, 10, 64)
	return strconv.FormatInt(decimal, 2)
}

func parseDecimalFromBinarySlice(b []string) int {
	i, _ := strconv.ParseInt(strings.Join(b, ""), 2, 64)
	return int(i)
}

func sumVals(m map[int]int) int {
	s := 0
	for _, val := range m {
		s += val
	}
	return s
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