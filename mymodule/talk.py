from mypackage.speak_hear import *
import numpy as np
from time import sleep

""" q1 = open("D:\\2022_2\\AI_code\\database\\question_ques.txt", mode='r', encoding="utf8")
ques1 = q1.read().split("\n")
a1 = open("D:\\2022_2\\AI_code\\database\\answer_ques.txt", mode='r', encoding="utf8")
answ1 = a1.read().split("\n") """

def talk():
    speak("yes, i would love to talk to you ")
    speak("Do you want to ask or answer ?")
    while True:
        boss = hear()
        if boss is None:
            speak("i can't hear you, please say again")
        elif "ask" in boss:
            ask()
        elif "answer" in boss:
            ans()
        elif "previous" in boss:
            speak("Do you need any other help?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            speak("i can't hear you, please say again")


# def choose_ans():
#     speak("choose one question")
#     while True:
#         i = int(input())
#         if i >= 0 or i <= len(answ2):
#             i = i - 1
#             break
#         else:
#             speak(f"I just learn {len(answ2)}, please choose again")
#     return i


def ask():
    speak("please talk to me")
    while True:
        boss = hear()
        if boss is None:
            speak("I can't hear you, please say again")
        elif "previous" in boss:
            speak("Do you want to talk to me more?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            Api = handle_data_ques(boss)
            if Api is None:
                speak("I can't hear you, please say again")
            else:
                speak(Api)


def ans():
    speak("please talk to me")
    i =0
    while True:
        boss = hear()
        if boss is None:
            speak("I can't hear you, please say again")
        elif "previous" in boss:
            speak("Do you want to talk to me more?")
            break
        elif "goodbye" in boss:
            speak("goodbye boss")
            exit()
        elif "hold on" in boss:
            speak("enter any press to continue")
            input()
        else:
            Api = handle_data_ans(boss,i)
            if Api is None:
                speak("I can't hear you, please say again")
            else:
                speak(Api)
                i = i+1
                if i == len(ques1):
                    i = 0



# def practice():
#     while True:
#         boss = hear()
#         if boss is None:
#             speak("I can't hear you, please say again")
#         elif "previous" in boss:
#             speak("Do you want to talk to me more?")
#             break
#         elif "goodbye" in boss:
#             speak("goodbye boss")
#             exit()
#         elif "hold on" in boss:
#             speak("enter any press to continue")
#             input()
#         else:
#             i = 1
#             for ans in answ4:
#                 Api = ans
#                 if Api is None:
#                     speak("I can't hear you, please say again")
#                 else:
#                     speak(Api)
#                     i = i+1
#                     input()
#                 if i == len(answ4):
#                     speak("You have done all question!!!")

def handle_data_ques(text):
    # chia câu hỏi người dùng thành các từ riêng biệt
    if text is None:
        return None
    else:  # what+ your + name         3
        text1 = text.split(" ")
        # khởi tạo list rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng với data question đã tạo
        que = []
        # tính toán tỷ lệ phần trăm
        for s in ques1:
            text2 = s.lower().split(" ")
            count = 0
            a = len(text2)
            for i in text1:
                if i in text2:
                    count += 1
            ratio = count * 100 / a
            que.append(ratio)
        return answ1[np.argmax(que)]  # trả về vị trí có tỷ lệ % cao nhất


def handle_data_ans(text,i):
    if text is None:
        return None
    else:
        return ques1[i]


# def question(i):
#     speak(ques3[i])
