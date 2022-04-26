import asciishift
import vietnameseaccent as vn
import vnchar
import random

sentence = "Anha"
sentence = vn.preprocess(sentence)          # Tiền xử lí
_sentence = vn.remove_vn_accent(sentence)   # Bỏ dấu câu

ekey = random.randrange(1, 95) # Cho random một key bất kì từ 1 đến 94 để thực hiện Ascii shift cipher
# print ("Key " + str(ekey))
# ekey = 94
_sentence = asciishift.encode(ekey, _sentence) 
# print (_sentence)

# Dò kết quả bằng cách duyệt từ key = 1 (Vét cạn)
results = asciishift.decode(_sentence)

print("Results:")
index = 0
length = len(_sentence)
for result in results:
    index += 1
    point = vnchar.checkSentence(result.lower()) # Chấm điểm dựa trên nhóm ký tự phổ biến của Tiếng Việt
    if(point > length/4): # Lựa chọn mức độ điểm tương đối, nếu điểm càng cao thì số đề xuất sẽ ít
        print(str(index) + "-> " + result + " ->" + str(point) + "p") # In kết quả

pos = input('Vị trí đề xuất kết quả: ') # Chọn kết quả đã decrypt để đề xuất sang Tiếng Việt

print()
try:    
    words = results[int(pos) - 1].split()
    k = 3
    vn_results = vn.beam_search(words, k)

    print('Text: ' + results[ int(pos) - 1])
    print('Proposals (Các đề xuất):')
    for i in range(0, k):
        print('Output['+ str(i) + ']:', ' '.join(vn_results[i][0]))
except:
    print()