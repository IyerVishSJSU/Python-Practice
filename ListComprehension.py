#Code to illustrate List Comprehension to return positive numbers in Integer Format
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
#for x in numbers:
#    if x>0:
#        newlist.append(int(x))
newlist=[int(x) for x in numbers if x>0]
print newlist