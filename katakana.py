from microbit import *
class Katakana:
    kana = [
        0x1f09c84,
        0x113284,
        0x4fc426,
        0xf909f,
        0x2f9952,
        0x4f94a5,
        0x8f93e2,
        0xf88444,
        0x87c844,
        0xf843f,
        0xafa844,
        0x90a44c,
        0x1f11151,
        0x8fa50f,
        0x14a44c,
        0xf4dc44,
        0x713c44,
        0xad42e,
        0xe27c88,
        0x843928,
        0x2f8888,
        0x703e0,
        0x1f0a8d9,
        0x4f89d5,
        0x10889c,
        0x52a20,
        0x10fc20f,
        0xf844c,
        0x45260,
        0x4f92a4,
        0xf88c9,
        0xc0300c,
        0x444bc1,
        0x151151,
        0x4e7087,
        0x8fa508,
        0x7085f,
        0x1f0fc3f,
        0xe07c22,
        0x118c444,
        0xa56c4,
        0x1084b90,
        0x1f8c7e0,
        0x1f8c444,
        0x1f0fc26,
        0xc844c
    ]
    data = [
        [0, 0, 0x1000000, 24],
        [1, 0, 0x800000, 23],
        [2, 0, 0x400000, 22],
        [3, 0, 0x200000, 21],
        [4, 0, 0x100000, 20],
        [0, 1, 0x80000, 19],
        [1, 1, 0x40000, 18],
        [2, 1, 0x20000, 17],
        [3, 1, 0x10000, 16],
        [4, 1, 0x8000, 15],
        [0, 2, 0x4000, 14],
        [1, 2, 0x2000, 13],
        [2, 2, 0x1000, 12],
        [3, 2, 0x800, 11],
        [4, 2, 0x400, 10],
        [0, 3, 0x200, 9],
        [1, 3, 0x100, 8],
        [2, 3, 0x80, 7],
        [3, 3, 0x40, 6],
        [4, 3, 0x20, 5],
        [0, 4, 0x10, 4],
        [1, 4, 0x8, 3],
        [2, 4, 0x4, 2],
        [3, 4, 0x2, 1],
        [4, 4, 0x1, 0]
    ]

    img = Image()

    def __init__(self):
        pass

    def getNum(self, c):
        n = {
            "a": 0,
            "i": 1,
            "u": 2,
            "e": 3,
            "o": 4,
            "ka": 5,
            "ki": 6,
            "ku": 7,
            "ke": 8,
            "ko": 9,
            "sa": 10,
            "si": 11,
            "su": 12,
            "se": 13,
            "so": 14,
            "ta": 15,
            "ti": 16,
            "tu": 17,
            "te": 18,
            "to": 19,
            "na": 20,
            "ni": 21,
            "nu": 22,
            "ne": 23,
            "no": 24,
            "ha": 25,
            "hi": 26,
            "hu": 27,
            "he": 28,
            "ho": 29,
            "ma": 30,
            "mi": 31,
            "mu": 32,
            "me": 33,
            "mo": 34,
            "ya": 35,
            "yu": 36,
            "yo": 37,
            "ra": 38,
            "ri": 39,
            "ru": 40,
            "re": 41,
            "ro": 42,
            "wa": 43,
            "wo": 44,
            "nn": 45,
        }
        return n[c]

    def display_kana(self, s):
        for c in s.split(" "):
            n = self.getNum(c)
            for d in self.data:
                self.img.set_pixel(
                    d[0], 
                    d[1],
                    (((self.kana[n] & d[2]) >> d[3]) * 8))
            display.show(self.img)
            sleep(800)