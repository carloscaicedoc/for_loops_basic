# 1. Basic - Print all integers from 0 to 150.
print("Integers 0 to 150")
for x in range(151):
    print(x)

# while loop version
print("Integers 0 to 150 - while loop")

num = 0 
while num < 151:
    print(num)
    num += 1

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print("Multiples of Five")
for x in range(5, 1001, 5):
    print(x)

# while loop version
print("Multiples of Five - while loop")
n = 5
while n < 1001:
    print(n)
    n += 5

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".

print("Dojo Count")
for c in range(1, 101):
    if c % 10 == 0:
        print("Coding Dojo")
    elif c % 5 == 0:
        print("Coding")
    else:
        print(c)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

print("Whoa. That Sucker's Huge!")
sum = 0 
for y in range(1, 500001, 2):
    sum += y
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print("Countdown by Fours")
for z in range(2018, 0, -4):
    print(z)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

print("Flexible Counter")

lowNum = 2
highNum = 9
mult = 3
for f in range(lowNum, highNum + 1):
    if f % mult == 0:
        print(f)