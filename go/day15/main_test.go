package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 436, Part1([]int{0, 3, 6}))
	assert.Equal(t, 206, Part1([]int{7, 14, 0, 17, 11, 1, 2}))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 175594, Part2([]int{0, 3, 6}))
	assert.Equal(t, 955, Part2([]int{7, 14, 0, 17, 11, 1, 2}))
}
