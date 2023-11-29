# copyfile() = copies contents of a file
# copy()=copyfile() + permissions mode + destination can be directory
# copy2() = copyfile() + copuy metadata (files crations and modification time)

import shutil
shutil.copyfile("./file.txt", "./copy.txt")  # src,dest
