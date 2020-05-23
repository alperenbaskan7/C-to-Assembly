list_function_name=[]
sum_elements = []
subtract_operation =[]
multiply_elements = []
if_condition_list=[]
list_for_loop = []
c_file = open("program.c","r")

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

def sum(text):
    a = text.find("+")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1:
        if text.find("return"):
            sum_elements.append("return")

        length = len(text)
        text = text.replace(" ", "")
        list1 = list(text)
        index1 = list1.index("+")
        sum_elements.append("+")
        sum_elements.append(list1[index1-1])
        sum_elements.append(list1[index1+1])
        print(sum_elements)

def substract(text):
    a = text.find("-")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1:
        length = len(text)
        text = text.replace(" ", "")
        list1 = list(text)
        index1 = list1.index("-")
        subtract_operation.append("-")
        subtract_operation.append(list1[index1 - 1])
        subtract_operation.append(list1[index1 + 1])
        print(subtract_operation)

def multiply(text):
    a = text.find("*")
    if a != -1 and text.find("if") == -1:
        length = len(text)
        text = text.replace(" ", "")
        list1 = list(text)
        index1 = list1.index("*")
        multiply_elements.append("*")
        multiply_elements.append(list1[index1 - 1])
        multiply_elements.append(list1[index1 + 1])
        print(multiply_elements)

def find_forloop(text):
    if text.find("for") != -1 and text.find("(") != -1 and text.find(")") != -1 :
        text = text.replace("for","").replace("\t","").replace("\n","").replace(" ","").replace("{","").replace("(","").replace(")","")
        text = text.split(";")
        list_for_loop = text
        print(list_for_loop)


def find_ifcommand(text):
    if text.find("if") != -1 and text.find("(") != -1 and text.find(")") != -1 and text.find("else") == -1:
        text = text.replace("if", "").replace(" ", "").replace("\n", "").replace("{", "").replace(" ","").replace("\t","")
        list1 = list(text)
        if_condition_list.append("if")
        if text.find(";") == -1:
            if text.find("+") != -1 :
                index1 = list1.index("+")
                if_condition_list.append("+")
                if_condition_list.append(list1[index1 - 1])
                if_condition_list.append(list1[index1 + 1])
            elif text.find("-") != -1 :
                index1 = list1.index("-")
                if_condition_list.append("-")
                if_condition_list.append(list1[index1 - 1])
                if_condition_list.append(list1[index1 + 1])
            elif text.find("*") != -1 :
                index1 = list1.index("*")
                if_condition_list.append("*")
                if_condition_list.append(list1[index1 - 1])
                if_condition_list.append(list1[index1 + 1])
            elif text.find("||") != -1 :
                index1 = list1.index("||")
                if_condition_list.append("||")
                if_condition_list.append(list1[index1 - 2])
                if_condition_list.append(list1[index1 + 2])
            elif text.find("&&") != -1 :
                index1 = list1.index("&&")
                if_condition_list.append("&&")
                if_condition_list.append(list1[index1 - 2])
                if_condition_list.append(list1[index1 + 2])

            elif text.find("^") != -1:
                index1 = list1.index("^")
                if_condition_list.append("^")
                if_condition_list.append(list1[index1 - 1])
                if_condition_list.append(list1[index1 + 1])
                 # if block havent get tested yet


def main():
    for x in c_file:
        function_detector(x)
        sum(x)
        substract(x)
        multiply(x)
        find_ifcommand(x)
        find_forloop(x)
    print(if_condition_list)
    print(list_function_name)
main()

