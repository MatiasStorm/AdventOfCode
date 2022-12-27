use std::fs;




fn main() {
    println!("Hello, world!");
}

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
