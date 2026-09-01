import os
import subprocess
import time

def run_cmd(command, ignore_errors=False):
    print(f"\n🚀 Executing: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=not ignore_errors)
    if result.returncode != 0 and not ignore_errors:
        print(f"⚠️ Error: {result.stderr.strip()}")
    elif not ignore_errors and result.stdout:
        print(result.stdout.strip())
    time.sleep(1)

# 1. Setting up Repository and README file
repo_dir = "git-practice-day26"
os.makedirs(repo_dir, exist_ok=True)
os.chdir(repo_dir)

run_cmd("git init")
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Git Version Control & Rebase Practice\n")
run_cmd("git add README.md")
run_cmd('git commit -m "docs: add initial README file"')

# 2. Creating Artificial Merge Conflict
with open("main.py", "w", encoding="utf-8") as f:
    f.write('print("Hello World")\n')
run_cmd("git add main.py")
run_cmd('git commit -m "feat: setup initial greeting script"')

run_cmd("git checkout -b feature/new-greeting")
with open("main.py", "w", encoding="utf-8") as f:
    f.write('print("Hello User")\n')
run_cmd("git add main.py")
run_cmd('git commit -m "feat: update greeting to target users"')

run_cmd("git checkout main")
with open("main.py", "w", encoding="utf-8") as f:
    f.write('print("Hello Admin")\n')
run_cmd("git add main.py")
run_cmd('git commit -m "feat: update greeting to target admins"')

# Triggering Merge Conflict
run_cmd("git merge feature/new-greeting", ignore_errors=True)

# 3. Resolving Merge Conflict
print("\n🛠️ Conflict is being resolved automatically via Python...")
with open("main.py", "w", encoding="utf-8") as f:
    f.write('print("Hello Admin and User")\n')
run_cmd("git add main.py")
run_cmd('git commit -m "fix: resolve merge conflict in greeting script"')

# 4. Practical Refactoring (Improving the code)
refactored_code = """def generate_greeting(role: str) -> str:
    return f"Hello, {role}!"

if __name__ == "__main__":
    print(generate_greeting("Admin"))
    print(generate_greeting("User"))
"""
with open("main.py", "w", encoding="utf-8") as f:
    f.write(refactored_code)
run_cmd("git add main.py")
run_cmd('git commit -m "refactor: extract greeting logic into a modular function"')

print("\n✅ Automated phase is completed!")