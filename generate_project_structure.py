import os
import yaml
import shutil

# Remove the 'projects' folder if it exists and all its contents
if os.path.exists('projects'):
    shutil.rmtree('projects')

# Assuming 'TableOfContents.yml' is in the root of the repository
file_path = os.path.join(os.getcwd(), 'TableOfContents.yml')

with open(file_path, 'r') as file:
    projects = yaml.safe_load(file)

# Check if 'Projects' key exists in the YAML file
if isinstance(projects, list):
    for project_data in projects:
        project = project_data.get('Project', {})
        project_number = project.get('Number')
        project_title = project.get('Title')
        contributor = project.get('Contributor', [])

        # Skip projects without 'Number' or 'Title' keys
        if project_number is None or project_title is None:
            print(f"Skipping invalid project: {project}")
            continue

        folder_name = f"projects/{project_number}_{project_title.replace(' ', '_')}"
        os.makedirs(folder_name, exist_ok=True)

        with open(f"{folder_name}/README.md", 'w') as readme_file:
            readme_file.write(
                f"# {project_title} ({project_number})\n\n"
                f"Contributor: {contributor if contributor else 'None'}\n\n"
                f"Difficulty: {project.get('Difficulty', 'Unknown')}\n\n{project.get('Description', 'No description provided')}")

        with open(f"{folder_name}/{project_number}_{project_title.replace(' ', '_')}.py", 'w') as code_file:
            code_file.write(
                f"# {project_title} ({project_number})\n"
                f"# Contributor: {contributor if contributor else 'None'}\n"
                f"# Difficulty: {project.get('Difficulty', 'Unknown')}\n"
                "# " + "\n# ".join(project.get('Description', 'No description provided').split('\n')) + "\n\n"
                f"# Add your code here"
            )

else:
    print("Invalid YAML file format. Please ensure that the 'Projects' key is present.")
