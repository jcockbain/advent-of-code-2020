package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 6559, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 626670513163231, Part2("input.txt"))
}
