let read_lines (pth : string) : string list =
  let ic = try Some (open_in pth) with _ -> None in
  match ic with
  | None ->
      print_endline "Failed to read file";
      exit 1
  | Some f ->
      let rec read_lines_aux acc =
        try
          let line = input_line f in
          read_lines_aux (line :: acc)
        with End_of_file ->
          close_in f;
          List.rev acc
      in
      read_lines_aux []

let show_day (day : int) (sol_one : string) (sol_two : string) =
  Printf.printf "\n============ Day %d =============\n> Solution One: %s\n> Solution Two: %s\n"
    day sol_one sol_two

let sd (day: int) (sol : string) =
  Printf.printf "\n============ Day %d =============\n> Solution One: %s\n"  
    day sol

let show_day_ints (day : int) (sol_one : int) (sol_two : int) =
  Printf.printf "\n============ Day %d =============\n> Solution One: %d\n> Solution Two: %d\n"
    day sol_one sol_two

let sdi (day: int) (sol : int) =
  Printf.printf "\n============ Day %d =============\n> Solution One: %d\n"
    day sol 