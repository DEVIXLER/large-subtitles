# Scar32

import math

font_data = {'!': '􏽀􏿻', '"': '􏿼􏿳􏿯', '#': '򐟛𑽯􏶾􏾿', '$': '󆾳󫠃􏦾􏾿', '%': '򭟽񷼷􏗏󯿽', '&': '󋞉󋶫򏯾󯿺', '\\': '􉿼򏼿􇿾', "'": '􏿼􏿻',
             '(': '򌼇􎿺􏿯', ')': '򌯾􏰞􏿯', '*': '􎿺􏿫􏿯', '+': '󿿟󏰟􏷿􏾿', ',': '󏻿􍿿', '-': '󿿟􏽿􏿯', '.': '􏽿􏿻', '/': '󷼿􉿏􇿿',
             '0': '󏞁􍷻􏠞􏾿', '1': '򐝽􏷿􏿯', '2': '򿜹󽶻􏞞􏾿', '3': '󋞾󹷋􏣮􏾿', '4': '􉿷𑿗􏽾􏾿', '5': '󋞰󽷛􏣮􏾿', '6': '󅾇񍶷􇿿', '7': '􏟾󵰻􏿏󯿿',
             '8': '󋞉󽷛􏢞􏾿', '9': '󫝹󓽛􇿿', ':': '􏽷􏿻', ';': '󋻿􍿿', '<': '󿿟񯺿󏝿󯿻', '=': '󧾯񯺿􏫿􏾿', '>': '󿿟񯺿󏝿󯿻', '?': '􏟹󽴻􏾟􏾿',
             '@': '󮿃󅶛󿑮􏃺􏻿', 'A': '󹼏򷽳􏃿􏾿', 'B': '󋜀󽷛􏢞􏾿', 'D': '󏜀򋷻􏰿􏾿', 'E': '󋜀󽷛􏟮􏾿', 'F': '􋜀󽿛􏿯􏾿', 'G': '󮿃󭷻񿛮󯿼', 'H': '􋼀󿿟􏀏􏾿',
             'I': '򐝾􏷻􏿯', 'J': '󏾟􏷿􏠎􏾿', 'K': '􋼀󋾯􏏯􏾿', 'L': '󏼀􏷿􏟾􏾿', 'M': '􎜀򯿏󷼿􌀿􏻿', 'N': '􎜀򯿏𗏿󯿸', 'C': '󮿃􍷻󿟮󯿽',
             'O': '󮿃􍷻󿟮􏃽􏻿', 'Q': '󮿃􍷻󿗮􍃽􏻿', 'P': '􋜀󽿛􏾟􏾿', 'R': '􋜀󝿛􏆟􏾿', 'S': '󋞹󽷛􏣞􏾿', 'T': '􏟾􍰃􏿯􏾿', 'U': '󯿀􏷿𗯾󯿾',
             'V': '󳿸򟳿􏾏􏾿', 'W': '򯼀󷼿􏳿􌀹􏻿', 'X': '󽼼󇾟􏏏􏾿', 'Y': '􍿼􇰟􏿏􏾿', 'Z': '򿜾󽶻󷞮󯿻', '[': '􏀀􎿹􏿯', ']': '􏏾􎀁􏿯', '^': '􎿻􋿻􏾿􏾿',
             '`': '􎿾􍿿', 'a': '򻾿򿵟􏃾􏾿', 'b': '󇼀󿷟􏣾􏾿', 'c': '󋾏󿷟􏫾􏾿', 'd': '󋾏󯷟􏀎􏾿', 'e': '򻾏򿵟􏳾􏾿', 'f': '򐿻􏿫􏿯', 'g': '󋶏󮷝􌁶􏾿',
             'h': '􇼀󿿟􏃿􏾿', 'i': '􏼂􏿻', 'j': '𑏿􍿾', 'k': '󿼀󿺿􇿾', 'l': '􏼀􏿻', 'm': '􋼇𯿟󏽾􌏿􏻿', 'n': '􇼇󿿟􏃿􏾿', 'o': '󋾏󿷟􏣾􏾿',
             'p': '󇠇󿷟􏣾􏾿', 'q': '󋾏󯷟􈁾􏾿', 'r': '􇼇󿿟􏻿􏾿', 's': '򻽯􏻟􏿯', 't': '󐟻􏷯􏿯', 'u': '󏾇􏷿􏁾􏾿', 'v': '󟿧񏷿􏹿􏾿', 'w': '󏾇󟹿􏧿􎇻􏻿',
             'x': '󧽷񯽿􏝿􏾿', 'y': '󏮇􏯾􏡾􏾿', 'z': '򫽷󟵟􏝾􏾿', '{': '𠿟􎿺􏿿􏾿', '|': '􏠀􏿻', '}': '𠯾􏽾􏿯', '~': '󿾿򏽿􏯿󯿾', '_': '󏽿􏷿􏟾􏾻',
             ' ': '􏿿􏿿􇿿'}
f = open("demofile3.txt", "w")
fontsizey = 11
wrapping = 0
displayWidth = 50 
subtitle = 1
timestamp = 0
timeUnits = [1000, 60, 60]


def timestampms(ms):
    time = ms
    ram = []
    for i in timeUnits:
        ram.append('0' * (len(str(i - 1)) - len(str(int(time % i)))) + str(
            int(time % i)))  # holy shit SRT just why... also this bullshit 0.0 ruined my shit
        time = (time - time % i) / i
    ram.append(str(int(time % i)) + '0' * (2 - len(str(int(time)))))
    output = ',' + ram[0]
    for i in range(1, 3):
        output = ':' + ram[i] + output
    output = ram[-1] + output
    return output


def addsubs(text, addtime):
    global subtitle, timestamp
    f.write(str(subtitle) + '\n')
    timeadd = addtime
    f.write(timestampms(timestamp) + ' --> ' + timestampms(timestamp + addtime * 1000))
    f.write('\n')
    for i in text:
        f.write(i + '\n')
    f.write('\n')
    subtitle += 1
    timestamp += addtime * 1000


def setTimestamp(t):
    global timestamp
    timestamp = timestampms(t * 1000)


def bits2character(bits):
    character = 1114111
    for i in range(20):
        character -= int(bits[i]) * 2 ** i
    return chr(character)


characters = '01'


def character2bits(character):
    n = 1114111 - ord(character)
    out = ''
    for l in range(20):
        char = int(n) % 2
        out += characters[char]
        n = (n - char) / 2
    return out


def bits2string(bits):
    out = ''
    bits = bits + '1' + '0' * (20 - len(bits) % 20 - 1)  # my format puts a 1 at the end of the bits followed by zeros
    for p in range(int((len(bits) + 1) / 20)):
        chunk = ''
        for s in range(20):
            chunk += bits[p * 20 + s]
        out += bits2character(chunk)
    return out


def string2bits(string):
    data = ''
    for i in string:
        data += character2bits(i)
    while data[-1] == '0':
        data = data[: -1]
    data = data[: -1]
    return data


spacelength = len(string2bits(font_data[' '])) / fontsizey


def text2pixels(s):
    if wrapping > 8:
        wordlength = [0, ]  # wordwrapping first
        words = ['', ]
        for c in s:
            if not font_data.__contains__(c):  # if the character is not in the font then forget it
                print(c)
            elif c != ' ':  # is it is not a space then it is another character in the "word"
                wordlength[-1] += int(len(string2bits(font_data[c])) / 11)
                words[-1] += c
            else:  # if it is a space then we are at the end of the word so reset everything
                wordlength.append(0)
                words.append('')
        wordsPerLines = [0, ]
        lines = ['', ]
        for w in range(len(words)):
            if not wordsPerLines[-1] + wordlength[
                w] + spacelength > wrapping:  # if adding the word with a space doesn't makes it go over
                wordsPerLines[-1] += wordlength[w] + spacelength  # keep count of the length of the line with a space
                lines[-1] += words[w] + ' '  # and add on the word
            elif not wordsPerLines[-1] + wordlength[
                w] > wrapping:  # if it's too big check if it works without the space
                wordsPerLines[-1] += wordlength[w]  # counts without the space
                lines[-1] += words[w]  # add word without the space
                wordsPerLines.append(0)  # reset everything
                lines.append('')
            else:  # if it's still too big add a new line with the word on the end
                wordsPerLines.append(wordlength[w] + spacelength)
                lines.append(words[w] + ' ')
    else:  # no wrapping
        lines = [s]
    output = []
    for line in lines:
        for i in range(fontsizey):  # set up the output for the thing
            output.append('')
        gridlength = len(output) - fontsizey
        for i in line:
            bits = string2bits(font_data[i])
            for b in range(len(bits)):
                output[int(b % fontsizey) + gridlength] += bits[b]
    return output


offsetx = '00011101'
offsety = '01201233'


def pixels2braille(pixels):
    hight = len(pixels)
    width = len(pixels[0])
    output = []
    for y in range(math.ceil(hight / 4)):
        row = ""
        for x in range(math.ceil(width / 2)):
            bit = 0
            for i in range(len(offsetx)):
                scany = y * 4 + int(offsety[i])
                scanx = x * 2 + int(offsetx[i])
                if scanx < width and scany < hight:
                    bit += int(pixels[scany][scanx]) * 2 ** i
            row += chr(int(bit) + 10240)
        output.append(row)
    return output


def display(text, speed, time):
    pixels = text2pixels(text)
    if len(pixels[0]) > displayWidth:  # if the text is longer than the display width then scroll it
        for i in range(len(pixels[0])):
            output = []
            for row in pixels:
                if i < displayWidth:
                    output.append('0' * (displayWidth - i) + row[0:i])
                else:
                    output.append(row[i - displayWidth:i])
            if time:
                addsubs(pixels2braille(output), speed / (len(pixels[0]) + displayWidth))
            else:
                addsubs(pixels2braille(output), speed)
        for i in range(displayWidth):
            output = []
            for row in pixels:
                output.append(row[len(row) - displayWidth + i:len(row)] + '0' * (displayWidth - i))
            if time:
                addsubs(pixels2braille(output), speed / (len(pixels[0]) + displayWidth))
            else:
                addsubs(pixels2braille(output), speed)
    else: # if it fits slap that text in the middle!
        output = []
        for i in pixels:
            output.append(('0' * int((displayWidth - len(pixels[0]) / 2)) + i))
        if time:
            addsubs(pixels2braille(output), speed)
        else:
            addsubs(pixels2braille(output), len(pixels[0]) * float(speed))


demo = ['Scar32', 'presents', 'large & scrolling subtitle text demo!',
        "this scrolling text took me quite a long time to make so i hope you'll enjoy this",
        'this text was made with my own custom pixel text engine with variable-width font and text wrapping which is not being used in this demo',
        'this font has UPPERCASE LETTERS and lowercase letters and all the ascii characters',
        "!\"#$%&\\'()*+,-./0123456789:;<=>?@ABDEFGHIJKLMNCOQPRSTUVWXYZ[]^`abcdefghijklmnopqrstuvwxyz{|}~_",
        'to make this text scroll was a pain in the ass and im not gonna get into the details',
        'it scrolls the text of there is not enough space for the "display" and flashes them', 'up', 'like', 'this',
        'when there is enough room for the entier string of text', 'hope you enjoied this little demo! :3',
        'anyway cya! UwU', 'and one more thing, if you want to use this scrolling subtitle in your own videos i will '
                           'leave this code up on github and that will be in the discription of this video',
        'thanks for watching this demo!', 'bye!! :D']

# display(1, 2, 3)
# 1. type your text here
# 2. speed/time, speed is how fast you want the subs to show to the size of the text (longer text make it go by faster)
# 2. for time type in the amount of time you want the subs to be shown in secs
# 3. if you want it to be time type True, if you want speed type False
# demo program
timestamp = 7000
for i in range(3):
    display(str(3 - i), 1, True)

for i in demo:
    display(i, 0.05, False)
