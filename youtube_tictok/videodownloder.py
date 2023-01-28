from pytube import YouTube

#location where you save.
PATH = "D:/" #to_do 

#link of video.
link=["https://www.youtube.com/watch?v=p8FuTenSWPI", 
	"https://www.youtube.com/watch?v=JWbnEt3xuos"
	]#list of video links. 
for i in link: 
	try: 
		yt = YouTube(i) 
	except: 
		print("Connection Error") #to handle exception 
	
	#check files with "mp4" extension 
	try:
		# mp4files = yt.streams.filter(progressive = True,file_extension = "mp4").first().download(output_path = "E:\Mohamed's sessions\pytube", 	filename = "Reiner and Bertholdt Transformation scene")
		stream = yt.streams.first()
	except:
		print("Connection Error") #to handle exception 

	# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
	try: 
		stream.download() 
	except: 
		print("Some Error!") 
print('Task Completed!') 
