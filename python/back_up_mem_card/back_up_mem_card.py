import shutil, os

copy_list = [
    # [source, destionation],
    [r"C:\Users\USERNAME\Documents\Games\Playstation 1\ePSXe205\memcards\epsxe000.mcr", r"C:\Users\USERNAME\Documents\Games\Playstation 1\memcards\USERNAME Mem Card 1\epsxe000.mcr"],
    [r"C:\Users\USERNAME\Documents\Games\Playstation 1\ePSXe205\memcards\epsxe001.mcr", r"C:\Users\USERNAME\Documents\Games\Playstation 1\memcards\USERNAME Mem Card 1\epsxe001.mcr"]
]

for copy in copy_list:
    src, dst = copy

    shutil.copyfile(src, dst)

folder_path = r"C:\Users\USERNAME\Documents\Games\Playstation 1\memcards\USERNAME Mem Card 1"

os.startfile(folder_path)