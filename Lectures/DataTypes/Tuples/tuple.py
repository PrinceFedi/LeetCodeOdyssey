#  How to create a Tuple? - shit is immutable, cannot update and delete individual elements

newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')

print(newTuple1)

# Access Tuple elements

print(newTuple[0])

#  Traverse through tuple

for i in newTuple:
    print(i)

for index in range(len(newTuple)):
    print(newTuple[index])

#  How to search for an element in Tuple?

print('a' in newTuple)


def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'


print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
myTuple = (1, 4, 3, 2, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)

print(myTuple + myTuple1)  # Output: (1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7)
print(myTuple * 4)  # Output : (1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)
print(2 in myTuple1)  # Output : true

myTuple1.count(2)  # Returns the number of occurrences of inputted value
myTuple1.index(2)  # Returns the first index of inputted value
