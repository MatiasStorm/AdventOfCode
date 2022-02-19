use std::fs;

type Command = (String, i32);

fn get_input() -> Vec<Command>{
    let mut content = fs::read_to_string("input.txt").expect("Could not read file");
    content.pop(); // remove trailing '\n'
    return content.split("\n").map(|row| { 
        let mut data = row.split("\n");
        let cmd = data.nth(0).unwrap().to_string();
        let dist = data.nth(1).unwrap().parse::<i32>().unwrap();
        return (cmd, dist) 
    }).collect();
}

fn first(commands:Vec<Command>) -> i32 {
    let mut d = 0;
    let mut h = 0;
    for (cmd,n) in commands.iter() {
        match *cmd{
            "forward": h += cmd.1,
        }
    }
}

fn main() {
    let commands = get_input();
    println!("1: {}", first(commands));
}
