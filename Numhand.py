#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 20:
                    id20 = int(id)
                    cx20 = cx
                if id == 19:
                    id19 = int(id)
                    cx19 = cx
                if id == 16:
                    id16 = int(id)
                    cx16 = cx
                if id == 15:
                    id15 = int(id)
                    cx15 = cx
            if cx4 > cx3:
                Nfing = 4
                if cx20 < cx19:
                    Nfing = 3
                    if cx16 < cx15:
                        Nfing = 2
            else:
                Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    fps = "Copter"; #Frame rate per second
    cv2.putText(img, str(str(fps)), (400, 400), cv2.FONT_HERSHEY_PLAIN, 3,
                (200, 100, 200), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()