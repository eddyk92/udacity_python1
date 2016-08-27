def rename_file():
	file_list = os.listdir ("/Users/kevineddy/Udacity/FullStack/one/message")
	print(file_list)
	saved_path = os.getcwd()
	print("Current Working Directory is " + saved_path)
	os.chdir("/Users/kevineddy/Udacity/FullStack/one/message")

	for file_name in file_list:
		print("Old Name - " + file_name)
		print("New Name - " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)

rename_file()