# Split Video
00:48-00:51
```
ffmpeg -i 9000.webm -ss 00:00:48 -c copy -t 00:00:03.0 9000.part1.webm
```
00:52-00:55
```
ffmpeg -i 9000.webm -ss 00:00:52 -c copy -t 00:00:03.6 9000.part2.webm
```

# Add Text
https://ffmpeg.org/ffmpeg-filters.html#drawtext-1
```
ffmpeg -i 9000.part1.webm -vf drawtext="fontfile=/opt/pycharm-professional/jre64/lib/fonts/DroidSans.ttf: \
text='What does the scouter say about his power level?': fontcolor=white: fontsize=13: box=1: boxcolor=black@0.5: \
boxborderw=5: x=(w-text_w)/2: y=7*(h-text_h)/8" -codec:a copy 9000.part1.text.webm
```

```
ffmpeg -i 9000.part2.webm -vf drawtext="fontfile=/opt/pycharm-professional/jre64/lib/fonts/DroidSans.ttf: \
text='ITS OVER 9000!': fontcolor=white: fontsize=32: box=1: boxcolor=black@0.5: \
boxborderw=5: x=(w-text_w)/2: y=7*(h-text_h)/8" -codec:a copy 9000.part2.text.webm
```

# Photo
## ZoomPan Image
See https://el-tramo.be/blog/ken-burns-ffmpeg/

### Topleft
```
ffmpeg -i cropped.jpg -filter_complex "zoompan=z='zoom+0.01':d=25*3:s=320x240" -pix_fmt yuv420p -c:v libx264 zoompan.mp4
```

### Bottom Left
```
ffmpeg -i cropped.jpg -filter_complex "zoompan=z='zoom+0.01':d=25*3:y='ih-ih/zoom':s=320x240" -pix_fmt yuv420p -c:v libx264 zoompan.mp4
```

### Bottom and slightly right
```
ffmpeg -i cropped.jpg -filter_complex "zoompan=z='zoom+0.01':d=25*3:y='ih-ih/zoom':x='55*zoom':s=320x240" -pix_fmt yuv420p -c:v libvpx-vp9 zoompan.webm
```


# Concat
https://trac.ffmpeg.org/wiki/Concatenate#protocol
```
ffmpeg -f concat -i concatlist.txt -c copy output.webm
```


# To Gif
```
ffmpeg -i input.webm -pix_fmt rgb24 output.gif
```