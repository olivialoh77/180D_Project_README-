import easyocr 
import cv2 

#interface
lang = 'en' #default 

#robot arm
robotarm = False


while 1:
    nextpage = False

    #Text capture 
    camera_result = "Test"

    #OCR process 
    reader = easyocr.Reader([lang],gpu=False)
    OCR_result = reader.readtext(camera_result)

    #send OCR_result 

    #While text still in result 
    counter = OCR_result.length

    while counter != 0:
        #Diplay on GUI
        print(OCR_result)

        #Voice reader of text 

        #if stop with Gesture or Pose or Voice
        
        #if Annotation 

        #if speed up or slow down 

        #if user wants to completely stop 
        if exit:
            quit()

        counter = counter - 1
        
    #wait for user to input command
    

    #Exit if no more pages 
    if not nextpage:
        quit()
