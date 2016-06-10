#################################################################################
#           This program will write things to a file.                           #
#           This program will also provide reading from the same file           #
#           Author : Shane Cronk                                                #
#           Date : 6/10/2016                                                    #
#################################################################################



def _writeFile():
    filename = input("Please input a filename: ")
    with open("filename","w") as out_file:
        out_file.write(uName)