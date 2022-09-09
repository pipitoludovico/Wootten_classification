from parser import *


class Wotten:
    def __init__(self, dataframe):
        self.lista = []
        self.wootten_dict = Parser.wootten
        try:
            self.check = dataframe.copy(deep=True)
            if int(self.check[1].str.extract('(\d+)').max()) >= 36:
                try:
                    self.dataframe = dataframe
                    k = 0
                    for i in self.dataframe.itertuples():
                        if int(str(i[2]).split(":")[1]) in (self.wootten_dict.keys()):
                            self.dataframe.loc[k, [1]] = i[2] + " (" + self.wootten_dict[
                                int(str(i[2].split(":")[1]))] + ")"
                        else:
                            self.dataframe.loc[k, [1]] = i[2] + " (ECD)"
                        k += 1
                    print("\nWoottened DF:")
                    print(self.dataframe)
                except:
                    print("\nParsed empty dataframe:")
            else:
                try:
                    self.dataframe = dataframe
                    k = 0
                    for i in self.dataframe.itertuples():
                        if int(str(i[2]).split(":")[1]) in (self.wootten_dict.keys()):
                            self.dataframe.loc[k, [1]] = i[2] + " (" + self.wootten_dict[
                                int(str(i[2].split(":")[1]))] + ")"
                        else:
                            self.dataframe.loc[k, [1]] = i[2] + " (ECD)"
                        k += 1
                    print("\nWoottened DF:")
                    print(self.dataframe)
                except:
                    print("\nParsed empty dataframe:")
                    print("")
        except:
            print("See warning below:")

    def getExcel(self):
        return self.dataframe
