use std::fs;

fn get_input() -> Vec<i32> {
    let mut content = fs::read_to_string("input.txt").expect("Could not read file");
    content.pop(); // remove trailing '\n'
    content.split("\n").map(|d| d.parse::<i32>().unwrap()).collect()
}

fn get_increments(measurements:&Vec<i32>, window_size:usize) -> i32 {
    let mut increments = 0;
    let mut prev_depth = 0;
    let mut depth : i32;
    for i in 0..measurements.len(){
        if i + window_size < measurements.len() {
            depth = measurements[i.. i+window_size].iter().sum();
            if depth > prev_depth {
                increments += 1;
            }
            prev_depth = depth;
        }
        else {
            return increments;
        }
    }
    increments
}

fn main() {
    let depths:Vec<i32> = get_input();
    println!("1: {}", get_increments(&depths, 1));
    println!("2: {}", get_increments(&depths, 3));
}
