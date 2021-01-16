import os

def get_files(path, substr, suffix):
    all_files = []
    for dir, _, files in os.walk(path):
        for f in files:
            if suffix != "" and not f.endswith(suffix):
                continue

            if substr != "" and not f.find(substr):
                print(f)
                continue

            complete_path = os.path.join(dir, f)
            all_files.append(complete_path)
            print(complete_path)

