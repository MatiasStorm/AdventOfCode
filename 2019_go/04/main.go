package main

import (
	"os"
	"strconv"
)

func main() {
    from, to := readInput("input.txt")
    validPasswords := 0
    for p := from; p <= to; p++ {
        if isValidPassword(strconv.Itoa(p), 6){
            validPasswords++
        }
    }
    println("Part 1: ", validPasswords)
}

func readInput(name string) (int, int) {
    data, err := os.ReadFile(name)
    if err != nil {
        panic(err)
    }
    numbers := []int{}
    strNumber := ""

    for i := 0; i < len(data); i++ {
        if data[i] == '-' || data[i] == '\n' {
            number, err := strconv.Atoi(strNumber)
            if err != nil {
                panic(err)
            }
            numbers = append(numbers,number)
            strNumber = ""
            continue
        }
        strNumber += string(data[i])
    }
    return numbers[0], numbers[1]
}


func isValidPassword(p string, maxDuplicates int) bool {
    increases := false
    duplicate := false
    increaseChar = p[0]

    for i := 1; i < len(p); i++ {
        if p[i] == p[i - 1] {
            duplicate = true
        }
        if p[i] >= p[i - 1]{
            increases += true
        } else {
            increases += false
            break
        }
    }
    return increases && duplicate
}
