package common

import (
    "os"
    "strings"
)

func Test() string {
    return "TEST common"
}

func GetInput(name string) []string {
    data, err := os.ReadFile(name)
    if err != nil {
        panic(err)
    }
    lines := strings.Split(string(data), "\n")
    return lines[:len(lines) - 1]
}


