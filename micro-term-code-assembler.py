'''
Author = Alperen Başkan

Please for any questions or advises for this program ;
alperen.baskan@yahoo.com.tr

This program mainly gets a C file (.c) and convert it to MSP430 Assembly code (.asm)
For now , it works for only the basic C programs and converts to the asm code just like
MSP430 gcc 6.2.1
'''
list_for_loop = []
else_list = []
print("Please enter the name of your C program with extension (YourProgram.c):")
my_c_program = input()
c_file = open(my_c_program, "r")
asm_file = open("assembly-converted.asm","w")
# this function gives the name of defined all int functions
def function_detector(text):
    a = text.find("int")
    b = text.find("(")
    if a != -1 and b != -1 and text.find("main") == -1:
        text = text.replace("int", "").replace("\n", "").replace(" ", "")
        list1 = list(text)
        index1 = list1.index("(")
        del list1[index1:]
        new_String = "".join(map(str, list1))
        asm_file.write(new_String)
        asm_file.write(": \n\t")
        asm_file.write("SUB.W   #4, R1\n\tMOV.W   R12, 2(R1)\n\tMOV.W   R13, @R1\n")
    if text.find("main") != -1:
        asm_file.write("main:\n\tSUB.W   #6, R1\n")

def sum(text):
    a = text.find("+")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            asm_file.write("\tMOV.W   2(R1), R12\n\tADD.W   @R1, R12\n\tADD.W   #4, R1\n\tRET\n")

def substract(text):
    a = text.find("-")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            asm_file.write("\tMOV.W   2(R1), R12\n\tSUB.W   @R1, R12\n\tADD.W   #4, R1\n\tRET\n")

def multiply(text):
    a = text.find("*")
    if a != -1 and text.find("if") == -1 and text.find("for") == -1 and text.find("else") == -1:
        if text.find("return"):
            asm_file.write("\tMOV.W   @(R1), R13\n\tCALL    #__mspabi_mpyi\n\tADD.W   #4, R1\n\tRET\n")

def find_forloop(text):
    if text.find("for") != -1 and text.find("(") != -1 and text.find(")") != -1 :
        text = text.replace("for","").replace("\t","").replace("\n","").replace(" ","").replace("{","").replace("(","").replace(")","")
        text = text.split(";")
        list_for_loop = text

def find_ifcommand(text):
    if text.find("if") != -1 and text.find("(") != -1 and text.find(")") != -1 and text.find("else") == -1:
        asm_file.write("\n\tMOV.W   4(R1),R12\n\tSUB.W   2(R1), R12")
        text = text.replace("if", "").replace(" ", "").replace("\n", "").replace("{", "").replace(" ","").replace("\t","").replace("(","").replace(")","")
        list1 = list(text)
        if text.find(";") == -1:
            if text.find("==") != -1:
                index_for_number = text.index("==")
                number_in_if = text[index_for_number+2:]
                asm_file.write("\n\tCMP.W   #")
                asm_file.write(number_in_if)
                asm_file.write(", R12 { JNE .L10\n")

def else_command(text):
    if text.find("else") != -1 and text.find("if") == -1:
        text = text.replace("else", "").replace(" ", "").replace("\n", "").replace("{", "").replace(" ", "").replace("\t", "")
        else_list.append("else")

def assignments_func(text):
    if text.find("=") != -1 and text.find("int") != -1 and text.find(";") != -1 :
        text = text.replace("int", "").replace("\n", "").replace(";", "").replace("\t", "")
        new_list =text.split(",")
        list2 = []
        for a in new_list:
            if a.find("=") != -1:
                index1 = a.index("=")
                list1 = list(a)
                del list1[0:index1+1]
                new_String = "".join(map(str, list1))
                list2.append(new_String)
        asm_file.write("\tMOV.W   #")
        asm_file.write(list2[0])
        asm_file.write(", 4(R1)\n\t")
        asm_file.write("MOV.W   #")
        asm_file.write(list2[1])
        asm_file.write(", 2(R1)\n")
    if text.find("int") == -1 and text.find("=") != -1 and text.find(";")!= -1 and text.find("^") == -1 and text.find("(") == -1:
        text = text.replace(" ", "").replace(";", "").replace("}","").replace("\n","")
        index_num = text.index("=")
        list_new = list(text)
        del list_new[0:index_num+1]
        asm_file.write("\tMOV.W   #")
        asm_file.write(list_new[0])
        asm_file.write(", 4(R1)\n\tBR      #.L11\n")

def xor_function(text):
    if text.find("^") != -1 and text.find("=") != -1 and text.find(";") != -1:
        asm_file.write("\tMOV.W   4(R1), R12\n\tXOR.W   2(R1), R12\n\tMOV.W   R12, @R1")

def main():
    for x in c_file:
        if x != "{\n":
            function_detector(x)
            sum(x)
            substract(x)
            multiply(x)
            find_ifcommand(x)
            find_forloop(x)
            else_command(x)
            assignments_func(x)
            xor_function(x)
main()
c_file.close()
asm_file.close()
asm_file = open("assembly-converted.asm", "r")
x = asm_file.read()
asm_file.close()
asm2_file = open("assembly-converted.txt", "w")
asm2_file.write(x)
asm2_file.close()
print("Please check the file that you put C file to see your converted (assembly-converted.asm) file\nAlso You can find the file assembly-converted.txt to see the text in the assembly program")
print("\nYou can first try with the existing file (program.c) ")
k = input("Press Enter to Exit")
