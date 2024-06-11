class CarShowroom:
    def companyname(self):
        companyname = input("Please enter the car company name (Toyota, Mahindra, Mercedes): ")
        return companyname
    
    def modelname(self, companyname):
        if companyname == "Toyota":
            print(f"Hey, welcome to the {companyname} showroom!")
            modelname = input("Enter the specific model you needed (Innova, Hybrid): ")
            if modelname not in ["Innova", "Hybrid"]:
                print("Invalid model name!")
            else:
                if modelname == "Innova":
                    exprice = 5000000
                elif modelname == "Hybrid":
                    exprice = 6000000
        elif companyname == "Mahindra":
            print(f"Hey, welcome to the {companyname} showroom!")
            modelname = input("Enter the specific model you needed (Thar, Scorpio): ")
            if modelname not in ["Thar", "Scorpio"]:
                print("Invalid model name!")
            else:
                if modelname == "Thar":
                    exprice = 7000000
                elif modelname == "Scorpio":
                    exprice = 8000000
        elif companyname == "Mercedes":
            print(f"Hey, welcome to the {companyname} showroom!")
            modelname = input("Enter the specific model you needed (G Class, Maybach): ")
            if modelname not in ["G Class", "Maybach"]:
                print("Invalid model name!")
            else:
                if modelname == "G Class":
                    exprice = 10000000
                elif modelname == "Maybach":
                    exprice = 15000000
        else:
            print("Invalid Company Name")
                            
        return modelname, exprice
    
    def variant(self):
        variant = input("Please Enter the variant you needed (Petrol, Diesel): ")
        if variant not in ["Petrol", "Diesel"]:
            print("Invalid variant model!")
        return variant

    def display(self, exprice, cgst, sgst, insurance):
        print(f"Exprice: {exprice}")
        onroadprice = exprice + cgst + sgst + insurance
        print(f"Onroadprice: {onroadprice}")

showroom = CarShowroom()
companyname = showroom.companyname()
modelname, exprice = showroom.modelname(companyname)
variant = showroom.variant()
showroom.display(exprice,25000,25000,25000)
