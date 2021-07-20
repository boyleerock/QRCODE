import qrcode

link = input("Enter the link or string context:")
img = qrcode.make(link)
img.save("andysportscenter_qrcode.jpg")