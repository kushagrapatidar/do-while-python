# Initialization expression (Change 'i=10' as per need)
i=10

# Conditional Statement
def conditional_statement(i):
    #Change the conditional statement 'i<10 and i>=0' as per need
    return i<10 and i>=0

# Conditional Statement for the loop. Do not tinker with below statement
def loop_conditional_statement(i):
    return conditional_statement(i) or not conditional_statement(i)

# Using the loop_conditional_statement, 1st iteration of the while loop runs un-conditionally and later the loop runs condition based
# Do Not Tinker with loop initialization
while loop_conditional_statement(i):
    # Body of the loop. Change as per need
    print("Hello World")
    
    i-=1
    
    # End of Body
    
    # Check the feasibility of the condtional_statement after the first execution
    # for exit control of the while loop
    # Do not tinker with below statement
    if not conditional_statement(i):
        break

