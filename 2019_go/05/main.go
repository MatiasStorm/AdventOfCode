package main

import (
    "fmt"
    "math"
    "os"
    "strconv"
    "strings"
)


func main() {
    input := readInput("input.txt")
    println("Part 1:")
    part1(input)
    // fmt.Printf("Solution to 2: %d\n", _2(input))
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

func part1(input []int) {
    program := make([]int, len(input))
    copy(program, input)
    intcodeComputer(program, 1)
}

func intcodeComputer(program []int, input int) {
    var p1, p2, p3 int
    pc := 0
    var opCode OpCode
    for ;; {
        println("PC", pc)
        opCode.fromInt(program[pc])
        fmt.Println("Operation:", opCode.op, opCode.parameterModes)

        p1, pc = getParam(program, pc, opCode.parameterModes[0])
        println("Param 1, pc, op:", p1, pc, opCode.op)
        fmt.Println("OP:", opCode.op, opCode.parameterModes)
        if opCode.op == 1 || opCode.op == 2 {
            p2, pc = getParam(program, pc, opCode.parameterModes[1])
            p3, pc = getParam(program, pc, opCode.parameterModes[2])
            println("PARAMs:", p1, p2, p3)
            switch opCode.op {
            case 1:
                program[p3] = p1 + p2
            case 2:
                program[p3] = p1 * p2
            }
        } else if opCode.op == 3 || opCode.op == 4 {
            switch opCode.op {
            case 3:
                program[p1] = input
            case 4:
                println(program[p1])
            }
        } else if opCode.op == 99 {
            break;
        } else {
            panic(fmt.Sprintf("Unknown op code: %d", opCode.op))
        }
        pc++
    }
}

type OpCode struct {
    op int
    parameterModes [3]int
}

func (opCode *OpCode) fromInt(op int) {
    var mode int
    for i := 4; i >= 2; i-- {
        mode = 0
        if op >= int(math.Pow10(i)) {
            mode = 1
            op -= int(math.Pow10(i))
        }         
        opCode.parameterModes[i - 2] = mode
    }
    opCode.op = op
}

func getParam(program []int, pc int, mode int) ( int, int ) {
    pc++
    if mode == 1 {
        return program[pc], pc
    } else {
        return program[ program[pc] ], pc
    }
}
