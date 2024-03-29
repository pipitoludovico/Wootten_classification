import os
import pathlib

from wotten import *

cwd = os.getcwd()
script_dir = os.path.dirname(__file__)

os.system("tr -s ' ' < vdw_resfrequencies.tsv | tr '\t' ' ' > vdw.tsv")
os.system("sed -i 's/HSP/HIS/g' vdw.tsv")
os.system("sed -i 's/HSE/HIS/g' vdw.tsv")
os.system("sed -i 's/HSD/HIS/g' vdw.tsv")

os.system("tr -s ' ' < hbss_resfrequencies.tsv | tr '\t' ' ' > ss.tsv")
os.system("sed -i 's/HSP/HIS/g' ss.tsv")
os.system("sed -i 's/HSE/HIS/g' ss.tsv")
os.system("sed -i 's/HSD/HIS/g' ss.tsv")

os.system("tr -s ' ' < hbsb_resfrequencies.tsv | tr '\t' ' ' > sb.tsv")
os.system("sed -i 's/HSP/HIS/g' sb.tsv")
os.system("sed -i 's/HSE/HIS/g' sb.tsv")
os.system("sed -i 's/HSD/HIS/g' sb.tsv")

pathVDW = "vdw.tsv"
pathSS = "ss.tsv"
pathSB = "sb.tsv"

VDW_abs_file_path = os.path.join(script_dir, pathVDW)
SS_abs_file_path = os.path.join(script_dir, pathSS)
SB_abs_file_path = os.path.join(script_dir, pathSB)


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
