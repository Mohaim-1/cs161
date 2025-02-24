Use Pycharm to enter and run your scripts.

You must comment on your code. Explain what each section of code accomplishes.    
 \-5 points if not commented.

When you get your script to work, submit your .py file.

1\.  Write a for or while loop that prints out all the even numbers between two numbers that the user inputs.  A sample run is below.

**Enter the lower number:  36**

**Enter the higher number:  43**

**The even numbers between 36 and 43 are: 36 38 40 42**

 2\.  Write a while loop that prints out all the factors of a given positive integer.  Use the mod operation to check if a certain number evenly divides into the given number.

 **Enter a positive integer:  27**

**The integers that are factors of 27 are:  1 3 9 27**

**Loop \- Iteration**

3\. Given the list **alphabet \= \["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"\]**

And given **your** name as input

Write a simple Python program that uses **Iteration** to calculate the sum of the numeric position of the letters of your last name (or any name). (i.e. cagney: c=2 \+ a=0 \+ g=6 \+ n=13, e=4, y=24 so the sum is 49.)  **Note it starts with “a” as 0 (zero).**

**Recursion**  
4\. Write a recursive function that takes one positive integer as a parameter.  The function will then print all occurrences of the squares of all integers starting at 1 and going to the number that was received as a parameter.  
If the user enters a 4, it should print   
1  
4  
9  
16

**TeePee Sort**  
5\. Given an unsorted list of integers,  
	Write a sort that will create a teepee of the numbers with the largest in the center  
Odd numbers in order to the left ascending from center, Even numbers in order to the right descending from center

Example: unsorted\_list \= (12, 43, 22, 34, 2, 21, 3, 33, 81\)  
	     sorted \_list   \= ( 3, 21, 33, 43, 81, 34, 22,12, 2\)

Lists for evens and list for odds, sort, then each list, concatenate   \+  
Need to compare both lists because largest will b in either list \- so not to duplicate largest number

**Find the next Highest Number**  
6\. Design an algorithm that, when given an arrangement of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, rearranges the digits so that the new arrangement represents the next larger value that can be represented by these digits (or reports that no such rearrangement exists if no rearrangement produces a larger value). Thus 5647382901 would produce 5647382910\.

This can be implemented using recursion.  

Implement your algorithm in Python and submit.

Think about it for a bit, but don’t go crazy.   A solution is on the next page.

Starting from the right end of the input, find the first digit that is smaller than the one to its right. (If there isn't such a digit, no the input cannot be rearranged to represent a larger value.)

 Call the position in the input in which this digit was found the target position.

Interchange the digit found above with the smallest digit to its right that is still larger than itself.

Sort the digits to the right of the target position in descending order from right to left.

9521760834 to

9521760843

