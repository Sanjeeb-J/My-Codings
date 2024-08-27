ans = input("File name: ").lower()

#.gif (image/gif)
if ".gif" in ans:
    print("image/gif")
#.jpeg (image/jpeg)
elif ".jpeg" in ans:
    print("image/jpeg")
#.jpg (image/jpeg)
elif ".jpg" in ans:
    print("image/jpeg")
#.png (image/png)
elif ".png" in ans:
    print("image/png")
#.pdf (application/pdf)
elif ".pdf" in ans:
    print("application/pdf")
#.txt (text/plain)
elif ".txt" in ans:
    print("text/plain")
#.zip (application/zip)
elif ".zip" in ans:
    print("application/zip")
#Nothing (application/octet-stream)
else:
    print("application/octet-stream")
