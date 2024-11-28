import json
import os

# Load the JSON file
with open('Front-End/public/teas.json', 'r') as file:
    data = json.load(file)

# Base folder for the Markdown files
output_base_folder = "teas_md"
os.makedirs(output_base_folder, exist_ok=True)

# Process each category and its teas
for category, content in data.items():
    # Create a folder for the category
    category_folder = os.path.join(output_base_folder, category.replace(' ', '-'))
    os.makedirs(category_folder, exist_ok=True)
    
    # Process each tea in the category
    for tea in content.get('tealist', []):
        tea_id = tea.get('id')
        group = tea.get('group')
        tea_type = tea.get('type')
        name = tea['tea']['name']
        details = tea['tea']['details']
        
        # Create a string for the Markdown content
        md_content = f"""---
id: {tea_id}
group: "{group}"
type: "{tea_type}"
name: "{name}"
description: "{details['description']}"
origin: "{details['origin']}"
harvest_notes: "{details['harvest_notes']}"
brewing_methods: "{details['brewing_methods']}"
health_benefits: "{details['health_benefits']}"
popularity: "{details['popularity']}"
layout: ../../../layouts/teaPage.astro
---
"""

        # File name based on the tea name
        file_name = f"{name}.md"
        file_path = os.path.join(category_folder, file_name)
        
        # Write to the Markdown file
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(md_content)

print(f"Markdown files have been created in the '{output_base_folder}' directory, organized by categories.")
