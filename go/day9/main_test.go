package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 127, Part1("test1.txt", 5))
	assert.Equal(t, 57195069, Part1("input.txt", 25))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 62, Part2("test1.txt", 5))
	assert.Equal(t, 7409241, Part2("input.txt", 25))
}
