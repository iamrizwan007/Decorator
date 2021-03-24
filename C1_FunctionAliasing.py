def wish(name):
 print('Good Morning:', name)
greeting = wish
wish('rizwan')
greeting('rizwan')
print(id(wish))
print(id(greeting))
del wish
greeting('rizwan')