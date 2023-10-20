text='a cat is an animal'
lim=6

done = False
output = []
counter = 0

while not done:
    space_index = text.index(' ')
    if len(text[counter:space_index+1]) <= lim:
        next_space_index = text[space_index+1:].index(' ')
        if len(text[counter:next_space_index+1]) > lim:
            start=counter
            counter = next_space_index
        else:
            start=counter
            counter = space_index
        output.append(text[start:counter])
    print(output)