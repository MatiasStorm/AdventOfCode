package main

import (
    "fmt"
    "strconv"
    "os"
    "strings"
)

func main() {
    input := readInput("01/input1.txt")
    fmt.Printf("Solution to 1: %d\n", _1(input))
    fmt.Printf("Solution to 2: %d\n", _2(input))
}

func readInput(name string) []string {
    data, err := os.ReadFile(name)
    if err != nil {
        panic(err)
    }
    lines := strings.Split(string(data), "\n")
    return lines[:len(lines) - 1]
}

func _1(values []string) int {
    var sum = 0
    for _, val := range values {
        val, err := strconv.Atoi(val)
        if err != nil {
            panic(err)
        }
        sum += val / 3 - 2
    }
    return sum
}

func _2(values []string) int {
    var sum = 0
    for _, val := range values {
        val, err := strconv.Atoi(val)
        if err != nil {
            panic(err)
        }
        val = val / 3 - 2
        for val > 0 {
            sum += val
            val = val / 3 - 2
        }
    }
    return sum
}
