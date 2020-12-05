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
	var validPassports int
	passports := createPassports(filename)

	for _, p := range passports {
		if p.validatePart1() {
			validPassports += 1
		}
	}

	return validPassports
}

func Part2(filename string) int {
	var validPassports int
	passports := createPassports(filename)

	for _, p := range passports {
		if p.validatePart2() {
			validPassports += 1
		}
	}
	return validPassports
}

type passport map[string]string

func createPassports(filename string) []passport {
	lines := input.ReadRaw(filename)
	data := strings.Split(lines, "\n\n")
	passports := []passport{}
	for _, d := range data {
		splitBySpaces := strings.ReplaceAll(d, "\n", " ")
		p := passport{}
		for _, f := range strings.Split(splitBySpaces, " ") {
			pair := strings.SplitN(f, ":", 2)
			if len(pair) == 2 {
				p[pair[0]] = pair[1]
			}
		}
		passports = append(passports, p)
	}
	return passports
}

func (p passport) validatePart1() bool {
	requiredFields := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, required := range requiredFields {
		_, found := p[required]
		if !found {
			return false
		}
	}
	return true
}

func (p passport) validatePart2() bool {
	if !p.isValidByr() {
		return false
	}
	if !p.isValidIyr() {
		return false
	}
	if !p.isValidEyr() {
		return false
	}
	if !p.isValidHgt() {
		return false
	}
	if !p.isValidHcl() {
		return false
	}
	if !p.isValidEcl() {
		return false
	}
	if !p.isValidPid() {
		return false
	}
	return true
}

func (p passport) isValidByr() bool {
	if p["byr"] == "" {
		return false
	}
	n := toInt(p["byr"])
	return 1920 <= n && n <= 2002
}

func (p passport) isValidIyr() bool {
	if p["iyr"] == "" {
		return false
	}
	n := toInt(p["iyr"])
	return 2010 <= n && n <= 2020
}

func (p passport) isValidEyr() bool {
	if p["eyr"] == "" {
		return false
	}
	n := toInt(p["eyr"])
	return 2020 <= n && n <= 2030
}

func (p passport) isValidHgt() bool {
	if p["hgt"] == "" {
		return false
	}
	re := regexp.MustCompile(`(\d+)([a-z]+)`)
	parts := re.FindStringSubmatch(p["hgt"])
	if len(parts) != 3 {
		return false
	}
	n, units := toInt(parts[1]), parts[2]
	if units == "in" {
		return 59 <= n && 76 >= n
	}
	if units == "cm" {
		return 150 <= n && n <= 193
	}
	return false
}

func (p passport) isValidHcl() bool {
	if p["hcl"] == "" {
		return false
	}
	re := regexp.MustCompile(`#[a-f\d]{6}`)
	return re.MatchString(p["hcl"])
}

func (p passport) isValidEcl() bool {
	if p["ecl"] == "" {
		return false
	}
	cols := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	for _, c := range cols {
		if c == p["ecl"] {
			return true
		}
	}
	return false
}

func (p passport) isValidPid() bool {
	if p["pid"] == "" {
		return false
	}
	re := regexp.MustCompile(`\d{9}`)
	return re.MatchString(p["pid"])
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
