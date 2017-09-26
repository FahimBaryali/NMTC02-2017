
#voornaam = input("geef me jouw voornaam")
#achternaam = input("geef me jouw acternaam")
#leeftijd = input("geef me jouw leeftijd")

#print ("\nvoornaam : {0:} \nachternaam: {1:} \nleeftijd: {2} ".format (voornaam,achternaam, leeftijd))

#n = int(input("Input your number"))
#result = n+n*n+n*n*n
#print("\nResult : {0}".format(result))

#x = int(input("input ur first number"))
#y = int(input ("input ur second number"))
#answer = (x+y)*(x+y)
#print("\nYour answer is{0}".format(answer))

#day = int(input("Enter number of day"))
#hour =int (input("enter number of hour"))
#min = int(input("enter number of minutes"))
#sec = int(input("enter number of seconds"))
#seconds = day*86400+hour*3600+min*60+sec

#print("\nSeconds:{0}".format(seconds))

x = input('enter seconds: ')

t = int(x)

day = t // 86400
hour = (t - (day * 86400)) // 3600
minit = (t - ((day * 86400) + (hour * 3600))) // 60
seconds = t - ((day * 86400) + (hour * 3600) + (minit * 60))
print(day, 'days', hour, ' hours', minit, 'minutes', seconds, ' seconds')


#hey its the new version
