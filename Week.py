def week():
    print('Enter a number from 1 to 7')
    user = int(input())
    if user.__eq__(1):
        print('Monday')
    elif user.__eq__(2):
        print('Tuesday')
    elif user.__eq__(3):
        print('Wednesday')
    elif user.__eq__(4):
        print('Thursday')
    elif user.__eq__(5):
        print('Friday')
    elif user.__eq__(6):
        print('Saturday')
    elif user.__eq__(7):
        print('Sunday')
    else:
        print('Invalid number.Please try again.')


print(week())