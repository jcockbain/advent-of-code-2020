package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestPart1(t *testing.T) {
	got := Part1("input.txt")
	assert.Equal(t, 440979, got)
}

func TestPart2(t *testing.T) {
	got := Part2("input.txt")
	assert.Equal(t, 82498112, got)
}

func testTwoSum(t *testing.T){
	t.Parallel()
	testCases := []struct{
		name string
		ints []int
		target int
		expected int
	} {
		{
			"test-1",
			[]int{1, 2, 3, 4 },
			5,
			6,
		},
		{
			"test-2",
			[]int{10, 21, 31, 4 },
			14,
			40,
		},
		{
			"test-3",
			[]int{12, 1, 23, 3},
			4,
			3,
		},
	}

	for _, tt := range testCases {
		tt := tt
		t.Run(tt.name, func(t *testing.T){
			t.Parallel()
			got, err := twoSum(tt.ints, tt.target)
			assert.Nil(t, err)
			assert.Equal(t, tt.expected, got)
		})
	}
}
