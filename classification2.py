import pytesseract

import cv2

import os

import re
from numpy import array

from pdf2image import convert_from_path

import pymongo
from pymongo import MongoClient

#print(spell.correction("tezt"))

 

'''from autocorrect import spell

c = spell.speller("tezt")

print(c)'''

 

# pytesseract.pytesseract.tesseract_cmd = r'F:\Anaconda3\tesseract.exe'

 

#pages = convert_from_path(r'C:\Users\benob\Desktop\Makathon 2019 Q4\Invoice Maker.pdf', 500, grayscale=True, fmt='jpeg')

#for page in pages:

#   result = pytesseract.image_to_data(page)

#   print(result)

class classifier:
    def classifier_function(self, path):
# /path = '/home/soumyojit/Desktop/pdfs'
        #db setup
        client = MongoClient("mongodb://localhost:27017")

        db = client.get_database('test')
        # print(db)

        collection = db.Invoice

        d = {}
        if not os.path.exists(path+"/imgs"):
            os.mkdir(path+"/imgs")
           
        
        output_path = path+"/imgs/"

        filename = "image"
        counter = 0
        collection.drop()
        for file in os.listdir(path):

            if file.endswith(".pdf"):

                pages = convert_from_path(os.path.join(path, file), 500, grayscale=True, fmt='jpeg')
#change
                dictionary = dict()
                dictionary['type'] = 'unknown'
                dictionary['number'] = ''
                dictionary['invoice_number'] = ''
                dictionary['cost'] = ''

            

                

                for page in pages:
                    counter = counter + 1
                    #page.save(output_path+filename+str(counter)+".JPEG","JPEG")
                    imcv = array(page)
                    result = pytesseract.image_to_data(page, output_type = pytesseract.Output.DICT)

                    no_words = len(result['text'])

                    i = 0

                    while i < no_words:

                        try:

                            if result['text'][i].strip()=='':

                                for x,y in result.items():

                                    del result[x][i]

                            else: i += 1

                        except: break

                    no_words = len(result['text'])
                    if no_words < 15:
                        continue
                    
                    # print(result)

                    for i in range(no_words):

                        if(result['text'][i].strip() != ''):

                            if (re.findall(r"[a-zA-Z]+",result['text'][i]) != []):

                                word = re.findall(r"[a-zA-Z]+",result['text'][i])[0]

                                print(word)

                            

                                if word.lower() == 'invoice':

                                    dictionary['type'] = 'invoice'

                                    j = i+1
#change
                                    while dictionary['number'] == '' or dictionary['invoice_number'] == '':
                                        pattern = re.compile("no|number")
                                        try:
                                            if result['text'][j].lower() == 'invoice' and pattern.match(result['text'][j+1].lower()):
                                                j += 2
                                                while len(result['text'][j]) < 3: j += 1
                                                dictionary['invoice_number'] = result['text'][j]
                                                (x,y,w,h) = (result['left'][j],result['top'][j],result['width'][j],result['height'][j])
                                                imcv = cv2.rectangle(imcv,(x-7,y-7),(x+w+14,y+h+14),(0,255,0),8)
                                            elif result['text'][j].lower() == 'order' and pattern.match(result['text'][j+1].lower()):
                                                j += 2
                                                while len(result['text'][j]) < 3: j += 1
                                                dictionary['number'] = result['text'][j]
                                                (x,y,w,h) = (result['left'][j],result['top'][j],result['width'][j],result['height'][j])
                                                imcv = cv2.rectangle(imcv,(x-7,y-7),(x+w+14,y+h+14),(0,255,0),8)
                                            else: j += 1
                                        except: break

                                

                                elif word.lower() == 'purchase':

                                    j = i+1

                                    while dictionary['type'] == 'unknown':

                                        # print(result['text'][j])

                                        if result['text'][j].lower() == 'order':

                                            if ((result['block_num'][j] == result['block_num'][i] and

                                                result['par_num'][j] == result['par_num'][i] and

                                                result['line_num'][j] == result['line_num'][i] and

                                                int(result['word_num'][j]) == int(result['word_num'][i]) + 1) or

                                            

                                                (result['block_num'][j] == result['block_num'][i] and

                                                result['par_num'][j] == result['par_num'][i] and

                                                int(result['line_num'][j]) == int(result['line_num'][i]) + 1)):

                                            

                                                dictionary['type'] = 'PO'

                                            

                                                k = j

                                                pattern = re.compile("[no|number]")

                                                if pattern.match(result['text'][k].lower()): k += 1

                                            

                                                #while dictionary['number'] == '':

                                                #f len(re.findall('/d', result['text'][k])) == 0:

                                                # print(result['text'][k])

                                                dictionary['number'] = result['text'][k]
                                                (x,y,w,h) = (result['left'][k],result['top'][k],result['width'][k],result['height'][k])
                                                imcv = cv2.rectangle(imcv,(x-7,y-7),(x+w+14,y+h+14),(0,255,0),8)
                                            

                                        else: j += 1

                        

                                if dictionary['type'] != 'unknown': break

                            #spell.correction()

                    #change
                    for i in range(no_words-1, 0, -1):
                        pattern = re.compile('total')
                        if(len(pattern.findall(result['text'][i].lower())) > 0):
                            j = i+1
                            pattern = re.compile('\d+\.\d+')
                            try:
                                while (len(pattern.findall(result['text'][j].lower())) == 0):
                                
                                    j += 1
                            except:
                                break
                            dictionary['cost'] = result['text'][j]
                            (x,y,w,h) = (result['left'][j],result['top'][j],result['width'][j],result['height'][j])
                            imcv = cv2.rectangle(imcv,(x-7,y-7),(x+w+14,y+h+14),(0,255,0),8)
                            break    
                    cv2.imwrite(output_path+filename+str(counter)+".JPEG",imcv)

                    dictionary["_id"] = filename+str(counter)+".JPEG"
                    print(dictionary)   
                    collection.insert_one(dictionary)
                    d[filename+str(counter)+".JPEG"] = dictionary
                    print('-------------------------')

        # print(d)
        return d
                

                    

        

        #img = Image.open(r"C:\Users\benob\Desktop\Makathon 2019 Q4\invoice_exp.pdf")

        

        #pdfFile = Image(filename = r"C:\Users\benob\Desktop\Makathon 2019 Q4\invoice_exp.pdf", resolution = 300)

        #image = pdfFile.convert('jpeg')

        

        

        #img = Image.open(r"C:\Users\benob\Desktop\Makathon 2019 Q4\out.jpg")

        

        #img.show()

        

        

        

        #res = pytesseract.image_to_string(img)

        

#         #print(res)
# ob = classifier()
# ob.classifier_function('/home/soumyojit/Desktop/pdfs')