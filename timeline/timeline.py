#!/usr/bin/env python3

import datetime

from labella import scale, timeline, utils


def bgcolor(data):
    py_ver = data.get('python')
    if py_ver:
        if py_ver >= 3:
            return "#4584b6"
        elif py_ver >= 2:
            return "#ddbe47"
        elif py_ver >= 1:
            return "#FF76ab"

    BG_COLOUR = {
        'django': "#0C3C26",
        'yii': "#9BB76C",
        'marvel': "#f0141e",
        'starwars': "#1ed014",
        'jquery': "#1ed014",
        'bs': "#141ed0",
        'windows': "#1e14d0",
        'ruby': "#CC342D",
        'php': "#4f5b93",
        'java': "#ED8B00",
        'js': "#F6D140",
        'r': '#4671AD',
    }
    return BG_COLOUR.get(data.get('source'), "#000000")  # if matched return value, if not return default


def fgcolor(data):
    FG_COLOR = {
        'js': "#000000",
        # 'r': '#000000',
    }
    return FG_COLOR.get(data.get('source'), "#FFFFFF")  # if matched return value, if not return default


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
    {'source': 'jquery', 'text': 'jquery 1.0', 'time': datetime.date(2006, 8, 26)},
    {'source': 'jquery', 'text': 'jquery 1.1', 'time': datetime.date(2007, 1, 14)},
    {'source': 'jquery', 'text': 'jquery 1.2', 'time': datetime.date(2007, 9, 10)},
    {'source': 'jquery', 'text': 'jquery 1.3', 'time': datetime.date(2009, 1, 14)},
    {'source': 'jquery', 'text': 'jquery 1.4', 'time': datetime.date(2010, 1, 14)},
    {'source': 'jquery', 'text': 'jquery 1.5', 'time': datetime.date(2011, 1, 31)},
    {'source': 'jquery', 'text': 'jquery 1.6', 'time': datetime.date(2011, 5, 3)},
    {'source': 'jquery', 'text': 'jquery 1.7', 'time': datetime.date(2011, 11, 3)},
    {'source': 'jquery', 'text': 'jquery 1.8', 'time': datetime.date(2012, 8, 9)},
    {'source': 'jquery', 'text': 'jquery 1.9', 'time': datetime.date(2013, 1, 15)},
    {'source': 'jquery', 'text': 'jquery 1.10', 'time': datetime.date(2013, 5, 24)},
    {'source': 'jquery', 'text': 'jquery 1.11', 'time': datetime.date(2014, 1, 24)},
    {'source': 'jquery', 'text': 'jquery 1.12', 'time': datetime.date(2016, 1, 8)},
    {'source': 'jquery', 'text': 'jquery 2.0', 'time': datetime.date(2013, 4, 18)},
    {'source': 'jquery', 'text': 'jquery 2.1', 'time': datetime.date(2014, 1, 24)},
    {'source': 'jquery', 'text': 'jquery 2.2', 'time': datetime.date(2016, 1, 8)},
    {'source': 'jquery', 'text': 'jquery 3.0', 'time': datetime.date(2016, 6, 9)},
    {'source': 'jquery', 'text': 'jquery 3.1', 'time': datetime.date(2016, 7, 7)},
    {'source': 'jquery', 'text': 'jquery 3.2', 'time': datetime.date(2017, 3, 16)},
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
    {'text': 'Python 1.0', "python": 1.0, 'time': datetime.date(1994, 1, 1)},
    {'text': 'Python 1.5', "python": 1.5, 'time': datetime.date(1997, 12, 31)},
    {'text': 'Python 1.6', "python": 1.6, 'time': datetime.date(2000, 8, 5)},
    {'text': 'Python 2.0', "python": 2.0, 'time': datetime.date(2000, 10, 16)},
    {'text': 'Python 2.1', "python": 2.1, 'time': datetime.date(2001, 4, 17)},
    {'text': 'Python 2.2', "python": 2.2, 'time': datetime.date(2001, 12, 21)},
    {'text': 'Python 2.3', "python": 2.3, 'time': datetime.date(2003, 7, 29)},
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
    {'text': 'Python 3.7', "python": 3.7, 'time': datetime.date(2018, 6, 27)},
    {'text': 'Python 3.8', "python": 3.8, 'time': datetime.date(2019, 10, 20)},
]


DJANGO_VERSIONS = [
    # {'source': 'django', 'text': 'Django 0.9', 'time': datetime.date(2005, 11, 16)},
    # {'source': 'django', 'text': 'Django 0.91', 'time': datetime.date(2006, 1, 11)},
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
    {'source': 'django', 'text': 'Django 2.1', 'time': datetime.date(2018, 8, 1)},
    {'source': 'django', 'text': 'Django 2.2', 'time': datetime.date(2019, 8, 1)},
]

PHP_VERSIONS = [
    {'source': 'php', 'text': 'PHP 1.0', 'time': datetime.date(1995, 6, 8)},
    {'source': 'php', 'text': 'PHP 2.0', 'time': datetime.date(1997, 11, 1)},
    {'source': 'php', 'text': 'PHP 3.0', 'time': datetime.date(1998, 6, 6)},
    {'source': 'php', 'text': 'PHP 4.0', 'time': datetime.date(2000, 5, 22)},

    {'source': 'php', 'text': 'PHP 5.0', 'time': datetime.date(2004, 7, 13)},
    {'source': 'php', 'text': 'PHP 5.1', 'time': datetime.date(2005, 11, 24)},
    {'source': 'php', 'text': 'PHP 5.2', 'time': datetime.date(2006, 11, 2)},
    {'source': 'php', 'text': 'PHP 5.3', 'time': datetime.date(2009, 6, 30)},
    {'source': 'php', 'text': 'PHP 5.4', 'time': datetime.date(2012, 3, 1)},
    {'source': 'php', 'text': 'PHP 5.5', 'time': datetime.date(2013, 6, 20)},
    {'source': 'php', 'text': 'PHP 5.6', 'time': datetime.date(2014, 8, 28)},

    {'source': 'php', 'text': 'PHP 7.0', 'time': datetime.date(2015, 12, 3)},
    {'source': 'php', 'text': 'PHP 7.1', 'time': datetime.date(2016, 12, 1)},
    {'source': 'php', 'text': 'PHP 7.2', 'time': datetime.date(2017, 11, 30)},
    {'source': 'php', 'text': 'PHP 7.3', 'time': datetime.date(2018, 12, 6)},
]

YII_VERSIONS = [
    {'source': 'yii', 'text': 'Yii 1.0', 'time': datetime.date(2008, 12, 3)},
    {'source': 'yii', 'text': 'Yii 1.1', 'time': datetime.date(2010, 1, 10)},
    {'source': 'yii', 'text': 'Yii 1.1.15',
        'time': datetime.date(2014, 6, 29)},
    {'source': 'yii', 'text': 'Yii 2.0', 'time': datetime.date(2014, 10, 12)},
]


RUBY_VERSIONS = [
    {'source': 'ruby', 'text': 'Ruby 1.0', 'time': datetime.date(1996, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 1.8', 'time': datetime.date(2003, 8, 4)},
    {'source': 'ruby', 'text': 'Ruby 1.9', 'time': datetime.date(2007, 12, 25)},

    {'source': 'ruby', 'text': 'Ruby 2.0', 'time': datetime.date(2013, 2, 24)},
    {'source': 'ruby', 'text': 'Ruby 2.1', 'time': datetime.date(2013, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 2.2', 'time': datetime.date(2014, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 2.3', 'time': datetime.date(2015, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 2.4', 'time': datetime.date(2016, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 2.5', 'time': datetime.date(2017, 12, 25)},
    {'source': 'ruby', 'text': 'Ruby 2.6', 'time': datetime.date(2018, 12, 25)},

    # {'source': 'ruby', 'text': 'Ruby 3.0', 'time': datetime.date(2020, 2, 24)},
]

JAVA_VERSIONS = [
    {'source': 'java', 'text': 'Java 1.0', 'time': datetime.date(1996, 1, 1)},
    {'source': 'java', 'text': 'Java 1.1', 'time': datetime.date(1997, 2, 1)},
    {'source': 'java', 'text': 'Java 1.2', 'time': datetime.date(1998, 12, 1)},
    {'source': 'java', 'text': 'Java 1.3', 'time': datetime.date(2000, 5, 1)},
    {'source': 'java', 'text': 'Java 1.4', 'time': datetime.date(2002, 2, 1)},
    {'source': 'java', 'text': 'Java 5.0', 'time': datetime.date(2004, 9, 1)},
    {'source': 'java', 'text': 'Java 6.0', 'time': datetime.date(2006, 12, 1)},
    {'source': 'java', 'text': 'Java 7.0', 'time': datetime.date(2011, 6, 1)},
    {'source': 'java', 'text': 'Java 8.0', 'time': datetime.date(2014, 3, 1)},
    {'source': 'java', 'text': 'Java 9.0', 'time': datetime.date(2017, 9, 1)},
    {'source': 'java', 'text': 'Java 10.0', 'time': datetime.date(2018, 3, 1)},
    {'source': 'java', 'text': 'Java 11.0', 'time': datetime.date(2018, 9, 1)},
    {'source': 'java', 'text': 'Java 12.0', 'time': datetime.date(2019, 3, 1)},
]

JS_VERSIONS = [
    {'source': 'js', 'text': 'JavaScript 1.0', 'time': datetime.date(1996, 3, 1)},
    {'source': 'js', 'text': 'JavaScript 1.1', 'time': datetime.date(1996, 8, 1)},
    {'source': 'js', 'text': 'JavaScript 1.2', 'time': datetime.date(1997, 6, 1)},
    {'source': 'js', 'text': 'JavaScript 1.3', 'time': datetime.date(1998, 10, 1)},
    {'source': 'js', 'text': 'JavaScript 1.5', 'time': datetime.date(2000, 11, 1)},
    {'source': 'js', 'text': 'JavaScript 1.6', 'time': datetime.date(2005, 11, 1)},
    {'source': 'js', 'text': 'JavaScript 1.7', 'time': datetime.date(2006, 10, 1)},
    {'source': 'js', 'text': 'JavaScript 1.8', 'time': datetime.date(2008, 6, 1)},
]

ES_VERSIONS = [
    {'source': 'js', 'text': 'ECMA Script 1.0', 'time': datetime.date(1997, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 2.0', 'time': datetime.date(1998, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 3.0', 'time': datetime.date(1999, 12, 1)},

    {'source': 'js', 'text': 'ECMA Script 5.0', 'time': datetime.date(2009, 12, 1)},
    {'source': 'js', 'text': 'ECMA Script 5.1', 'time': datetime.date(2011, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 6.0', 'time': datetime.date(2015, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 7.0', 'time': datetime.date(2016, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 8.0', 'time': datetime.date(2017, 6, 1)},
    {'source': 'js', 'text': 'ECMA Script 9.0', 'time': datetime.date(2018, 6, 1)},
]

R_VERSIONS = [
    {'source': 'r', 'text': 'R 0.6', 'time': datetime.date(1997, 12, 5)},
    {'source': 'r', 'text': 'R 1.0', 'time': datetime.date(2000, 2, 29)},
    {'source': 'r', 'text': 'R 1.4', 'time': datetime.date(2001, 12, 19)},

    {'source': 'r', 'text': 'R 2.0', 'time': datetime.date(2004, 10, 4)},
    {'source': 'r', 'text': 'R 2.1', 'time': datetime.date(2005, 4, 18)},
    {'source': 'r', 'text': 'R 2.11', 'time': datetime.date(2010, 4, 22)},
    {'source': 'r', 'text': 'R 2.13', 'time': datetime.date(2011, 4, 14)},
    {'source': 'r', 'text': 'R 2.14', 'time': datetime.date(2011, 10, 31)},
    {'source': 'r', 'text': 'R 2.15', 'time': datetime.date(2012, 3, 30)},

    {'source': 'r', 'text': 'R 3.0', 'time': datetime.date(2013, 4, 3)},
    {'source': 'r', 'text': 'R 3.4', 'time': datetime.date(2017, 4, 21)},
    {'source': 'r', 'text': 'R 3.5', 'time': datetime.date(2018, 4, 23)},
]


tl = timeline.TimelineTex(
    [
        {'source': 'today', 'text': 'Today', 'time': datetime.date.today()},
    ]
    + PY_VERSIONS
    + DJANGO_VERSIONS
    + YII_VERSIONS
    # + MARVEL
    # + STARWARS
    # + JQUERY
    + WINDOWS
    + PHP_VERSIONS
    + RUBY_VERSIONS
    + JAVA_VERSIONS
    + JS_VERSIONS
    + ES_VERSIONS
    + R_VERSIONS
    ,
    options={
        # 'direction': 'down',
        'dotColor': bgcolor,
        'labelBgColor': bgcolor,
        'labelTextColor': fgcolor,
        'linkColor': bgcolor,
        'scale': scale.TimeScale(),
        # 'layerGap': 40,
        # 'initialWidth': 2000,
        'initialHeight': 3200,
        'labelPadding': {'left': 0, 'right': 0, 'top': 0, 'bottom': 0},
    },
)
tl.export('python_versions.tex')
