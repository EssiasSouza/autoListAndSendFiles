# AUTO LIST AND SEND FILES

This application goals is to send files from a directory to a list of destination directories. The application is capable to list all folders in the root directory and look for the destinations that matches with the term from the destination file list. For example:

If do you have a list with terms as:

- Dir202412
- Folder1500
- FolderTest
- FolderTwo

And you need to look for this folders in C:\Backups\ that have dirs as:

- C:\Backups\Dir202312
- C:\Backups\Dir202412
- C:\Backups\Folder1500
- C:\Backups\FolderTest

The application can do it as the example below.

- Found C:\Backups\Dir202412
- Found C:\Backups\Folder1500
- Found C:\Backups\FolderTest
- Not found FolderTwo

And if into these folder exists other folder, the application is capable to perform the search as well.

Example:

Subfolder = Pack01

- Found C:\Backups\Dir202412\Pack01
- Found C:\Backups\Folder1500\Pack01
- Found C:\Backups\FolderTest\Pack01
- Not found FolderTwo

To copy files is necessary to put into the folder to send and all files that be there will be copied.

- Copy successfuly C:\Backups\Dir202412\Pack01\Test01.txt
- Copy successfuly C:\Backups\Dir202412\Pack01\Test02.txt

- Copy successfuly C:\Backups\Folder1500\Pack01\Test01.txt
- Copy successfuly C:\Backups\Folder1500\Pack01\Test02.txt

- Copy successfuly C:\Backups\FolderTest\Pack01\Test01.txt
- Copy successfuly C:\Backups\FolderTest\Pack01\Test02.txt

- Not found FolderTwo

## HOW IT WORKS

The application starts reading the file of destinations (this file should be set in the `settings.json/Destinations` file). After this the application also read the root from `settings.json/root_folder`. With these two lists the application will look for the destinations in the root_folder. To each found folder the an information is appended to the list of destinations. If there is a subfolder in `settings.json/SubFolders` the appliction will compose the path as `root_folder`/`destination`/`subfolder`. Once with the full path, the application starts to copy each files in the `settings.json/filesSource` to the destination path.

The path and log file can be also configured in the settings.json.

````
[
    {
        "PARAMETERS": {
        "root_folder": "\\\\server\\root_folder",
        "filesSource":  ".\\files-to-be-sent", 
        "SubFolders": "pack-1",
        "Destinations": "destination-list.txt"
        }
    },
    {
        "logs_path": ".\\logs",
        "log_name": "sentFiles.log"
    }

]
````