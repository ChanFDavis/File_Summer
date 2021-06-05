# File Summer

## Features:
- Only splits between two people
- Blank lines are ignored
- Lines starting with a character [a-z,A-Z] are printed as price categories.
- A line without a symbol (defaults to '$') marks the number as going to person 1
- A line with a defined symbol (defaults to '$') marks the following number as going to person 2
- A line with a '/' symbol marks the following number as split between the two people.
  - In the case of an odd number, the first person gets the extra decimal.
- All numbers are added to a file total variable.
- At the end of each category, print the total of each person for that category, as well as their current total so far.
- At the end of the file, print the total for each person, as well as the total of the entire file.