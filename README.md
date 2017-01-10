# Jiří Šebele: Semestrální práce pro BI-PYT

Tento repozitář obsahuje kód pro semestrální práci na předmět BI-PYT v zimním semestru roku 2016/2017.

## Zadání

Body za semestrální práci tvoří druhou třetinu bodů do známky. Narozdíl od domácích úkolů jde o přidělení bodů metodou „všechno nebo nic“. Podmínkou nutnou (nikoli dostačující :-) je zpracování práce pomocí nějakého systému pro distribuovanou správu verzí (git, mercurial…)!

Výstupem semestrální práce bude aplikace napsaná v Python'u, která dokáže načíst vstupní obrázek a na něm provádět vybrané základní grafické operace:

 * inverzní obraz;
 * převod do odstínů šedi;
 * zesvětlení/ztmavení;
 * zvýraznění hran.

Co se aplikace týká, může to být buď klasické GUI (tkinter není podmínkou, klidně si to pište třeba v Qtéčku), v kterémžto případě očekávám u prováděných operací vizuální odezvu nad zpracovávaným obrázkem, nebo konzolová aplikace, v kterémžto případě zase musí obsahovat velmi podrobnou nápovědu, jak se má používat (což se naštěstí v Python'u píše zrovna docela snadno).

*(citováno z http://vyuka.ookami.cz/@CVUT_2016+17-ZS_BI-PYT/)*

## Použití aplikace

Práce je realizována formou CLI aplikace pomocí knihovny [Click](http://click.pocoo.org/). Obrazové operace jsou zajištěny knihovnou [Pillow](https://pillow.readthedocs.io/). Aplikace obsahuje návod k použití, nevyžaduje proto separátní manuál. Jednotlivé podpříkazy jsou dokumentovány také.

```
$ ./main.py

Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Function stub that acts as a group for all image commands the application
  supports.

Options:
  --help  Show this message and exit.

Commands:
  brightness  Increase / decrease image brightness
  edges       Edge detection filter
  greyscale   Color removal
  invert      Color inversion
```
