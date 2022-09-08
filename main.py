import sys, os, pathlib

cwd = os.getcwd()

from wotten import *


def main():
    parser = Parser()

    vdw = parser.readVDW(sys.argv[1])
    hbls = parser.readHBLS(sys.argv[2])
    hbsb = parser.readHBSB(sys.argv[3])

    wottenvdw = Wotten(vdw)
    wottenls = Wotten(hbls)
    wottensb = Wotten(hbsb)
    path = pathlib.PurePath(cwd)

    try:
        wottenvdw.getExcel().to_excel(str(path.parent.name)+"_vdw.xls")
    except:
        print("vdW table is empty. Check the tsv file.")
    try:
        wottenls.getExcel().to_excel(str(path.parent.name)+"_ls.xls")
    except:
        print("HBLS table is empty. Check the tsv file.")
    try:
        wottensb.getExcel().to_excel(str(path.parent.name)+"_sb.xls")
    except:
        print("HBSB table is empty. Check the tsv file.")


if __name__ == '__main__':
    main()
