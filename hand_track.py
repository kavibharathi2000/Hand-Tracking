import cv2
import mediapipe as mp 


vedio = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

count =0 

while True:
    condition , frame = vedio.read()
    rgb_img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_img)
    print(results.multi_hand_landmarks)
    count +=1
    cv2.putText(frame,str(count),(10,70), cv2.FONT_HERSHEY_COMPLEX,3, (255,255,255), 3)


    if results.multi_hand_landmarks:
        print("The Frame: ",count)
        for handlms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame, handlms,mphands.HAND_CONNECTIONS)
            for id,lm  in enumerate(handlms.landmark):
                h,w,c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy )

                if id==0:
                    cv2.circle(frame, (cx,cy),15, (255,0,255), cv2.FILLED)




    cv2.imshow("Output", frame)



    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
vedio.release()
