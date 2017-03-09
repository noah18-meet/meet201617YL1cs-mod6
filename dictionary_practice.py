#Module 6, Part 5: Practice with dictionaries here

'''
my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}
num=my_phonebook["Statue of Liberty"]
my_phonebook["Ghostbusters"]=2125559876
print (my_phonebook.values())
'''

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###

###
#Print the variable, num
###

###
#Change the value of the Ghostbusters' phone number to 2125559876
###

#Here's an empty dictionary
your_phonebook={}
your_phonebook['rina']='0503199381'
your_phonebook['shachar']='0546995649'
your_phonebook['ziv']='0543333333'
your_phonebook['noa']='0546651600'
your_phonebook['niki']='dogs do not have phone numbers'

your_phonebook.keys()
sequence_of_keys=[your_phonebook]
for i in sequence_of_keys :
    print (your_phonebook)
    
###
#Add 5 values to it like this
#your_phonebook['key']=value
###

###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

#Loop over this sequence with a for loop
#using syntax like

#for key in sequence_of_keys :
#    #Do stuff

#Use the loop to print to the shell the key and value
#of every element in the dictionary
###

