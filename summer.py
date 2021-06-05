'''
The purpose of this program is to sum all of the integers from a given text file.
'''

DEFAULT_SUM_FILE = './nums_to_sum.txt'

person_name_1 = ""
person_name_2 = ""

def main():
   file_sum = 0
   category_sum = 0
   person_sum_1 = 0
   person_sum_2 = 0

   # DEBUG:
   # sum_file = input('Enter the name of the file: ')
   sum_file = None

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
         
         # If the line is only a float, then add it to the total.
         try:
            num = float(line)
            print(f'{category_sum}  + {num: 3} = ', end='')
         except ValueError:
            # If it is not blank nor only a float, check the first character of the string.
            first_char = line[0]
            if first_char == '/':
               num = float(line[1:]) / 2
               person_sum_1 += num
               person_sum_2 += num
               print(f'{category_sum}  + {num: 3} ({line[1:]} / 2) = ', end='')
            elif first_char == '+':
               person_sum_1 += float(line[1:])
            elif first_char == '-':
               person_sum_2 += float(line[1:])
            else:
               print(f'\n<Category Total: {category_sum: 4}>')
               print('\n---')
               print(f'{line}')
               category_sum = 0

         file_sum += num
         category_sum += num
         print(f'{category_sum}')

   print(f'\n<Total: {category_sum: 4}>')
   print(f'\n===\n')
   print(f'File Total: {file_sum: 4}')
   print(f"{person_name_1}'s total is: {person_sum_1}.")
   print(f"{person_name_2}'s total is: {person_sum_2}.")

if __name__ == '__main__':
   person_name_1 = input("Please enter the first person's name: ")
   person_name_2 = input("Please enter the second person's name: ")

   main()