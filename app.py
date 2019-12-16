import os


os.chdir('../../FlaskMySQLDialogflow')
print(os.getcwd())
# files = os.listdir()
# print(files)

folders_to_ignore = [".hg", ".svn", ".git", ".tox", "__pycache__", "env", "venv", ".idea"]

for root, dirs, files in os.walk(".", topdown=True):
    for folder in folders_to_ignore:
        if folder in dirs:
            dirs.remove(folder)
        for f in files:
            if os.path.splitext(f)[1] != ".py":
                files.remove(f)
    # dirs[:] = [d for d in dirs if d not in folders_to_ignore] -- this can also be used.
    print(dirs)
    print(files)
