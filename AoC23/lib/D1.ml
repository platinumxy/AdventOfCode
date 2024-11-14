let day_one_file = "./files/day1.txt"


    
let int_map = function  
  | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" as c -> Some c
  | _ -> None

let full_string_map = function 
  | "one"  | "1" -> Some "1"
  | "two"  | "2" -> Some "2"
  | "three"| "3" -> Some "3"
  | "four" | "4" -> Some "4"
  | "five" | "5" -> Some "5"
  | "six"  | "6" -> Some "6"
  | "seven"| "7" -> Some "7"
  | "eight"| "8" -> Some "8"
  | "nine" | "9" -> Some "9"
  | _ -> None
  
let parse_string (parse_func: string -> string option) (s: string) : int =
    let out = ref [] in
    for i = 0 to (String.length s) - 1 do
      for j = i to (String.length s) - 1 do
        match parse_func (String.sub s i (j - i + 1)) with 
        | Some value -> out := value :: !out 
        | None -> ()
      done;
    done;
  
    match !out with 
    | [] -> raise (Failure "No elements found in the list")
    | [x] -> int_of_string (x ^ x)
    | first :: _ ->
      let rec find_last l =
        match l with
        | [] -> raise (Failure "INVALID STATE")
        | [x] -> x
        | _ :: tail -> find_last tail
      in
      let last = find_last !out in
      int_of_string (last ^ first) (*why is ocmal like this?*)

let lines = Common.read_lines day_one_file
let solution_one = List.fold_left (+) 0 (List.map (parse_string int_map) lines)
let solution_two = List.fold_left (+) 0 (List.map (parse_string full_string_map) lines) 

(*
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. 
The Elves have even given you a map; on it, they've used stars to mark the top fifty 
locations that are likely to be having problems. You've been doing this long enough to
know that to restore snow operations, you need to check all fifty stars by December 25th.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the
Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle
grants one star. Good luck! You try to ask why they can't just use a weather machine 
("not powerful enough") and where they're even sending you ("the sky") and why your map 
looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the
sky ("of course, where do you think snow comes from") when you realize that the Elves are
already loading you into a trebuchet ("please hold still, we need to strap you in"). As 
they're making the final adjustments, they discover that their calibration document 
(your puzzle input) has been amended by a very young Elf who was apparently just excited
to show off her art skills. Consequently, the Elves are having trouble reading the values
on the document. The newly-improved calibration document consists of lines of text; each
line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last
digit (in that order) to form a single two-digit number. For example:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding 
these together produces 142. Consider your entire calibration document. What is the sum of
all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid 
"digits". Equipped with this new information, you now need to find the real first and last 
digit on each line. For example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these 
together produces 281. What is the sum of all of the calibration values?
*)