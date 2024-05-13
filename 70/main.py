import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

while True:

    try:
        success, cameraFeedImg = cap.read()
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        hands, cameraFeedImg = detector.findHands(
            cameraFeedImg, flipType=False, draw=True)

        if hands:
            hand1 = hands[0]
            lmList = hand1["lmList"]
            bbox = hand1["bbox"]
            fingers = detector.fingersUp(hand1)
            if len(lmList) > 0:
                # Create a variable named 'signText' to hold the text message
                signText = ""
                # If All fingers and thumb are up set 'signText' to 'Hello'
                if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                    signText = "Hey!"
                # If four fingers are up set 'signText' to "How are your?"
                if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                    signText = "How are you doing?"
                # If thumb and small finger is up set 'signText' to "I was on a call."
                if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
                    signText = "Sorry, I was on a call."
                # If first two fingers are up set 'signText' to "Be Quick!"
                if fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    signText = "Do it faster!"
                # If last three fingers are up set 'signText' to "Urgent work!"
                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                    signText = "This is very urgent!"
                # If all fingers and thumb are down set 'signText' to "Stop"
                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    signText = "Stop now."

                cameraFeedImg = cv2.rectangle(
                cameraFeedImg, (bbox[0]-30, bbox[1]-60), (bbox[0]+bbox[2]+30, bbox[1]-20), (255, 255, 0), -1)
                # Display the signText at [bbox[0], bbox[1]-30]
                cameraFeedImg = cv2.putText(cameraFeedImg, signText, [
                bbox[0], bbox[1]-30], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    except Exception as e:
        print(e)

    # Show final image
    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)
