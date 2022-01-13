#CSC110, Christina Nguyen, 3/6/2021, returns fixed string and displays in nice layout

def main():
    string = input("Enter inventory string: ")
    fields = string.split("*")

    typeElement = fields[1]
    partNumberAndDescription = fields[2]
    quantity = fields[3]
    location = fields[4]
    cost = fields[5]
    price = fields[6]
    make = fields[7]
    model = fields[8]
    years = fields[9].split("-")
    partNumber = partNumberAndDescription[0:8]
    description = partNumberAndDescription[8:len(partNumberAndDescription)]
        
    fixedType = fixType(typeElement)
    print(format("Type:",'11s'), fixedType)
    fixedPartNumber = fixPartNumber(partNumber)
    print(format("Part#:",'11s'), fixedPartNumber)
    fixedDescription = fixDescription(description)
    print(format("Desc:",'11s'), fixedDescription) 
    quantity = fixQuantity(quantity)
    print(format("Qty:",'11s',), quantity)
    fixedLocation = fixLocation(location)
    print(format("Loc:",'11s'), fixedLocation)
    fixedCost = fixCost(cost)
    print(format("Cost:",'11s'), fixedCost)
    fixedPrice = fixPrice(price)
    print(format("Price:",'11s'), fixedPrice)
    fixedMake = fixMake(make)
    print(format("Make:",'11s'), make)
    fixedModel = fixModel(model)
    print(format("Model:",'11s'), model)
    yearStart = fixYearStart(years)
    print(format("Year Start:",'9s'), yearStart)
    yearEnd = fixYearEnd(years)
    print(format("Year End:",'11s'), yearEnd)
    
def fixType(typeElement):
    lowercasePart = typeElement.lower()
    fixedType = typeElement[0] + lowercasePart[1:len(lowercasePart)]

    if typeElement[0].islower():
        fixedType = typeElement[0].upper() + lowercasePart[1:len(lowercasePart)]
    
    return fixedType
   
def fixPartNumber(partNumber):
    fixedPartNumber = partNumber.replace("O","0")
    return fixedPartNumber
    
def fixDescription(description):
    descripWithNoWhiteSpace = description.strip()
    emptyString = ''
    for char in descripWithNoWhiteSpace:
        if char.isupper():
           char = " " + char
        emptyString += char 
    fixedDescription = emptyString.strip() #After line 58 exacutes, empty string turns into the fixed description with 1 extra space. 
    return fixedDescription
       
def fixQuantity(quantity):
    quantity = int(quantity)
    return quantity
    
def fixLocation(location):
    fixedLocation = location.replace(" ", '')
    return fixedLocation
    
def fixCost(cost):
    noDollarSignCost = cost.replace("$",'')
    noCommaCost = noDollarSignCost.replace(",",'')
    fixedCost = float(noCommaCost)
    return fixedCost
  
def fixPrice(price):
    noDollarSignPrice = price.replace("$",'')
    noCommaPrice = noDollarSignPrice.replace(",",'')
    fixedPrice = float(noCommaPrice)
    return fixedPrice
    
def fixMake(make):
    fixedMake = make 
    return fixedMake
    
def fixModel(model):
    fixedModel = model
    return fixedModel
    
def fixYearStart(years):
    yearStart = int(years[0]) 
    return yearStart
    
def fixYearEnd(years):
    yearEnd = int(years[1])
    return yearEnd
    
if __name__ == '__main__':
    main()

#I approached this assignment by first writing very exstentive psuedocode
#I tested each function individually before moving on to the next function and that decreased the number of bugs compared to past projects by a lot.
#The only place I got stuck on was the fixDescription function.
#From this project I learned how to use a lot of new methods. Although I didn't use it, I learned how to attach methods to methods.
#I tested my program using PyUnit and entering the sample strings from my classmates
#The test strings and their results were:
#*PART*DRPNO432DriverDoorPanel *2*Shop 1*$1,012.84*1,499.99*Chevy*Camaro*2011-2013*
#Type:       Part
#Part#:      DRPN0432
#Desc:       Driver Door Panel
#Qty:        2
#Loc:        Shop1
#Cost:       1012.84
#Price:      1499.99
#Make:       Chevy
#Model:      Camaro
#Year Start: 2011
#Year End:   2013
    
#*PART*DO0OO432PassengerDoorHandle *10*Shop 15*$12,112.99*$499*Honda*Civic*2011-2013*
##Type:       Part
##Part#:      D0000432
##Desc:       Passenger Door Handle
##Qty:        10
##Loc:        Shop15
##Cost:       12112.99
##Price:      499.0
##Make:       Honda
##Model:      Civic
##Year Start: 2011
##Year End:   2013

#*pART*flux1210FluxCAPACITOR* 88*workshop  1*$0.01*$1.21*DMC*DeLorean*1981-1983*
#Type:       Part
#Part#:      flux1210
#Desc:       Flux C A P A C I T O R
#Qty:        88
#Loc:        workshop1
#Cost:       0.01
#Price:      1.21
#Make:       DMC
#Model:      DeLorean
#Year Start: 1981
#Year End:   1983

#I also tested part and pArT in fixType() which yeilded Part.
#Something that I'd wish to fix as I learn more find a method that can split at multiple different types of characters instead of just one.
#Something I'd do different on the next project is check off what lectures I've watched, what Q&As I've read etc.
#Q&As being everywhere felt very disorganized. 
