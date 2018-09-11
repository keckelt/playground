import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt


print('Started script.')
# define the model options and run
options = {
    'model': 'bin/prjeddie/yolov2-tiny.cfg',
    'load': 'bin/prjeddie/yolov2-tiny.weights',
    'threshold': 0.4,
    'gpu': 0
}

print('Loading darkflow.')
tfnet = TFNet(options)


print('Read image')
# read the color image and covert to RGB
img = cv2.imread('media/input/1395447642477-linzerstr.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print('Predict the image')
# use YOLO to predict the image
predictions = tfnet.return_predict(img)

# pull out some info from the results
print('Render result')

for prediction in predictions:
    tl = (prediction['topleft']['x'], prediction['topleft']['y'])
    br = (prediction['bottomright']['x'], prediction['bottomright']['y'])
    label = prediction['label']

    # add the box and label and display it
    img = cv2.rectangle(img, tl, br, (0, 255, 0), 4)
    img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    
plt.imshow(img)
plt.show()