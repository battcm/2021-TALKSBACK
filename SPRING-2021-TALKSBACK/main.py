import os.path
import random
import time
from os import path

import nltk
import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import rosegraphics as rg


# ---------------------------------------------------------------------------------------------------------------------
# CARSON BATT
# 3-17-21
# ENGD 150
# FRESHMAN SPRING INDIVIDUAL PROJECT
# ---------------------------------------------------------------------------------------------------------------------


# MAIN
def main():  # VOID
    # nltk.download('punkt')
    # nltk.download('averaged_perceptron_tagger')
    in_put = input("yo wassup? ")
    tagged = get_tagged(in_put)
    write_txt(tagged)
    sentiment_scores(in_put)
    out_put = make_sentence(tagged)
    print(out_put)
    speak(out_put)


# JUDGES SENTIMENT OR CONNOTATION OF USER INPUT
def sentiment_scores(sentence):  # VOID
    slid_object = SentimentIntensityAnalyzer()
    sentiment_dict = slid_object.polarity_scores(sentence)

    if 0.5 >= sentiment_dict['compound'] >= 0.05:
        neutral_face()
    if sentiment_dict['compound'] > 0.5:
        surprised_face()
    if -0.7 <= sentiment_dict['compound'] <= - 0.05:
        angry_face()
    if sentiment_dict['compound'] < -0.7:
        sad_face()
    if 0.05 > sentiment_dict['compound'] > - 0.05:
        confused_face()


# OUTPUT TEXT TO SPEECH
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def neutral_face():  # Void
    window = rg.RoseWindow(1000, 1000)
    background = rg.Rectangle(rg.Point(0, 0), rg.Point(1000, 1000))
    background.fill_color = "white"
    background.attach_to(window)
    mouth = rg.Rectangle(rg.Point(200, 700), rg.Point(800, 600))
    mouth.fill_color = "green"
    mouth.attach_to(window)

    mouth2 = rg.Rectangle(rg.Point(300, 650), rg.Point(700, 600))
    mouth2.fill_color = "white"
    mouth2.outline_color = "white"
    mouth2.attach_to(window)

    left_eye = rg.Circle(rg.Point(350, 200), 80)
    left_eye.fill_color = "green"
    left_eye.attach_to(window)

    right_eye = rg.Circle(rg.Point(650, 200), 80)
    right_eye.fill_color = "green"
    right_eye.attach_to(window)

    window.render()
    time.sleep(1)
    window.close()


def angry_face():  # Void
    window = rg.RoseWindow(1000, 1000)
    background = rg.Rectangle(rg.Point(0, 0), rg.Point(1000, 1000))
    background.fill_color = "white"
    background.attach_to(window)
    mouth = rg.Rectangle(rg.Point(200, 700), rg.Point(800, 600))
    mouth.fill_color = "red"
    mouth.attach_to(window)

    mouth2 = rg.Rectangle(rg.Point(300, 700), rg.Point(700, 650))
    mouth2.fill_color = "white"
    mouth2.outline_color = "white"
    mouth2.attach_to(window)

    left_eye = rg.Circle(rg.Point(350, 200), 80)
    left_eye.fill_color = "red"
    left_eye.attach_to(window)

    right_eye = rg.Circle(rg.Point(650, 200), 80)
    right_eye.fill_color = "red"
    right_eye.attach_to(window)

    left_eyebrow = rg.Line(rg.Point(350, 100), rg.Point(450, 180))
    left_eyebrow.thickness = 50
    left_eyebrow.color = "white"
    left_eyebrow.attach_to(window)

    right_eyebrow = rg.Line(rg.Point(650, 100), rg.Point(550, 180))
    right_eyebrow.thickness = 50
    right_eyebrow.color = "white"
    right_eyebrow.attach_to(window)

    window.render()
    time.sleep(1)
    window.close()


def sad_face():
    window = rg.RoseWindow(1000, 1000)
    background = rg.Rectangle(rg.Point(0, 0), rg.Point(1000, 1000))
    background.fill_color = "white"
    background.attach_to(window)
    mouth = rg.Rectangle(rg.Point(200, 700), rg.Point(800, 600))
    mouth.fill_color = "blue"
    mouth.attach_to(window)

    mouth2 = rg.Rectangle(rg.Point(300, 700), rg.Point(700, 650))
    mouth2.fill_color = "white"
    mouth2.outline_color = "white"
    mouth2.attach_to(window)

    left_eye = rg.Circle(rg.Point(350, 200), 80)
    left_eye.fill_color = "blue"
    left_eye.attach_to(window)

    right_eye = rg.Circle(rg.Point(650, 200), 80)
    right_eye.fill_color = "blue"
    right_eye.attach_to(window)

    left_eyebrow = rg.Line(rg.Point(350, 100), rg.Point(250, 180))
    left_eyebrow.thickness = 50
    left_eyebrow.color = "white"
    left_eyebrow.attach_to(window)

    right_eyebrow = rg.Line(rg.Point(650, 100), rg.Point(750, 180))
    right_eyebrow.thickness = 50
    right_eyebrow.color = "white"
    right_eyebrow.attach_to(window)

    window.render()
    time.sleep(1)
    window.close()


def surprised_face():  # Void
    window = rg.RoseWindow(1000, 1000)
    background = rg.Rectangle(rg.Point(0, 0), rg.Point(1000, 1000))
    background.fill_color = "white"
    background.attach_to(window)
    mouth = rg.Rectangle(rg.Point(200, 700), rg.Point(800, 600))
    mouth.fill_color = "yellow"
    mouth.attach_to(window)

    mouth2 = rg.Rectangle(rg.Point(300, 650), rg.Point(700, 600))
    mouth2.fill_color = "white"
    mouth2.outline_color = "white"
    mouth2.attach_to(window)

    left_eye = rg.Circle(rg.Point(350, 200), 80)
    left_eye.fill_color = "yellow"
    left_eye.attach_to(window)

    right_eye = rg.Circle(rg.Point(650, 200), 80)
    right_eye.fill_color = "yellow"
    right_eye.attach_to(window)

    left_dimple = rg.Circle(rg.Point(350, 280), 70)
    left_dimple.fill_color = "white"
    left_dimple.outline_color = "white"
    left_dimple.attach_to(window)

    right_dimple = rg.Circle(rg.Point(650, 280), 70)
    right_dimple.fill_color = "white"
    right_dimple.outline_color = "white"
    right_dimple.attach_to(window)

    window.render()
    time.sleep(1)
    window.close()


def confused_face():  # Void
    window = rg.RoseWindow(1000, 1000)
    background = rg.Rectangle(rg.Point(0, 0), rg.Point(1000, 1000))
    background.fill_color = "white"
    background.attach_to(window)
    mouth = rg.Rectangle(rg.Point(200, 700), rg.Point(800, 600))
    mouth.fill_color = "orange"
    mouth.attach_to(window)

    mouth2 = rg.Rectangle(rg.Point(300, 700), rg.Point(700, 650))
    mouth2.fill_color = "white"
    mouth2.outline_color = "white"
    mouth2.attach_to(window)

    left_eye = rg.Circle(rg.Point(350, 220), 80)
    left_eye.fill_color = "orange"
    left_eye.attach_to(window)

    right_eye = rg.Circle(rg.Point(650, 180), 80)
    right_eye.fill_color = "orange"
    right_eye.attach_to(window)

    left_dimple = rg.Circle(rg.Point(350, 200), 50)
    left_dimple.fill_color = "white"
    left_dimple.outline_color = "white"
    left_dimple.attach_to(window)

    right_dimple = rg.Circle(rg.Point(650, 200), 50)
    right_dimple.fill_color = "white"
    right_dimple.outline_color = "white"
    right_dimple.attach_to(window)

    left_cornea = rg.Circle(rg.Point(360, 200), 20)
    left_cornea.fill_color = "orange"
    left_cornea.outline_color = "white"
    left_cornea.attach_to(window)

    right_cornea = rg.Circle(rg.Point(640, 200), 20)
    right_cornea.fill_color = "orange"
    right_cornea.outline_color = "white"
    right_cornea.attach_to(window)

    window.render()
    time.sleep(1)
    window.close()


# CONSTRUCTS "SENTENCE" USING DATA.TXT LINES AS TEMPLATES
def make_sentence(tagged):  # STRING
    sentence = ""
    for k in range(len(tagged)):
        name = (tagged[k][1] + ".txt")
        if path.exists(name) and os.path.getsize(name) != 0:
            with open(tagged[k][1] + ".txt") as f:
                line = random.choice(f.readlines())
                sentence += line[:len(line) - 1]
        else:
            sentence += tagged[k][0]
        sentence += " "
    return sentence


# WRITES WORDS FROM INPUT INTO TEXT FILES
def write_txt(tagged):  # VOID
    for k in range(len(tagged)):
        name = tagged[k][1] + ".txt"
        f = open(name, "a")
        f.write(tagged[k][0] + "\n")
        f.close()


# DELETES TEXT FILES
def delete_files(tagged):  # VOID
    for k in range(len(tagged)):
        os.remove(tagged[k][1] + ".txt")


# BREAKS A SENTENCE INTO A TUPLE THAT MAPS A WORD TO ITS PART OF SPEECH
def get_tagged(string):  # TUPLE
    return nltk.pos_tag(nltk.word_tokenize(string))


main()
