﻿# Музыка и звуки
define audio.main = "music/main.mp3"
define audio.lose = "sounds/wasted.mp3"
define audio.win = "sounds/level_up.mp3"

define f = Character(color="#df0d76")

define k = 1

screen info_panel:
    frame:
        padding(10, 10)
        xalign 0.5
        yalign 0.07
        text "Уровень [k]"

label start:
    scene bg main
    
    show fumo_1:
        xalign 0.1
        yalign 0.82

    f '''
    Здравствуй, мой дорогой друг!
    {w} Ты попал в игру "Найди Фумо".

    Эта игра более известна в России под названием Найди пару.
    {w} Тебе придется пройти пять уровней.
    '''

    hide fumo_1

    show fumo_2:
        xalign 0.1
        yalign 0.82

    f '''
    Суть игры очень простая. 
    '''

    hide fumo_2

    show fumo_1:
        xalign 0.1
        yalign 0.82

    f '''
    Даны карточки, которые выкладываются «рубашкой» вверх. 
    {w} Далее вы открываете две любые карточки. 
    {w} Если на них изображены одинаковые Фумо, то карточки исчезают, и вы вскрываете следующую пару. 

    Однако, если изображения разные, то карточки возвращаются в режим «рубашкой вверх». 
    {w} Когда все карточки будут разобраны, вы переходите на другой уровень.

    Ой! {w} Чуть ни забыла. {w} Вы должны будете успеть сделать это за определенное время. 
    '''

    hide fumo_1

    show fumo_2:
        xalign 0.1
        yalign 0.82

    f '''
    Каждый уровень все сложнее и сложнее, чтобы было веселее!

    Вот и все! Очень-очень просто. 

    Желаю Вам удачи, мой дорогой друг!
    '''

    jump level_one


label level_one:
    play music main

    show screen info_panel

    $ max_time = 20
    $ ww, hh = 2, 3

    call memoria_game from _call_memoria_game
    jump level_two


label level_two:
    $ k += 1
    show screen info_panel

    $ max_time = 20
    $ ww, hh = 4, 2

    call memoria_game from _call_memoria_game_1
    jump level_three


label level_three:
    $ k += 1
    show screen info_panel

    $ max_time = 25
    $ ww, hh = 3, 4

    call memoria_game from _call_memoria_game_2
    jump level_four


label level_four:
    $ k += 1
    show screen info_panel

    $ max_time = 30
    $ ww, hh = 4, 4

    call memoria_game from _call_memoria_game_3
    jump level_five


label level_five:
    $ k += 1
    show screen info_panel

    $ max_time = 35
    $ ww, hh = 4, 5

    call memoria_game from _call_memoria_game_4
    jump finish


label finish:
    scene black
    with fade

    centered "{size=80}{b}Поздравляем!{/b}\n\n Вы прошли игру.{/size}"