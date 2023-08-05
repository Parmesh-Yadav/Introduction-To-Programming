# Name - Dhruv Gupta
# Roll No - 2020429
from a2 import *
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
    print('Welcome!')
    print('Here is the list of all options')
    print('1) Print all Data')
    print('2) Filter by First Name')
    print('3) Filter by Last Name')
    print('4) Filter by Full Name')
    print('5) Filter by Age')
    print('6) Count by Gender')
    print('7) Filter by Address')
    print('8) Find Alumni')
    print('9) Find topper of each institute')
    print('10) Find blood donors')
    print('11) Find common friends ')
    print('12) Related to: ')
    print('13) Delete by ID')
    print('14) Add Friend')
    print('15) Remove Friend')
    print('16) By Education')
    D=0 
    r = read_data_from_file(file_path="D:\college\sem 1\ip\Assignment_2\IP_Assignment_2\Final Code\data.json")
    while D!=-1:
        D=int(input('ENTER OPTION NUMBER'))
        if D==1:
            print(read_data_from_file(file_path="D:\college\sem 1\ip\Assignment_2\IP_Assignment_2\Final Code\data.json"))
        elif D==2:
            first_name=input('Enter First Name: ')
            print(filter_by_first_name(r, first_name))
        elif D==3:
            last_name=input('Enter Last Name: ')
            print(filter_by_last_name(r, last_name))
        elif D==4:
            full_name=input('Enter Full Name: ')
            print(filter_by_full_name(r, full_name))
        elif D==5:
            print('Enter Age: ')
        elif D==6:
            print(count_by_gender(r))
        elif D==7:
            print('Enter Address: ')
        elif D==8:
            print('Alumini: ')
        elif D==9:
            print('Topper of each institute: ')
        elif D==10:
            print('Blood donors: ')
        elif D==11:
            print('Find common friends: ')
        elif D==12:
            print('Related to: ')
        elif D==13:
            person_id=input('Enter Person ID: ')
            r=delete_by_id(r, person_id)
        elif D==14:
            person_id=input('Enter Person ID: ')
            friend_id=input('Enter Friend ID: ')
            r=add_friend(r, person_id, friend_id)
        elif D==15:
            person_id=input('Enter Person ID: ')
            friend_id=input('Enter Friend ID: ')
            r=remove_friend(r, person_id, friend_id)
        elif D==16:
            print('By education')
    print('Thank you!')
    
main()
    
