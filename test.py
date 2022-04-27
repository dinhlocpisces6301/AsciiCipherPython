import asciishift
import vietnameseaccent as vn
import vnchar
import random

sentence = "Xin Chao Cac Ban"
sentence = vn.preprocess(sentence)          # Tiền xử lí
_sentence = vn.remove_vn_accent(sentence)   # Bỏ dấu câu

ekey = random.randrange(1, 256) # Cho random một key bất kì từ 1 đến 255 để thực hiện Ascii shift cipher
_sentence = asciishift.encode(ekey, _sentence) 

# Dò kết quả bằng cách duyệt từ key = 1 (Vét cạn)
results = asciishift.decode(_sentence)
non_AsciiResults = []
for i in range(len(results)):
    non_AsciiResults.append(str(results[i]).encode('utf-8'))

print("Results:")
index = 0
length = len(_sentence)
for i in range(len(results)):
    point = vnchar.checkSentence(results[i].lower()) # Chấm điểm dựa trên nhóm ký tự phổ biến của Tiếng Việt
    if(point > 0): # Lựa chọn mức độ điểm tương đối, nếu điểm càng cao thì số đề xuất sẽ ít
        print(str(i + 1) + '-> ' + non_AsciiResults[i].decode() + ' ->' + str(point) + 'p')

# Chọn kết quả đã decrypt để đề xuất sang Tiếng Việt
pos = input('Vị trí đề xuất kết quả: ') 
print()
try:    
    words = results[int(pos) - 1].split()
    k = 3
    vn_results = vn.beam_search(words, k)

    print('Text: ' + results[ int(pos) - 1])
    print('Proposals (Các đề xuất):')
    for i in range(k):
        print('Output['+ str(i) + ']:', ' '.join(vn_results[i][0]))
except:
    print()