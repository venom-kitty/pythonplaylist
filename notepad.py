# version 1 :D

print("Type '*' to save the file")

lines = []  # Create a list to store all input lines

while True:
    line = input('Add Line\n> ')
    
    if line == '*':
        name = input('\nName your file\n> ')
        
        with open(f'{name}.txt', 'w') as file:
            file.write("\n".join(lines))  # Write all the collected lines to the file
        break  # Exit the loop after saving the file
    else:
        lines.append(line)  # Add each line to the list
