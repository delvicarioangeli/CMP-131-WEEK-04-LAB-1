
# Name: Angelina Del Vicario
# Lab: 01
# Week: 04 
# Date: 09/11/2026


#ticket prices
adultPrice = 10.00
childPrice = 6.00

movieName = input("Please Enter Your Movie Name: ")
adultTickets = int(input("Please enter amount of Adult Tickets Sold: "))
childTickets = int(input("Please enter amoutn of Child Tickets Sold: "))

adultProfit = adultTickets * adultPrice
childProfit = childTickets * childPrice
grossProfit = adultProfit + childProfit
netBox = grossProfit * 0.2
distributor = grossProfit - netBox



print ("________Box_Office_Report________")
print ("Movie Name: " + movieName)
print ("Adult Tickets Sold: " + adultTickets)
print ("Child Tickets Sold: " + childTickets)
print ("Gross Box Office Profit: " + grossProfit)
print ("Net Box Office Profit: " + netBox)
print ("Amount Paid to Distrubutor: " + distributor)
