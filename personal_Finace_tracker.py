import math

# Income 

income = int(input("Enter your monthly income: ₹"))

# Split
def split():
    '''
    Here you can mange your money on the basis of needs, wants and investments
    '''
    needs = int(input("Enter your needs percentage:"))
    wants = int(input("Enter your wants percentage:"))
    investments = int(input("Enter your invesments percentage:"))
    
    if needs + wants + investments != 100:
        print("Enter Valid Number")
        return
    
    

    needs = int(needs*income/100)
    wants = int(wants*income/100)
    investments = int(investments*income/100)

    print(f"Your needs are :₹{needs}")
    print(f"Your wants are :₹{wants}")
    print(f"Your invesments are :₹{investments}")

    return 



split()



# Transcactions