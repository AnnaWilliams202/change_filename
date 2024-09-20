import os
from datetime import datetime


directory = '/Users/annawilliams/Desktop/files'
filenames = os.listdir(directory)  # Get the list of all files
day = datetime.now().strftime('%Y-%m-%d')  # Set a format for the date

for f in filenames:
    filepath = os.path.join(directory, f)

    # Check if the file has a .txt extension because it was renaming py file as well
    if f.endswith('.txt'):
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Create the new filename with the date appended
        new_filename = f'{f[:-4]}-{day}.txt'
        new_filepath = os.path.join(directory, new_filename)
        
        os.rename(filepath, new_filepath)
        print(f'Renamed {f} to {new_filename}')
    else:
        print(f'Skipping {f}, not a .txt file.')
