import sys, os, pathlib

cwd = os.getcwd()
script_dir = os.path.dirname(__file__)

pathVDW = "vdw_resfrequencies.tsv"
pathSS = "hbss_resfrequencies.tsv"
pathSB = "hbsb_resfrequencies.tsv"

VDW_abs_file_path = os.path.join(script_dir, pathVDW)
SS_abs_file_path = os.path.join(script_dir, pathSS)
SB_abs_file_path = os.path.join(script_dir, pathSB)

from wotten import *


def main():
    parser = Parser()

    vdw = parser.readVDW(VDW_abs_file_path)
    hbss = parser.readHBSS(SS_abs_file_path)
    hbsb = parser.readHBSB(SB_abs_file_path)

    wottenvdw = Wotten(vdw)
    wottenls = Wotten(hbss)
    wottensb = Wotten(hbsb)
    path = pathlib.PurePath(cwd)

    try:
        wottenvdw.getExcel().to_excel(str(path.parent.name) + "_vdw.xls")
    except:
        print("vdW table is empty. Check the tsv file.")
    try:
        wottenls.getExcel().to_excel(str(path.parent.name) + "_ls.xls")
    except:
        print("HBLS table is empty. Check the tsv file.")
    try:
        wottensb.getExcel().to_excel(str(path.parent.name) + "_sb.xls")
    except:
        print("HBSB table is empty. Check the tsv file.")


if __name__ == '__main__':
    main()
