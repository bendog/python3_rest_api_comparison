#!/usr/bin/env python3

import datetime

from labella import scale, timeline, utils


def pycolor(data):
    py_ver = data.get('python', None)
    if py_ver:
        if py_ver >= 3:
            return "#4584b6"
        elif py_ver >= 2:
            return "#ddbe47"
        elif py_ver >= 1:
            return "#FF76ab"
    if data.get('source', None) == 'django':
        return "#0C3C26"
    if data.get('source', None) == 'marvel':
        return "#f0141e"
    if data.get('source', None) == 'starwars':
        return "#1ed014"
    if data.get('source', None) == 'js':
        return "#1ed014"
    if data.get('source', None) == 'bs':
        return "#141ed0"
    if data.get('source', None) == 'windows':
        return "#1e14d0"
    return "#000000"


WINDOWS = [
    {'source': 'windows', 'time': datetime.date(1993, 11, 1), 'text': 'Windows 3.11'},
    {'source': 'windows', 'time': datetime.date(1995, 8, 24), 'text': 'Windows 95'},
    {'source': 'windows', 'time': datetime.date(1998, 6, 25), 'text': 'Windows 98'},
    {'source': 'windows', 'time': datetime.date(2000, 2, 17), 'text': 'Windows 2000'},
    {'source': 'windows', 'time': datetime.date(2000, 9, 14), 'text': 'Windows ME'},
    {'source': 'windows', 'time': datetime.date(2001, 10, 25), 'text': 'Windows XP'},
    # {'source': 'windows', 'time': datetime.date(2002, 9, 9), 'text': 'Windows XP SP1'},
    # {'source': 'windows', 'time': datetime.date(2004, 8, 25), 'text': 'Windows XP SP2'},
    # {'source': 'windows', 'time': datetime.date(2008, 4, 21), 'text': 'Windows XP SP3'},
    {'source': 'windows', 'time': datetime.date(2007, 1, 30), 'text': 'Windows Vista'},
    {'source': 'windows', 'time': datetime.date(2009, 10, 22), 'text': 'Windows 7'},
    {'source': 'windows', 'time': datetime.date(2012, 10, 26), 'text': 'Windows 8'},
    {'source': 'windows', 'time': datetime.date(2013, 10, 17), 'text': 'Windows 8.1'},
    {'source': 'windows', 'time': datetime.date(2015, 6, 29), 'text': 'Windows 10'},
]

MARVEL = [
    {'source': 'marvel', 'time': datetime.date(2008, 5, 2), 'text': 'Iron Man'},
    {'source': 'marvel', 'time': datetime.date(2008, 6, 13), 'text': 'The Incredible Hulk'},
    {'source': 'marvel', 'time': datetime.date(2010, 5, 7), 'text': 'Iron Man 2'},
    {'source': 'marvel', 'time': datetime.date(2011, 5, 6), 'text': 'Thor'},
    {'source': 'marvel', 'time': datetime.date(2011, 7, 22), 'text': 'Captain America'},
    {'source': 'marvel', 'time': datetime.date(2012, 5, 4), 'text': 'The Avengers'},

    {'source': 'marvel', 'time': datetime.date(2013, 5, 3), 'text': 'Iron Man 3'},
    {'source': 'marvel', 'time': datetime.date(2013, 11, 8), 'text': 'Thor: Dark World'},
    {'source': 'marvel', 'time': datetime.date(2014, 4, 4), 'text': 'Capt America: Winter Soldier'},
    {'source': 'marvel', 'time': datetime.date(2014, 8, 1), 'text': 'Guardians of the Galaxy'},
    {'source': 'marvel', 'time': datetime.date(2015, 5, 1), 'text': 'Avengers: Age of Ultron'},
    {'source': 'marvel', 'time': datetime.date(2015, 7, 17), 'text': 'Ant-Man'},

    {'source': 'marvel', 'time': datetime.date(2016, 5, 6), 'text': 'Capt America: Civil War'},
    {'source': 'marvel', 'time': datetime.date(2016, 11, 4), 'text': 'Doc Strange'},
    {'source': 'marvel', 'time': datetime.date(2017, 5, 5), 'text': 'Guardians of the Galaxy 2'},
    {'source': 'marvel', 'time': datetime.date(2017, 7, 7), 'text': 'Spider-man: Homecomming'},
]

JQUERY = [
    {'source': 'js', 'text': 'jquery 1.0', 'time': datetime.date(2006, 8, 26)},
    {'source': 'js', 'text': 'jquery 1.1', 'time': datetime.date(2007, 1, 14)},
    {'source': 'js', 'text': 'jquery 1.2', 'time': datetime.date(2007, 9, 10)},
    {'source': 'js', 'text': 'jquery 1.3', 'time': datetime.date(2009, 1, 14)},
    {'source': 'js', 'text': 'jquery 1.4', 'time': datetime.date(2010, 1, 14)},
    {'source': 'js', 'text': 'jquery 1.5', 'time': datetime.date(2011, 1, 31)},
    {'source': 'js', 'text': 'jquery 1.6', 'time': datetime.date(2011, 5, 3)},
    {'source': 'js', 'text': 'jquery 1.7', 'time': datetime.date(2011, 11, 3)},
    {'source': 'js', 'text': 'jquery 1.8', 'time': datetime.date(2012, 8, 9)},
    {'source': 'js', 'text': 'jquery 1.9', 'time': datetime.date(2013, 1, 15)},
    {'source': 'js', 'text': 'jquery 1.10', 'time': datetime.date(2013, 5, 24)},
    {'source': 'js', 'text': 'jquery 1.11', 'time': datetime.date(2014, 1, 24)},
    {'source': 'js', 'text': 'jquery 1.12', 'time': datetime.date(2016, 1, 8)},
    {'source': 'js', 'text': 'jquery 2.0', 'time': datetime.date(2013, 4, 18)},
    {'source': 'js', 'text': 'jquery 2.1', 'time': datetime.date(2014, 1, 24)},
    {'source': 'js', 'text': 'jquery 2.2', 'time': datetime.date(2016, 1, 8)},
    {'source': 'js', 'text': 'jquery 3.0', 'time': datetime.date(2016, 6, 9)},
    {'source': 'js', 'text': 'jquery 3.1', 'time': datetime.date(2016, 7, 7)},
    {'source': 'js', 'text': 'jquery 3.2', 'time': datetime.date(2017, 3, 16)},
]

BOOTSTRAP = [
    {'source': 'bs', 'text': 'bootstrap 1', 'time': datetime.date(2011, 8, 19)},
    {'source': 'bs', 'text': 'bootstrap 2', 'time': datetime.date(2012, 1, 31)},
    {'source': 'bs', 'text': 'bootstrap 3', 'time': datetime.date(2013, 8, 19)},
    {'source': 'bs', 'text': 'bootstrap 4 beta', 'time': datetime.date(2017, 8, 10)},
]


SHIT_SONGS = [
    {
        'time': datetime.date(2010, 10, 2),
        'text': "Like a G6 by Far East Movement"
    },
]


STARWARS = [
    {'time': datetime.date(1977, 4, 25), 'episode': 4,
     'source': 'starwars',
     'text': 'A New Hope'},
    {'time': datetime.date(1980, 4, 17), 'episode': 5,
     'source': 'starwars',
     'text': 'The Empire Strikes Back'},
    {'time': datetime.date(1984, 4, 25), 'episode': 6,
     'source': 'starwars',
     'text': 'Return of the Jedi'},
    {'time': datetime.date(1999, 4, 19), 'episode': 1,
     'source': 'starwars',
     'text': 'The Phantom Menace'},
    {'time': datetime.date(2002, 4, 16), 'episode': 2,
     'source': 'starwars',
     'text': 'Attack of the Clones'},
    {'time': datetime.date(2005, 4, 19), 'episode': 3,
     'source': 'starwars',
     'text': 'Revenge of the Sith'},
    {'time': datetime.date(2015, 11, 18), 'episode': 7,
     'source': 'starwars',
     'text': 'The Force Awakens'},
]


PY_VERSIONS = [
    # {'text': 'Python 1.0', "python": 1.0, 'time': datetime.date(1994, 1, 1)},
    # {'text': 'Python 1.5', "python": 1.5, 'time': datetime.date(1997, 12, 31)},
    # {'text': 'Python 1.6', "python": 1.6, 'time': datetime.date(2000, 8, 5)},
    # {'text': 'Python 2.0', "python": 2.0, 'time': datetime.date(2000, 10, 16)},
    # {'text': 'Python 2.1', "python": 2.1, 'time': datetime.date(2001, 4, 17)},
    # {'text': 'Python 2.2', "python": 2.2, 'time': datetime.date(2001, 12, 21)},
    # {'text': 'Python 2.3', "python": 2.3, 'time': datetime.date(2003, 7, 29)},
    {'text': 'Python 2.4', "python": 2.4, 'time': datetime.date(2004, 11, 30)},
    {'text': 'Python 2.5', "python": 2.5, 'time': datetime.date(2006, 9, 19)},
    {'text': 'Python 2.6', "python": 2.6, 'time': datetime.date(2008, 10, 1)},
    {'text': 'Python 2.7', "python": 2.7, 'time': datetime.date(2010, 7, 3)},
    {'text': 'Python 3.0', "python": 3.0, 'time': datetime.date(2008, 12, 3)},
    {'text': 'Python 3.1', "python": 3.1, 'time': datetime.date(2009, 6, 27)},
    {'text': 'Python 3.2', "python": 3.2, 'time': datetime.date(2011, 2, 20)},
    {'text': 'Python 3.3', "python": 3.3, 'time': datetime.date(2012, 9, 29)},
    {'text': 'Python 3.4', "python": 3.4, 'time': datetime.date(2014, 3, 16)},
    {'text': 'Python 3.5', "python": 3.5, 'time': datetime.date(2015, 9, 13)},
    {'text': 'Python 3.6', "python": 3.6, 'time': datetime.date(2016, 12, 23)},
    # {'text': 'Python 3.7', "python": 3.7, 'time': datetime.date(2018, 6, 15)},
]


DJANGO_VERSIONS = [
    {'source': 'django', 'text': 'Django 0.9', 'time': datetime.date(2005, 11, 16)},
    {'source': 'django', 'text': 'Django 0.91', 'time': datetime.date(2006, 1, 11)},
    {'source': 'django', 'text': 'Django 0.95', 'time': datetime.date(2006, 7, 29)},
    {'source': 'django', 'text': 'Django 0.96', 'time': datetime.date(2007, 3, 23)},
    {'source': 'django', 'text': 'Django 1.0', 'time': datetime.date(2008, 9, 3)},
    {'source': 'django', 'text': 'Django 1.1', 'time': datetime.date(2009, 7, 29)},
    {'source': 'django', 'text': 'Django 1.2', 'time': datetime.date(2010, 5, 17)},
    {'source': 'django', 'text': 'Django 1.3', 'time': datetime.date(2011, 3, 23)},
    {'source': 'django', 'text': 'Django 1.4', 'time': datetime.date(2012, 3, 23)},
    {'source': 'django', 'text': 'Django 1.5', 'time': datetime.date(2013, 2, 26)},
    {'source': 'django', 'text': 'Django 1.6', 'time': datetime.date(2013, 11, 6)},
    {'source': 'django', 'text': 'Django 1.7', 'time': datetime.date(2014, 9, 2)},
    {'source': 'django', 'text': 'Django 1.8', 'time': datetime.date(2015, 4, 1)},
    {'source': 'django', 'text': 'Django 1.9', 'time': datetime.date(2015, 12, 1)},
    {'source': 'django', 'text': 'Django 1.10', 'time': datetime.date(2016, 8, 1)},
    {'source': 'django', 'text': 'Django 1.11', 'time': datetime.date(2017, 4, 4)},
    {'source': 'django', 'text': 'Django 2.0', 'time': datetime.date(2017, 12, 15)},
    # {'source': 'django', 'text': 'Django 2.1', 'time': datetime.date(2018, 8, 15)},
]


tl = timeline.TimelineTex(
    PY_VERSIONS + DJANGO_VERSIONS,  # + JQUERY, # + MARVEL,
    options={
        # 'direction': 'down',
        'dotColor': pycolor,
        'labelBgColor': pycolor,
        'linkColor': pycolor,
        'scale': scale.TimeScale(),
        # 'layerGap': 40,
        # 'initialWidth': 2000,
        'initialHeight': 1000,
        'labelPadding': {'left': 0, 'right': 0, 'top': 0, 'bottom': 0},
    },
)
tl.export('python_versions.tex')
