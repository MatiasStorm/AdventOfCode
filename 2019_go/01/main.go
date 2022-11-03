package main

import (
    "fmt"
    "advent_of_code_2019/common"
    "strconv"
)

func main() {
    input := common.GetInput("01/input1.txt")
    fmt.Printf("Solution to 1: %d\n", _1(input))
    fmt.Printf("Solution to 2: %d\n", _2(input))
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
