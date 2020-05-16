list_function_name=[]
# this function gives the name of defined all int functions
def function_detector(text):
    a = text.find("int")
    b = text.find("(")
    if a != -1 and b !=-1 :
        text = text.replace("int","")
        text = text.replace("\n","")
        text =  text.replace(" ","")
        length = len(text)

        list1 = list(text)
        index1 = list1.index("(")
        del list1[index1:length]
        #print(list1)
        new_String = "".join(map(str,list1))
        #print(new_String)
        list_new = list(new_String.split("\n"))
        list_function_name.append(new_String)
        #print(list_function_name)



c_file = open("program.c","r")
for x in c_file:
    function_detector(x)
print(list_function_name)
