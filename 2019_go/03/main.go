package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)

type Orientation int
const (
    vertical Orientation    = 1
    horizontal              = 2
)


type wireSegment struct {
    x1 int
    y1 int
    x2 int
    y2 int
    orientation Orientation
}

type wire struct {
    segemnts wireSegment
}


func main() {
    fmt.Println("Hello")
}

func getInput(file string) [2]wireSegment {
    data, err := os.ReadFile(file)
    if err != nil {
        panic(err)
    }
    var wires = []wire{}
    for _, l := range strings.Split(string(data), "\n") {
        var x, y = 0, 0
        var wire = wire{}
        for _, e := range strings.Split(l, ",") {
            segment := wireSegment{x1: x, y1: y}
            dist, err := strconv.Atoi(e[1:4])
            if err != nil {
                panic(err)
            }
            switch dir := e[0]; dir {
            case 'U':
                y += dist
            case 'D':
                y -= dist
            case 'L':
                x -= dist
            case 'R':
                x += dist
            default:
                panic("Unkown direction")
            }
            segment.x2 = x
            segment.y2 = y
            append(wire.segments, segment)
        }
        append(wires, wire)
    }
    return wires
}

func 
