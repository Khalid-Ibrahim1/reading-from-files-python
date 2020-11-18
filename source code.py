import tkinter as tk
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
import json

#----
Tobj = Tk() #tkinter object
Tobj.title("Select file")
Message(Tobj,text= "Select the data file",font = 120).grid(padx = 50,pady = 50)
file_path = filedialog.askopenfilename(filetypes = [("json data file","*.json")]) #aks the user to select the json data file
Tobj.withdraw()


with open(file_path) as i:  #here python opens the data file that was selected from the code above
    data = json.load(i)     #here assign the data file to val "data"

#----
number_of_members = len(data["Members"])    #calculating the number of members in the data file using the built in function "len()"
#----
def MemberCycling(i):  #this function cycles between members in the data file
    Member = "Member1"
    memedit= list(Member)
        
    memedit[6]= str(i)
    Member = "".join(memedit)   #this function takes the word "Member1" and map it in to a list using "list()" built in function and then 
    return Member               #modefies the last element from "1" to the last member (n) in the datafile

#----
def BookCycling(j):    #this function cycles between books in the data file
    bookstring = "Book1"
    bookedit= list(bookstring) 

    bookedit[4] = str(j)
    bookstring = "".join(bookedit)  #this function takes the word "Member1" and map it in to a list using "list()" built in function and then 
    return bookstring               #modefies the last element from "1" to the last book that is in the member in the datafile

#----
def NumberOfBooks(number_of_members): #Number of books read by the whole group members
    number_of_books = 0
    i = 1
    while i <= number_of_members:#cycle through members and add all books
        number_of_books += int(len(data["Members"][MemberCycling(i)]["Books"]))
        i += 1
    return print("Number of books:", number_of_books,end=".\n\n")
#NumberOfBooks(number_of_members)#func call

#----
def number_of_pages(number_of_members) : #Number of pages read by the whole group members
    number_of_pages = 0

    for f in range(1,number_of_members+1): #to cycle between members
        MemberCycling(f)
        for j in range(1,len(data["Members"][MemberCycling(f)]["Books"])+1): #to cycle between books
            number_of_pages += int(data["Members"][MemberCycling(f)]["Books"][BookCycling(j)]["Number of pages"]) 
    return print("Total number of pages:", number_of_pages,end= ".\n")
#number_of_pages(number_of_members)#func call

#----
def RankingOfCategories(number_of_members) : #Ranking of books categories mostly read by the group members
    categories = []
    count_categories = {}

    for f in range(1,number_of_members+1): #to cycle between members
        MemberCycling(f)
        for j in range(1,len(data["Members"][MemberCycling(f)]["Books"])+1): #to cycle between books
            categories.append(data["Members"][MemberCycling(f)]["Books"][BookCycling(j)]["Category"]) # add the category to the list categories

    categories.sort() #sort the list using sort() built in function
    
    for cat in categories:          #here the loop cycles every category that is in var "categories" and then if the category is not already in the dict "count_categories" the if statement makes
        if cat in count_categories: #the category a key value and initialize it by "1" after that if the category is already available it adds one to the key value
            count_categories[cat] += 1
        else:
            count_categories[cat] = 1
            
    count_categories_sorted = sorted(count_categories, key=count_categories.get, reverse=True) #here we sorted the dict using "sorted()" built in function and gave it "count_categories" to cycle through
    counter = 0                                                                                # and using "key=count_categories.get" we get the values of each category and then sort by the values of the keys
    count_categories_sorted_len = len(count_categories_sorted)                                                                                
    print('Ranking of books categories mostly read by the group members: ')
    for c in count_categories_sorted: #printing the dict
        counter +=1
        if counter == count_categories_sorted_len:
            print(c + ":", count_categories[c], end=".\n")
        else:
            print(c + ":", count_categories[c], end=", ")
    
    cate = list(count_categories.keys())    #here we used the built-in func called Matplotlib to make the charts
    values_cat = list(count_categories.values())
    plt.bar(cate,values_cat,label="Books")  #to implement a bar chart
    plt.title("Ranking of categories.")
    plt.legend()    
    plt.xlabel('Categories')
    plt.ylabel('Number of books')   
    plt.show()             
#RankingOfCategories(number_of_members)#func call

#----
def RankingBasedOnBooksRead(number_of_members): #Ranking of group members based on number of books read
    print()
    count_books = {} #dict to store the total number books read by members
    m = 1
    while m <= number_of_members: #to cycle between members
        count_books[MemberCycling(m)] = len(data["Members"][MemberCycling(m)]["Books"]) #it puts the total number of books in the current member in count_books
        m += 1

    countbooks_sorted = sorted(count_books, key=count_books.get, reverse=True) #sort the dict count_books using "sorted()" built in function
    print('Ranking of group members based on number of books read: ')

    countbooks_sorted_len = len(countbooks_sorted)
    counter =0
    for b in countbooks_sorted: #printing the dict
        counter += 1
        if counter == countbooks_sorted_len:
            print(b + ":", str(count_books[b]) + " Books",end=".\n")
        else:
            print(b + ":", str(count_books[b]) + " Books", end=", ")
    
    books = list(count_books.keys())
    value_books = list(count_books.values())
    plt.bar(books,value_books,color='#444444' ,label="Books")   #here we used the built-in func called Matplotlib to make the charts
    plt.title("Ranking based on books read.")
    plt.legend()
    plt.xlabel("Members")
    plt.ylabel("Number of books read")
    plt.show()     
#RankingBasedOnBooksRead(number_of_members)#fun call

#----
def RankingBasedOnPagesRead(number_of_members): #Ranking of group members based on number of pages read
    print()
    number_of_pages = 0
    countpages = {} #dict to store the total number of pages read by a member
   
    for m in range(1,number_of_members+1):  #to cycle between members
        MemberCycling(m)
        number_of_pages = 0  #reset the number of pages to 0, so they don't add up with other members
        for j in range(1,len(data["Members"][MemberCycling(m)]["Books"])+1): #to cycle between books to get number of pages
            
            number_of_pages += int(data["Members"][MemberCycling(m)]["Books"][BookCycling(j)]["Number of pages"]) #adding number of pages
            countpages[MemberCycling(m)] = number_of_pages #putting it the dict
    
    countpages_sorted = sorted(countpages, key=countpages.get, reverse=True) #sort the dict countpages
    countpages_sorted_len = len(countpages_sorted)
    print('Ranking of group members based on number of pages read: ')
    counter = 0
    for b in countpages_sorted: #printing the dict
        counter += 1
        if counter == countpages_sorted_len:
            print(b + ":", str(countpages[b]) + "p",end=".\n")
        else:
            print(b + ":", str(countpages[b]) + "p", end=", ")
    
    pages = list(countpages.keys())
    value_pages = list(countpages.values())
    plt.bar(pages,value_pages,color="g" ,label="Pages")   #here we used the built-in func called Matplotlib to make the charts
    plt.title("Ranking based on Pages read.")
    plt.legend()
    plt.xlabel("Members")
    plt.ylabel("Number of Pages read")
    plt.show()    
#RankingBasedOnPagesRead(number_of_members)#func call

#----
Tobj = Tk() #object for the tkinter
Tobj.title("CS213 Project") 
def TaskOne():
    Label(Tobj, command= NumberOfBooks(number_of_members))
    return
def TaskTwo():
    Label(Tobj, command= number_of_pages(number_of_members))
    return
def TaskThree():
    Label(Tobj, command= RankingOfCategories(number_of_members))
    return
def TaskFour():
    Label(Tobj, command= RankingBasedOnBooksRead(number_of_members))
    return
def TaskFive():
    Label(Tobj, command= RankingBasedOnPagesRead(number_of_members))    #functions for the buttons in the gui
    return

ButtonOne = Button(Tobj, text= "Task One",padx= 10,pady=10, command = TaskOne)
ButtonOne.grid(row=0, column=0)
ButtonTwo = Button(Tobj, text= "Task Two",padx= 10,pady=10,command = TaskTwo)
ButtonTwo.grid(row=1, column=0)
ButtonThree = Button(Tobj, text= "Task Three",padx= 10,pady=10,command = TaskThree)
ButtonThree.grid(row=2, column=0)
ButtonFour = Button(Tobj, text= "Task Four",padx= 10,pady=10,command = TaskFour)
ButtonFour.grid(row=0, column=4)
ButtonFive = Button(Tobj, text= "Task Five",padx= 10,pady=10,command = TaskFive)
ButtonFive.grid(row=1, column=4)
ButtonExit = Button(Tobj, text= "Exit",padx= 10,pady=10,command = Tobj.quit)
ButtonExit.grid(row=2, column=4)    #here's the gui buttons and there placement
Tobj.mainloop()