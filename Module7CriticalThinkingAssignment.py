def main():
    # Create dictionaries with provided key-value pairs
    CourseNumber_RoomNumber = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755', 'NET110': '1244', 'COM241': '1411'}
    CourseNumber_Instructor = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}
    CourseNumber_MeetingTime = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

    # Create Quit variable for while loop
    Quit = ""

    # Loop to continue the program until user quits
    while Quit != "Y":
        # Prompt user for key
        UserCourse = input("Please enter a course number: ")

        # Attempt to locate the key in the dictionaries and output the corresponding values
        try:
            print("The Room Number is: ", CourseNumber_RoomNumber[UserCourse])
            print("The Instructor is: ", CourseNumber_Instructor[UserCourse])
            print("The Meeting Time is: ", CourseNumber_MeetingTime[UserCourse])
            #Quit = input("Would you like to quit? (Y/N): ")
        # If key not found, handle the exception
        except KeyError:
            print("The Course Number entered was not found.")
        # Always ask the user if they'd like to quit
        finally:
            Quit = input("Would you like to quit? (Y/N): ")

    # Exit program and say bye!
    print("Thanks for using the course lookup dictionary!")
main()