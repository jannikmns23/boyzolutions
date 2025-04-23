import os
from datetime import datetime

# Settings
repo_path = r"B:\boyzolutions"  # Repo Path of local repository
filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
file_path = os.path.join(repo_path, filename)

# 1. Create a dummy Python file
with open(file_path, "w") as f:
    f.write(f"# Auto-generated file at {datetime.now()}\nprint('Hello world')\n")

# 2. Git automation
os.chdir(repo_path)
os.system(f"git add {filename}")
os.system(f'git commit -m "Auto push: {filename}"')
os.system("git push origin main")  # Replace with your branch
