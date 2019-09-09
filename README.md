# OCR 

### Install Package into Environment
``` script
pip install pillow
pip install pytesseract
```

### Install Pytesseract
1. download .exe and install

2. inside pytesseract.py (if Windows)
```python
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
# tesseract_cmd = 'tesseract'
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
```
### Change language model
1. download .tessdata
> chinese-traditional: [chi_tra.traineddata](https://github.com/tesseract-ocr/tessdata/blob/master/chi_tra.traineddata])


2. set language mode inside code
```python
ans = pytesseract.image_to_string(img, lang='chi_tra')
```

## References
1. https://ithelp.ithome.com.tw/articles/10208992?sc=iThelpR
2. https://github.com/tesseract-ocr/tessdata
