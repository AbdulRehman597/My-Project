def CGPA(a,b,c):
    avg = (a + b + c)/3
    print(f"Your CGPA so far is {avg}")

semester = int(input("How many semesters do you have completed/have obtained grades for? "))
if semester == 3:
    inp_1 = float(input("Enter your GPA for the 1st semester:"))    
    inp_2 = float(input("Enter your GPA for the 2nd semester:"))    
    inp_3 = float(input("Enter your GPA for the 3rd semester:"))

    CGPA(inp_1, inp_2, inp_3) 
if semester == 2:
    inp_1 = float(input("Enter your GPA for the 1st semester:"))    
    inp_2 = float(input("Enter your GPA for the 2nd semester:"))    

    CGPA(inp_1, inp_2, 0)
if semester == 1:
    inp_1 = float(input("Enter your GPA for the 1st semester:"))    

    CGPA(inp_1, 0, 0)         
    
  