
# question 1 & 2
#my_string = input("Enter a string: ")


#i = 0 


#while i < len(my_string) and not my_string[i].isdigit():
#        i += 1

#if i < len(my_string):
#    j = i
#    while j < len(my_string) and not my_string[j].isalpha():
#        j += 1
#    print(my_string[i:j-1], i)
#else:
#    print("no numbers here")
    
    
    
#question 3

#string = input("Enter a string: ")

#repdigit_found = False

#i = 0
#while i < len(string) and not repdigit_found:
#    j = i + 1
#    while j < len(string) and not string[i] == string[j]:
#        i += 1
#        j += 1
    
#    if j < len(string):

#        while j < len(string) and string[i] == string[j]:
#            j += 1

#        if string[i] == string[j-1]:
#            repdigit_found = True
#            print(string[i:j])
    
#    i = j + 1


 #question 4 
 
q4_string = input("Enter some text: ")
find = input("What word would you like to search for? ")
 
occurences = 0
 
i = 0
while i < len(q4_string):
    j = i
    while j < len(q4_string) and not q4_string[j] == find[0]:
        j += 1
         
    if j <len(q4_string) and q4_string[j:j+len(find)] == find:
           occurences += 1 
 
    i = j+ 1
    
print("The word '" + find + "' occurs " + str(occurences) + " times.  ")