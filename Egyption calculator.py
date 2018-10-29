#Author: Hussein Sahib
#Course: Introduction to programming 142
#Date: December 10 2016
#Program informarion: This program is a Egyption fraction calculator,
#it takes a pizza number and number of students then outputs the Egyption fraction for pizza over student.
#for extra credit I added a function called extracredit that will give the user, the nearest number practical number if students are are not practical number.  


import itertools
def factor(students): # This function takes the numbers of students and returns it's factors
    factorList = []
    # This for loop will calculate the factors of students.    
    for num in range(1,students+1): 
        dfactor = students / num
        intfactor = students // num 
        if dfactor == intfactor:
            factorList.append(num) 
    return factorList
def sumsOfSublists(lst): #This function takes the factorList from the number students and out puts the sum of the sublists (sumList)
    sumList = []
    # This for loop sum of the sub List    
    for i in range(2, len(lst)+1):
       zlist = list(itertools.combinations(lst,i))
       for el in zlist:
           sumList.append(sum(el))
    return sorted(sumList)       
def fraction(factorList,students,pizza): # This function takes in the factor list of students, the number students and the number pizza and returns a print statment for the Egyption fractions.
    count = 0
    strList = []
    division = 0
    factorList = factorList[::-1] # reverses the List
    # This for loop will subtract the sublists of the factorList and then append the resulr to strList     
    for num in factorList:
        if (pizza - num) >= 0:
            division = int(students/num)
            strList.append(division)
            pizza = pizza - num
    # This for loop will look at each character and prints it in the form of 1/n           
    for char in strList:
        count += 1
        if count == 1:
            print('1/{} '.format(char), end = '')
        else:
            print('+ 1/{} '.format(char), end = '')
    print()    #prints empty line (I used print in this function instead of return because I think it is a shorter way to do it)


def extracredit(students): #This function takes in the number of students if it is not a practical number and returns the nearest practical number. 
    count = 0
    #This for loop will go throug range student into 100 number bigger than student and then resets count every time it goeses through the loop    
    for num in range(students+1, students+100):
        count = 0
    #This for loop checks if num is a practical number and return it if it is a practical number        
        for char in range(1, num+1):
            if char in (sumsOfSublists(factor(num)) + factor(num)):
                count += 1
        if count == num: 
            return num 
def main(): # this is the main function.
    print('Welcome !')
    print('We calculate Egiption fractions') 
    repeat = 'y'
    # this while loop will keep the program going until the user decides to stop.    
    while repeat == 'y':
        
        count = 0
        pizza = int(input("Enter pizzas: "))
        students = int(input("Enter students: "))
        if students > pizza and students >= 0 and pizza >= 0 and students == int(students) and pizza == int(pizza):
            
            print("Denominator factors: {}".format(factor(students)))
            # this for loop checks if this student is a practical num then it prints             
            for num in range(1, students+1):
                if num in (sumsOfSublists(factor(students)) + factor(students)):
                    count += 1
            if count == students:                                                         # this if it is practical number ELSE
                print("Students are practical number")
                fraction(factor(students),students,pizza)
            else :                                                                        # it prints this and    
                print("Students are not practical number")
                print("{} is the nearest practical number".format(extracredit(students))) # runs this function with print statment
        else:
            print("You enter invalid pizza or student number")
        repeat = (input("Do you want to repeat the program? Enter y for yes, anything for no: ")).lower()    
    print('Thank you for using our calcullator, please come again :) ')        
main()    # call main function
        
               
