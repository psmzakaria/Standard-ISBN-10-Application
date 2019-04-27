#Application to convert a Product ID to a standard ISBN-10 Number

#Function to detect only numbers are entered by the users

def allowedNumber(ID):
    for char in productID:
        if not char in '1234567890.':
            return print("These arent numbers")
    return True


#Start of main program

userInput=input("Welcome! Got a Product ID to be converted into an ISBN-10 number? Press Enter")

while userInput!="Q":
    print("To get your ISBN ---> Press 1")
    print("To quit ---> Press Q")
    userInput=(input("Enter your choice"+"  ")).upper()
    
    while userInput=="1" and userInput !="N":
        productID=input("Enter your Product ID number"+"  ")

        #Remove prefix
        value=productID[3:]

        if(allowedNumber(productID)):
            True
        

        if len(value) !=9:
          print("Incorrect Product ID number")
          userInput="N"
        else:
            totalSum = 0
            for i in range(9):
                if 0 <= int(value[i]) <= 9: 
                    totalSum += int(value[i]) * (10 - i)
                else:
                    False

            #next highest value multiple of 11
            x=(int((totalSum/11))+1)*11

            #error is the error control digit
            error=x-totalSum

            if error ==10:
                print('\n'"Your ISBN is"+" "+value+"x")
            elif totalSum%11==0:
                print('\n'"Your ISBN is"+" "+value+"0")
            else:
                print('\n'"Your ISBN is"+" "+value+str(error))


            userInput=input("Enter N to return to main menu"+"  "+"Enter 1 to convert more Product IDs"+"    ").upper()

