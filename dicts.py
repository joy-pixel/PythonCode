people = {
    'htanaka':'haru tanaka',
    'ppatel':'Priya Patel',
    'bagarcia':'Benjamin Alberto Garcia',
    'zmin':'Zhang Min',
    'afarooqi':'Ayesh',
    'hajackosn':'hanna Jackson',
    'papatel':'Pratyush Aarav patel',
    'hrjackson':'Henry jackson',
}
print(people)

#Define a dictionary named people

people  = {
     'htanaka':'haru tanaka',
    'ppatel':'Priya Patel',
    'bagarcia':'Benjamin Alberto Garcia',
    'zmin':'Zhang Min',
    'afarooqi':'Ayesh',
    'hajackosn':'hanna Jackson',
    'papatel':'Pratyush Aarav patel',
    'hrjackson':'Henry jackson',
}


#make a copy of the people dict
peeps2 = people.copy()

#show whats in both dict

print(people)
print(peeps2)


#Deleting items
people = {   'htanaka':'haru tanaka',
    'ppatel':'Priya Patel',
    'bagarcia':'Benjamin Alberto Garcia',
    'zmin':'Zhang Min',
    'afarooqi':'Ayesh',
    'hajackosn':'hanna Jackson',
    'papatel':'Pratyush Aarav patel',
    'hrjackson':'Henry jackson',
    }
  
print(people)
del people["htanaka"]
print(people)

products = {
     'RB00111':{'name':'Ryaban Sunglasses','price':112.98,'models':['black','tortoise']},
     'DWCO317':{'name':'Drone with camera','price':72.95,'models':['white','black']},
     'MTS0540':{'name':'T-Shirt','price':2.95,'models':['medium','large']},
     'ECD2989':{'name':'Echo Dot','price':29.99,'models':[]},
 }
print(products)