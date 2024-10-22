package main

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	got := Part1("input.txt")
	assert.Equal(t, 289, got)
}

func TestPart2(t *testing.T) {
	got := Part2("input.txt")
	assert.Equal(t, 5522401584, got)
}