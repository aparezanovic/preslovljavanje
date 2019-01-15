# -*- encoding: utf-8 -*-

#Preslovljavanje , Transliterator - ćirilica / latinica

azbuka = ['lj', 'nj', 'dž', 'a', 'b', 'v', 'g', 'd', 'đ', 'e', 'ž', 'z', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'r', 's', 't', 'ć', 'u', 'f', 'h', 'c', 'č', 'š', 'LJ', 'NJ', 'DŽ', 'A', 'B',
        'V', 'G', 'D', 'Đ', 'E', 'Ž', 'Z', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'R', 'S', 'T', 'Ć', 'U', 'F', 'H', 'C', 'Č', 'Š']
latini = ['љ', 'њ', 'џ', 'а', 'б', 'в', 'г', 'д', 'ђ', 'е', 'ж', 'з', 'и', 'ј', 'к', 'л',  'м', 'н',
          'о', 'п', 'р', 'с', 'т', 'ћ', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'Љ', 'Њ', 'Џ', 'А', 'Б',
          'В', 'Г', 'Д', 'Ђ', 'Е', 'Ж', 'З', 'И', 'Ј', 'K', 'Л', 'М', 'Н', 'О',
          'П', 'Р', 'С', 'Т', 'Ћ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш']
recnik = dict(zip(azbuka, latini))

def cir(tekst):
    for cir, lat in recnik.items():
        tekst = tekst.replace(cir, lat)
    return tekst

def lat(tekst):
    for cir, lat in recnik.items():
        tekst = tekst.replace(lat, cir)
    return(tekst)
