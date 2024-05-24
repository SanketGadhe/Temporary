no_of_files=int(input('Enter the no of files: '))
size_of_block=[None]*100
starting_block=[None]*100
t_starting_block=[None]*100
block_occupied=[[0 for x in range(100)] for y in range(100)]
for i in range(no_of_files):
    size_of_block[i]=int(input('Enter no. of blocks occupied by file {}: '.format(i+1)))
    starting_block[i]=int(input('Enter starting block of file {}: '.format(i+1)))
    t_starting_block[i]=starting_block[i]
    for j in range(size_of_block[i]):
        print('check',i,j,starting_block[i])
        block_occupied[i][j]=starting_block[i]
        starting_block[i]+=1
print('FileName Start BlockLength')
for i in range(no_of_files):
    print(i+1,'  ',t_starting_block[i],'  ',size_of_block[i])

for i in range(no_of_files):
    print('File Name',i+1)
    print(block_occupied[i][0:size_of_block[i]])
    
