import json, re

transtable = str.maketrans('áäàÁćéèÉÈƒĹìíÍÌĺńŃóÒŕŔúÚýÝ', 'aaacAeeEEfLiiIIlnNoOrRuUyY')
def clean_sentence(sentence, escape = ['']):
    return_sentence = ''
    sentence = sentence.translate(transtable)
    regex = []
    regex += [r'[\u0030-\u007a]+']
    regex += [r'[\u3041-\u9fff]+']
    regex = "|".join(regex)
    for word in sentence:
        _ord = ord(word)
        this_word = word
        if 0x4e00 <= _ord <= 0x9fff: # 中文
            pass
        elif 0x0061 <= _ord <= 0x007a: # 小寫英文
            pass
        elif 0x0041 <= _ord <= 0x005a: # 大寫英文
            pass
        elif 0x00e5 <= _ord <= 0x007a: # 小寫英文
            pass
        elif 0x0041 <= _ord <= 0x005a: # 大寫英文
            pass
        elif 0x0030 <= _ord <= 0x0039: # 數字
            pass
        elif 0xff41 <= _ord <= 0xff5a: # 全形小寫英文
            _ord -= 0xfee0
        elif 0xff21 <= _ord <= 0xff3a: # 全形大寫英文
            _ord -= 0xfee0
        elif 0xff10 <= _ord <= 0xff19: # 全形數字
            _ord -= 0xfee0
        elif 0xff66 <= _ord <= 0xff9d: # 半形日文
            pass
        elif 0x3041 <= _ord <= 0x30ff: # 全形日文
            pass
        elif _ord == 0x3000 or _ord == 0x0020 or _ord == 0x200b:
            _ord = 32 
        elif word in escape:
            pass
        else:
            _ord = 32 
            
        return_sentence = return_sentence + chr(_ord)
    sent_list = re.compile(regex).findall(re.sub(' +', ' ', return_sentence.lower().strip()))
    #sent_list = ['nnnnn' if _w.isdigit() else _w for _w in sent_list]
    return ' '.join(sent_list)

def checkword (x):
    return any('\u4e00' <= c <= '\u9fff' for c in x)

if __name__ == "__main__":
    print('肉 RÒU by T-HAMÉ'.translate(transtable))
    print(clean_sentence('啡。冷の萃 Nitro Tea&coffee --\/啡冷萃éÒＱＲＳＴＵ'))
    # follow test code output "html 你覺得我給你 10 個蘋果 ok 嗎 不 我要 20 個"
    r = clean_sentence("<html>你覺得我給你１０個蘋果ok嗎?   不 ！ 我要20個.")
    print(r)
