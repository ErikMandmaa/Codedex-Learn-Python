def happy_birthday():
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear friend')
  print('Happy birthday to you')

happy_birthday()


def happy_birthday(name):
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear ' + name )
  print('Happy birthday to you')

name = input("Enter the name of the birthday person: ")
happy_birthday(name)