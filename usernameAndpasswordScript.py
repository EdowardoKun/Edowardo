# A function that saves an input username and password
import re

def SaveFile(userp, usern):
    Filereader = "" # The location of the text file

    while True: # start a while loop, so i can have the option to use break

        with open(Filereader, 'a') as textwrite: # open the text file using append mode

            if re.match(r'\d[0-9]{8,40}', userp): # creating a restriction system using regex so that the input could only consist of numbers from 8 to 0.
                textwrite.write("\nPassword: " + userp) # save the password inside the text file
                print("Your password was successfully saved") # confirm the password inside the program

                break # close the while loop

            else:
                print("ERROR: Your password must be atleast 8 digits long, and has to have no marks/signs") # shows an ERROR if password did not get accepted
                break # closes the loop


    while True: # starts another while loop

        with open(Filereader, 'a') as textwrite: # opens the text file again
            if len(usern) > 2: # put a condition so only a word with more than 2 letters can pass
                textwrite.write("\nUsername: " +usern) # save the username into the text file
                textwrite.write("\n")

                textwrite.close() # close the text file
                print("Your username was successfully saved") # confirm the username success using print

                break # closes/breaks the loop

            else:
                print("ERROR: Your username must have at least 3 letters ") # shows an error if the username does not have more than 2 letters
                break # closes the loop




print(SaveFile(input(), input()))



