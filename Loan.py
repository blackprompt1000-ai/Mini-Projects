def c_emi(pri, ar, n):
    R = ar / (12 * 100)
    N = n * 12
    emi = int((pri * R * ((1 + R) ** N)) / (((1 + R) ** N) - 1))
    return emi

print("Please fill the following details carefully for type of deposit, account or loan you want to choose \nPlease fill the asked details in Capital)")
name=input("Enter your name please ")
a=int(input("enter your age please "))
pn=int(input("enter your phone number "))
add=(input("enter your address please "))
y=int(input("enter the years of experience you have with our bank "))



if (a>20):
    pr=input("Please enter the purpose of which you prefer to have loan (EDUCATIONAL, HOME, GOLD, PERSONAL) ")
    match pr:
        case "EDUCATIONAL" | "EDUCATION" | "LOAN FOR EDUCATION" | "EDUCATIONAL LOAN":
            if (y>=5):
                print("\nloan will be assigned with the rate of 5, per month interest ")
                ar=5
            else:
                print("\nloan will be assigned with the rate of 7, per month interest ")
                ar=7
                        
        case "HOME" |"HOME LOAN"|"HOUSE"|"LOAN FOR HOUSE"|"LOAN FOR HOME":
            if (y>=5):
                print("\nloan will be assigned with the rate of 8.5, per month interest ")
                ar=8.5
            else:
                print("\nloan will be assigned with the rate of 10, per month interest ")
                ar=10
                            
        case "LOAN OF GOLD"|"LOAN FOR GOLD"|"GOLD LOAN"|"GOLD":
            if (y>=5):
                print("\nloan will be assigned with the rate of 12, per month interest ")
                ar=12
            else:
                print("\nloan will be assigned with the rate of 14, per month interest ")
                ar=14

        case "PERSONAL"|"PERSONAL LOAN"|"LOAN FOR PERSONAL PURPOSE":
            if (y>=5):
                print("\nloan will be assigned with the rate of 12, per month interest ")
                ar=12
            else:
                print("\nloan will be assigned with the rate of 13, per month interest ")
                ar=13
        case _:
            print("Please enter a valid type of loan")
    
    pri=int(input("\nenter the loan amount you want "))
    n=int(input("enter the time period (in years) for which you want loan "))
    emi=c_emi(pri,ar,n)

    print(f"\nYour {pr} LOAN will be assigned with the rate of {ar}, per month interest ")
    print(f"\nYour monthly EMI will be: {emi}")

else:
    print("You are not eligible for loan due to age restrictions")


