# Name - Apoorva Agrawal 
# Roll No - 2020426
from a2 import*

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


def main():
    print("1. all data")
    print("2. filter by first name")
    print("3. filter by last name")
    print("4. filter by full name")
    print("5. filter by age range")
    print("6. count by gender")
    print("7. filter by address")
    print("8. find alumni")
    print("9. find topper of each institute")
    print("10. find blood donors")
    print("11. get common friends")
    print("12. persons related")
    print("13. delete by id")
    print("14. add friends")
    print("15. remove friends")
    print("16. add education")
    A=0
    while A!= -1:
        A= int(input("enter your choice:"))
        if A==1:
            print(read_data_from_file(file_path="C:/Users/hp/Downloads/data.json"))
        elif A==2:
            first_name= input("enter first name:")
            print(filter_by_first_name(Records, first_name))
        elif A==3:
            last_name= input("enter last name:")
            print(filter_by_last_name(Records, last_name))
        elif A==4:
            full_name= input("enter full name:")
            print(filter_by_full_name(Records, full_name))
        elif A==5:
            None
        elif A==6:
            print(count_by_gender(Records))
        elif A==7:
            None
        elif A==8:
            None
        elif A==9:
            None
        elif A==10:
            None
        elif A==11:
            None
        elif A==12:
            None
        elif A==13:
            person_id= input("enter id to delete:")
            Records= delete_by_id(Records, person_id) 
        elif A==14:
            person_id= input("add first id:")
            friend_id= input("add second id:")
            Records= add_friend(Records, person_id, friend_id)
        
        elif A==15:
            person_id= input("add first id:")
            friend_id= input("add second id:")
            Records= remove_friend(Records, person_id, friend_id)
        elif A==16:
            None
    print("thankyou!")
        
main()