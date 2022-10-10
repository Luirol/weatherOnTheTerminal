# weatherOnTheTerminal
Используемый язык программирования: Python

# Просмотр погоды на терминале
Данный скрипт показывает погоду только в Лондоне, Шереметьево и Череповце. Но разобравшись с данным скриптом вы с легкостью можете получать информацию о погоде для любого места на нашей планете.
Для этого обратитесь к документации [https://wttr.in/:help]

## Создание локального репозитория

Предположим, что ваш проект находится в папке /home/user/project. 
Переходим в папку с проектом /home/user/project:

```cd /home/user/project```

Скачиваем проект

```git clone git@github.com:Luirol/weatherOnTheTerminal.git```

Создание виртуального окружения:
Выполните команду:
```pip install -r requirements.txt```

## Запуск тестового примера
Для тестирования запускаем на выполнение скрипт:

```python3 weather.py```

Результат вывода в терминал:
```
svo

      \   /     Ясно
       .-.      +12(10) °C     
    ― (   ) ―   ↑ 5 м/c        
       `-’      10 км          
      /   \     0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 08 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │     \   /     Ясно           │
│      .--.     +13(11) °C     │      .-.      +11(8) °C      │
│   .-(    ).   ↗ 5-6 м/c      │   ― (   ) ―   ↗ 5-8 м/c      │
│  (___.__)__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 09 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │      .-.      Умеренный дожд…│
│      .--.     +13(11) °C     │     (   ).    +9(8) °C       │
│   .-(    ).   ↗ 6-7 м/c      │    (___(__)   → 2 м/c        │
│  (___.__)__)  10 км          │   ‚‘‚‘‚‘‚‘    7 км           │
│               0.0 мм | 0%    │   ‚’‚’‚’‚’    3.6 мм | 87%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      +12(11) °C     │      .-.      +6(5) °C       │
│   ― (   ) ―   ↓ 3 м/c        │   ― (   ) ―   ↓ 1-3 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

London

      \   /     Ясно
       .-.      16 °C          
    ― (   ) ―   → 1 м/c        
       `-’      10 км          
      /   \     0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 08 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │    \  /       Переменная обл…│
│      .-.      17 °C          │  _ /"".-.     13 °C          │
│   ― (   ) ―   → 3 м/c        │    \_(   ).   ↑ 1-2 м/c      │
│      `-’      10 км          │    /(___(__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 09 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Пасмурно       │
│      .-.      18 °C          │      .--.     14 °C          │
│   ― (   ) ―   ↑ 5 м/c        │   .-(    ).   ↑ 1-2 м/c      │
│      `-’      10 км          │  (___.__)__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Местами дождь  │     \   /     Ясно           │
│   ,\_(   ).   15 °C          │      .-.      +12(11) °C     │
│    /(___(__)  ↓ 4 м/c        │   ― (   ) ―   ↘ 2-3 м/c      │
│      ‘ ‘ ‘ ‘  10 км          │      `-’      10 км          │
│     ‘ ‘ ‘ ‘   0.3 мм | 66%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Череповец

      \   /     Ясно
       .-.      +12(9) °C      
    ― (   ) ―   ↑ 6 м/c        
       `-’      10 км          
      /   \     0.0 мм         
                        ┌─────────────┐                        
┌───────────────────────┤ Сб. 08 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Облачно        │
│      .-.      +12(10) °C     │      .--.     +11(8) °C      │
│   ― (   ) ―   ↗ 6-7 м/c      │   .-(    ).   ↗ 6-10 м/c     │
│      `-’      10 км          │  (___.__)__)  10 км          │
│     /   \     0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вс. 09 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Слабая морось  │     \   /     Ясно           │
│     (   ).    +10(8) °C      │      .-.      +8(5) °C       │
│    (___(__)   ↗ 5-7 м/c      │   ― (   ) ―   → 3-5 м/c      │
│     ‘ ‘ ‘ ‘   2 км           │      `-’      10 км          │
│    ‘ ‘ ‘ ‘    0.7 мм | 91%   │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 окт. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     +9(7) °C       │      .-.      +6(4) °C       │
│    \_(   ).   ↗ 3-4 м/c      │   ― (   ) ―   ↗ 3-6 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
```
