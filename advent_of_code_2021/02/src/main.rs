use std::fs;

type Command = (String, i32);

fn get_input() -> Vec<Command>{
    let mut content = fs::read_to_string("input.txt").expect("Could not read file");
    content.pop(); // remove trailing '\n'
    return content.split("\n").map(|row| { 
        let mut data = row.split(" ");
        let cmd;
        match data.nth(0) {
            Some(command) => cmd = command.to_string(),
            None => panic!("No command..."),
        }
        let dist;
        match data.nth(0) {
            Some(string) => {
                match string.parse::<i32>() {
                    Ok(value) => dist = value,
                    Err(e) => panic!("Error parsing int: {:?}", e),
                }
            },
            None => panic!("No command value...")
        }
        return (cmd, dist) 
    }).collect();
}

fn first(commands:&Vec<Command>) -> i32 {
    let mut d = 0;
    let mut h = 0;
    for cmd in commands {
        match cmd.0.as_str(){
            "forward" => h += cmd.1,
            "up" => d -= cmd.1,
            "down" => d += cmd.1,
            _ => println!("Unknown command {}", cmd.0)
        }
    }
    return d * h;
}

fn second(commands:&Vec<Command>) -> i32 {
    let mut d = 0;
    let mut h = 0;
    let mut a = 0;
    for cmd in commands {
        match cmd.0.as_str(){
            "forward" => { 
                h += cmd.1;
                d += cmd.1 * a;
            },
            "up" => a -= cmd.1,
            "down" => a += cmd.1,
            _ => println!("Unknown command {}", cmd.0)
        }
    }
    return d * h;
}

fn main() {
    let commands = get_input();
    println!("1: {}", first(&commands));
    println!("2: {}", second(&commands));
}
