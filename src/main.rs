use std::fs;
use std::u32;

fn main() {
    let contents = fs::read_to_string("input.txt")
        .expect("Something went wrong reading the file");

    let mut highest_calories = vec![0; 3];
    let mut highest_calories_elf = vec![0; 3];
    let mut total_calories = 0;
    let mut elf = 0;

    for line in contents.split("\n") {
        if line.is_empty() {
            elf += 1;
            for i in 0..3 {
                if total_calories > highest_calories[i] {
                    for j in (i+1..3).rev() {
                        highest_calories[j] = highest_calories[j-1];
                        highest_calories_elf[j] = highest_calories_elf[j-1];
                    }
                    highest_calories[i] = total_calories;
                    highest_calories_elf[i] = elf;
                    break;
                }
            }
            total_calories = 0;
        } else {
            let calories: u32 = line.parse().unwrap_or(0);
            total_calories += calories;
        }
    }

    let top_calories: u32 = highest_calories.iter().sum();
    println!("The top three elves carrying the most Calories are {:?}: {}", highest_calories_elf, top_calories);
}
