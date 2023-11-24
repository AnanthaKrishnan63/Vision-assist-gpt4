import whisper
import os
from PIL import Image

#TO RESIZE THE IMAGE
def imgresize():
#Create an Image Object from an Image
    im = Image.open('PXL_20231112_155050486.jpg')
#Display actual image
    im.show()
#Make the new image half the width and half the height of the original image
    resized_im = im.resize((round(im.size[0]*0.1693121), round(im.size[1]*0.126984)))
#Display the resized imaged
    resized_im.show()
#Save the cropped image
    resized_im.save('PXL_20231112_155050486_resized_1.jpg')

# this is Speech to text codeblock
def stt():
    model = whisper.load_model("small.en")
    result = model.transcribe("test3.mp4")
    return result["text"]
x=stt()
print(x)

#to del the audio file after processing
def delaudio(): 
    os.remove('test3.mp4')

delaudio()
 