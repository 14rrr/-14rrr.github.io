import webbrowser
class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video():
	title = input("Enter title: ") + "\n"
	link = input("Enter link: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ", video.title, end="")
	print("Video link: ", video.link, end="")

def read_videos():
	videos = []
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("Enter video ", i+1)
		vid = read_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	for i in range(len(videos)):
		print("Video " + str(i + 1) + ":")
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)

def write_videos_txt(videos,file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_txt(videos[i], file)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()		
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_description = input("Enter playlist description: ") + "\n"
	playlist_rating = input("Enter rating (1-5): ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data_blog.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file)
	print("Successfully write playlist to txt")

def read_playlist_from_txt():
	with open("data_blog.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("-------")
	print("Playlist name: " +  playlist.name, end="")
	print("Playlist description: " +  playlist.description, end="")
	print("Playlist rating: " +  playlist.rating, end="")
	print_videos(playlist.videos)

def show_menu():
	print("Main Menu:")
	print("------------------------------")
	print("| Option 1: Create playlist  |")
	print("| Option 2: Show playlist    |")
	print("| Option 3: Play a video     |")
	print("| Option 4: Add a video      |")
	print("| Option 5: Update playlist  |")
	print("| Option 6: Remove video     |")
	print("| Option 7: Save and Exit    |")
	print("------------------------------")

def select_in_range(prompt , min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max :
		choice = input(prompt)
	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)

	choice = select_in_range("Select an option (1," + str(total) + "):",1,total)
	print("Open video:" + playlist.videos[choice-1].title + playlist.videos[choice-1].link , end="")
	playlist.videos[choice-1].open()

def add_video(playlist):
	print("Enter a video informent:")
	new_video_title = input("Video title: ") + "\n"
	new_video_link = input("Video link: ") + "\n"
	new_video = Video(new_video_title,new_video_link)
	playlist.videos.append(new_video)
	return playlist

def update_playlist(playlist):
	print("Update playlist?")
	print("1. Name")
	print("2. Description")
	print("3. Rating")

	choice = select_in_range("Enter what you want to update: ",1,5)
	if choice == 1:
		new_playlist_name = input("Enter new name playlist: ") + "\n"
		playlist.name = new_playlist_name
		return playlist 

	elif choice == 2:
		new_playlist_description = input("Enter new description playlist: ") + "\n"
		playlist.name = new_playlist_description
		return playlist

	elif choice == 3:
		new_playlist_rating = str(select_in_range("Enter new rating playlist (1-5): ",1,5)) + "\n"
		playlist.rating = new_playlist_rating
		return playlist

def remove_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	choice = select_in_range("Enter you want to delete: ",1,total)
	del playlist.videos[choice-1]
	print("Delete Successfully !!!")
	return playlist

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully !!!")
	except:
		print("Welcome first user !!!")		

	while True:
		show_menu()
		choice = select_in_range("Select an option (1-7):",1 ,7 )
		if choice == 1:
			playlist = read_playlist()
			input("\nPress enter to continue...\n")		
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress enter to continue...\n")	
		elif choice == 3:
			play_video(playlist)
			input("\nPress enter to continue...\n")	
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress enter to continue...\n")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress enter to continue...\n")
		elif choice == 6:
			playlist = remove_video(playlist)
			input("\nPress enter to continue...\n")
		elif choice == 7:
			write_playlist_txt(playlist)
			input("\nPress enter to continue...\n")	
			break
		else:
			print("Error input")
			break
main()