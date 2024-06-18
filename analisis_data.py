import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D

# Load data from CSV files
data_mahasiswa = pd.read_csv('Data_Mahasiswa.csv')
performa_akademik = pd.read_csv('Performa_Akademik.csv')
penggunaan_ai = pd.read_csv('Penggunaan_AI.csv')

# Merge data
merged_data = data_mahasiswa.merge(performa_akademik, on='ID').merge(penggunaan_ai, on='ID')

# Calculate the difference in grades and attendance before and after AI usage
merged_data['Grade_Change'] = merged_data['Grades_After'] - merged_data['Grades_Before']
merged_data['Attendance_Change'] = merged_data['Attendance_After (%)'] - merged_data['Attendance_Before (%)']

# Define a color palette
palette = sns.color_palette("coolwarm", as_cmap=True)

# 1. Descriptive statistics
print("Descriptive Statistics:")
print(merged_data.describe())

# 2. Distribution of Grades and Attendance Before and After AI Usage
plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Grades_Before'], kde=True, color=palette(0.2), label='Grades Before', bins=10)
sns.histplot(merged_data['Grades_After'], kde=True, color=palette(0.8), label='Grades After', bins=10)
plt.title('Distribution of Grades Before and After AI Usage')
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Attendance_Before (%)'], kde=True, color=palette(0.2), label='Attendance Before', bins=10)
sns.histplot(merged_data['Attendance_After (%)'], kde=True, color=palette(0.8), label='Attendance After', bins=10)
plt.title('Distribution of Attendance Before and After AI Usage')
plt.xlabel('Attendance (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 3. Distribution of Grade and Attendance Changes
plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Grade_Change'], kde=True, color=palette(0.5))
plt.title('Distribution of Grade Changes After AI Usage')
plt.xlabel('Grade Change')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(merged_data['Attendance_Change'], kde=True, color=palette(0.5))
plt.title('Distribution of Attendance Changes After AI Usage')
plt.xlabel('Attendance Change (%)')
plt.ylabel('Frequency')
plt.show()

# 4. Analysis by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Gender', y='Grade_Change', palette='coolwarm')
plt.title('Grade Change by Gender')
plt.xlabel('Gender')
plt.ylabel('Grade Change')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Gender', y='Attendance_Change', palette='coolwarm')
plt.title('Attendance Change by Gender')
plt.xlabel('Gender')
plt.ylabel('Attendance Change (%)')
plt.show()

# 5. Analysis by Major
plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Major', y='Grade_Change', palette='coolwarm')
plt.title('Grade Change by Major')
plt.xlabel('Major')
plt.ylabel('Grade Change')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(data=merged_data, x='Major', y='Attendance_Change', palette='coolwarm')
plt.title('Attendance Change by Major')
plt.xlabel('Major')
plt.ylabel('Attendance Change (%)')
plt.show()

# 6. AI Usage vs Grade Change and Attendance Change
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(merged_data['Usage_Hours_per_Week'], merged_data['Grade_Change'], merged_data['Attendance_Change'], c=merged_data['Grade_Change'], cmap='coolwarm')
ax.set_title('AI Usage vs Grade Change and Attendance Change')
ax.set_xlabel('AI Usage Hours per Week')
ax.set_ylabel('Grade Change')
ax.set_zlabel('Attendance Change (%)')
fig.colorbar(scatter, ax=ax)
plt.show()

# 7. Correlation Analysis
correlation_matrix = merged_data[['Usage_Hours_per_Week', 'Grade_Change', 'Attendance_Change']].corr()
print("Correlation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

# 8. Simple Linear Regression Analysis
X = merged_data['Usage_Hours_per_Week']
y = merged_data['Grade_Change']
X = sm.add_constant(X)  # adding a constant
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print(model.summary())

# Plot regression line
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(merged_data['Usage_Hours_per_Week'], merged_data['Grade_Change'], predictions, c=merged_data['Grade_Change'], cmap='coolwarm')
ax.set_title('AI Usage vs Grade Change with Regression Line')
ax.set_xlabel('AI Usage Hours per Week')
ax.set_ylabel('Grade Change')
ax.set_zlabel('Predicted Grade Change')
fig.colorbar(scatter, ax=ax)
plt.show()
