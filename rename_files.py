import os

def rename_files():
	# (1) get file names from a folder
	file_list = os.listdir("prank")
	saved_path = os.getcwd()
	os.chdir("prank")
	# (2) for each file, rename filename
	for file_name in file_list:
		new_name = file_name.translate(None, "0123456789")
		os.rename(file_name, new_name)
		print(new_name)

	os.chdir(saved_path)

rename_files()