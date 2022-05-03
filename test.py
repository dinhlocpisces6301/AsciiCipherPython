import asciishift
import vietnameseaccent as vn
import vnchar
import random

sentence = "Xin Chao Cac Ban".lower()
_sentence = vn.preprocess(sentence)          # Tiền xử lí
_sentence = vn.remove_vn_accent(sentence)   # Bỏ dấu câu

ekey = random.randrange(1, 256) # Cho random một key bất kì từ 1 đến 255 để thực hiện Ascii shift cipher
_sentence = asciishift.encode(ekey, _sentence) 

# Dò kết quả bằng cách duyệt từ key = 1 (Vét cạn)
results = asciishift.decode(_sentence)

print("Results:")

for result in results:
    result[1] = result[1].encode('utf-8').replace(b'\x00', b'\xe2\x96\xa1')
    result[1] = result[1].decode()
    if(result[2] > 0): # Lựa chọn mức độ điểm tương đối, nếu điểm càng cao thì số đề xuất sẽ ít
        print(str(result[0]) + '-> ' + result[1] + ' ->' + str(result[2]) + 'p')

# Chọn kết quả đã decrypt để đề xuất sang Tiếng Việt
pos = input('Vị trí đề xuất kết quả: ') 
print()
try:    
    tmp = results[int(pos) - 1].lower()
    words = tmp[1].split()
    k = 3
    vn_results = vn.beam_search(words, k)

    print('Text: ' + tmp[1])
    print('Proposals (Các đề xuất):')
    for i in range(k):
        print('Output['+ str(i) + ']:', ' '.join(vn_results[i][0]))
except:
    print('.....')