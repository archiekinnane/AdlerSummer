from astropy.table import Table, Column

archie = Table(names = ('ra', 'dec'))


def spellTime(phrase, filename, topleft_word_ra = 40, letterwidth = 6, topleft_word_dec = 45, letterheight = 4):
    from data2ops import files2ops
    #archie.remove_rows(slice(0, len(archie)))
    #archie.keep_columns([])
    #archie = Table(names = ('ra', 'dec'))
    phrase = phrase.upper()
    for i in range(0, len(phrase)):
        if phrase[i] == 'A':
            makeA(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'B':
            makeB(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'C':
            makeC(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'D':
            makeD(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'E':
            makeE(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'F':
            makeF(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'G':
            makeG(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'H':
            makeH(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'I':
            makeI(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'J':
            makeJ(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'K':
            makeK(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'L':
            makeL(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'M':
            makeM(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'N':
            makeN(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'O':
            makeO(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'P':
            makeP(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'Q':
            makeQ(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'R':
            makeR(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'S':
            makeS(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'T':
            makeT(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'U':
            makeU(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'W':
            makeW(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'X':
            makeX(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'Y':
            makeY(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == 'Z':
            makeZ(topleft_word_ra - i*letterwidth, topleft_word_dec, letterwidth - 1, letterheight)
        elif phrase[i] == ' ':
            good = 1
        else:
            print('letter skipped')
    files2ops.createFiles(archie, filename, filename ,'/Universe/other', 'spellTime')

numb = 30

def addVertLine(ra, start_dec, finish_dec):
    dec = start_dec
    for i in range(0,numb):
        archie.add_row([ra, dec])
        dec = dec + abs(finish_dec - start_dec)/numb
def addHorLine(start_ra, finish_ra, dec):
    ra = start_ra
    for i in range(0,numb):
        archie.add_row([ra, dec])
        ra = ra + abs(finish_ra - start_ra)/numb
def addDiagLine(start_ra, finish_ra, start_dec, finish_dec):
    ra = start_ra
    dec = start_dec
    if start_ra < finish_ra:
        if start_dec < finish_dec:
            for i in range(0,numb):
                archie.add_row([ra, dec])
                dec = dec + abs(finish_dec - start_dec)/numb
                ra = ra + abs(finish_ra - start_ra)/numb
        elif start_dec > finish_dec:
            for i in range(0,numb):
                archie.add_row([ra, dec])
                dec = dec - abs(finish_dec - start_dec)/numb
                ra = ra + abs(finish_ra - start_ra)/numb
    elif start_ra > finish_ra:
        if start_dec < finish_dec:
            for i in range(0,numb):
                archie.add_row([ra, dec])
                dec = dec + abs(finish_dec - start_dec)/numb
                ra = ra - abs(finish_ra - start_ra)/numb
        elif start_dec > finish_dec:
            for i in range(0,numb):
                archie.add_row([ra, dec])
                dec = dec - abs(finish_dec - start_dec)/numb
                ra = ra - abs(finish_ra - start_ra)/numb

def makeC(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
def makeB(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    makeO(topleft_ra + width/4, topleft_dec, 0.75*width, height/2)
    makeO(topleft_ra + width/4, topleft_dec - height/2, 0.75*width, height/2)
def makeF(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra + 0.2*width, topleft_ra + width, topleft_dec - height/2)
def makeG(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec - height/2)
    addHorLine(topleft_ra + 0.2*width, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width/2, topleft_dec - height/2)
def makeH(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height/2)
def makeI(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width/2, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra + 0.25*width, topleft_ra + 0.75*width, topleft_dec)
    addVertLine(topleft_ra + width/2, topleft_dec - height, topleft_dec - height)
    addHorLine(topleft_ra + 0.25*width, topleft_ra + 0.75*width, topleft_dec - height)
def makeJ(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width/2, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra + width/2, topleft_ra + width, topleft_dec - height)
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec - 0.67*height)
def makeK(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra, topleft_ra + width, topleft_dec, topleft_dec - height/2)
    addDiagLine(topleft_ra, topleft_ra + width, topleft_dec - height, topleft_dec - height/2)
def makeL(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
def makeM(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra, topleft_ra + width/2, topleft_dec, topleft_dec - height/2)
    addDiagLine(topleft_ra + width/2, topleft_ra + width, topleft_dec -height/2, topleft_dec)
def makeN(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra + width, topleft_ra, topleft_dec, topleft_dec - height)
def makeQ(topleft_ra, topleft_dec, width, height):
    makeO(topleft_ra, topleft_dec, width, height)
    addDiagLine(topleft_ra + width/4, topleft_ra - width/4, topleft_dec - 0.75*height, topleft_dec - 1.25*height)
def makeS(topleft_ra, topleft_dec, width, height):
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height/2)
    addVertLine(topleft_ra + width, topleft_dec - height/2, topleft_dec)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec - height/2)
def makeV(topleft_ra, topleft_dec, width, height):
    addDiagLine(topleft_ra + width, topleft_ra + width/2, topleft_dec, topleft_dec - height)
    addDiagLine(topleft_ra, topleft_ra + width/2, topleft_dec, topleft_dec - height)
def makeW(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra, topleft_ra + width/2, topleft_dec - height, topleft_dec - height/2)
    addDiagLine(topleft_ra + width/2, topleft_ra + width, topleft_dec -height/2, topleft_dec - height)
def makeX(topleft_ra, topleft_dec, width, height):
    addDiagLine(topleft_ra + width, topleft_ra, topleft_dec, topleft_dec - height)
    addDiagLine(topleft_ra, topleft_ra + width, topleft_dec, topleft_dec - height)
def makeZ(topleft_ra, topleft_dec, width, height):
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
    addDiagLine(topleft_ra, topleft_ra + width, topleft_dec, topleft_dec - height)
def makeY(topleft_ra, topleft_dec, width, height):
    addDiagLine(topleft_ra, topleft_ra + width/2, topleft_dec, topleft_dec - height/2)
    addDiagLine(topleft_ra + width/2, topleft_ra + width, topleft_dec -height/2, topleft_dec)
    addVertLine(topleft_ra + width/2, topleft_dec - height, topleft_dec - height/2)
def makeO(topleft_ra, topleft_dec, width, height):
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
def makeU(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra, topleft_dec - height, topleft_dec)
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
def makeR(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra, topleft_ra + width, topleft_dec - height, topleft_dec - height/2)
    makeO(topleft_ra + width/3, topleft_dec, width/1.5, height/2)
def makeE(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec - height)
    addHorLine(topleft_ra + 0.2*width, topleft_ra + width, topleft_dec - height/2)
def makeA(topleft_ra, topleft_dec, width, height):
    addDiagLine(topleft_ra + width/2, topleft_ra + width, topleft_dec, topleft_dec - height)
    addDiagLine(topleft_ra + width/2, topleft_ra, topleft_dec, topleft_dec - height)
    addHorLine(topleft_ra + 0.2*width, topleft_ra + 0.8*width, topleft_dec - height/2)
def makeD(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    addDiagLine(topleft_ra + width, topleft_ra + 0.2*width, topleft_dec, topleft_dec - height/2)
    addDiagLine(topleft_ra + width, topleft_ra + 0.2*width, topleft_dec - height, topleft_dec - height/2)
def makeP(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width, topleft_dec - height, topleft_dec)
    makeO(topleft_ra + width/4, topleft_dec, 0.75*width, height/2)
def makeT(topleft_ra, topleft_dec, width, height):
    addVertLine(topleft_ra + width/2, topleft_dec - height, topleft_dec)
    addHorLine(topleft_ra, topleft_ra + width, topleft_dec)
def addApo(topleft_ra, topleft_dec,height):
    addVertLine(topleft_ra, topleft_dec - 0.5, topleft_dec)