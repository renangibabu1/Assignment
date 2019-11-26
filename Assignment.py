
'''

4.Create a function that accepts single list containing letters or may be words.
Total number of elements in a list may vary. In turn,
it counts the number of occurrences in a list for each element and returns user a dictionary with total number of counts for each element.
Please remember to include case-sensitive match i.e. 'user1' is not equal to 'User1' word.
Lets say, user provides a list as:

['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']

'''
def Dictionary(list): 
  
    """ Creating an empty dictionary  """
    dict = {} 
    for item in list: 
        if item in dict: 
            dict[item] += 1
        else: 
            dict[item] = 1
  
    for key, value in dict.items(): 
        print ((key, value)) 
  
    return dict

list = ['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1'] 
print(Dictionary(list)
        





'''

5.Create a function that accepts a list containing integers. Total number of elements in list may vary.
  Your method should return back the list removing duplicates from list.
  So lets say if user passes a following list to your function as input:
  [1,2,55,1,3,2,34,55]
  
'''

def Remove(dup): 
    list = [] 
    for num in dup:
        print(" List_values :",num,"\n")
        if num not in list: 
            list.append(num) 
    return list 
      

dup = [1,2,55,1,3,2,34,55]
print(Remove(dup))

''' withou using function '''
l = [1,2,55,1,3,2,34,55]
l1 = list(dict.fromkeys(l))
print(l1)

 
        



