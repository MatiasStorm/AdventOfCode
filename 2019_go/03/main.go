package main

import (
    "fmt"
    "os"
    "strings"
    "strconv"
    "math"
    "errors"
)


type Point struct {
    x float64
    y float64
}

type WireSegment struct {
    start   Point
    end     Point
    steps   float64
}

func main() {
    wires := getInput("./input.txt")
    wire1 := wires[0]
    wire2 := wires[1]

    minDist := math.MaxInt
    minSteps := math.MaxInt
    for _, s1 := range wire1[1:]{
        for _, s2 := range wire2[1:]{
            if doesWireSegmentsCross(s1, s2){
                intersect, err := getWireIntersection(s1, s2)
                if err != nil {panic(err)}

                // Part 1
                intersectDistance := getPointDistanceToOrigin(intersect)
                if minDist > intersectDistance {
                    minDist = intersectDistance
                }

                // Part 2
                steps := getCombinedWireSteps(s1, s2, intersect)
                if minSteps > steps {
                    minSteps = steps
                }
            }
        }
    }
    fmt.Println("Part 1:", minDist)
    fmt.Println("Part 2:", minSteps)
}

func getInput(file string) [][]WireSegment {
    data, err := os.ReadFile(file)
    if err != nil {
        panic(err)
    }
    var wires = [][]WireSegment{}
    for _, l := range strings.Split(string(data), "\n")[0:2] {
        var x, y = 0.0, 0.0
        wire := []WireSegment{}
        var segment WireSegment
        steps := 0.0
        for _, e := range strings.Split(l, ",") {
            startPoint := Point{x: x, y: y}
            distInt, err := strconv.Atoi(e[1:len([]rune(e))])
            if err != nil {
                panic(err)
            }
            dist := float64(distInt)
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
            segment = WireSegment{start: startPoint, end: endPoint, steps: steps }
            wire = append(wire, segment)
            steps += dist
        }
        wires = append(wires, wire)
    }
    return wires
}

func doesWireSegmentsCross(s1 WireSegment, s2 WireSegment) bool {
    var maxX, minX, maxY, minY, x, y float64
    if s1.start.y == s1.end.y { // s1 horizontal
        maxX = math.Max(s1.start.x, s1.end.x)
        minX = math.Min(s1.start.x, s1.end.x)
        maxY = math.Max(s2.start.y, s2.end.y)
        minY = math.Min(s2.start.y, s2.end.y)
        y = s1.start.y
        x = s2.start.x
    } else { // s2 horizontal
        maxX = math.Max(s2.start.x, s2.end.x)
        minX = math.Min(s2.start.x, s2.end.x)
        maxY = math.Max(s1.start.y, s1.end.y)
        minY = math.Min(s1.start.y, s1.end.y)
        y = s2.start.y
        x = s1.start.x
    }
    return  maxX >= x && 
            x >= minX &&
            maxY >= y &&
            minY <= y
}

func getWireIntersection(s1 WireSegment, s2 WireSegment) ( Point, error ) {
    if !doesWireSegmentsCross(s1, s2) {
        return Point{}, errors.New("WireSegments doesn't intersect")
    }
    var x, y float64
    if s1.start.y == s1.end.y {
        y = s1.start.y
        x = s2.start.x
    } else {
        y = s2.start.y
        x = s1.start.x
    }
    return Point{x, y}, nil
}

func getPointDistanceToOrigin(p Point) int {
    return int(math.Abs(p.x) + math.Abs(p.y))
}

func getCombinedWireSteps(s1 WireSegment, s2 WireSegment, p Point) int {
    if s1.start.y == s1.end.y { // s1 horizontal
        return int(s1.steps + math.Abs(p.x - s1.start.x) + s2.steps + math.Abs(p.y - s2.start.y))
    } else {
        return int(s1.steps + math.Abs(p.y - s1.start.y) + s2.steps + math.Abs(p.x - s2.start.x))
    }
}







