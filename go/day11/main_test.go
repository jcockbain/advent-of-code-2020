package main

import (
	"testing"
	// "fmt"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 37, Part1("test1.txt"))
	assert.Equal(t, 2270, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 26, Part2("test1.txt"))
	assert.Equal(t, 2042, Part2("input.txt"))
}

func TestFloor(t *testing.T) {
	s := 
`L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL`

s2 := 
`#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
`

s3 := 
`#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
`

s4 := 
`#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
`

s5 := 
`#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
`

s6 := 
`#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
`


	f := newFloor(s)
	assert.Equal(t, 10, f.height)
	assert.Equal(t, 10, f.width)

	newFloor, changes := f.getNext()

	assert.Equal(t, true, changes)
	assert.Equal(t, s2, newFloor.draw())
	assert.Equal(t, 71, newFloor.countOccupied())

	assert.Equal(t, 7, newFloor.countOccupiedNeighbours(pos{7, 3}))
	assert.Equal(t, 5, newFloor.countOccupiedNeighbours(pos{6, 2}))
	assert.Equal(t, 5, newFloor.countOccupiedNeighbours(pos{9, 5}))

	newFloor2, changes2 := newFloor.getNext()

	assert.Equal(t, true, changes2)
	assert.Equal(t, s3, newFloor2.draw())

	newFloor3, changes3 := newFloor2.getNext()

	assert.Equal(t, true, changes3)
	assert.Equal(t, s4, newFloor3.draw())

	newFloor4, changes4 := newFloor3.getNext()

	assert.Equal(t, true, changes4)
	assert.Equal(t, s5, newFloor4.draw())
	
	newFloor5, changes5 := newFloor4.getNext()

	assert.Equal(t, true, changes5)
	assert.Equal(t, s6, newFloor5.draw())

	_, changes6 := newFloor5.getNext()
	assert.Equal(t, false, changes6)
	assert.Equal(t, 37, newFloor5.countOccupied())
}
