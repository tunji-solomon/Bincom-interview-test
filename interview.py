#question 1 answer:
shirts = {
  'green' : 10,
  'yellow' : 5,
  'brown' : 6,
  'blue' : 31,
  'pink' : 5,
  'orange' : 9,
  'cream' : 2,
  'red' : 9,
  'white' : 16,
  'arsh' : 1,
  'black' : 1

}
sum_of_colors = 0
for k,v in shirts.items():
  sum_of_colors += v

mean_color = round(sum_of_colors/len(shirts))

for k,v in shirts.items():
  if mean_color == v:
    print(k)

#answer => mean color is ORANGE and RED

#question 2 
highest = 0
for k,v in shirts.items():
  if v > highest:
    highest = v
for k,v in shirts.items():
  if highest == v:
    print(k)

#The color mostly worn is BLUE

#question 3
def check_median(shirts):
    shirts = sorted(shirts.items(), key = lambda k: k[v])
    x = len(shirts)
    middle = x // 2
    first_half = shirts[: middle]
    second_half = shirts[middle :]
    first_half_end = first_half[-1]
    second_half_start = second_half[0]
    if len(shirts) % 2 == 0:
      print(first_half_end, second_half_start)
    else:
      print(second_half_start[0])

check_median(shirts)
# median color is BROWN


# question 4 solution
variance = 0
for k,v in shirts.items():
  variance += (v - mean_color)**2
total = variance / 4
print(total)

# variance is 188

# question 5
red_color_outcome =shirts['red'] 
total_color_outcome = sum_of_colors
probability_of_red = (red_color_outcome / total_color_outcome)
print(probability_of_red)

# OR IN PERCENTAGE
percentage = round(probability_of_red * 100,2)
print(percentage)




# import psycopg2
# connection = psycopg2.connect(
#   database = 'teetech',
#   user = 'Tunejeey',
#   password = 'Tunejeey',
#   host = 'localhost',
#   port = '5432'
# )

# connection.autocommit = True
# cursor = connection.cursor()

# query = '''CREATE TABLE SHIRT_COLOR( id interger primary key autoincrement,
#  color of shirt char(30) NOT NULL,
#   number of times interger NOT NULL );'''

# cursor.execute(query)
# columns = shirts.key()
# for k,v in shirts.items():
#   query2 = '''insert into SHIRT_COLOR(color of shirt, number of times) VALUES{};'''.format(k,v)
#   cursor.execute(query2)

# view_table = '''select * from SHIRT_COLOR;'''
# cursor.execute(view_table)

# for i in cursor.fetchall():
#   print(i)

# connection.commit()
# connection.close()

# HAVING SOME ISSUE INSTALLING POSTGRESQL DUE TO ADMINISTRATION PIN ON MY PC . SO I COULDNT COMPLETE THIS


# question 8
def baseConverter(x):
    import random
    count = 0
    my_list= []
    base10 = 0
    y = 0
    while count < 4: 
      random_number = round(random.random())
      my_list.append(random_number)
      count += 1
    while y < len(my_list):
      for i in my_list:
        base10 +=  (i * x)**y
        y += 1
        print(y)

    return print('{} base {} to base 10 = {}'.format(my_list,x,base10))


#baseConverter(3)

# question 9

a, b = 0, 1

sum_of_sequence = 0

n = 50

for i in range(n):

   print(a)
   sum_of_sequence += a

   a, b = b, a + b
print('the sum of first 50 fibonacci sequence = {}.'.format(sum_of_sequence))
