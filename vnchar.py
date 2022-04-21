vnchar = [
    'a', ['c', 'i', 'm', 'n', 'o', 'p', 't', 'u', 'y'      ],
    'b', ['a', 'e', 'i', 'o', 'u'                          ],
    'c', ['a', 'h', 'o', 'u'                               ],
    'd', ['a', 'e', 'i', 'o', 'u'                          ],
    'e', ['c', 'm', 'n', 'o', 'p', 't', 'u'                ],
    'f', [],
    'g', ['a', 'h', 'i', 'o', 'u'                          ],
    'h', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'i', ['a', 'c', 'e', 'm', 'n', 'p', 't', 'u'           ],
    'j', [],
    'k', ['h'                                              ],
    'l', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'm', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    'n', ['a', 'e', 'g', 'h', 'i', 'o', 'u'                ],
    'o', ['a', 'c', 'e', 'i', 'm', 'n', 'o', 'p', 't', 'u' ],
    'p', ['h'                                              ],
    'q', ['u'                                              ],
    'r', ['a', 'e', 'i', 'o', 'u'                          ],
    's', ['a', 'e', 'i', 'o', 'u', 'y'                     ],
    't', ['a', 'e', 'h', 'i', 'o', 'u', 'y'                ],
    'u', ['a', 'c', 'e', 'i', 'm', 'n', 'o', 'p', 't', 'y' ],
    'v', ['a', 'e', 'i', 'o', 'u'                          ],
    'w', [],
    'x', ['a', 'e', 'i', 'o', 'u'                          ],
    'y', ['e', 'n', 'u'                                    ],
    'z', [],
]

# text = "nananananananana"
def check(text):
    word = []
    for letter in text:
        word.append(letter)

    point = 0
    for i in range(0, len(text) - 1):
        if(word[i] in vnchar):
            id = vnchar.index(word[i])
            if(word[i + 1] in vnchar[id + 1]):
                point += 1
    return point

# print(check(text))