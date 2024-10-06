
inventory={'item1':10,'item2':20}

operations=[
    ("add","item1",5),
    ("remove","item2",10),
    ("check","item3"),
    ("remove","item3",5),



]





def manage_inventory(inventory,operations):

    
    
    result={}
    for item,value in inventory.items() : 
       
        if item==operations[0][1]:
            sum=operations[0][2]+value
            result[item]=sum

        if item==operations[1][1]:
            if operations[1][2]-value>0:
                sum=operations[1][2]-value
                result[item]=operations[1][2]
            else:
                result[item]=operations[1][2]


        if item==operations[2][1]:
            print("quantity",value)

        if item==operations[3][1]:
            if operations[3][2]-value>0:
                minus=operations[3][2]-value
                result[item]=minus
            else:
                result[item]=operations[3][2]
    return result    

       


        




final=manage_inventory(inventory,operations)
print(final)