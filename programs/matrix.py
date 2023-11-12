# [[1,2,3],[4,5,6],[7,8,9]]


row1 = ['😍','😍','😍']
row2 = ['😍','😍','😍']
row3 = ['😍','😍','😍']

matrix = [
    row1,row2,row3
]

print(f'{row1}\n {row2}\n {row3}')

row, col = input('Enter the row and column in (3,3) saparated by comma to hide the Data : \n').split(',')

selected_row = matrix[int(row)-1]
selected_row[int(col)-1] = 'xx'

print(f'{row1}\n {row2}\n {row3}')
# print(f'{matrix[0]}\n {matrix[1]}\n {matrix[2]}')
