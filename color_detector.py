import cv2

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter("output/color_detector.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while  True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rectangle = cv2.rectangle(frame, (290, 200), (370, 275), 0, 1)

    for i in range(240, 260):
        for j in range(315, 345) :
            if frame[i, j] < 130:
                cv2.putText(frame, "black", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0)
            elif 140 < frame[i, j] < 160:
                cv2.putText(frame, "gray", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0) 
            elif 170 < frame[i, j] <255:
                cv2.putText(frame, "white", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0)      
            
    
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

writer.release() 

       


