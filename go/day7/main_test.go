package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 4, Part1("test_input_1.txt"))
	assert.Equal(t, 370, Part1("input.txt"))
}

func TestPart2(t *testing.T) {
	assert.Equal(t, 32, Part2("test_input_1.txt"))
	assert.Equal(t, 126, Part2("test_input_2.txt"))
	assert.Equal(t, 29547, Part2("input.txt"))
}
