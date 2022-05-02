# Bảng ký tự Tiếng Việt và từ theo sau hợp lệ
vnchar = [
    'a', ['c', 'i', 'm', 'n', 'o', 'p', 't', 'u', 'y'      ],
    'b', ['a', 'e', 'i', 'o', 'u'                          ],
    'c', ['a', 'h', 'o', 'u'                               ],
    'd', ['a', 'e', 'i', 'o', 'u'                          ],
    'e', ['c', 'm', 'n', 'o', 'p', 't', 'u'                ],
    'f', [                                                 ],
    'g', ['a', 'h', 'i', 'o', 'u'                          ],
    'h', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'i', ['a', 'c', 'e', 'm', 'n', 'p', 't', 'u'           ],
    'j', [                                                 ],
    'k', ['h', 'e'                                         ],
    'l', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'm', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'n', ['a', 'e', 'g', 'h', 'i', 'o', 'u'                ],
    'o', ['a', 'c', 'e', 'i', 'm', 'n', 'o', 'p', 't', 'u' ],
    'p', ['h'                                              ],
    'q', ['u'                                              ],
    'r', ['a', 'e', 'i', 'o', 'u'                          ],
    's', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    't', ['a', 'e', 'h', 'i', 'o', 'r', 'u', 'y'           ],
    'u', ['a', 'c', 'e', 'i', 'm', 'n', 'o', 'p', 't', 'y' ],
    'v', ['a', 'e', 'i', 'o', 'u'                          ],
    'w', [                                                 ],
    'x', ['a', 'e', 'i', 'o', 'u'                          ],
    'y', ['e', 'n', 'u'                                    ],
    'z', [                                                 ],
]

# Bảng phụ âm đầu
consonant = [
    # Đơn
    [   'b', 'c', 'd', 'g', 'h',
        'k', 'l', 'm', 'n', 'r',
        's', 't', 'v', 'x'              ],
    # Ghép đôi
    [   'ch', 'gh', 'gi', 'kh', 'ng',
        'nh', 'ph', 'qu', 'th', 'tr'    ],
    # Ghép ba
    [   'ngh'                           ]
]

# Bảng vần
syllable = [
    [   'a', 'e', 'i', 'o', 'u'             ],
    [   
        'ac', 'ai', 'am', 'an', 'ao',
        'ap', 'at', 'au', 'ay', 'em',
        'en', 'eo', 'ep', 'et', 'eu',
        'ia', 'im', 'in', 'ip', 'it',
        'iu', 'oa', 'oc', 'oe', 'oi',
        'om', 'on', 'op', 'ot', 'ua',
        'uc', 'ue', 'ui', 'um', 'un',
        'uo', 'up', 'ut', 'uu', 'uy',       ],
    [   
        'ach', 'ang', 'anh', 'eng', 'ech',
        'enh', 'ich', 'inh', 'ong', 'ung',
        'iec', 'oai', 'iem', 'ien', 'iep',
        'iet', 'ieu', 'oan', 'oat', 'oay',
        'uan', 'uat', 'uoc', 'uoi', 'uom',
        'oun', 'uot', 'uya', 'uyt', 'uop',
        'uou', 'yen', 'yem', 'yeu'          ],
    [   
        'oach', 'ieng', 'oang', 'oanh', 
        'oung', 'uych', 'uynh', 'uyen',
        'uyet', 'oong'                      ],
]

def getCons(word):  #Lấy phụ âm đầu
    cons = ''
    for letter in word:
        if(letter in consonant[0]):
            cons += letter
        else: 
            break
    return cons

def getSyl(word): #Lấy vần
    syl = ''
    isAdded = False
    isSyllable = False
    for letter in word:
        isAdded = False
        if(letter in syllable[0]):
            syl += letter
            isAdded = True
            isSyllable = True
        elif(isSyllable == True and isAdded == False):
            syl += letter
    return syl

def checkLetter(text): #Check ký tự
    letters = []
    for letter in text:
        letters.append(letter)

    point = 0
    for i in range(0, len(text) - 1):
        if(letters[i] in vnchar):
            id = vnchar.index(letters[i])
            if(letters[i + 1] in vnchar[id + 1]):
                point += 1
    return point

def checkWord(word):    #Check từ
    point = 0
    cons = getCons(word) #Lấy phụ âm đầu
    syl = getSyl(word)   #Lấy vần

    if(len(cons) < 4 and len(cons) > 0):
        if(cons in consonant[len(cons) - 1]):
            point += 1

    if(len(syl) < 5 and len(syl) > 0):
        if(syl in syllable[len(syl) - 1]):
            point += 1
    return point

def checkSentence(sentence):    #Check câu
    point = 0
    point += checkLetter(sentence) #Check ký tự

    words = sentence.split(' ')
    for word in words:
        point += checkWord(word) #Check từ
    return point
