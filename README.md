# AirBnb Clone - The Console
A Command Interpreter to Manage AirBnb objects.

## Project Notes
### Environment
Files interpreted/run on Ubuntu 14.04 LTS with Python 3
### Style
All code is written in accordance with Pep8 https://www.python.org/dev/peps/pep-0008/

## How to use the Console
To start:
a. Interactive mode, `$ ./console.py`, and you will prompted with `(hbnb)`
b. Non-interactive mode, `$ echo "help" | ./console.py`
To close:
Type either `EOF` or `quit`
### Command usage of Console
* `help`
  * Usage: `help`
  * Documentation/help provided
* `create`
  * Usage: `create BaseModel`
  * Creates a new instance of a class, saves it (to the JSON file) and prints the `id`
* `show`
  * Usage: `show BaseModel 1234-5847-3912`
  * Prints the string representation of an instance based on the class name and `id`
* `destroy`
  * Usage: `destroy BaseModel 1234-5847-3912`
  * Deletes an instance based on the class name and `id` (save the change into the JSON file). 
* `all`
  * Usage: `all`
  * Prints all string representation of all instances based or not on the class name.
* `update`
  * Usage: `update User 1234-5678-9101 email 115@holbertonschool.com`
  * Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)

## Files
### `monty.h`
Header file with prototypes for all functions and structs used in the interpreter.
### `FILES`
* `main_monty.c`: the ``main_monty`` function from which all other files' execution originates.
* `check_funcs.c`: includes:
  * `check_args`: function to check if arguments are passed
  * `check_push_val`: function to assess if `push` argument is an integer
* `free_func.c`: includes:
  * `free_everything`: function to call all free functions
  * `free_pointers`: function to free double pointers
  * `free_stack`: function to free stack
* `helper_funcs.c`: includes:
  * `convert_push_arg`: converts string to integer
  * `make_struct`: mallocs space for global struct
  * `stack_len`: finds the number of nodes in a stack
  * `find_func`: searches for the op_code or prints message and return error
* `parsers.c`: includes:
  * `parse`: tokenizes buffer from getline into arguments for assessment
  * `parse_check`: checks that buff is not NULL and mallocs space for tok_args
* `op_math.c`: includes:
  * `op_add`: setting first node's value to the sum of the first two nodes' values
  * `op_sub`: sets first node's value to the remainder of subtracting the second node and it is removed
  * `op_mul`: multiply first and second node's values and store in the first node
  * `op_div`: divides second node's value by the first and stores in first node
  * `op_mod`: divides second nodes's value by first and remainder is stored in first node
* `op_other.c`: includes:
  * `op_pall`: prints all `n` values on stack
  * `op_pint`: print `n` value at the top of the stack
  * `op_nop`: does nothing!
* `op_stack_manipulation.c`: includes:
  * `op_push`: pushes a new node with `n` value to the stack
  * `op_pop`: removes/frees value at top of stack
  * `op_swap`: swaps the first two `n` values in the stack with one another

## Limitations


## Bugs


## Authors
* Carrie Ybay, <a href='https://github.com/hicarrie'>Github</a>
* Naomi Sorrell, <a href='https://github.com/NamoDawn'>Github</a>

## License
Public Domain, no copywrite protection