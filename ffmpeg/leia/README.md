# Cut VIdeo
 ffmpeg -i leia.webm -ss 00:00:29.5 -c copy -t 00:00:10.0 leia-cut.webm

# Crop Video
 ffmpeg -i leia-cut.webm -vf crop=360:300:0:100 leia-crop.webm
