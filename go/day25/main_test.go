package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	assert.Equal(t, 8, getLoopSize(5764801))
	assert.Equal(t, 11, getLoopSize(17807724))
	assert.Equal(t, 9420461, Part1("input.txt"))
}
