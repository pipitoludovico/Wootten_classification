import argparse
import sys

from parser import *

ap = argparse.ArgumentParser()
ap.add_argument('-r', '--receptor', nargs='*', required=True,
                help=' use -r and add all the chain IDs that belong to the receptor e.g. -r A B C D E F')
ap.add_argument('-l', '--ligand', nargs='*', required=True,
                help='use -l and add all the chain IDs that belong to the ligand e.g. -l G')
args = ap.parse_args()


class Wotten:
    def __init__(self, dataframe):
        self.wootten_dict = Parser.wootten
        self.check = dataframe.copy(deep=True)
        if sys.argv is not None:
            try:
                self.dataframe = dataframe
                for idx, row in enumerate(self.dataframe.iterrows()):
                    chainID_0 = self.dataframe.loc[idx].str.split(':')[0][0]
                    resname_0 = self.dataframe.loc[idx].str.split(':')[0][1]
                    resnum_0 = int(self.dataframe.loc[idx].str.split(':')[0][2])

                    chainID_1 = self.dataframe.loc[idx].str.split(':')[1][0]
                    resname_1 = self.dataframe.loc[idx].str.split(':')[1][1]
                    resnum_1 = int(self.dataframe.loc[idx].str.split(':')[1][2])
                    if chainID_0 in args.receptor:
                        if resnum_0 in self.wootten_dict.keys():
                            self.dataframe.loc[idx, [0]] = resname_0 + " " + str(resnum_0) + " " + self.wootten_dict[
                                resnum_0]
                        elif resnum_0 not in self.wootten_dict.keys():
                            self.dataframe.loc[idx, [0]] = resname_0 + " " + str(resnum_0) + " REC"
                    if chainID_0 in args.ligand:
                        self.dataframe.loc[idx, [1]] = resname_1 + " " + str(resnum_1) + " LIG"
                    if chainID_1 in args.ligand:
                        self.dataframe.loc[idx, [1]] = resname_1 + " " + str(resnum_1) + " LIG"
                print(self.dataframe)
            except:
                print("Empy dataframe, check that your chain selection was set properly")

    def getExcel(self):
        return self.dataframe
