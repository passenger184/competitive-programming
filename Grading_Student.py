def gradingStudents(grades):
    # Write your code here
    grade = []
    for i in grades:
        if i < 38:
            grade.append(i)
        else:
            x = i % 5
            if x < 3:
                grade.append(i)
            else:
                grade.append(i + (5 -x))    
                
    return grade
