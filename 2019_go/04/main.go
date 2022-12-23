package main

import (
	"os"
	"strconv"
)

func main() {
    from, to := readInput("input.txt")
    println("Part 1: ", getNumberOfValidPasswords(from, to, getPart1Validators()))
    println("Part 1: ", getNumberOfValidPasswords(from, to, getPart2Validators()))
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

func getPart1Validators() []func(string) bool {
    var validators []func(string) bool
    validators = append(validators, onlyIncreases)
    validators = append(validators, containsDuplicates)
    return validators
}

func getPart2Validators() []func(string) bool {
    var validators []func(string) bool
    validators = append(validators, onlyIncreases)
    validators = append(validators, containsSingleDuplicate)
    return validators
}

func getNumberOfValidPasswords(from int, to int, validators []func(string) bool ) int {
    validPasswords := 0
    for p := from; p <= to; p++ {
        if isValidPassword(strconv.Itoa(p), validators){
            validPasswords++
        }
    }
    return validPasswords
}

func isValidPassword(p string, validators []func(string) bool) bool {
    for _, v := range(validators) {
        if !v(p){
            return false
        }
    }
    return true
}


func onlyIncreases(p string) bool {
    for i := 1; i < len(p); i++ {
        if p[i - 1] > p[i]{
            return false
        }     
    }
    return true
}

func containsDuplicates(p string) bool {
    for i := 1; i < len(p); i++ {
        if p[i - 1] == p[i]{
            return true
        }     
    }
    return false
}

func containsSingleDuplicate(p string) bool {
    duplicates := 1
    var groups []int
    for i := 1; i < len(p); i++ {
        if p[i - 1] == p[i]{
            duplicates += 1
        } else {
            groups = append(groups, duplicates)
            duplicates = 1
        }
    }
    groups = append(groups, duplicates)
    for _, g := range(groups){
        if g == 2 {
            return true
        }
    }
    return false
}

