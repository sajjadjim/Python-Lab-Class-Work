stack = []
stack.append(('Name:', 'JIM'))
stack.append((10, 22, 33))
stack.append('S.M.')
stack.append('Sajjad Hossain')
stack.append('Jim')

print('Initial stack:')
print(stack)

print("\nElements popped from the stack:")
print(stack.pop())

print("\nAfter popping the stack:")
print(stack)

print("\nAnother element popped from the stack:")
print(stack.pop())

# Print the stack again
print("\nStack after the second pop:")
print(stack)
