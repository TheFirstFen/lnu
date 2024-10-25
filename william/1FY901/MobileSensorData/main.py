from scipy.io import loadmat
import pandas as pd

# Load the .mat file
mat = loadmat("drop.mat")

# Extract the acceleration data from the dictionary
acceleration_data = mat['None'][0][0][3][0]

# Convert the acceleration data into a Pandas DataFrame
df = pd.DataFrame(acceleration_data, columns=['X', 'Y', 'Z'])

# Display the first few rows of the DataFrame
print(df.head())
