package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 25, Part1("test1.txt"))
	assert.Equal(t, 2297, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 286, Part2("test1.txt"))
	assert.Equal(t, 89984, Part2("input.txt"))
}
