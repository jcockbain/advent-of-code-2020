package main

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 5, Part1("test1.txt"))
	assert.Equal(t, 2080, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 8, Part2("test1.txt"))
	assert.Equal(t, 2477, Part2("input.txt"))
}