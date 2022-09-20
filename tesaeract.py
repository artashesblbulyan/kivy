import json
import os
from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
from pytesseract.pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to stringpytesseract
d = 0
c = []
f = {}

for filename in os.listdir('img_1'):
    d += 1
    a = pytesseract.image_to_string(Image.open('img_1/'+filename), lang='eng', config=tessdata_dir_config, nice=0)
    df = pytesseract.image_to_data(Image.open('img_1/'+filename), output_type=Output.DICT,lang='eng', config=tessdata_dir_config, nice=0)
    df_text = pytesseract.image_to_data(Image.open('img_1/'+filename), lang='eng', config=tessdata_dir_config, nice=0)
    # df = pytesseract.run_and_get_output(Image.open('img_1/'+filename),lang='eng', config = tessdata_dir_config)
    # print(a)

    a.encode(encoding='UTF-8', errors='strict')
    # df.encode(encoding='UTF-8', errors='strict')
    s = str(d) + filename + a
    # print(s)
    # print(len(df))
    # print(df)

    # with open('json_tex_file.txt', 'w') as text_a:
    #     # text_a.write(df)
    #     text_a.write(df)

    # for i in df.splitlines():
    #     i = i.split(' ')
    #     print(i)

    # with open("json_tex_file.txt", "r") as text_js_file:
    #     # data = text_js_file.read()
    #     for i in text_js_file:
    #         print(i)

    # for h in a.splitlines():
    #     h = h.split(' ')
    #     if h[0] == "K":
    #         f['file'].append([{'filename': filename, 'x': h[1], 'y':h[2], 'h': h[3]}])

    # with open("name_json.json", 'w') as da:
    #     a = json.loads(data)
    #     jstr = json.dump(a, da, indent=4)
    # if df != "":
    #     df = [i.split("\t") for i in df.split("\n")]
    #
    #
    #
    # print(df)
    with open('name.json', "w") as text_js_file:
        a = a.replace('\n', ' ')

        a.splitlines()
        a = a.split(' ')
        # f={filename:[c]}
        for list in a:
            if list == "" or (list.isalpha() == True and list != "KS"):
                a.remove(list)
        # for k in a.splitlines():
        #     a = k.split(' ')
        # f = {filename: [c]}
        # for h in df.splitlines():
        #     h = h.split(' ')
        #     print(h)
        #     if h[0] == "K":
        #         # print(d,filename, h[0], h[1],h)
        #         dfg =[]
        #         v = 0
        # for element in a:
        #     # v +=1
        #     # print(v,a.index(element),element)
        #     dfg = []
        #     if 'KS' in element and len(element) >2:
        #         dfg.append(element)
        #     if element == "KS":
        #         # print(v,a.index(element),a.index(element)+1,a[a.index(element)]+a[a.index(element)+1])
        #         qwe = a[a.index(element)]+a[a.index(element)+1]
        #         # print(qwe)
        #         a.remove(a[a.index(element)])
        #         dfg.append(qwe)
        #         # a.remove(a[a.index(element)])
        #
        #     else:
        #         dfg.append(element)

        los = {}
        lina = len(df['level'])
        for i in range(lina):
            # print(lina)
            # print(i)
            # print(df['level'])

            if df['level'][i] == 5:
                los['level']=df['level'][i]
                los['text']=df['text'][i]
                los['left']=df['left'][i]
                los['top']=df['top'][i]
                los['width']=df['width'][i]
                los['height']=df['height'][i]
        f[filename]=los
                # # print(df['level'][i],df['text'][i],df['left'][i],df['top'][i],df['width'][i],df['height'][i])
                # a = [df['level'][i],df['text'][i],df['left'][i],df['top'][i],df['width'][i],df['height'][i]]
                # print(a)

    # for j in los:
    #     df['level'].pop(los)
        # df['text'].pop(j)
        # df['left'].pop(j)
        # df['top'].pop(j)
        # df['width'].pop(j)
        # df['height'].pop(j)

        print(los)
        json.dump(f, text_js_file, indent=2)

        #     print(i)
        #     print(df['level'])
        #     for ksd in df['level']:
        #         if ksd == 5:
        #             print(i)
        #             asdf = (df['level'][df['level'].index(ksd)],)
        #             print(asdf)
        #             c.append({"filename": filename,'a': df})
        #             # print(dfg)
        #             # print(f)



                # data = text_js_file.write(filename+" "+x+" "+y+'\n')
    # with open('name.json', 'r') as js:
    #     print(json.load(js))

    # for j in a.splitlines():
    #     print(filename,j)
    #     j = j.split(' ')
        # print(j)
        # if 'KS' in j[0]:
        #     if len(j[0]) < 3:
        #         try:
        #             # os.rename('img_1/' + filename, 'img_1/' + j[0]+ j[1] + '.JPG')
        #             print( j[0]+ j[1])
        #         except:
        #             # print(b[0:8])
        #             continue
        #     else:
        #         try:
        #             # os.rename('img_1/' + filename, 'img_1/' + j[0] + '.JPG')
        #             print( j[0])
        #         except:
        #             # print(b[0:8])
        #             continue
        #     print(filename,j)



    # if a[0:2] == "KS":
    #     a.replace("\n", '')
    #     b = a.replace(" ", '')
        # if b[7] == "\n" or b[7] == "K" or b[7] == " ":
        #     b.replace(b[7], '')


    #     continue
    # else:

        #     print(a[0:8])

# # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# # NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))
#
# # List of available languages
# print(pytesseract.get_languages(config=''))
#
# # French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
#
# # Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))
#
# # Timeout/terminate the tesseract job after a period of time
# try:
#     print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
#     print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
#     # Tesseract processing is terminated
#     pass
#
# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))
#
# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))
#
# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))
#
# # Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default
#
# # Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')
#
# # Get ALTO XML output
# xml = pytesseract.image_to_alto_xml('test.png')