#1: Age Verification System

try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")
    print("Valid age")
except ValueError as e:
    print("Error:", e)



#2: Product Price Checker

try:
    price = float(input("Enter product price: "))
    if price < 0:
        raise ValueError("Price cannot be negative")
    print("Product price:", price)
except ValueError as e:
    print("Invalid price:", e)




#3: Tuple Element Access

cities = ("Delhi", "Mumbai", "Chennai", "Kolkata",
          "Jaipur", "Lucknow", "Prayagraj")

try:
    position = int(input("Enter position (0-6): "))
    print("City:", cities[position])
except IndexError:
    print("Invalid position")
except ValueError:
    print("Please enter an integer")



#4: Contact Information Lookup

contacts = {
    "Aman": "9876543210",
    "Riya": "9123456780",
    "Rahul": "9988776655"
}

try:
    name = input("Enter contact name: ")
    print("Phone number:", contacts[name])
except KeyError:
    print("Contact not found")




#5: File Writing Operation

try:
    filename = input("Enter filename: ")
    text = input("Enter text: ")

    with open(filename, "w") as file:
        file.write(text)

    print("File written successfully")

except PermissionError:
    print("Permission denied")
except OSError as e:
    print("File error:", e)



#6: Valid Roll Number Input

while True:
    try:
        roll = int(input("Enter roll number: "))
        if roll <= 0:
            raise ValueError("Roll number must be positive")
        print("Valid roll number:", roll)
        break
    except ValueError as e:
        print("Invalid input:", e)



#7: Custom Exception for Voting Eligibility


class NotEligibleToVoteError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise NotEligibleToVoteError("Not eligible to vote")
    print("Eligible to vote")
except NotEligibleToVoteError as e:
    print(e)
except ValueError:
    print("Enter a valid age")



#8: Bank Account Deposit Validation

try:
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    print("Deposit successful:", amount)
except ValueError as e:
    print("Error:", e)




#9: Shopping Cart Quantity Check
try:
    quantity = int(input("Enter item quantity: "))
    if quantity < 1:
        raise ValueError("Quantity must be at least 1")
    print("Quantity accepted:", quantity)
except ValueError as e:
    print("Error:", e)



#10: Password Strength Validator

try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    print("Password is valid")
except ValueError as e:
    print("Error:", e)



#11: Student Grade Calculator

try:
    m1 = float(input("Enter marks for subject 1: "))
    m2 = float(input("Enter marks for subject 2: "))
    m3 = float(input("Enter marks for subject 3: "))

    marks = [m1, m2, m3]

    if any(m < 0 or m > 100 for m in marks):
        raise ValueError("Marks must be between 0 and 100")

    total = sum(marks)
    average = total / 3

    print("Total marks:", total)
    print("Average marks:", average)

except ValueError as e:
    print("Error:", e)





#12: ATM PIN Verification

class PINVerificationError(Exception):
    pass

correct_pin = "1234"
attempts = 0

try:
    while attempts < 3:
        pin = input("Enter ATM PIN: ")

        if pin == correct_pin:
            print("PIN verified successfully")
            break

        attempts += 1
        print("Incorrect PIN")

    else:
        raise PINVerificationError("Three attempts failed")

except PINVerificationError as e:
    print("Error:", e)





#13: Email Address Validator

try:
    email = input("Enter email address: ")

    if "@" not in email or "." not in email:
        raise ValueError("Invalid email address")

    print("Email address accepted")

except ValueError as e:
    print("Error:", e)




#14: Division of List Elements

numbers = [10, 20, 0, 40, 50]

try:
    i = int(input("Enter first index (0-4): "))
    j = int(input("Enter second index (0-4): "))

    result = numbers[i] / numbers[j]
    print("Result:", result)

except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter valid integer indexes")





#15: Username Availability Checker

class UsernameExistsError(Exception):
    pass

usernames = ["aman", "riya", "rahul"]

try:
    username = input("Enter a username: ")

    if username in usernames:
        raise UsernameExistsError("Username already exists")

    print("Username is available")

except UsernameExistsError as e:
    print("Error:", e)



#16: Electricity Bill Calculator

try:
    units = float(input("Enter units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 300 + (units - 100) * 5
    else:
        bill = 800 + (units - 200) * 7

    print("Electricity bill: Rs.", bill)

except ValueError as e:
    print("Error:", e)






#17: #Student Record Search

students = {
    101: "Aman",
    102: "Riya",
    103: "Rahul"
}

try:
    student_id = int(input("Enter student ID: "))
    print("Student name:", students[student_id])

except KeyError:
    print("Student record not found")
except ValueError:
    print("Enter a valid student ID")






#18: #Mobile Number Validation

try:
    mobile = input("Enter mobile number: ")

    if not mobile.isdigit() or len(mobile) != 10:
        raise ValueError("Mobile number must contain 10 digits")

    print("Valid mobile number")

except ValueError as e:
    print("Error:", e)






#19: #Online Ticket Booking

class SeatsNotAvailableError(Exception):
    pass

available_seats = 50

try:
    tickets = int(input("Enter number of tickets: "))

    if tickets < 1:
        raise ValueError("Book at least one ticket")

    if tickets > available_seats:
        raise SeatsNotAvailableError("Not enough seats available")

    available_seats -= tickets

    print("Booking successful")
    print("Remaining seats:", available_seats)

except SeatsNotAvailableError as e:
    print("Error:", e)
except ValueError as e:
    print("Invalid input:", e)







#20: #Number Range Validator

try:
    num = int(input("Enter a number between 1 and 50: "))

    if num < 1 or num > 50:
        raise ValueError("Number must be between 1 and 50")

    print("Valid number:", num)

except ValueError as e:
    print("Error:", e)