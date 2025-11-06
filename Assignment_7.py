import pandas as pd

data = {
    'Name': ['Nilam', 'Shruti', 'snehal', 'saniya', 'shravni'],
    'Age': [25, 22, 23, 24, 26],
    'Marks': [85, 90, 88, 92, 79],
    'City': ['kolhapur', 'gadhinglaj', 'kale', 'koparde', 'kolhapur']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nFirst 3 Rows (head):")
print(df.head(3))

print("\nLast 2 Rows (tail):")
print(df.tail(2))

print("\nSelect 'Name' and 'Marks' columns:")
print(df[['Name', 'Marks']])

print("\nStudents older than 23:")
print(df[df['Age'] > 23])

print("\nSorted by Marks (descending):")
print(df.sort_values(by='Marks',ascending=False))

df['Result'] = ['Pass' if m >= 85 else 'Fail' for m in df['Marks']]
print("\nAfter adding Result column:")
print(df)

new_row = {'Name': 'Meena', 'Age': 21, 'Marks': 84, 'City': 'Chennai', 'Result': 'Fail'}
df.loc[len(df)] = new_row
print("\nAfter adding new row:")
print(df)
