import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
from six.moves import reduce
from collections import Counter 

def create_examples():
    number_array_examples = open('numArEx.txt', 'a')
    numbers_we_have = range(0,10)
    versions_we_have = range(1,10)

    for each_num in numbers_we_have:
        for each_ver in versions_we_have:
            #print(str(each_num)+'.'+str(each_ver))
            img_file_path = 'images/numbers/'+str(each_num)+'.'+str(each_ver)+".png"
            ei = Image.open(img_file_path)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            line_to_write = str(each_num)+'::'+eiar1+'\n'
            number_array_examples.write(line_to_write)
    

def threshold(image_array):
    balance_ar = []
    new_ar = image_array

    for each_row in image_array:
        for each_pix in each_row:
            avg_num = reduce(lambda x, y: int(x)+int(y), each_pix[:3])/3
            balance_ar.append(avg_num)
    balance = reduce(lambda x, y: int(x)+int(y), balance_ar)/len(balance_ar)

    for each_row in new_ar:
        for each_pix in each_row:
            if reduce(lambda x,y: int(x)+int(y), each_pix[:3]/len(each_pix[:3])) > balance:
                each_pix[0] = 255
                each_pix[1] = 255
                each_pix[2] = 255
                each_pix[3] = 255
            else:
                each_pix[0] = 0
                each_pix[1] = 0
                each_pix[2] = 0
                each_pix[3] = 255
    return new_ar
    
def what_num_is_this(filepath):
    matched_ar = []
    load_example = open('numArEx.txt','r').read()
    load_example = load_example.split('\n')

    i = Image.open(filepath)
    iar = np.array(i)
    iar1 = iar.tolist()

    in_question = str(iar1)

    for each_example in load_example:
        if len(each_example) > 3:
            split_ex = each_example.split('::')
            current_num = split_ex[0]
            current_ar = split_ex[1]

            each_pix_ex = current_ar.split('],')

            each_pix_in_question = in_question.split('],')

            x = 0
            while x < len(each_pix_ex):
                if each_pix_ex[x] == each_pix_in_question[x]:
                    matched_ar.append(int(current_num))

                x += 1

    print(matched_ar)
    x = Counter(matched_ar)
    print(x)

what_num_is_this('images/test.png')





                       
