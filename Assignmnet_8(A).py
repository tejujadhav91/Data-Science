import pandas as pd

data = {
    'Name': ['nilam', 'shruti', 'snehal', 'saniya', 'shravni'],
    'Age': [21, 22, 20, 23, 19],
    'Marks': [85, 90, 78, 84, 88]
}

df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)

print("data.csv file created successfully!")
print("\nPreview:\n", df)
