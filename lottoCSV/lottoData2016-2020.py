import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Download latest version
path = kagglehub.dataset_download("gogo827jz/uk-lotto-draw-history-20162020")
print("Path to dataset files:", path)

file_path = "/Users/shantirai/.cache/kagglehub/datasets/gogo827jz/uk-lotto-draw-history-20162020/versions/1/lotto_history.csv"
data = pd.read_csv(file_path)
print(data)

#what numbers show up and how many times for ball_1
ball_1_counts = data['Ball_1'].value_counts() # Count occurrences of each value in the 'Ball_1' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_1_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of Numbers in Ball_1')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()




# Ball_2
#what numbers show up and how many times for ball_2
ball_2_counts = data['Ball_2'].value_counts() # Count occurrences of each value in the 'Ball_2' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_2_counts.plot(kind='bar', color='pink')
plt.title('Frequency of Numbers in Ball_2')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()



#ball_3
#what numbers show up and how many times for ball_3
ball_3_counts = data['Ball_3'].value_counts() # Count occurrences of each value in the 'Ball_1' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_3_counts.plot(kind='bar', color='red')
plt.title('Frequency of Numbers in Ball_3')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()



#ball_4
#what numbers show up and how many times for ball_4
ball_4_counts = data['Ball_4'].value_counts() # Count occurrences of each value in the 'Ball_4' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_4_counts.plot(kind='bar', color='green')
plt.title('Frequency of Numbers in Ball_4')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()




#ball_5
#what numbers show up and how many times for ball_5
ball_5_counts = data['Ball_5'].value_counts() # Count occurrences of each value in the 'Ball_5' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_5_counts.plot(kind='bar', color='orange')
plt.title('Frequency of Numbers in Ball_5')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()




#ball_6
#what numbers show up and how many times for ball_1
ball_6_counts = data['Ball_6'].value_counts() # Count occurrences of each value in the 'Ball_6' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
ball_6_counts.plot(kind='bar', color='magenta')
plt.title('Frequency of Numbers in Ball_6')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()




#bonus_ball
#what numbers show up and how many times for Bonus_Ball
bonus_ball_counts = data['Ball_Bonus'].value_counts() # Count occurrences of each value in the 'Ball_Bonus' column

# Plot the counts as a bar chart
plt.figure(figsize=(10, 6))
bonus_ball_counts.plot(kind='bar', color='brown')
plt.title('Frequency of Numbers in Bonus_Ball')
plt.xlabel('Number')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate numbers for better readability if needed
plt.show()






