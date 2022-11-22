# coding: utf-8
# license: GPLv3

#import tkinter
#from tkinter.filedialog import *\

from sys import exec_prefix
import pygame
from solar_vis import *
from solar_model import *
from solar_input import *

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""


def execution(time_step):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects, time_step)
    for body in space_objects:
        update_object_position(space, body)
    physical_time += time_step


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True

    print('Started execution...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    print('Paused execution.')


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    
    global space_objects
    
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button

    print('Modelling started!')
    physical_time = 0

    pygame.init()
    space = pygame.display.set_mode((window_width, window_height))
    space.fill("white")
    clock = pygame.time.Clock()
    FPS = 30
    finished = False
    
    space_objects = read_space_objects_data_from_file("solar_system.txt")
    calculate_scale_factor(45e11)
    
    while not finished:
        pygame.display.update()
        space.fill("white")
        clock.tick(FPS)
        if perform_execution:
            for i in range(100):
                execution(1/FPS*10000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONUP:
                start_execution()


if __name__ == "__main__":
    main()
