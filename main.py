import cv2
img = cv2.imread("solar-system.jpg")



cv2.putText(img,
            "sun",
            (20,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),
            )


cv2.putText(img,
            "mercury",
            (90,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )


cv2.putText(img,
            "venus",
            (190,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "Earth",
            (280,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "MOON",
            (340,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "JUPITER",
            (490,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "MARS",
            (390,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "saturn",
            (790,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "uranius",
            (960,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.putText(img,
            "neptune",
            (1100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,555,55),

            )
cv2.imshow("output",img)
cv2.waitKey(0)