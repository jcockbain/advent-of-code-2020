package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestPart1(t *testing.T) {
	got := Part1("input.txt")
	assert.Equal(t, 822, got)
}

func TestPart2(t *testing.T) {
	got := Part2("input.txt")
	assert.Equal(t, 503, got)
}
