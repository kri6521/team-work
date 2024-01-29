questions = [
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] , 
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] , 
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1] ,
    ["what is my name ?" , "yuvraj" , "uv" "yuvi" ,"abhay" , 1]
]

levels = [ 1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000]
money = 0 
for i in range( 0 , len(questions)):
    question = questions[i]
    print(f"question for Rs.{int(levels[i])}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}") 

    reply = int(input("enter your answer (1-4)"))
    if(reply == question[-1]):
        print(f" correct answer , you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
                money = 32000
    else:
        print("wrong answer!!")
        break 
print( f"your take home money is {money}") 

# qt kumari present sir
