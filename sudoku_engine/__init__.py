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

    def items(self, showoption=ItemsShowOption.ShowAll):
        output = []
        tmp = self.board_fen.split("/")
        for i in range(81):
            row = i // 9
            column = i % 9
            value = (tmp[row])[column]

            if value=='e' and showoption==ItemsShowOption.SkipEmpty:
                next
            elif value!='e' and showoption==ItemsShowOption.EmptyOnly:
                next
            else:
                if 0<= row <=2 and 0<= column <=2: 
                    box = 1
                elif 0<= row <=2 and 3<= column <=5: 
                    box = 2
                elif 0<= row <=2 and 6<= column <=8: 
                    box = 3
                elif 3<= row <=5 and 0<= column <=2: 
                    box = 4
                elif 3<= row <=5 and 3<= column <=5: 
                    box = 5
                elif 3<= row <=5 and 6<= column <=8: 
                    box = 6
                elif 6<= row <=8 and 0<= column <=2: 
                    box = 7
                elif 6<= row <=8 and 3<= column <=5: 
                    box = 8
                elif 6<= row <=8 and 6<= column <=8: 
                    box = 9
                else:
                    0
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

