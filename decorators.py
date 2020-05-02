s = input('Ввести слова через пробел')
 
s = s.split()
 
s.sort(key=len)
 
print(s)
