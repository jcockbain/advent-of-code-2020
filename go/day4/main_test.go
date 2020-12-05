package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestPart1(t *testing.T) {
	got := Part1("input.txt")
	assert.Equal(t, 206, got)
}

func TestPart2(t *testing.T) {
	tests := []struct {
		input    string
		expected int
	}{
		{
			"test_input_1.txt",
			0,
		},
		{
			"test_input_2.txt",
			4,
		},
		{
			"input.txt",
			123,
		},
	}
	for _, tt := range tests {
		t.Run(tt.input, func(t *testing.T) {
			got := Part2(tt.input)
			assert.Equal(t, tt.expected, got)
		})
	}
}
