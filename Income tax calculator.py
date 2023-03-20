#Income Tax Calculator
# Analysis often requires the programmer to learn some things about the problem domain, in this case, the relevant tax law. For the sake of simplicity, let’s assume the following tax laws:

#-- All taxpayers are charged a flat tax rate of 20%
#-- All taxpayers are allowed a $10,000 standard deduction (-)
#--For each dependent, a taxpayer is allowed an additional $3,000 deduction (-)

# Gross income must be entered to the nearest penny
# The income tax is expressed as a decimal number

# -- Another part of analysis determines what information the user will have to provide. 
#-- In this case, the user inputs are gross income and number of dependents. 
# The program calculates the income tax based on the inputs and the tax law and then displays the income tax. The figure below shows the proposed terminal-based interface. 
# Characters in italics indicate user inputs. The program prints the rest. The inclusion of an interface at this point is a good idea because it allows the customer and
# the programmer to discuss the intended program’s behavior in a context understand- able to both.

income = float(input("Please enter your gross annual income: "))
dependent = int(input ("Please enter the number of dependent: "))
tax = 0
deduction =  (dependent*3000) + 10000
tax = (income - deduction) * 0.20
print ('Income tax total ' , tax )







