#Receiving the input from the User
def grade_calculation():
    try:
        mark=float(input("Enter your mark (0-100) to know your grade:"))

        if  (mark >=90 and mark <=100 ):
            GRADE='A'
        elif(mark >=80 and mark <=89  ):
            GRADE='B'
        elif(mark >=70 and mark <=79  ):
             GRADE='C'
        elif(mark >=60 and mark <=69  ):  
             GRADE='D'
        elif(mark <60  and mark >=0   ): 
             GRADE='E'
        else :
            raise ValueError("Invalid Value")

        print(f"MARK:{mark} -> GRADE : {GRADE}")
    except Exception as e:
        print(f"Error: {e}")


grade_calculation()


