#!/usr/bin/python3

line0 = line1 = line2 = line3 = line4 = line5 = line6 = line7 = line8 = ""
def userInput():
    global line0,line1,line2,line3,line4,line5,line6,line7,line8
    while True:
        line0 = input("Enter the digits of the 1st line. Press [Enter] when finished: ")
        if len(line0) != 9:
            print("Error! Try again! 1st line")
        else:
            while True:
                line1 = input("Enter the digits of the 2nd line. Press [Enter] when finished: ")
                if len(line1) != 9:
                    print("Error! Try again! 2nd line")
                else:
                    while True:
                        line2 = input("Enter the digits of the 3rd line. Press [Enter] when finished: ")
                        if len(line2) != 9:
                            print("Error! Try again! 3rd line")
                        else:
                            while True:
                                line3 = input("Enter the digits of the 4th line. Press [Enter] when finished: ")
                                if len(line3) != 9:
                                    print("Error! Try again! 4th line")
                                else:
                                    while True:
                                        line4 = input("Enter the digits of the 5th line. Press [Enter] when finished: ")
                                        if len(line4) != 9:
                                            print("Error! Try again! 5th line")
                                        else:
                                            while True:
                                                line5 = input("Enter the digits of the 6th line. Press [Enter] when finished: ")
                                                if len(line5) != 9:
                                                    print("Error! Try again! 6th line")
                                                else:
                                                    while True:
                                                        line6 = input("Enter the digits of the 7th line. Press [Enter] when finished: ")
                                                        if len(line6) != 9:
                                                            print("Error! Try again! 7th line")
                                                        else:
                                                            while True:
                                                                line7 = input("Enter the digits of the 8th line. Press [Enter] when finished: ")
                                                                if len(line7) != 9:
                                                                    print("Error! Try again! 8th line")
                                                                else:
                                                                    while True:
                                                                        line8 = input("Enter the digits of the 9th line. Press [Enter] when finished: ")
                                                                        if len(line8) != 9:
                                                                            print("Error! Try again! 9th line")
                                                                        else:
                                                                            break
                                                                    break
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break
    return (line0,line1,line2,line3,line4,line5,line6,line7,line8)