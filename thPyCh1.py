x = 3;
print("x is ",x);

#Exercise 1

#1) In a print statement, what happens if you leave out one or both of the parentheses?
# If you leave out one or both of the parentheses you will get a syntax error
# for example, print("Hello World" or print"Hello World") would give syntax errors
print("Hello World");
# ^^ you need both parentheses in the print command for it to work

#2) If you are trying to print a string, what happens if you leave out one/both of the quotation marks (or apostrophes)?
# a command like print(hello world") or print("hello world) would return a syntax error because you need both quotation marks (or apostrophes)
print('Hello World')
# print commands work with both quotations or apostrophes, as long as you have both at the start and end of the string

#3) You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
# putting a plus sign before a number doesn't affect it if its an int and not a string
print(+2);
# prints 2
print("+2");
# prints +2
print(2++2);
# prints 4
# putting multiple plus signs between 2 numbers doesnt change anything, still only adds the 2 numbers

#4) In math notation, leading zeros are ok, as in 09. What happens if you try this in Python? What about 011?
#print(08 + 04);
# you get a syntax error for the above message, because you cant have leading zeroes in Python
#the error reads: "SyntaxError: leading zeros in decimal integer literals are not permitted"

#5) What happens if you have two values with no operator between them?
#print(4 7);
#the above print command also returns a syntax error


#Exercise 2

#Start the Python interpreter and use it as a calculator.
#How many seconds are there in 42 minutes 42 seconds?
minutes = 42;
seconds = 42;
secInMin = minutes * 60;
totalSeconds = seconds + secInMin;
print("There are "+str(totalSeconds)+" seconds in "+str(minutes)+" minutes and "+str(seconds)+" seconds.");
#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilometers = 10;
miles = kilometers / 1.61;
print("There are "+str(miles)+" miles in "+str(kilometers)+" kilometers.");
#If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes -and seconds)? What is your average speed in miles per hour?
secPerMi = totalSeconds/miles
print(str(secPerMi)+" seconds per mile");
print(str(secPerMi//60)+" minutes and "+str((totalSeconds/miles)%60)+" seconds per mile");

print("x is still",x);
