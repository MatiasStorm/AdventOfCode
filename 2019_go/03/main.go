package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
)


type Point struct {
    x int
    y int
}

type WireSegment struct {
    start Point
    end Point
}

type Wire struct {
    horizontalSegments []WireSegment
    verticalSegments []WireSegment
}


func main() {
    print("Hello")
    wires := getInput("./input.txt")
    wire1 := wires[0]
    wire2 := wires[1]
    // var closestCrossingPoint Point
    for _, hs := range wire1.horizontalSegments{
        for _, vs := range wire2.verticalSegments{
            if hs.start.x   <= vs.start.x &&
                hs.end.x    >= vs.start.x && 
                vs.start.y  <= hs.start.y && 
                vs.end.y    >= hs.start.y {
                fmt.Println(hs, vs)
            }
        }
    }
    // for _, s := range wire1.verticalSegments{

    // }
    // fmt.Println(wire1, wire2)
}

func getInput(file string) []Wire {
    data, err := os.ReadFile(file)
    if err != nil {
        panic(err)
    }
    var wires = []Wire{}
    for _, l := range strings.Split(string(data), "\n")[0:2] {
        var x, y = 0, 0
        wire := Wire{}
        var segment WireSegment
        for _, e := range strings.Split(l, ",") {
            startPoint := Point{x: x, y: y}
            dist, err := strconv.Atoi(e[1:len([]rune(e))])
            if err != nil {
                panic(err)
            }
            dir := e[0]
            switch dir {
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
            endPoint := Point{x: x, y: y}
            segment = WireSegment{start: startPoint, end: endPoint}
            if startPoint.y != y {
                wire.verticalSegments = append(wire.verticalSegments, segment)
            } else {
                wire.horizontalSegments = append(wire.horizontalSegments, segment)
            }
        }
        wires = append(wires, wire)
    }
    return wires
}

