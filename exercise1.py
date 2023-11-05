# PROGRAMMING ASSIGNMENT 09
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def build_attraction_dict(filename):
    # write your code here for Task 1
    global dict1
    dict1 = {}
    file1 = open(filename, 'r')

    for line in file1: 
        #split the province and attraction
        words = line.split(',')
        #get province
        province = words[0]
        #get attraction
        attraction = words[1].strip('\n')
        dict1.update({attraction: province})
    
    return dict1  
    file1.close()

def add_attraction(dict1):
    # write your code here for Task 2
    dict2 = dict1
    add_attraction = input('Input a new attraction: ')
    add_province = input('Input the province: ')

    if add_attraction not in dict2 :
        dict2[add_attraction] = list()
    dict2.update({add_attraction: add_province})

def build_province_attraction_dict(dict1):
    # write your code here for Task 3
    dict3 = {}
    for key in dict1.keys():
        province = dict1[key]
        attraction = key
        if province not in dict3 :
            #make the attraction to a list
            attraction_update = [attraction]
            dict3.update({province: attraction_update})
        elif province in dict3:
            
            list1 = dict3[province]
            list1.append(attraction)
            dict3.update({province: list1})
    return dict3
        
def most_attractions(dict3):
    # write your code here for Task 4
    listmost = []
    for key in dict3.keys():
        if len(dict3[key]) >= 3:
            listmost.append(key)
    print('Provinces with at least 3 attractions:')
    print(*listmost, sep = "\n") 
    set1 = set(listmost)
    return set1

def main():
    # write your code here for Task 5
    
    build_attraction_dict("top_tourist_attractions.txt")
    add_attraction(dict1)
    new_dict = build_province_attraction_dict(dict1)
    most_attractions(new_dict)

##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
