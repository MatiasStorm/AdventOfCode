package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

func main() {
    input := readInput("02/input.txt")
    fmt.Println(input)
    fmt.Printf("Solution to 1: %d\n", _1(input))
    fmt.Printf("Solution to 2: %d\n", _2(input))
}

func readInput(name string ) []int {
    data, err := os.ReadFile(name)
    if err != nil{
        panic(err)
    }
    var program = []int{}
    for _, i := range strings.Split(strings.Trim(string(data), "\n"), ",") {
        j, err := strconv.Atoi(i)
        if err != nil {
            panic(err)
        }
        program = append(program, j)
    }
    return program
}

func _1(input []int) int {
    program := make([]int, len(input))
    copy(program, input)
    return intcodeComputer(program, 12, 2)
}

func _2(input []int) int {
    var output, noun, verb int
    program := make([]int, len(input))
    for noun = 0; noun < 100; noun++ {
        for verb = 0; verb < 100; verb++ {
            copy(program, input)
            output = intcodeComputer(program, noun, verb)
            if output == 19690720{
                return 100 * noun + verb
            }
        }
    }
    fmt.Printf("n: %d, v: %d\n", noun, verb)
    return -1
}

func intcodeComputer(program []int, noun int, verb int) int {
    program[1] = noun
    program[2] = verb
    var op, p1, p2, dest int
    for pc := 0; pc < len(program) -1; pc += 4 {
        op = program[pc]
        p1 = program[pc + 1]
        p2 = program[pc + 2]
        dest = program[pc + 3]
        switch op {
        case 1:
            program[dest] = program[p1] + program[p2]
        case 2:
            program[dest] = program[p1] * program[p2]
        case 99:
            break
        default:
            panic("Unkown op code")
        } 
    }
    return program[0]
}
