Sign Language App
==========================================

In this activity, you will learn to show the messages based on different hand signs.


<img src= "https://media.slid.es/uploads/1525749/images/10511522/pcp.gif" width = "480" height = "320">


Follow the given steps to complete this activity:


1. Set messages based on hand sign

* Open main.py file.
*  Create a variable named `signText` to hold the text message.
 
  `signText = ""`

* If All fingers and thumb are up set `signText` to `Hello`.
 
  `if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:`
  
    `signText = "Hello!"`
    
* If four fingers are up set `signText` to `"How are you?"`.

  `if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:`
  
    `signText = "How are your?"`
    
* If thumb and small finger is up set `signText` to `"I was on a call."`
 
  `if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:`
  
    `signText = "I was on a call."`
    
* If first two fingers are up set `signText` to `"Be Quick!"`.
 
  `if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:`
  
    `signText = "Be Quick!"`
    
* If last three fingers are up set `signText` to `"Urgent work!"`.
 
  `if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:`
  
    `signText = "Urgent work!"`
    
* If all fingers and thumb are down set `signText` to `"Stop"`.
 
  `if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:`
  
    `signText = "Stop"`

cameraFeedImg = cv2.rectangle(
    cameraFeedImg, (bbox[0]-30, bbox[1]-60), (bbox[0]+bbox[2]+30, bbox[1]-20), (255, 255, 0), -1)
    
* Display the `signText` at `[bbox[0], bbox[1]-30]`.
 
`cameraFeedImg = cv2.putText(cameraFeedImg, signText, [
                            bbox[0], bbox[1]-30], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)`

* Show final image.
 
     `cv2.imshow("Image", cameraFeedImg)`
     
    `cv2.waitKey(1)`
* Save and run the code to check the output.


