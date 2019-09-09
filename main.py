from PIL import Image
import pytesseract

img = Image.open('book_001.jpg')
img = img.convert('RGB')
ans = pytesseract.image_to_string(img, lang='chi_tra')
print(ans)
