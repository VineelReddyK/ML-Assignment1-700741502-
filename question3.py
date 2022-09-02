#Create a tuple containing names of your sisters and your brothers
brothers=('ram','krishna')

sister=('seetha','radha')

#Join brothers and sisters tuples and assign it to siblings
siblings=brothers+sister
print("siblings are :",siblings)

#How many siblings do you have?
print("total number of siblings :",len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents=('vishnu','lakshmi')
family_members=siblings+parents
print("adding mother and father to the tuple :",family_members)

