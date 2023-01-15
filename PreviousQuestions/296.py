school=[]
student=[]
dic={"xijing":"西京","lushan":"鲁山","pingyang":"平阳","danling":"丹凌","xinyuan":"新元"}
#file=open("D:\\code\\python\\PreviousQuestions\\in.txt","r")
while True:
    line=file.readline().replace("\n","").split(":")
    if line==['']:
        file.close()
        break
    try:
        int(line[0])
        student.append(school[-1]+line)
    except ValueError:
        school.append(line) 
for i in student:
    print(i[2].ljust(6),end=" ")
    print(i[0].ljust(30),end=" ")
    print(i[1].ljust(16),end=" ")
    print(dic[i[3]].ljust(8),end=" ")
    print(i[7].ljust(12),end=" ")
    print(i[5].ljust(10),end=" ")
    print(i[4].ljust(4),end=" ")
    print(i[6].ljust(16))
    

