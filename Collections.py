def lists():
    list_example_1 = ['kiwi','pucca','garu']
    print (list_example_1,'\n')
    
    list_example_1.append('alvin')
    print (list_example_1,'\n')

    list_example_1.pop()
    print (list_example_1,'\n')

    list_example_1.insert(0, 'apple')
    print (list_example_1,'\n')

    list_example_1.insert(0, 'Strawberry')
    print (list_example_1,'\n')

    list_example_1.pop(4)
    print (list_example_1,'\n')

    list_example_1.remove('pucca')
    print (list_example_1,'\n')

def pyramid_sum(lower, upper, margin = 0):
    blanks = " " * margin
    print(blanks, lower, upper) # Print the arguments

    if lower > upper:
        print(blanks, 0) # Print the returned value
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result) # Print the returned value
        return result


if __name__=="__main__":

    pyramid_sum(1, 4)
    