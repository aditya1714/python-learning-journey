'''Can you change the values inside a list which is contained in set S?'''
s = {8, 7, 12, "Harry", [1,2]}

# We cannot change the values inside a list if the list is part of a set,
# because Python sets only allow immutable (unchangeable) elements.
# A list is mutable, meaning its values can be changed, so it is not allowed
# inside a set and will cause an error (TypeError: unhashable type: 'list').
# If we want to store multiple values inside a set, we should use a tuple instead
# because tuples are immutable and allowed inside sets.
