# Requirements

## Prepare python environment
Create:
```console
conda create --name darkflow python=3.6
```

and activate:
```console
source activate darkflow
```

## Install dependencies
```console
pip install Cython
pip install numpy
pip install tensorflow
pip install opencv-python
```

## Install darkflow:
I install darkflow globally, becasue I didn't wan't to mix my files with the repo files in one folder:
```console
git clone git@github.com:thtrieu/darkflow.git
cd darkflow/
pip install -e .
cd ..
```

# Run
## Yolo v2 (608x608)
Download weights and config from [Joseph Redmon](https://pjreddie.com/darknet/yolo/).
```console
mkdir bin
cd bin/
wget https://pjreddie.com/media/files/yolov2.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2.cfg
cd ..
```

This model is trained on the COCO dataset.
Get correct labels:
```console
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names -O labels.txt
```

Get some video (`video.mp4`) and run:
```console
flow --model bin/prjeddie/yolov2.cfg --load bin/prjeddie/yolov2.weights --demo media/input/video.mp4 --saveVideo
```
## Yolo v2 (tiny)
Download weights and config from [Joseph Redmon](https://pjreddie.com/darknet/yolo/).
```console
mkdir bin
cd bin/
wget https://pjreddie.com/media/files/yolov2-tiny.weights
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2-tiny.cfg
cd ..
```

This model is trained on the COCO dataset.
Get correct labels:
```console
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names -O labels.txt
```

Add workaround to fix `AssertionError: expect 44948596 bytes, found 44948600` by replacing `self.offset = 16` with `self.offset = 20` in `darkflow/darkflow/utils/loader.py` `weights_walker` function.

Or, to stay compatible with the other models replace it with:
```python
            if 'yolov2-tiny.weights' in path:
                self.offset = 20
            else:
                self.offset = 16
```


Get some video (`video.mp4`) and run:
```console
flow --model bin/prjeddie/yolov2.cfg --load bin/prjeddie/yolov2.weights --demo media/input/video.mp4 --saveVideo
```

## Yolo v2 (voc tiny)
Download weights and config from [Joseph Redmon](https://pjreddie.com/darknet/yolo/).
Darkflow author Trieu H. Trinh also has some weights in his [ Google Drive](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU).
```console
mkdir bin
cd bin/
wget https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov2-tiny-voc.cfg
wget https://pjreddie.com/media/files/yolov2-tiny-voc.weights
cd ..
```

This model is trained on the VOC dataset (2007+2012).
Get correct labels:
```console
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/voc.names -O labels.txt
```

Get some video (`video.mp4`) and run:
```console
flow --model bin/prjeddie/yolov2-tiny-voc.cfg --load bin/prjeddie/yolov2-tiny-voc.weights --demo media/input/video.mp4 --saveVideo
```