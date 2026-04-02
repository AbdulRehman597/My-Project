# Function to convert Rupees into Dollars
def converter_R(R):
    Dollar = Rupees /278
    print(f"{R}PKR is equal to {Dollar}$")

# Function to convert Dollars into Rupees    
def converter_D(D):
    Rupees = D * 278
    print(f"{D}$ is equal to {Rupees}PKR")    

# Asking for the User's Choice of Currency
choice = input("Do you want USD as a resulting currency or PKR? ")


if choice == "USD":
    Rupees = float(input("Enter your rupees to be converted: "))
    converter_R (Rupees)

if choice == "PKR":
    Dollar = float(input("Enter your dollar amount to be converted: "))
    converter_D (Dollar)
    
