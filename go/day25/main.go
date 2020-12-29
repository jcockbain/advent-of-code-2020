package main

import (
	"fmt"

	input "aoc2020/inpututils"
)

func main() {
	fmt.Println("--- Part One ---")
	fmt.Println(Part1("input.txt"))
}

func Part1(filename string) int {
	publicKeys := input.ReadNumbers(filename)
	publicKey1, publicKey2 := publicKeys[0], publicKeys[1]
	loopSize1, loopSize2 := getLoopSize(publicKey1), getLoopSize(publicKey2)
	encryptionKey1 := transform(publicKey2, loopSize1)
	encryptionKey2 := transform(publicKey1, loopSize2)
	if encryptionKey1 != encryptionKey2 {
		panic(fmt.Sprintf("%v != %v", encryptionKey1, encryptionKey2))
	}
	return transform(publicKey1, loopSize2)
}

func getLoopSize(publicKey int) int {
	subject, val, size := 7, 1, 0
	for val != publicKey {
		size += 1
		val = (val * subject) % 20201227
	}
	return size
}

func transform(publicKey int, loopsSize int) int {
	subject, value := publicKey, 1
	for loops := 0; loops < loopsSize; loops++ {
		value = (value * subject) % 20201227
	}
	return value
}
