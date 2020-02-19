import os
import yagmail
import pandas as pd
import pyqrcode
# install pypng, xlrd in cmd prompt
z = yagmail.SMTP("yuddhavarna2020@gmail.com","csecse20")
df = pd.read_csv("testdata.csv")
#http://yuddhavarna.siteszilla.com/qrcode.php?id=56
text = """ <html><head><style>h1
{
font-family:cursive;
font-size:40px;
margin-top:0px;
}
</style>
</head>
<body>
<center><h1><span style='color:dodgerblue;'>Y</span><span style='color:forestgreen;'>u</span><span style='color:red;'>d</span><span style='color:dodgerblue;'>d</span><span style='color:orange;'>h</span><span style='color:forestgreen;'>a</span><span style='color:red;'>v</span><span style='color:dodgerblue;'>a</span><span style='color:red;'>r</span><span style='color:orange;'>n</span><span style='color:dodgerblue;'>a</span><span style='color:forestgreen'>2K20</span></h1></center><br>
</body>
</html>"""
try:
    for i in range(len(df)):
        id = df.iloc[i].values[1]
        receiver = df.iloc[i].values[4]
        name = df.iloc[i].values[2]
        msg = "<h3 style='font-size:19px;font-family:verdana;'> <span style='color:dodgerblue;font-size:22px;'>Hello {}</span>,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can find your respective QR code above or attached with this mail.<br><br> <span style='color:red;'>**It is mandatory to show this QR code to confirm your registration**</span><br><br> <span style='color:#3b5998;font-size:15px'>Thanks & Regards,<br>Yuddhavarna2020 - CSE, MKCE.</span></h3>".format(name)
        p = pyqrcode.create(r"http://yuddhavarna.siteszilla.com/qrcode.php?id={}".format((id)*1932))
        p.png("{}.png".format(id), scale=6)
        z.send(
        to = receiver,
        subject = "QR Code-Yuddhavarna2020-{}".format(name),
        attachments="{}.png".format(id),
        contents=[text,"<h3 style='color:red;font-size:15px'>** Mandatory QR code **</h3>",yagmail.inline("{}.png".format(id)),msg]

        )
        os.remove("{}.png".format(id))
        print("Mail sent : {}".format(receiver))
except:
    print("Wrong")