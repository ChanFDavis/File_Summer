'''
The purpose of this program is to sum all of the integers from a given text file.
'''

DEFAULT_SUM_FILE = './nums_to_sum.txt'

def main():
   file_sum = 0
   category_sum = 0
   category_str = ''

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
            pass
         
         # If the line is only a float, then add it to the total.
         try:
            num = float(line)
            print(f'{category_sum}  + {num: 3} = ', end='')
         except ValueError:
            # If it is not blank nor only a float, check the first character of the string.
            first_char = line[0]
            if first_char in ['/', '+', '-']: 
               num = float(line[1:]) / 2
               print(f'{category_sum}  + {num: 3} ({line[1:]} / 2) = ', end='')
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

if __name__ == '__main__':
   main()