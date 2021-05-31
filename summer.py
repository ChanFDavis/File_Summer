'''
The purpose of this program is to sum all of the integers from a given text file.
'''


DEFAULT_SUM_FILE = './nums_to_sum.txt'

def main():
   file_sum = 0
   category_sum = 0
   category_str = ''
   sum_file = input('Enter the name of the file: ')

   if not sum_file:
      sum_file = DEFAULT_SUM_FILE
      print(f'Nothing entered. Using \'{DEFAULT_SUM_FILE}\'')

   with open(sum_file, 'r') as num_file:
      for line in num_file:
         line = line.strip()
         if line.isdigit():

            print(f'{category_sum}   + {int(line): 3} = ', end='')

            file_sum += int(line)
            category_sum += int(line)
            
            print(f'{category_sum: 3}')
         else:
            print(f'\n<Category Total: {category_sum: 4}>')
            print('\n---\n')
               
            print(f'{line}:\n')

            category_sum = 0


   print(f'\n<Total: {category_sum: 4}>')
   print(f'\n===\n')
   print(f'File Total: {file_sum: 4}')

if __name__ == '__main__':
   main()