no_of_process=int(input('Enter no of process: '))
no_of_resources=int(input('Enter no of resources: '))
allocated_resources=[[0 for i in range(no_of_resources)] for j in range(no_of_process)]
maxneed_resources=[[0 for i in range(no_of_resources)] for j in range(no_of_process)]
print('Enter the max need resources matrix')
for i in range(no_of_process):
    print('Enter max need for process {}'.format(i+1))
    for j in range(no_of_resources):
        maxneed_resources[i][j]=int(input())
print('Max NEEd',maxneed_resources)
for i in range(no_of_process):
    print('Enter allocated resource for process {}'.format(i+1))
    for j in range(no_of_resources):
        allocated_resources[i][j]=int(input())
print('Allocation need',allocated_resources)

resources=[0 for i in range(no_of_resources)]
print('Enter resouces')
for i in range(no_of_resources):
    resource=int(input())
available=[0 for i in range(no_of_resources)]
print('Available resources')
for i in range(no_of_resources):
    available[i]=int(input())
m=[None for i in range(no_of_process)]
k=0
for i in range(no_of_process):
    if(sum(allocated_resources[i])==0):
        m[k]=i
        k+=1
for i in range(no_of_process):
    if i not in m:
        flag=True
        for j in range(no_of_resources):
            if allocated_resources[i][j]>available[j]:
                flag=False
                break
        if flag:
             m[k]=i
             k+=1
print('Deadlock causing process')
for i in range(no_of_process):
    if i not in m:
        print(i+1)
