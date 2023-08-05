# Name - PARMESH YADAV  
# Roll No - 2020319

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

    print('Welcome to my code')
    print()
    print('Following are the queries that can be performed...')
    print()
    print('1. Print All Data')
    print('2. Filter Data by FIRST NAME')
    print('3. Filter Data by LAST NAME')
    print('4. Filter Data by FULL NAME')
    print('5. Filter Data by AGE RANGE')
    print('6. Count By Gender')
    print('7. Filter Data by ADDRESS')
    print('8. Find Alumni of an Institute')
    print('9. Find Topper of each institute')
    print('10. Find Blood Donors')
    print('11. Get Common Friends')
    print('12. Find if Related on not')
    print('13. Delete an entry by ID')
    print('14. Add Friend')
    print('15. Remove Friend')
    print('16. Add Education')

    records = read_data_from_file()

    while True:

        choice = int(input('Enter query code(1-16) you wish to perform....to stop enter -1'))

        if choice == -1:
            break

        elif choice == 1:
            print(records)

        elif choice == 2:
            first_name = input('Enter FIRST Name You Wish To Search For')
            if first_name.isalpha():
                print(filter_by_first_name(records,first_name))
            else:
                print('FIRST should be alphabet only')

        elif choice == 3:
            last_name = input('Enter LAST Name You Wish To Search For')
            if last_name.isalpha():
                print(filter_by_last_name(records,last_name))
            else:
                print('LAST should be alphabet only')

        elif choice == 4:
            full_name = input('Enter FULL Name You Wish To Search For')
            print(filter_by_full_name(records,full_name))

        elif choice == 5:
            minage = int(input('Enter the MIN age.'))
            maxage = int(input('Enter the MAX age.'))
            print(filter_by_age_range(records,minage,maxage))

        elif choice == 6:
            print(count_by_gender(records))

        elif choice == 7:
            houseno = int(input('Enter House no....enter 0 to skip.'))
            Block = input('Enter Block...press enter to skip.')
            Town = input('Enter Town...press enter to skip.')
            City = input('Enter City...press enter to skip.')
            State = input('Enter State...press enter to skip.')
            Pincode = int(input('Enter Pincode....enter 0 to skip.'))
            d  = {'house_no':houseno,'block':Block,'town':Town,'city':City,'state':State,'pincode':Pincode}
            d_ = dict()
            for i in d:
                if d[i] == 0 or d[i] == '':
                    None
                else:
                    d_[i] = d[i]
            print(d_)

            print(filter_by_address(records,d_))

        elif choice == 8:
            institutename = input('Enter the name of the institute you wish to know the alumni of')
            if institutename.isalpha():
                print(find_alumni(records,institutename))

        elif choice == 9:
            print(find_topper_of_each_institute(records))

        elif choice == 10:
            recieversid = int(input('Enter recievers ID'))
            print(find_blood_donors(records,recieversid))

        elif choice == 11:
            listofids = list()
            n = int(input('Enter for how many people you wish to find out the common friends for'))
            for i in range(n):
                a = int(input('Enter the persons ID'))
                listofids.append(a)
            print(get_common_friends(records,listofids))

        elif choice == 12:
            personid1 = int(input('Enter ID of the First Person'))
            personid2 = int(input('Enter ID of the Second Person'))
            print(is_related(records,personid1,personid2))

        elif choice == 13:
            personid = int(input('Enter the ID of the Person whose record you wish to be deleted'))
            records = delete_by_id(records,personid)

        elif choice == 14:
            personid = int(input('Enter the ID of one of the people you wish to make friends'))
            friendid = int(input('Enter the ID of the other.'))
            records = add_friend(records,personid,friendid)

        elif choice == 15:
            personid = int(input('Enter the ID of one of the people you wish to remove as friends'))
            friendid = int(input('Enter the ID of the other.'))
            records = remove_friend(records,personid,friendid)

        elif choice == 16:
            personid = int(input('Enter the Id of the person you wish to add an education for.'))
            institutename = input('Enter the Institute Name')
            ongoing = bool(int(input('Enter if the person is still going to this institute.....enter 1 for True and 0 for False')))
            if ongoing == True:
                Percentage = 0
            else:
                Percentage = int(input("Enter the acquired Percentage"))
            records = add_education(records,personid,institutename,ongoing,Percentage)

        else:
            print('Invalid code Entered. TRY AGAIN!')
    print('Thank You!')




main()

