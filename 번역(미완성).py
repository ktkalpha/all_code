import pyautogui
from googletrans import Translator
tts=0
import os
from gtts import gTTS
translator = Translator()
pyautogui.alert('txt파일을 읽을려면 txt파일을 바탕 화면에 넣어주세요.')
user_name=pyautogui.prompt("유저 이름")#()안에 사용자 이름을 넣어주세요.
while True:
    dari=pyautogui.confirm(text='번역',buttons=['직접 입력','txt'])
    if dari=='직접 입력':
        변역_입력=pyautogui.prompt("입력 하세요.")
    if dari=='txt':
        pi=pyautogui.prompt('txt 파일 이름은?')
        text=open('C:/Users/'+str(user_name)+'/OneDrive/바탕 화면/'+pi+'.txt','r')
        변역_입력=text.read()
        text.close()
    변역_언어=pyautogui.confirm(text="번역 언어 선택(종료할때는 꼭 종료버튼으로 종료해주세요.)",buttons=['일','영','중','한','종료'])
    if 변역_언어=='중':
        if pyautogui.confirm(translator.translate(변역_입력, dest="zh-CN").text)=='txt 저장':
            f = open("C:/Users/"+str(user_name)+"/OneDrive/바탕 화면/변역.txt",'w')
            f.write(translator.translate(변역_입력, dest="zh-CN").text)
        tts = gTTS(text=translator.translate(변역_입력, dest="zh-CN").text, lang='zh-CN')
        tts.save("hello.mp3")
        os.system("hello.mp3")
    if 변역_언어=="영":
        if pyautogui.confirm(text=translator.translate(변역_입력, dest="en").text,buttons=['확인','txt 저장'])=='txt 저장':
            f = open("C:/Users/"+str(user_name)+"/OneDrive/바탕 화면/변역.txt",'w')
            f.write(translator.translate(변역_입력, dest="en").text)
        tts = gTTS(text=translator.translate(변역_입력, dest="en").text, lang='en')
        tts.save("hello.mp3")
        os.system("hello.mp3")
    if 변역_언어=="일":
        if pyautogui.confirm(translator.translate(변역_입력, dest="ja").text,buttons=['확인','txt 저장'])=='txt 저장':
            f = open("C:/Users/"+str(user_name)+"/OneDrive/바탕 화면/변역.txt",'w')
            f.write(translator.translate(변역_입력, dest="ja").text)
        tts = gTTS(text=translator.translate(변역_입력, dest="ja").text, lang='ja')
        tts.save("hello.mp3")
        os.system("hello.mp3")
    if 변역_언어=="한":
        if pyautogui.confirm(text=translator.translate(변역_입력, dest="ko").text,buttons=['확인','txt 저장'])=='txt 저장':
            f = open("C:/Users/"+str(user_name)+"/OneDrive/바탕 화면/변역.txt",'w')
            f.write(translator.translate(변역_입력, dest="ko").text)
        tts.save("hello.mp3")
        os.system("hello.mp3")
    if 변역_언어=='종료':
        os.unlink("hello.mp3")
        break
os.unlink("hello.mp3")
