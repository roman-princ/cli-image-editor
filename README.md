# Grafický CLI Editor
Tento projekt je jednoduchý grafický editor ovládaný z příkazové řádky (CLI), který umožňuje provádět různé základní grafické operace na obrázcích.
## Funkce
Editor podporuje následující operace:
- `--mirror`: Zrcadlí obrázek horizontálně.
- `--lighten <0-100>`: Zesvětluje obrázek o zadané procento.
- `--darken <0-100>`: Ztmavuje obrázek o zadané procento.
- `--inverse`: Vytváří inverzní obraz (negativ).
- `--bw`: Konvertuje obrázek do odstínů šedi.
- `--sharpen`: Aplikuje na obrázek vyostřovací filtr.
- `--blur`: Aplikuje na obrázek rozostřovací filtr.
- `--ed`: Aplikuje Sobel–Feldmanův filtr pro detekci hran.
- `--rc`: Aplikuje Robertsův křížový filtr.
- `--rotate [90, 180, 270]`: Otočí obrázek o 90, 180 nebo 270 stupňů doprava.

## Instalace
* Naklonujte si repozitář pomocí SSH nebo HTTPS protokolu
    * SSH: `git@gitlab.fit.cvut.cz:BI-PYT/B232/princrom.git`
    * HTTPS: `https://gitlab.fit.cvut.cz/BI-PYT/B232/princrom.git`
* Přesuňte se do adresáře projektu 
    * `cd editor`
* Vytvořte a aktivujte virtuální prostředí
    * `python3 -m venv venv `
    * `source venv/bin/activate`
* Nainstalujte závislosti
    * `pip install -r requirements.txt`

## Použití
Spusťte program pomocí příkazové řádky s požadovanými parametry:  
* `python main.py [OPERACE] INPUT_IMAGE_PATH OUTPUT_IMAGE_PATH`

### Příklady příkazů

* Rotace obrázku o 90 stupňů doprava:
    * `python main.py --rotate 90 input.jpg output.jpg`
* Převod obrázku do odstínů šedi a jeho zesvětlení o 25 %:
    * `python main.py --bw --lighten 25 input.jpg output.jpg`
* Aplikace vyostřovacího filtru a následné ztmavení o 10 %:
    * `python main.py --sharpen --darken 10 input.jpg output.jpg`

## Testování
Pro spuštění testů použijte přikaz `pytest`.

## Autor
Roman Princ, ČVUT-FIT, princrom@fit.cvut.cz
