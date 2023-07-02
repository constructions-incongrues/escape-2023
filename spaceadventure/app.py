from asciimatics.effects import Cycle, Stars
from asciimatics.effects import RandomNoise
from asciimatics.event import MouseEvent, KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.screen import Screen
from random import randint
import sys
from frames import *

def title(screen):
    effects = [
        Cycle(
            screen,
            FigletText("SPACE", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ADVENTURE", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]

    return Scene(effects, -1)

def question1(screen):
    return Scene([
        Question1Frame(screen),
        Stars(screen, 200)
    ], -1)

def question2(screen):
    return Scene([
        Question2Frame(screen),
        Stars(screen, 200)
    ], -1)

def question3(screen):
    return Scene([
        Question3Frame(screen),
        Stars(screen, 200)
    ], -1)

def question4(screen):
    return Scene([
        Question4Frame(screen),
        Stars(screen, 200)
    ], -1)

def question5(screen):
    return Scene([
        Question5Frame(screen),
        Stars(screen, 200)
    ], -1)

def noise(screen, text= None):
    if text is None:
        effects = [RandomNoise(screen)]
    else:
        effects = [RandomNoise(screen, signal=Rainbow(screen, FigletText("DANGER")))]

    return Scene(effects, -1)

def unhandled_input(event):
    if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
        raise NextScene
    else:
        return event

def main(screen, scene):
    scenes = [
        title(screen),
        question1(screen),
        noise(screen),
        question2(screen),
        noise(screen),
        question3(screen),
        noise(screen),
        question4(screen),
        noise(screen),
        question5(screen),
    ]
    screen.play(scenes, unhandled_input=unhandled_input)

last_scene = None
while True:
    Screen.wrapper(main, arguments=[last_scene])
    sys.exit(0)
