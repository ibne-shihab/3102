import pandas as pd

Stu_Info=[["Student Name","Roll","CGPA"],
         ["Sayeeda",200604,4.00],
         ["Khan",200604,4.00],
         ["A",515448,0.00],
         ["B",2544545,2.00]]
Student_Information = pd.DataFrame(Stu_Info)


Student_Information



Student_Information=pd.DataFrame(Stu_Info[1:],columns=Stu_Info[0])



Student_Information




Student_Information.to_csv('Student_Information.csv')



SI=pd.read_csv('Student_Information.csv')




SI




mean=SI['CGPA'].mean()
print(f"Mean is:{mean}")




median=SI['CGPA'].median()
print(f"Median is:{median}")




mode=SI['CGPA'].mode()
print(f"Mode is:{mode}")





variance=SI['CGPA'].var()
print(f"variance is:{variance}")




SD=SI['CGPA'].std()
print(f"Sta_Dev is:{SD}")





