package main

import (
	input "aoc2020/inpututils"

	"fmt"
	"strconv"
	"strings"
)

const (
	emptySeat    rune = 'L'
	occupiedSeat rune = '#'
	path         rune = '.'
)

var (
	directions = []pos{pos{-1, -1}, pos{-1, 0}, pos{-1, 1}, pos{0, -1}, pos{0, 1}, pos{1, -1}, pos{1, 0}, pos{1, 1}}
)

type pos struct {
	r, c int
}

type tiles map[pos]rune

type floor struct {
	tiles         tiles
	height, width int
}

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("test1.txt"))

	fmt.Println("--- Part Two ---")
	fmt.Println(Part2("input.txt"))
}

func Part1(filename string) int {
	floorString := input.ReadRaw(filename)
	f := newFloor(floorString)
	changes := true
	for changes == true {
		f, changes = f.getNext()
	}
	return f.countOccupied()
}

func Part2(filename string) int {
	floorString := input.ReadRaw(filename)
	f := newFloor(floorString)
	changes := true
	for changes == true {
		f, changes = f.getNext2()
	}
	return f.countOccupied()
}

func newFloor(floorString string) floor {
	lines := strings.Split(floorString, "\n")

	t := tiles{}
	h := len(lines)
	w := len(lines[0])

	for r, s := range lines {
		for c, tile := range s {
			p := pos{r, c}
			t[p] = tile
		}
	}
	return floor{
		height: h,
		width:  w,
		tiles:  t,
	}
}

func (f floor) getNext() (floor, bool) {
	changes := false
	newFloor := floor{
		height: f.height,
		width:  f.width,
		tiles:  tiles{},
	}
	for r := 0; r < f.height; r++ {
		for c := 0; c < f.width; c++ {
			loc := pos{r, c}
			tile := f.tiles[loc]
			if tile == path {
				newFloor.tiles[loc] = tile
				continue
			}
			occupied := f.countOccupiedNeighbours(loc)
			switch {
			case tile == emptySeat && occupied == 0:
				newFloor.tiles[loc] = occupiedSeat
				changes = true
			case tile == occupiedSeat && occupied >= 4:
				newFloor.tiles[loc] = emptySeat
				changes = true
			default:
				newFloor.tiles[loc] = tile
			}
		}
	}
	return newFloor, changes
}

func (f floor) getNext2() (floor, bool) {
	changes := false
	newFloor := floor{
		height: f.height,
		width:  f.width,
		tiles:  tiles{},
	}
	for r := 0; r < f.height; r++ {
		for c := 0; c < f.width; c++ {
			loc := pos{r, c}
			tile := f.tiles[loc]
			if tile == path {
				newFloor.tiles[loc] = tile
				continue
			}
			occupied := f.countOccupiedNeighboursInSight(loc)
			switch {
			case tile == emptySeat && occupied == 0:
				newFloor.tiles[loc] = occupiedSeat
				changes = true
			case tile == occupiedSeat && occupied >= 5:
				newFloor.tiles[loc] = emptySeat
				changes = true
			default:
				newFloor.tiles[loc] = tile
			}
		}
	}
	return newFloor, changes
}

func (f floor) draw() string {
	s := ""
	for r := 0; r < f.height; r++ {
		for c := 0; c < f.width; c++ {
			loc := pos{r, c}
			s += string(f.tiles[loc])
		}
		s += "\n"
	}
	return s
}

func (f floor) countOccupied() int {
	occupied := 0
	for r := 0; r < f.height; r++ {
		for c := 0; c < f.width; c++ {
			if f.tiles[pos{r, c}] == occupiedSeat {
				occupied += 1
			}
		}
	}
	return occupied
}

func (f floor) countOccupiedNeighbours(l pos) int {
	var occupied int
	for _, dir := range directions {
		r, c := l.r+dir.r, l.c+dir.c
		if (0 <= c && c < f.width) && (0 <= r && r < f.height) {
			if f.tiles[pos{r, c}] == occupiedSeat {
				occupied += 1
			}
		}
	}
	return occupied
}

func (f floor) countOccupiedNeighboursInSight(l pos) int {
	var occupied int
	for _, dir := range directions {
		r, c := l.r+dir.r, l.c+dir.c
		for (0 <= c && c < f.width) && (0 <= r && r < f.height) && f.tiles[pos{r, c}] != emptySeat {
			if f.tiles[pos{r, c}] == occupiedSeat {
				occupied += 1
				break
			}
			r, c = r+dir.r, c+dir.c
		}
	}
	return occupied
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
