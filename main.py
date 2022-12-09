import qrcode
from PIL import Image

logo = Image.open('./logo.jpg')
logo.thumbnail((206, 206))

qr_white = Image.open('./qr_white.jpg')
qr_bg = Image.open('./qr_bg.png')

urls = ["https://www.naver.com/", "https://blog.false.kr/"]

i = 0

for url in urls:
    i+=1
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,version=7,box_size=12,border=1)
    qr.add_data(url)
    qr.make()
    qr_img = qr.make_image().convert('RGB')

    # BG 적정 사이즈로 조절
    qr_img = qr_img.resize((420,420))

    # QR 중앙 공백 영역 생성  || 206 x 62
    pos = ((qr_img.size[0] - qr_white.size[0]) // 2, (qr_img.size[1] - qr_white.size[1]) // 2)
    qr_img.paste(qr_white, pos)

    # QR 중앙 공백 내 로고 삽입
    pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
    qr_img.paste(logo, pos)

    # 작성된 QR 백그라운드에 삽입
    pos = ((qr_bg.size[0] - qr_img.size[0]) // 2, (qr_bg.size[1] - qr_img.size[1]) // 2)
    qr_bg.paste(qr_img, pos)

    qr_bg.save('/QR/'+i+'.png')
