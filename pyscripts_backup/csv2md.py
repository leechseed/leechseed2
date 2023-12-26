import pandas as pd
import os

def csv_to_markdown(csv_file_path, md_file_name):
    # Read CSV content
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to Markdown table format
    markdown_table = df.to_markdown(index=False)

    # Construct Markdown file path in the same folder as the CSV file
    md_file_path = os.path.join(os.path.dirname(csv_file_path), md_file_name)

    # Write markdown table to file
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(markdown_table)

    return md_file_path

# File paths
csv_file_path = r'C:\Users\U01_LEECHSEED\Desktop\LEECHSEED_GIT\leechseed2\leechseed2\OBSIDIAN_CATALOG\LIBRARY\00_THEORY OF COMPOSITION\00001_BAL - Narratology Introduction\00001E output.csv'
md_file_name = '00001E-BAL - Narratology Complete Glossary.md'  # Markdown file name

# Convert CSV to Markdown and get the path of the Markdown file
md_file_path = csv_to_markdown(csv_file_path, md_file_name)

print(f"Markdown file created: {md_file_path}")
