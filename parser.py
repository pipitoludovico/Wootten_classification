import pandas as pd


class Parser:
    wootten = {138: '1.33', 139: '1.34', 140: '1.35', 141: '1.36', 142: '1.37', 143: '1.38', 144: '1.39',
               145: '1.40', 146: '1.41', 147: '1.42', 148: '1.43', 149: '1.44', 150: '1.45', 151: '1.46',
               152: '1.47', 153: '1.48', 154: '1.49', 155: '1.50', 156: '1.51', 157: '1.52', 158: '1.53',
               159: '1.54', 160: '1.55', 161: '1.56', 162: '1.57', 163: '1.58', 164: '1.59', 165: '1.60',
               166: '1.61', 167: '1.62', 168: '1.63', 169: '1.64', 170: 'ICL1', 171: 'ICL1', 172: 'ICL1',
               173: 'ICL1', 174: '2.44', 175: '2.45', 176: '2.46', 177: '2.47', 178: '2.48', 179: '2.49',
               180: '2.50', 181: '2.51', 182: '2.52', 183: '2.53', 184: '2.54', 185: '2.55', 186: '2.56',
               187: '2.57', 188: '2.58', 189: '2.59', 190: '2.60', 191: '2.61', 192: '2.62', 193: '2.63',
               194: '2.64', 195: '2.65', 196: '2.66', 197: '2.67', 198: '2.68', 199: '2.69', 200: '2.70',
               201: '2.71', 202: 'ECL1', 203: 'ECL1', 204: 'ECL1', 205: 'ECL1', 206: 'ECL1', 207: 'ECL1',
               208: 'ECL1', 209: 'ECL1', 210: 'ECL1', 211: 'ECL1', 212: 'ECL1', 213: 'ECL1', 214: 'ECL1',
               215: 'ECL1', 216: 'ECL1', 217: 'ECL1', 218: 'ECL1', 219: 'ECL1', 220: 'ECL1', 221: 'ECL1',
               222: 'ECL1', 223: 'ECL1', 224: '3.27', 225: '3.28', 226: '3.29', 227: '3.30', 228: '3.31',
               229: '3.32', 230: '3.33', 231: '3.34', 232: '3.35', 233: '3.36', 234: '3.37', 235: '3.38',
               236: '3.39', 237: '3.40', 238: '3.41', 239: '3.42', 240: '3.43', 241: '3.44', 242: '3.45',
               243: '3.46', 244: '3.47', 245: '3.48', 246: '3.49', 247: '3.50', 248: '3.51', 249: '3.52',
               250: '3.53', 251: '3.54', 252: '3.55', 253: '3.56', 254: '3.57', 255: '3.58', 256: '3.59',
               257: '3.60', 258: 'ICL2', 259: 'ICL2', 260: 'ICL2', 261: 'ICL2', 262: '4.38', 263: '4.39',
               264: '4.40', 265: '4.41', 266: '4.42', 267: '4.43', 268: '4.44', 269: '4.45', 270: '4.46',
               271: '4.47', 272: '4.48', 273: '4.49', 274: '4.50', 275: '4.51', 276: '4.52', 277: '4.53',
               278: '4.54', 279: '4.55', 280: '4.56', 281: '4.57', 282: '4.58', 283: '4.59', 284: '4.60',
               285: '4.61', 286: '4.62', 287: '4.63', 288: '4.64', 289: '4.65', 290: '4.66', 291: '4.67',
               292: '4.68', 293: 'ECL2', 294: 'ECL2', 295: 'ECL2', 296: 'ECL2', 297: 'ECL2', 298: 'ECL2',
               299: 'ECL2', 300: 'ECL2', 301: 'ECL2', 302: '5.32', 303: '5.33', 304: '5.34', 305: '5.35',
               306: '5.36', 307: '5.37', 308: '5.38', 309: '5.39', 310: '5.40', 311: '5.41', 312: '5.42',
               313: '5.43', 314: '5.44', 315: '5.45', 316: '5.46', 317: '5.47', 318: '5.48', 319: '5.49',
               320: '5.50', 321: '5.51', 322: '5.52', 323: '5.53', 324: '5.54', 325: '5.55', 326: '5.56',
               327: '5.57', 328: '5.58', 329: '5.59', 330: '5.60', 331: '5.61', 332: '5.62', 333: '5.63',
               334: '5.64', 335: '5.65', 336: '5.66', 337: '5.67', 338: '5.68', 339: '5.69', 340: 'ICL3',
               341: '6.30', 342: '6.31', 343: '6.32', 344: '6.33', 345: '6.34', 346: '6.35', 347: '6.36',
               348: '6.37', 349: '6.38', 350: '6.39', 351: '6.40', 352: '6.41', 353: '6.42', 354: '6.43',
               355: '6.44', 356: '6.45', 357: '6.46', 358: '6.47', 359: '6.48', 360: '6.49', 361: '6.50',
               362: '6.51', 363: '6.52', 364: '6.53', 365: '6.54', 366: '6.55', 367: '6.56', 368: '6.57',
               369: '6.58', 370: '6.59', 371: '6.60', 372: 'ECL3', 373: 'ECL3', 374: 'ECL3', 375: 'ECL3',
               376: 'ECL3', 377: '7.32', 378: '7.33', 379: '7.34', 380: '7.35', 381: '7.36', 382: '7.37',
               383: '7.38', 384: '7.39', 385: '7.40', 386: '7.41', 387: '7.42', 388: '7.43', 389: '7.44',
               390: '7.45', 391: '7.46', 392: '7.47', 393: '7.48', 394: '7.49', 395: '7.50', 396: '7.51',
               397: '7.52', 398: '7.53', 399: '7.54', 400: '7.55', 401: '7.56', 402: '7.57', 403: '7.58',
               404: '7.59', 405: '7.60', 406: '8.47', 407: '8.48', 408: '8.49', 409: '8.50', 410: '8.51',
               411: '8.52', 412: '8.53', 413: '8.54', 414: '8.55', 415: '8.56', 416: '8.57', 417: '8.58',
               418: '8.59', 419: '8.60', 420: '8.61', 421: '8.62', 422: '8.63', 423: '8.64', 424: '8.65',
               425: '8.66', 426: '8.67', 427: '8.68', 428: '8.69', 429: '8.70', 430: '8.71', 431: '8.72'}

    def __init__(self):

        self.file = None
        self.dataframe = None

    def readVDW(self, file=None):
        try:
            self.dataframe = pd.read_csv(file, sep=" ", comment='#', header=None)
            self.dataframe[2] = self.dataframe[2].apply(lambda x: x * 100)

            self.dataframe = self.dataframe[self.dataframe[2] > 35]
            self.dataframe.reset_index(drop=True, inplace=True)
            self.dataframe.sort_values(by=[1])
            print("VDW DF:")
            print(self.dataframe)
            return self.dataframe

        except:
            print("\nvdW table is empty")

    def readHBSS(self, file=None):
        try:
            self.dataframe = pd.read_csv(file, sep=" ", comment="#", header=None)
            self.dataframe[2] = self.dataframe[2].apply(lambda x: x * 100)

            self.dataframe = self.dataframe[self.dataframe[2] > 15]
            self.dataframe.reset_index(drop=True, inplace=True)
            self.dataframe.sort_values(by=[1])
            print("HBSS DF:")
            print(self.dataframe)
            return self.dataframe

        except:
            print("\nHB-LS table is empty")

    def readHBSB(self, file=None):
        try:
            self.dataframe = pd.read_csv(file, sep=" ", comment="#", header=None)
            self.dataframe[2] = self.dataframe[2].apply(lambda x: x * 100)
            self.dataframe = self.dataframe[self.dataframe[2] > 15]
            self.dataframe.reset_index(drop=True, inplace=True)
            self.dataframe.sort_values(by=[1])
            print("HBSB DF:")
            print(self.dataframe)
            return self.dataframe

        except:
            print("\nHB-SB table is empty")
