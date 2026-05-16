# This is a simple Python program that greets the user and asks for their name and job.
print (" Hello World ")
user_name = input("What is your name? ")
user_name = user_name.strip().title() # Remove any leading or trailing whitespace and convert the name to title case (first letter of each word capitalized)
#user_name = input("What is your name? ").strip().title() This can be also used instead of 2 lines we can do it in a single line
first_name = user_name.split()[0] # Get the first name by splitting the full name and taking the first element
print (f"Hello {first_name}!")
print ("Welcome to Python programming!")    
user_job = input("What is your job? ")
user_job = user_job.strip().title() # Remove any leading or trailing whitespace and convert the job to title case (first letter of each word capitalized)
#user_job = input("What is your job? ").title().split() This can be also used instead of 2 lines we can do it in a single line
print (f"Wow! {user_job} is a great job!")
print (f"UPPERCASE Name: {user_name.upper()} ")
print (f"UPPERCASE Job: {user_job.upper()} ")
