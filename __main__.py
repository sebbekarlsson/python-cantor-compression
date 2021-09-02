import math

cantor = lambda k1, k2: int(((k1 + k2) * (k1 + k2 + 1)) / 2 + k2)


def decant(z):
  w = math.floor((math.sqrt(z * 8 + 1) - 1) / 2)
  a = int(z - (w * (w + 1)) / 2)
  b = int(w - a)

  return [b, a]


# "abcd"
# [["a", "b"], ["c", "d"]]
def chunk(text):
    chunks = []

    # hur manga chunks kommer vi vilja ha?
    nr = len(text) / 2
    # rundar av uppat
    rounded = math.ceil(nr)


    for i, c in enumerate(range(rounded)):

        k = i*2
        # k = nuvarande index i loopen, vi multiplicerar med 2 for att vi plockar
        # tva varden varje gang i loopen.
        v1 = k  # indexet pa forsta delen i paret
        v2 = min(len(text)-1, k+1)  # v2 ar indexet pa andra delen i paret
        pair = [text[v1], text[v2]]
        chunks.append(pair)

    if len(chunks) > nr:
        chunks[-1][1] = ''

    return chunks


# ger oss ascii numret av en bokstav, om bokstaven inte ar tom, annars 0
chrnum = lambda c: ord(c) if c else 0


def compress(text):
    # 1. Vi delar upp texten i chunks, dvs [["a", "b"], ["c", "d"]] ... osv
    chunks = chunk(text)

    # 2. Vi gor om bokstavs-paren till nummer
    # # [[97, 98], [99, 100]] ... osv
    numbered = map(lambda pair: [chrnum(pair[0]), chrnum(pair[1])], chunks)


    # 3. Vi kor cantor pa alla paren, vilket gor om paren till
    # enskilda tal istallet.
    # Dvs, ett par ["a", "b"] blir ett tal istallet.
    compressed_list = map(lambda pair: cantor(pair[0], pair[1]), numbered)

    # 4. Vi gor om alla tal i compressed_list till bokstaver / bytes.
    bytes_list = map(lambda v: chr(v), compressed_list)

    # 5. Gor vi om listan av bokstaver till en strang, genom att
    # sy ihop dom med .join
    return ''.join(bytes_list)


def uncompress(text):
    # 1. Skapa en lista med alla bokstaver i texten, (en array alltsa).
    bytes_list = [c for c in text]

    # 2. Gor om alla bokstaver till nummer, med ord() funktionen.
    numbered = map(lambda v: ord(v), bytes_list)

    # 3. Kor `decant` metoden pa alla nummer, vilket resulterar i en lista
    # med par av nummer. Dvs ex. [[97, 98], [99, 100]]
    decanted = map(decant, numbered)

    # 4. Vi gor om alla par av nummer till bokstaver
    # genom att anvanda chr metoden pa varje bokstav.
    # Varje par av bokstav limmas aven ihop med .join.
    # Sa att ['a', 'b'] blir "ab"
    chars = map(lambda pair: ''.join([chr(v) for v in pair]), decanted)
    # nu har vi en lista som ser ut sa har:
    # ["ab", "cd"] ... osv

    # 5. Vi limmar ihop listan som skapades ovan sa att
    # ["ab", "cd"] blir "abcd"
    return ''.join(chars)


a = compress("hello world")
print('after compression: length ({})'.format(len(a)))
print(a)

b = uncompress(a)
print('before compression: length ({})'.format(len(b)))
print(b)
