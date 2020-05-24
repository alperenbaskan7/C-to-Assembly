list_function_name = []
sum_elements = []
subtract_operation = []
multiply_elements = []
if_condition_list = []
list_for_loop = []
else_list = []
c_file = open("program.c", "r")
asm_file = open ("assembly.txt","w")
# this function gives the name of defined all int functions
def function_detector(text):
    a = text.find("int")
    b = text.find("(")
    if a != -1 and b != -1 and text.find("main") == -1:
        text = text.replace("int", "")
        text = text.replace("\n", "")
        text = text.replace(" ", "")
        #length = len(text)
        list1 = list(text)
        index1 = list1.index("(")
        del list1[index1:]
        #print(list1)
        new_String = "".join(map(str, list1))
        #print(new_String)
        #list_new = list(new_String.split("\n"))
        list_function_name.append(new_String)
        #print(list_function_name)
        asm_file.write(new_String)
        asm_file.write(": \n\t")
        asm_file.write("SUB.W   #4, R1\n\tMOV.W   R12, 2(R1)\n\tMOV.W   R13, @R1\n")
def sum(text):
    a = text.find("+")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            sum_elements.append("return")
            asm_file.write("\tMOV.W   2(R1), R12\n\tADD.W   @R1, R12\n\tADD.W   #4, R1\n\tRET\n")
        new_index1 = []
        new_index2 = []
        length = len(text)
        text = text.replace(" ", "").replace("return","").replace(";","").replace("\n","").replace("\t","")
        list1 = list(text)
        index1 = list1.index("+")
        sum_elements.append("+")
        new_index1 = "".join(map(str, list1[0:index1]))
        new_index2 = "".join(map(str, list1[index1+1:]))
        sum_elements.append(new_index1)
        sum_elements.append(new_index2)
        #print(sum_elements)

def substract(text):
    a = text.find("-")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            subtract_operation.append("return")
            asm_file.write("\tMOV.W   2(R1), R12\n\tSUB.W   @R1, R12\n\tADD.W   #4, R1\n\tRET\n")
        new_index1 = []
        new_index2 = []
        length = len(text)
        text = text.replace(" ", "").replace("return","").replace(";","").replace("\n","").replace("\t","")
        list1 = list(text)
        index1 = list1.index("-")
        subtract_operation.append("-")
        new_index1 = "".join(map(str, list1[0:index1]))
        new_index2 = "".join(map(str, list1[index1 + 1:]))
        subtract_operation.append(new_index1)
        subtract_operation.append(new_index2)
        print(subtract_operation)

def multiply(text):
    a = text.find("*")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            multiply_elements.append("return")
            asm_file.write("\tMOV.W   @(R1), R13\n\tCALL    #__mspabi_mpyi\n\tADD.W   #4, R1\n\tRET\n")
        new_index1 = []
        new_index2 = []
        text = text.replace(" ", "").replace("return","").replace(";","").replace("\n","").replace("\t","")
        list1 = list(text)
        index1 = list1.index("*")
        multiply_elements.append("*")


        new_index1 = "".join(map(str, list1[0:index1]))
        new_index2 = "".join(map(str, list1[index1 + 1:]))

        multiply_elements.append(new_index1)
        multiply_elements.append(new_index2)
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
            elif text.find("||") != -1:
                index1 = list1.index("||")
                if_condition_list.append("||")
                if_condition_list.append(list1[index1 - 2])
                if_condition_list.append(list1[index1 + 2])
            elif text.find("&&") != -1:
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

def else_command(text):
    if text.find("else") != -1 and text.find("if") == -1:
        text = text.replace("else", "").replace(" ", "").replace("\n", "").replace("{", "").replace(" ", "").replace("\t", "")
        else_list.append("else")
        print(else_list)

def main():
    for x in c_file:
        function_detector(x)
        sum(x)
        substract(x)
        multiply(x)
        find_ifcommand(x)
        find_forloop(x)
        else_command(x)
    print(if_condition_list)
    print(list_function_name)
    print(sum_elements)
main()

