"""
birth_year = input('input ur birth year')
age = 2023 - int(birth_year)
print(type(age))
print(f'ur age is {age}')  """
"""
good_credit = True
price = 1000000
if good_credit :
  price-= price/10
else:
  price-=price/5
print(f'payments overall is {int(price)}')  """
"""
name = input("input your name")
if len(name) < 3:
  print(f"the name {name} has less than 3 characters")
elif len(name) > 50:
  print(f"your name has more than 50 characters")
else:
  print(f"welcome, {name}")  """
"""
weight = int(input('enter your mass '))
pkg = input('its on (p)Pounds or (k)Killograms')
if pkg.lower() == 'k':
  print(f'in pounds it will be {int(weight*2.20462)}')
elif pkg.lower() == 'p':
  print(f'in killograms that will be {int(weight*0.453592)}')
else:
  print("Give true datatypes")"""
"""
          Not working simple cod that actually working ;]
pea = input('type help')
if pea.lower() == 'help':
  print('''
  *start 
  *finish''')
elif pea.lower() == 'start':
  secret = 9
  limit = 3
  attempts = 0
  while attempts < limit:
    guess = int(input('guess the num'))
    attempts+=1
    if guess == secret:
      print('Congrats, you guessed it!')
      break
  else:
    print("you failed")
  """
#  pp = [1,2,3,4,5,6,7,8,9]
#  print(int(sum(pp)/len(pp)))
'''
numbers = [5,2,5,2,2]
for o in numbers:
  ou = ''
  for s in range(o):
    ou+='x'
  print(ou)
'''


# def  biggest num of the list
def find_max(l1st):
  au = l1st[0]
  for o in l1st:
    if o > au:
      au = o
  return au


# from list to set 2 examples
"""
print(set(num))
bumb = []
for o in num:
  if o not in bumb:
    bumb.append(o)
print(bumb)  
"""
#tuple example
"""
coo = (10,5,2.5)
a,b,c = coo
print(a,b,c)"""
#dictionary example
'''
bluh = input('input tiv')
nNames = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three'
}
us = ''
for o in bluh:
   us += nNames.get(o, ' x ') + ""
print(us) '''
#dictionary emoji function example
'''
def emp(txt):
  em0j = {
    ':)': '🙂',
    ':(': '😞'
  }
  output = ''
  words = txt.split(' ')
  for word in words:
    output+=em0j.get(word, word) +' '
  return(output)
print(emp('hi honey :)'))
'''
#class examples
'''
class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def move(self):
    print("move")
  def draw(self):
    print("draw")
#

point = Point(10,20)

print(point.x, point.y) 
'''
