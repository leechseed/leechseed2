import pandas as pd

def markdown_to_csv(md_file_path, csv_file_path, log_file_path):
    # Read markdown content from file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process the lines to extract table data
    table_data = []
    for line in lines:
        if '|' in line:
            cells = line.strip().strip('|').split('|')
            # Remove markdown formatting and consider only rows with exactly 2 columns
            if len(cells) == 2:
                table_data.append([cell.strip().strip('*') for cell in cells])

    if not table_data:
        raise ValueError("No valid table data found in the Markdown file.")

    # Create DataFrame
    df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Assuming the first row is the header

    # Add a temporary lowercase column for case-insensitive sorting
    df['Term_lowercase'] = df[df.columns[0]].str.lower()

    # Identify and remove duplicates, saving them to a log file
    duplicates = df[df.duplicated('Term_lowercase', keep='first')]
    df_no_duplicates = df.drop_duplicates('Term_lowercase', keep='first')

    # Save duplicates to log file
    duplicates.to_csv(log_file_path, index=False)

    # Sort the DataFrame by the lowercase column and write to CSV
    df_sorted = df_no_duplicates.sort_values(by='Term_lowercase')
    df_sorted.drop('Term_lowercase', axis=1, inplace=True)  # Remove the temporary column
    df_sorted.to_csv(csv_file_path, index=False)

markdown_file_path = r'C:\Users\U01_LEECHSEED\Desktop\LEECHSEED_GIT\leechseed2\leechseed2\OBSIDIAN_CATALOG\LIBRARY\00_THEORY OF COMPOSITION\00001_BAL - Narratology Introduction\00001E-BAL - Narratology Complete Glossary.md'
csv_file_path = r'C:\Users\U01_LEECHSEED\Desktop\output.csv'
log_file_path = r'C:\Users\U01_LEECHSEED\Desktop\duplicates_log.csv'

# Convert markdown to CSV, sort, and log duplicates
try:
    markdown_to_csv(markdown_file_path, csv_file_path, log_file_path)
    print(f"CSV file '{csv_file_path}' created and sorted by term.")
    print(f"Duplicate entries logged in '{log_file_path}'.")
except ValueError as e:
    print(f"Error: {e}")
