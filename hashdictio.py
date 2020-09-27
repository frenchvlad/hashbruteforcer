#coding: utf-8
import hashlib
"""
made by frenchvlad from paris
"""
def main():
    with open("password.txt") as f:
        #for line in f:
            #line = line.strip()
        algorithm = input("Select the algorithm (md5/sha1) : ")
        if algorithm == "md5" or algorithm == "MD5":
            bb = input("Enter the hash (len = 32) : ")
            if len(bb) == 32:
                print("\n")
                for line in f:
                    line = line.strip()
                    hashes = hashlib.md5(line.encode('utf-8')).hexdigest()
                    if hashes == bb:
                        print(" [+] The hash matches the password : "+str(line))
                        exit()
                    else:
                        print(" [-] Hash is not : "+str(line))
            else:
                print("Wrong hash.")
                exit()
        if algorithm == "sha1" or algorithm == "SHA1":
            bb = input("Enter the hash (len = 40) : ")
            if len(bb) == 40:
                print("\n")
                for line in f:
                    line = line.strip()
                    hashes = hashlib.sha1(line.encode('utf-8')).hexdigest()
                    if hashes == bb:
                        print(" [+] The hash matches the password : "+str(line))
                        exit()
                    else:
                        print(" [-] Hash is not : "+str(line))
            else:
                print("Wrong hash.")
                exit()
        else:
            exit()
main()
