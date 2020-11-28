package example

import (
	"testing"
	"github.com/stretchr/testify/assert"
)

func TestPart1(t *testing.T) {
	got := Part1("input.txt")
	assert.Equal(t, 15, got)
}