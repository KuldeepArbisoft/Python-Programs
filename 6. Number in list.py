
# coding: utf-8

# In[150]:


# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If the first number in the string is greater than or equal 
# to the proceeding number, the proceeding number should be inserted 
# into a sublist. Continue adding to the sublist until the proceeding number 
# is greater than the first number before the sublist. 
# Then add this bigger number to the normal list.

#Hint - "int()" turns a string's element into a number



# In[151]:


def numbers_in_lists(string):
    listA = []
    listTemp = []
    i = 0;
    count = 0;
    while(i < (len(string)-1)):
        if int(string[i]) >=  int(string[i+1]):
            listA.append(int(string[i]));
            count += 1;
            temp  = int(string[i]);
            i += 1;
            while(i < len(string) and temp >= int(string[i])):
                #print i
                listTemp.append(int(string[i]));
                i += 1
            count += len(listTemp)
            listA.append(listTemp)
            listTemp = []
        else:
            count += 1;
            listA.append(int(string[i]))
            i += 1
    if(count < len(string)):
        listA.append(int(string[count]))
    return listA                


# In[152]:




#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print  repr(string), numbers_in_lists(string)== result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string),   numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result


# In[ ]:




