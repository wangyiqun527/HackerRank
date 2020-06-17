# Day 0: Hello world
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)

# DAY 1: DATA TYPES
i = 4
d = 4.0
s = 'HackerRank '
# DECLARE second integer, double, and String variables.
a = 0
b = 0.0
c = "" 
# Read and save an integer, double, and String to your variables.
a = int(input())
b = float(input())
c = str(input())
# Print the sum of both integer variables on a new line.
print(i+a)
# Print the sum of the double variables on a new line.
print(d+b)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+c)

# DAY 2: OPERATORS
def get_total_cost_of_meal():
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    # Write your calculation code here
    tip = meal_cost*tip_percent/100 # calculate tip
    tax = meal_cost*tax_percent/100 # caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost+tip+tax))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")

# DAY 3: INTRO TO CONDITIONAL STATEMENTS


# DAY 9: RECURSION
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(int(input())))
 
 
# DAY 10: Binary Numbers
# Given a base-10 number, convert it to base-2, and find maximum number of consecutive 1's.
print(len(max(bin(int(input().strip()))[2:].split('0'))))

# or:
n = int(input().strip())
bi=bin(n)[2:]
current=0
out=0
for i in range(len(bi)):
    if bi[i]=='1':
        current+=1
        if current>out:
            out=current        
    else:
        current=0
print(out)   

# DAY 11: 2D arrays
# Given a 6 by 6 2D array, find the largest sum of a hourglass shape.
import sys
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
   
c=arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2]
for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        hourglass=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        if hourglass>c:
            c=hourglass
print(c) 
    
# or:
res = []
for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)
	
print(max(res))



# DAY 12: # Class Inheritance 
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.

    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.

    def calculate(self):
        a=sum(self.scores)/len(self.scores)
        if a >= 90:
            return 'O'
        elif 90>a>=80:
            return 'E'
        elif 80>a>=70:
            return 'A'
        elif 70>a>=55:
            return 'P'
        elif 55>a>=40:
            return 'D'
        else:
            return 'T'        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())


# DAY 13: # abstract class
#Write MyBook class
class MyBook:
    price = 0
    def __init__(self, title, author, price):
        self.price = price 
        self.title=title
        self.author=author

    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price: "+ str(price))


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()



# DAY 14: # Class scope
# find maximum difference between 2 elements in a list
class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        self.maximumDifference = max(a) - min(a) 
        
# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference) 

# or:
def computeDifference(self):
    self.maximumDifference = abs(max(self.__elements) - min(self.__elements)) 
    
def computeDifference(self):
    self.maximumDifference = max([abs(x-y) for x in self.numbers for y in self.numbers])


# DAY 15: # Linked List
# Complete the insert function in your editor so that it creates a new Node (pass data as 
# the Node constructor argument) and inserts it at the tail of the linked list referenced 
# by the head parameter. Once the new node is added, return the reference to the head node.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head
  
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	


# DAY 16: Exceptions - String to Integer 
# convert a string to integer, print out, o/w print "Bad String"
#!/bin/python3

import sys

S = input().strip()
try:
    print(int(S))
except ValueError: 
    print ("Bad String")



# Day 17: More exceptions
# Write a Calculator class with a single method: int power(int,int). The power method takes
# two integers, n and p, as parameters and returns the integer result of . If either n or p is
# negative, then the method must throw an exception with the message: n and p should be non-negative.
class Calculator:   
    def power(self,n,p):
        self.n=n
        self.p=p
        if n<0 or p<0:
            return ValueError('n and p should be non-negative') 
        else:
            return n**p
            
              
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
        

# DAY 18: Queues and Stacks
class Solution:
    # Write your code here
      def __init__(self):
          self.mystack = list()
          self.myqueue = list()
          return(None)

      def pushCharacter(self, char):
          self.mystack.append(char)

      def popCharacter(self):
          return(self.mystack.pop(-1))

      def enqueueCharacter(self, char):
          self.myqueue.append(char)

      def dequeueCharacter(self):
          return(self.myqueue.pop(0))

    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  
    
# DAY 19: interfaces JAVA skipped. 

# DAY 20: Sort
# bubble sort
import sys
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps=0
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]  ## !!!!!! instead of swap. 
            swaps+=1

print('Array is sorted in',swaps,'swaps.')   
print('First Element:',a[0])
print('Last Element:',a[-1])

     
# DAY 21: Generics JAVA. skipped

# DAY 22: Binary Search Trees
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
        
    def getHeight(self,root):
        #Write your code here
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)
            
            if leftDepth > rightDepth:
                return leftDepth + 1
            else: 
                return rightDepth + 1
        else:
            return -1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height) 

# binary insert:
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)    
r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
print "in order:"
in_order_print(r)
print "pre order"
pre_order_print(r)

# DAY 23: BST level traversal
# A level-order traversal, also known as a breadth-first search, visits
# each level of a tree's nodes from left to right, top to bottom. 
# You are given a pointer, root, pointing to the root of a binary search tree. 
# Complete the levelOrder ft so that it prints the level-order traversal of BST.
# add to the class Solutions
def levelOrder(self,root):
    queue = [root] if root else []
    
    while queue:
        node = queue.pop()
        print(node.data, end=" ")
        
        if node.left: queue.insert(0,node.left)
        if node.right: queue.insert(0,node.right)

# DAY 24: More linked list
# remove duplicates
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def removeDuplicates(self,head):
        #Write your code here
        current = head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 


# DAY 25: Running time and complexity
t=int(input())
def is_prime(x):
    if x>1:
        for i in range(2, int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    else:
        return False
    
                   
for _ in range(t):
    n=int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')
        
# DAY 26: nested logic
borrow=[int(x) for x in input().split()]
due=[int(x) for x in input().split()]
d1,m1,y1=borrow[0],borrow[1],borrow[2]
d2,m2,y2=due[0],due[1],due[2]
if y1>y2:
    print(10000)
elif y1==y2:
    if m1>m2:
        print(500*(m1-m2))
    if m1==m2:
        if d1>d2:
            print(15*(d1-d2))
        elif d1<=d2:
            print(0)
    if m1<m2:
        print(0)
elif y1<y2:
    print(0)    
  
