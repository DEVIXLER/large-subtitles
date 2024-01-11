# Scar32

import math

unfired_data = ['011', '00100000100000100010001010000010111', '01100000100000010010100010001001001',
                '1010010010000110111011001000111011100001010100010110001000010010001',
                '1011000011001100101001001010000011100001011001011010110110110001111100101010111011100110111000101010100001001011001',
                '1110011011010100101010010100010101100001001000001110010010101000101011001110110100101001011101101101001011101110101011100111001000110110001110100111101010110110111',
                '110101101100000100100000111001001010100010101100111011010010000111100010101001101110111011110110011',
                '1000000010001110111', '0010000010000001001', '011010001000010011100001011000100010011010101010111',
                '011000001000010011101001011010110010011110100011111',
                '10100001000100010010100010001001001001011010100100001101101', '10100010010100100110100111001010111',
                '0100011011000011001', '1000001001001110011', '0010001010000010111', '1000001011001100101',
                '101011001000010010100000111000101010011011101110111100101011000011101100101',
                '0110000011000100101001101110001011001010111',
                '10100001000000001110010010101100101100001111000100100110001000101010001011110010111',
                '10100000100100001010010110101001011011010111000110110010101011101110011011100010101',
                '10101110110011001010000110110001101',
                '10110000100000001010000111100101101011011011000111110010101011101110011011100010101',
                '1010000010010000101011001110100110101010111',
                '10110000110011001010010010100000111000010111000111110010101011101110011011100010101000011111000101110000111',
                '10110000100000100010001010100110111011101111001010110010001011011110010111100010001',
                '10100010110100010111000011101100101001001010000011100001011001011010110110110001011',
                '00100001100000011110001010000010111', '01000101100001011110011010000010111',
                '101100011100001001110010111', '10000010000011100010001001001110011', '101000011101001001100010111',
                '1010000100000000111001001010110010110000111100010010110101101001111010100010101010001010111',
                '11110110100100101110101011100010011000010010100010110000101110010011101001110110001101010011010101110001001010010010010101100110001010100111001001110110001',
                '1010001011001000101100101110010111001101111',
                '101011101100001011100000101011001011000011110001011011011010000110101101100100011111001010101110111',
                '101010001000000010100010111010101110111010110010001100010110110011101000101',
                '101100001000000010100010111100101110000110001001101', '1011000010000000101000101110000110001001101',
                '101100001001001011100010110000001010000110010001101',
                '101100001001001011100010110000001010000110010001101',
                '111100001001001010101110111001101110001010100010011',
                '101000001000001011110000100000100010100101010010111', '101000001000001011110010111',
                '1110001011000000101011101111100010111010111', '10100010110000001011001011110000101',
                '11111001000100001010100010100001001000100110101011110010111110100111100111101101111',
                '1111100100010000101010001010000100100010011010101111001011111010011',
                '111110010001000010101000101000010010001001101010111100101111101001111001001',
                '1111100100010000101010001010000100100010011010101111001011111010011110010011001001011010111',
                '10100010110000001010110010110000111100010110110110100001101',
                '1010001011000000101011001011000011110001011011011010000110101001101011011111001001110010111',
                '101100001100110010100100101000001110000101100101101011011011000111110010101011101110011011100010101',
                '10110000100000001010100010001010111',
                '1111100010011010001101101011001011101010111001101010001000100000101',
                '11100000100000001010111011111000101', '1110000010000110111011010111011011111000101',
                '10100000100100101111000010000010111', '1010000010001001101100001010100110001010111',
                '11000000100101001010001011110110111', '01101000100000001010001111101011111',
                '01100000100010001010101111100011111', '101000010100100010110001011', '0100000010000100111',
                '10001110000001100010001001100010101001101110101011101110101011101110111010001101111010011010010110100001111',
                '10000000100000101110000111000101101010011010110111101110101010101110011011100010101',
                '1000110111001001101001011010000111100010101001101110101011101110101',
                '10001100100011101110110111001001101001011010000111100010101001101110101011101110101',
                '10000010000011100010110111101001101001011010000111100010101001101110101011101110101',
                '100001101100010011101000101011001010000110001001101',
                '1000110111001001101001011010000111100010101001101110101011101110101011011010111010001111101010111110011111100011101',
                '10000000100000101110000111000101101010011010110111101110111', '00100001010000101110000010000000111',
                '011010010100101110100111111000111110100010001000111',
                '100000001000001011101101100000100110011000001110111', '0010000010000010111',
                '111000011000001011100001110001011010100110101101111011101110110111010001101101011011100111111010111',
                '10000001100000101110000111000101101010011010110111101110111',
                '100011101000110111101001101001011010000111100010101001101110101011101110101',
                '1000001111000001101000011100010110101001101011011110111010101010111001101110011011100010101',
                '1000110111001001101001011010000111100010101001101110101011101110101011011010111010001111111',
                '011000101100000110100001110001011010100110101101111',
                '1000110111001001101001011010000111100110001010100010111001101110101010101110011011100010101',
                '0110010010000110101010101110000101001001011',
                '1000000110000010101001101110101011101110101011011010111010001110111', '101000011000101011110001101',
                '1110000110000110111011011011011011111001101', '10000001100011101110110110000010111',
                '10000001100001101110110110000011111', '10000001100011011010001011101110111',
                '01101000100001001110010111100010001001100110011110101011111', '0010000010000011111',
                '01100000100001001110010111101010001001100110011110100011111',
                '110000100000010111101001111011100011001000110101111', '1100001011011010111']
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