from parser import *


class Wotten:
    def __init__(self, dataframe):
        self.wootten_dict = Parser.wootten
        try:
            self.check = dataframe.copy(deep=True)
            try:
                self.dataframe = dataframe
                k = 0
                if self.dataframe[1].str.contains("B:").any() and self.dataframe[1].str.contains("C:").any():
                    for i in self.dataframe.itertuples():
                        if int(str(i[2]).split(":")[2]) in (self.wootten_dict.keys()) and (i[2]).split(":")[0] == "C":
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2] + " (" + self.wootten_dict[int(str(i[2].split(":")[2]))] + ")"
                        elif int(str(i[2]).split(":")[2]) not in (self.wootten_dict.keys()) and (i[2]).split(":")[0] == "C":
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2] + " (ECD)"
                        else:
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2]
                        k += 1
                if self.dataframe[1].str.contains("B:").any():
                    for i in self.dataframe.itertuples():
                        if int(str(i[2]).split(":")[2]) in (self.wootten_dict.keys()) and (i[2]).split(":")[0] == "B":
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2] + " (" + self.wootten_dict[int(str(i[2].split(":")[2]))] + ")"
                        elif int(str(i[2]).split(":")[2]) not in (self.wootten_dict.keys()) and (i[2]).split(":")[0] == "B":
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2] + " (ECD)"
                        else:
                            self.dataframe.loc[k, [1]] = i[2].split(":")[1] + " " + i[2].split(":")[2]
                        k += 1


                print("\nWoottened DF:")
                print(self.dataframe)
            except:
                print("\nParsed empty dataframe:")
        except:
            print("See warning below:")

    def getExcel(self):
        return self.dataframe
