

import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size =10 , border = 2)
qr.add_data("https://www.youtube.com/watch?v=OKuiyX5k6zg&t=3411s")
qr.make(fit = True)
img = qr.make_image(fill_color ="red",back_color= "black")
img.save("wscube_web.png")

