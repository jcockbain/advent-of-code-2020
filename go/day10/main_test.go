package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 35, Part1("test1.txt"))
	assert.Equal(t, 220, Part1("test2.txt"))
	assert.Equal(t, 1856, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 8, Part2("test1.txt"))
	assert.Equal(t, 19208, Part2("test2.txt"))
	assert.Equal(t, 2314037239808, Part2("input.txt"))
}
