#Numpy_project1
#student-mark-analysis
import numpy as np
np.random.seed(42)#creates different marks for all
marks = np.random.randint(35,101,size=(30,5)) 

subject =["Math","Physics", "Chemistry", "English", "Computer Science"]
student_names = [
    "Ayaan", "Zara", "Farhan", "Nusrat", "Rakib", 
    "Sadia", "Tanvir", "Meem", "Imran", "Puja", 
    "Shakil", "Lamia", "Rabby", "Anika", "Sojib", 
    "Sumaiya", "Mahmud", "Nadia", "Jahangir", "Maliha", 
    "Ashik", "Tanjim", "Fahmida", "Raihan", "Orpi", 
    "Nabil", "Tasnia", "Sabbir", "Sharmin", "Zubair"
]

totalmarks = np.sum(marks,axis =1)
averagemarks = np.mean(marks,axis=1)
averagesubject = np.mean(marks, axis =0)
highestmarkssub = np.argmax(averagesubject)
lowestsub = np.argmin(averagesubject)


while True:
    print("=================================================================================")
    print("1.The average mark of each student.")
    print("2.Overall class topper.")
    print("3.Student with the lowest overall average.")
    print("4.The highest and lowest scored subject.")
    print("5.The student who scored above 90 in all subjects. ")
    print("6.Grade of each student in each subject.")
    print("7.Grade according to averagemarks of each student")
    print("8.The students who passed all five subjects.")
    print("9.The student who failed in any subject.")
    print("10.Exit")
    
   
    print("================================================================================")

    try:
        choice = int(input("choose from above:"))

        if choice == 1:
            for i in range(len(marks)):
                print(f"{student_names[i]} has a average marks of  {averagemarks[i]}")



        elif choice ==2:
            topper_index= np.argmax(averagemarks)
            print(f"The topper of the class is {student_names[topper_index]}")
                



        elif choice == 3:
            backbencher_index = np.argmin(averagemarks)
            print(f"The lowest scores student of the class is  {student_names[backbencher_index]}")
             



        elif choice==4:
            
            print(f"The highest scored subject is {subject[highestmarkssub] }")
            print(f"The lowest scored subject is {subject[lowestsub] }")
                



        elif choice ==5:
            ninetyabove = np.all(marks>90, axis =1)
            ninety_index = np.where(ninetyabove)[0]
          
            if len(ninety_index) > 0:
               for i in ninety_index:
                  print(student_names[i])
                 
            else:
                print("There are none.")



        elif choice ==6:
            
            condition_marks = [marks >=90,
                         marks >=80,
                         marks>=70,
                         marks>=60,
                         marks>=50,
                         marks>=40
                         ]
            grades = ["A+","A","A-","B","C","D"]
            fixing_grades =np.select(condition_marks,grades,default = "F")

            
            for i in range(len(student_names)):
                print("--------------------------------------------------------------------")
                print(f"Student : {student_names[i]}")

                for j in range(len(subject)):
                    print(f" {subject[j]} : {fixing_grades[i,j]}" )



        elif choice ==7:
             condition_average = [averagemarks >= 90,
                                    averagemarks >= 80,
                                    averagemarks >= 70,
                                    averagemarks >= 60,
                                    averagemarks >= 50,
                                    averagemarks >= 40
                                     
             ]
             grades = ["A+","A","A-","B","C","D"]
             fixing_grades_final = np.select(condition_average,grades, default ="F")
             for i in range(len(averagemarks)):
                 print("-------------------------------------------------------------")
                 print(f"Name :{student_names[i]} \n Grade: {fixing_grades_final[i]}")



        elif choice ==8:

            passedall = np.all(marks>= 40,axis =1)
            passed_index = np.where(passedall)[0]

            if len(passed_index)>0:
                for i in passed_index:
                     print(f"The student who passed in all 5 subjects are {student_names[i]}")
            else:
                 print("No student passed all five subjects.")



        elif choice ==9:
            failedany = np.any(marks < 40,axis = 1)
            failed_index = np.where(failedany)[0]
            
            if len(failed_index)>0:
                for i in failed_index:
                    print(f"{student_names[i]} failed in a subject  ")
                    
            else:
                print("No body Failed.")
               

        
        elif choice ==10:
            print("Have a good day!!")
            break


        else:
            print("Please enter a number from above.")

    except ValueError:
        print("Please choose a whole number from above!!")
        
             