
#importing modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
import yaml 

#Uploading of rates database
dataweb='http://api.fixer.io/latest' #you can use the database you already have
rates=urlopen(dataweb)
preparedata = BeautifulSoup(rates)


rates=preparedata.p.string
ratedictionary=yaml.load(rates) #removing tags and transform it from string to a dictionary
rates=ratedictionary['rates'] #extracting just the money rates
rates['EUR']=1 #add the EUR to the list

#money converter function

def money_converter(amount,input,output=True):
    if input == 'EUR' and output!=True:
        conversion= amount*rates.get(output)
        return conversion
    elif input !='EUR' and output!=True:
        conversion=(amount/(rates.get(input)))*rates.get(output)
        return conversion
    elif input =='EUR' and output == False:
        ratesb = {k:v*amount for k, v in rates.items()}
        return ratesb
    else:
        toEUR=amount/rates.get(input)
        ratesc = {k: v * toEUR for k, v in rates.items()}
        return ratesc 


#currency symbols conversion: for the currency symbols similitud, the best way is request the user to write the international 3letters
    #currency name in case of problem
    
dictionary = {'EUR':'€', 'USD':'$','CAD':'$'} #example of dictionary with similar symbols
def currency_symbols(symbol):
    if symbol in dictionary:
        return symbol

    count = 0
    symbols = ()
    for i in dictionary:
        if dictionary[i] == symbol:
            count += 1
            symbols += (i,)
            new_symbol = i
    if count == 1:
        return new_symbol
    elif count > 1:
        return 'Error: Introduced symbol is the same for several money currencies. Please use the international 3-letters name of the currency'
