#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

#Pseudocode

# Set a starting point
print("Printing current and previous number sum in a range(10)")

# Set the previous number to 0
previous_number = 0

# Create an loop for 10 numbers that is even numbers  (start = 0, stop = 20, step = 2)
for current_number in range(0, 20, 2):

    # Create an arithemtic expression to express the sum of previous and current number
    sum = previous_number + current_number

    # Print the values 
    print("The previous number is " + str(previous_number), "The current value of " + str(current_number) , "The sum is " + str(sum) ) 

    #Update the previous_number for the next iteration
    previous_number = current_number
   
        
    


