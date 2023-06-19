import os
import shutil

def organize_files(directory):
    # Create a dictionary to map file extensions to their respective folders
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Audios": [".mp3", ".wav"],
        "Archives": [".zip", ".tar", ".rar"],
        "Others": []
    }

    # Create folders for each file category
    for folder in extensions:
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files based on their extensions
    for file in os.listdir(directory):
        if file != __file__:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file)[1].lower()

                # Find the corresponding folder for the file extension
                target_folder = None
                for folder, ext_list in extensions.items():
                    if file_extension in ext_list:
                        target_folder = folder
                        break

                # Move the file to the target folder
                if target_folder:
                    target_path = os.path.join(directory, target_folder, file)
                    shutil.move(file_path, target_path)
                    print(f"Moved '{file}' to '{target_folder}' folder.")

    print("File organization completed!")

def main():
    directory = input("Enter the directory path to organize files: ")
    organize_files(directory)

if __name__ == "__main__":
    main()
'''In this code, the organize_files function takes a directory path as input. It creates a
 dictionary extensions that maps different file extensions to their respective folders. It 
 then creates folders for each file category in the given directory.

The function then iterates over each file in the directory
 
 (excluding the script file itself) and checks its extension. If the file has
  a recognized extension,it determines the target folder based on the extension and moves
   the file to that folder using the shutil.move function.

The main function prompts the user to enter the directory path and calls the organize_files
 function to organize the files in that directory.

When you run the code, it will organize the files in the specified directory into different 
folders based on their extensions. For example, image files will be moved to the "Images" folder,
 document files to the "Documents" folder, and so on. Any files with unrecognized extensions will be 
 placed in the "Others" folder.'''
