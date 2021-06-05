'''
The purpose of this program is to sum all of the integers from a given text file.
'''

import math

DEBUG = False

# TODO: Come up with a better name.
CHARGE_SYMBOL = '$'

DEFAULT_SUM_FILE = './nums_to_sum.txt'

p_name_1 = ''
p_name_2 = ''

def main():
   file_sum = 0   # The total sum for the entire file
   cat_sum = 0    # The total sum for a category
   p_tot_1 = 0    # The file total for person 1
   p_tot_2 = 0    # The file total for person 2
   p_cat_1 = 0    # The category total for person 1
   p_cat_2 = 0    # The category total for person 2
   is_even = True # Whether the number is odd or even
   rmnders = 0    # The total of remaining cents after splitting odd numbers

   if DEBUG:
      sum_file = None
   else:
      sum_file = input('Enter the name of the file: ')

   if not sum_file:
      sum_file = DEFAULT_SUM_FILE
      print(f'Nothing entered. Using \'{DEFAULT_SUM_FILE}\'')

   with open(sum_file, 'r') as num_file:
      for line in num_file:
         num = 0
         line = line.strip()

         # Skip blank lines
         if line == '':
            continue

         # TODO: move sums to math.fsum()
         # If the line is only a float, then add it to the total for person 1.
         try:
            num = round(float(line), 2)
            p_tot_1 += num

            print(f'\t{p_name_1}: {p_cat_1} + {num} = ', end='')
            p_cat_1 += num
            print(f'{p_cat_1: 3}')
         except ValueError:
            # If it is not blank nor only a float, check the first character of the string.
            first_char = line[0]

            # Check if the number should be split or check allocated to person 2.
            if first_char in [CHARGE_SYMBOL, '/']:
               # Trim the symbol from the front of the string.
               line = line[1:]

               # For splitting, find out value has odd or even number of cents.
               # TODO: Make this more pythonic
               is_even = False
               if (len(line) > 3
                  and line[-3] == '.'
                  and int(line[-1]) % 2 == 0):
                  is_even = True

               if DEBUG:
                  print(f'DEBUG: line={line} : len={len(line)} : last_char={line[-1]} : is_even={is_even}')
               num = float(line)
               file_sum += num
               cat_sum += num

               if first_char == '/':
                  # If the number is even, move one cent to the remainder count before dividing.
                  if not is_even:
                     num -= 0.01
                     rmnders += 0.01

                  num = round(num / 2, 2)

                  p_tot_1 += num
                  p_tot_2 += num

                  # TODO: Export this to some helper function
                  print(f'\t{p_name_1}: {p_cat_1} + {num} = ', end='')
                  p_cat_1 += num
                  print(f'{p_cat_1: 3}')

                  print(f'\t{p_name_2}: {p_cat_2} + {num} = ', end='')
                  p_cat_2 += num
                  print(f'{p_cat_2: 3}')
               elif first_char == CHARGE_SYMBOL:
                  print(f'\t{p_name_2}: {p_cat_2} + {num} = ', end='')
                  p_tot_2 += round(float(line[1:]), 2)
                  print(f'{p_cat_2: 3}')
            else:
               print(f'\n<Category Total: {cat_sum: 3}>')
               print(f'<{p_name_1}\'s Category Total: {p_cat_1: 3}>')
               print(f'<{p_name_2}\'s Category Total: {p_cat_2: 3}>')
               print('\n---')
               print(f'{line}')
               cat_sum = 0
               p_cat_1 = 0
               p_cat_2 = 0

         print('') # Add a blank line

   # Print the last category's totals.
   print(f'\n<Category Total: {cat_sum: 4}>')
   print(f'<{p_name_1}\'s Category Total: {p_cat_1: 3}>')
   print(f'<{p_name_2}\'s Category Total: {p_cat_2: 3}>')

   print(f'\n===\n') # Divider


   print(f'File Total: {file_sum: 4}')
   print(f'{p_name_1}\'s Total is: {p_tot_1}.')
   print(f'{p_name_2}\'s Total is: {p_tot_2}.')
   print(f'Remaining: {rmnders}')


if __name__ == '__main__':

   if DEBUG:
      p_name_1 = "1st Person"
      p_name_2 = "2nd Person"
   else:
      p_name_1 = input("Please enter the first person's name: ")
      p_name_2 = input("Please enter the second person's name: ")

   main()