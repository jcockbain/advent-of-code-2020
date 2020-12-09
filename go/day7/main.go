package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"regexp"
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
	bags := CreateGraph(lines)

	var goldBagInside func(string)bool

	goldBagInside = func(startBag string) bool{
		if contents, bagExists := bags[startBag]; !bagExists || len(contents) == 0 {
			return false
		}
		if startBag == "shiny gold bag"{
			return true
		}
		contents := bags[startBag]
		for _, b := range contents {
			if goldBagInside(b.name){
				return true
			}
		}
		return false
	}

	var s int
	for bag, _ := range(bags) {
		if bag != "shiny gold bag" && goldBagInside(bag){
			s += 1
		}
	}
	return s
}

func Part2(filename string) int {
	lines := input.ReadLines(filename)
	graph := CreateGraph(lines)

	var countBags func(string) int
	
	countBags = func(bag string) int {
		if contents, bagExists := graph[bag]; !bagExists || len(contents) == 0 {
			return 0
		}
		contents, s := graph[bag], 0
		for _, b := range(contents){
			s += b.num + (b.num * countBags(b.name))
		}
		return s
	}
	return countBags("shiny gold bag")
}

func CreateGraph(lines []string) map[string][]innerBag {
	bags := map[string][]innerBag{}
	for _, line := range lines {
		splittedString := strings.Split(line, "contain")
		outerBag, innerBags := splittedString[0], splittedString[1]
		outerBag = strings.TrimSpace(outerBag)
		outerBag = strings.TrimRight(outerBag, "s")
		bags[outerBag] = []innerBag{}
		if innerBags != "no other bags." {
			innerBags = strings.TrimRight(innerBags, ".")
			splitBags := strings.Split(innerBags, ",")
			for _, bag := range splitBags {
				bag = strings.TrimRight(bag, "s")
				re := regexp.MustCompile(`(\d+) (\S+.*)`)
				parts := re.FindStringSubmatch(bag)
				if len(parts) == 3 {
					num, bagName := toInt(parts[1]), parts[2]
					bags[outerBag] = append(bags[outerBag], innerBag{bagName, num})
				}
			}
		}
	}
	return bags
}

type innerBag struct {
	name string
	num  int
}

func sum(arr []int) int {
	var s int
	for _, a := range arr {
		s += a
	}
	return s
}

func toInt(s string) int {
	i, err := strconv.Atoi(s)
	check(err)
	return i
}

func check(err error) {
	if err != nil {
		panic(err)
	}
} 
