from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import matplotlib.pyplot as plt
import json

#----

Tobj = Tk() #tkinter object
Tobj.withdraw()
file_path = filedialog.askopenfilename(title= "Select the data file(.Json)",filetypes = [("json data file","*.json")]) #aks the user to select the json data file
Tobj.withdraw()


with open(file_path) as i:  #here python opens the data file that was selected from the code above
    data = json.load(i)     #here assign the data file to var "data"


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
    print_number = "Number of books:" + str(number_of_books)
    messagebox.showinfo("Task One", print_number)

#NumberOfBooks(number_of_members)#func call

#----

def number_of_pages(number_of_members) : #Number of pages read by the whole group members
    number_of_pages = 0

    for f in range(1,number_of_members+1): #to cycle between members
        MemberCycling(f)
        for j in range(1,len(data["Members"][MemberCycling(f)]["Books"])+1): #to cycle between books
            number_of_pages += int(data["Members"][MemberCycling(f)]["Books"][BookCycling(j)]["Number of pages"]) 
    print_pages = "Total number of pages:" + str(number_of_pages)
    messagebox.showinfo("Task two", print_pages)

#number_of_pages(number_of_members)#func call

#----

def RankingOfCategories(number_of_members) : #Ranking of books categories mostly read by the group members
    plt.figure(figsize=(15,5))
    categories = []
    count_categories = {}

    for f in range(1,number_of_members+1): #to cycle between members
        MemberCycling(f)
        for j in range(1,len(data["Members"][MemberCycling(f)]["Books"])+1): #to cycle between books
            categories.append(data["Members"][MemberCycling(f)]["Books"][BookCycling(j)]["Category"]) # add the category to the list categories
    
    for cat in categories:          #here the loop cycles every category that is in var "categories" and then if the category is not already in the dict "count_categories" the if statement makes
        if cat in count_categories: #the category a key value and initialize it by "1" after that if the category is already available it adds one to the key value
            count_categories[cat] += 1
        else:
            count_categories[cat] = 1
            
    count_categories_sorted = dict(sorted(count_categories.items(), key= lambda x:x[1],reverse= True)) #here we sorted the dict using "dict(sorted())" built in function and gave it "count_categories" to cycle through

    """
    counter = 0 # and using "key=count_categories.get" we get the values of each category and then sort by the values of the keys
    count_categories_sorted_len = len(count_categories_sorted)                                                                                
    print('Ranking of books categories mostly read by the group members: ')
    for c in count_categories_sorted: #printing the dict
        counter +=1
        if counter == count_categories_sorted_len:
            print(c + ":", count_categories[c], end=".\n")
        else:
            print(c + ":", count_categories[c], end=", ")
    """
    plt.bar(count_categories_sorted.keys(),count_categories_sorted.values(),label="Books")  #to implement a bar chart
    plt.title("Ranking of categories.")
    plt.legend()    
    plt.xlabel('Categories')
    plt.ylabel('Number of books')
    plt.gcf().canvas.set_window_title("Task Three")
    plt.show()

#RankingOfCategories(number_of_members)#func call

#----

def RankingBasedOnBooksRead(number_of_members): #Ranking of group members based on number of books read
    plt.figure(figsize=(15,5))
    count_books = {} #dict to store the total number books read by members
    m = 1
    while m <= number_of_members: #to cycle between members
        count_books[MemberCycling(m)] = len(data["Members"][MemberCycling(m)]["Books"]) #it puts the total number of books in the current member in count_books
        m += 1

    countbooks_sorted = dict(sorted(count_books.items(), key= lambda x:x[1],reverse= True)) #sort the dict count_books using "dict(sorted())" built in function

    """
    print('Ranking of group members based on number of books read: ')
    countbooks_sorted_len = len(countbooks_sorted)
    counter =0
    for b in countbooks_sorted: #printing the dict
        counter += 1
        if counter == countbooks_sorted_len:
            print(b + ":", str(count_books[b]) + " Books",end=".\n")
        else:
            print(b + ":", str(count_books[b]) + " Books", end=", ")
    """
    plt.bar(countbooks_sorted.keys(),countbooks_sorted.values(),color='#444444' ,label="Books")   #here we used the built-in func called Matplotlib to make the charts
    plt.title("Ranking based on books read.")
    plt.legend()
    plt.xlabel("Members")
    plt.ylabel("Number of books read")
    plt.gcf().canvas.set_window_title("Task four")
    plt.show()     

#RankingBasedOnBooksRead(number_of_members)#fun call

#----

def RankingBasedOnPagesRead(number_of_members): #Ranking of group members based on number of pages read
    plt.figure(figsize=(15,5))
    number_of_pages = 0
    countpages = {} #dict to store the total number of pages read by a member
   
    for m in range(1,number_of_members+1):  #to cycle between members
        MemberCycling(m)
        number_of_pages = 0  #reset the number of pages to 0, so they don't add up with other members
        for j in range(1,len(data["Members"][MemberCycling(m)]["Books"])+1): #to cycle between books to get number of pages
            
            number_of_pages += int(data["Members"][MemberCycling(m)]["Books"][BookCycling(j)]["Number of pages"]) #adding number of pages
            countpages[MemberCycling(m)] = number_of_pages #putting it the dict
    
    countpages_sorted = dict(sorted(countpages.items(), key= lambda x:x[1],reverse= True)) #sort the dict countpages

    """
    countpages_sorted_len = len(countpages_sorted)
    print('Ranking of group members based on number of pages read: ')
    counter = 0
    for b in countpages_sorted: #printing the dict
        counter += 1
        if counter == countpages_sorted_len:
            print(b + ":", str(countpages[b]) + "p",end=".\n")
        else:
            print(b + ":", str(countpages[b]) + "p", end=", ")
    """
    plt.bar(countpages_sorted.keys(),countpages_sorted.values(),color="g" ,label="Pages")   #here we used the built-in func called Matplotlib to make the charts
    plt.title("Ranking based on Pages read.")
    plt.legend()
    plt.xlabel("Members")
    plt.ylabel("Number of Pages read")
    plt.gcf().canvas.set_window_title("Task five")
    plt.show()    

#RankingBasedOnPagesRead(number_of_members)#func call

#----

Tobj = Tk() #object for the tkinter
Tobj.title("CS213 Project") 
def TaskOne():
    NumberOfBooks(number_of_members)
    return
def TaskTwo():
    number_of_pages(number_of_members)
    return
def TaskThree():
    RankingOfCategories(number_of_members)
    return
def TaskFour():
    RankingBasedOnBooksRead(number_of_members)
    return
def TaskFive():
    RankingBasedOnPagesRead(number_of_members)    #functions for the buttons in the gui
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
