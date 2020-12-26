
# -----Lists-----#

names = ['karthik','kiran','varun','praveen']
print('reading the values from list');
print(names[0]);
print(names[1]);
print(names[2]);
print(names[3]);
for name in names:
    statement = 'Hello there ' +  name
    print(statement)



names = ['karthik','kiran','varun','praveen']
print('reading the values from list');

for name in names:
    statement = ' '.join(['Hello there', name,'srikanth'])
print(statement)    

test1="learn python"
test2="learn python"
print(id(test1))
print(id(test2))


mynewlist = [iter for iter in range(100)]
print(mynewlist)

listofplaces = ["hyderabad","mumbai","chennai","kolkata","ka"]
first3letters = [place[0:3] for place in listofplaces if len(place)>3]
print(first3letters)

voiceofletters = ["capable","congrates","complain"]
first1letter = [letter[0:5] for letter in voiceofletters]
print(first1letter)


list1=[[1,2,3]+[2,4,6]]
list2=[2,3,4,5,6]
list3=[list1+list2]
print(list3)

sports = ["cricket","hockey","volleyball","baseball"]
print(sports)
sports.append("tennis")
print(sports)
sports.insert(4,"football")
print(sports)
sports.remove("cricket")
print(sports)
sports.pop(3)
print(sports)
print(sports.index('hockey'))
print(sports.index('tennis'))
sports


sports=['kabadi','shettle','khokho']
print(sports)
sports.pop(2)
print(sports)

 

names = ['python','scripting','coding','multimedia','business']
print(names)
print(names[1])
print(names[4])
print(names[2])

print('most trending business in society:-'+names[3]);
print(names[1:4])