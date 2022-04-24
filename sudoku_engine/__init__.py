#from email import iterators
import enum

class ItemsShowOption(enum.Enum):
    ShowAll = 1,
    EmptyOnly = 2
    SkipEmpty = 3

class SudokuBoard():
    def __init__(self):
        self.board_fen = "1ee24eeee/24e8e59e3/eee7e12e4/4e9158ee6/7e1ee9e4e/526eeee9e/e125eeeee/eeee37162/6eeeee5e8"
    def __init__(self, FEN):
        self.board_fen = FEN
        
    def Show(self):
        lines = self.board_fen.split('/')
        line_index=0
        for line in lines:
            newline = line.replace('e',' ')
            if line_index%3==0:
                print('|---+---+---|')
            print("|"+newline[0:3]+"|"+newline[3:6]+"|"+newline[6:9]+"|")
            line_index=line_index+1
        print('|---+---+---|')

    def calculate_box(self,ROW, COL):
        output = 0
        if 1<= ROW <=3 and 1<= COL <=3: 
            output = 1
        elif 1<= ROW <=3 and 4<= COL <=6: 
            output = 2
        elif 1<= ROW <=3 and 7<= COL <=9: 
            output = 3
        elif 4<= ROW <=6 and 1<= COL <=3: 
            output = 4
        elif 4<= ROW <=6 and 4<= COL <=6: 
            output = 5
        elif 4<= ROW <=6 and 7<= COL <=9: 
            output = 6
        elif 7<= ROW <=9 and 1<= COL <=3: 
            output = 7
        elif 7<= ROW <=9 and 4<= COL <=6: 
            output = 8
        elif 7<= ROW <=9 and 7<= COL <=9: 
            output = 9
        else:
            output = 0
        return output
    def items(self, showoption=ItemsShowOption.ShowAll):
        output = []
        tmp = self.board_fen.split("/")
        for i in range(81):
            row = (i // 9)
            column = (i % 9)
            value = (tmp[row])[column]
            if value=='e' and showoption==ItemsShowOption.SkipEmpty:
                next
            elif value!='e' and showoption==ItemsShowOption.EmptyOnly:
                next
            else:
                box = self.calculate_box(row+1, column+1)
                output.append({'val':value, 'row':row+1, 'col':column+1, 'box':box})
        return output

    def row(self, ROW, showoption=ItemsShowOption.ShowAll):
        output = []
        for item in self.items(showoption):
            if item['row'] == ROW:
                output.append(item)
        return output

    def column(self, COLUMN, showoption=ItemsShowOption.ShowAll):
        output = []
        for item in self.items(showoption):
            #print(item)
            if item['col'] == COLUMN:
                output.append(item)
        return output


    def box(self, BOX, showoption=ItemsShowOption.ShowAll):
        output = []
        for item in self.items(showoption):
            #print(item)
            if item['box'] == BOX:
                output.append(item)
        return output

    def allValidDigits(self, ROW, COL):
        column_digits = set({ x['val'] for x in self.column(COL, showoption=ItemsShowOption.SkipEmpty) })
        row_digits = set({ x['val'] for x in self.row(ROW, showoption=ItemsShowOption.SkipEmpty) })
        BOX = self.calculate_box(ROW,COL)
        box_digits = set({ x['val'] for x in self.box(BOX, showoption=ItemsShowOption.SkipEmpty) })
        output = []
        for x in set({'1','2','3','4','5','6','7','8','9'}).difference(column_digits | row_digits | box_digits):
            output.append({'val': str(x), 'row': ROW, 'col': COL, 'box': BOX})
        return output

    def setDigit(self, ROW, COL, val):
        BOX = self.calculate_box(ROW,COL)
        if {'val':str(val), 'row':ROW, 'col':COL, 'box':BOX } in  self.allValidDigits(ROW, COL):
            index = 10*(ROW-1)+(COL-1)          
            new_fen = self.board_fen[0:index] + f'{val}' + self.board_fen[index+1:]
            self.board_fen = new_fen
            return {'val':str(val), 'row':ROW, 'col':COL, 'box':BOX }
        else:
            raise ValueError(f"You cannot put {val} into ({ROW},{COL})")