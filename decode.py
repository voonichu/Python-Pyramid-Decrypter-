def decode(message_file):
    file = open(message_file, "r")
    content = file.readlines()
    
    num_string = ""
    smallest = 100000
    sorted_lines = []
    num_list = []
    countdown = len(content)
    Sorted = True
    while Sorted:
        for i in range(len(content)):
            for j in range(len(content[i])):
                if content[i][j].isdigit():
                    num_string += content[i][j]
            num = int(num_string)
            num_list.append(num)
            num_string = ""
            if num < smallest:
                smallest = num
        for x in range(len(num_list) - 1):
            if num_list[x] == smallest:
                index = num_list.index(num_list[x])
                sorted_lines.append(content[index])
                content.remove(content[index])
                num_list.remove(num_list[x])
                smallest = 100000
                countdown -= 1
        if countdown == 0:
            Sorted = False

    prism_size = 0
    stepper = 1
    message = []
    for i in range(len(sorted_lines)):
        if prism_size == i:
            message.append(sorted_lines[i])
            stepper += 1
            prism_size += stepper 
        
    for i in message:
        print(i)
    
    write_file(message)
    
    file.close()
    

def write_file(message):
    file = open("decoded_message.txt", "w")
    
    for i in message:
        file.write(i)
    
    file.close()
    


encrypted = input("What is the filename that you want to decode?\n")   
decode(encrypted)