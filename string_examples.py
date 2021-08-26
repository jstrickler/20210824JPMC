s1 = "spam\n"
print(s1, len(s1))
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print(s2, len(s2))
print("It's the best thing ever")
print('It is the "best" thing ever')
print("""It's the "best" thing ever!""")

query = """
select * 
from customers
where customer_id = '1234'
"""

print(type(s1), len(s1))

actor = "Chris Hemsworth"

a1 = actor.upper()
print(a1)
print(actor.upper())
# actor.upper()
print(actor)
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
# actor.endswith(...)
print('wort' in actor)
print('hops' in actor)

print(actor)
print(actor.find('Hem'))
print(actor.find('Shem'))

print(actor.replace('Chris', 'Liam'))
print(actor.replace('h', 'X'))
print(actor.replace('h', 'X', 1))

names = actor.split()
print(names)
raw_cities = 'Denver:San Francisco:Columbus:Plano'
city_list = raw_cities.split(':')
print(city_list)

s = "       All my exes live in Texas       "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s = "xyxxyyxxxyyyxxxxyyyyAll my exes live in Texasyyyyxxxxyyyxxxyyxx"
print("|" + s.lstrip("xy") + "|")
print("|" + s.rstrip("xy") + "|")
print("|" + s.strip("xy") + "|")
print()

x = "spam\n"
y = x.rstrip()  # all space characters
y = x.rstrip('\n\r')
print(y)






