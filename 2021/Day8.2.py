#fp = open('Input8.sample')
fp = open('Input8.txt')

class Output:
    output = {}
    outputDisp = [0,0,0,0,0,0,0,0,0,0]

    def __init__(self, wirings):
        self.output = {}
        self.outputDisp = [0,0,0,0,0,0,0,0,0,0]
        for wiring in wirings.split(' '):
            wiring = ''.join(sorted(wiring))
            if len(wiring) == 2:
                self.output[wiring] = [1]
                self.outputDisp[1] = wiring
            if len(wiring) == 3:
                self.output[wiring] = [7]
                self.outputDisp[7] = wiring
            if len(wiring) == 4:
                self.output[wiring] = [4]
                self.outputDisp[4] = wiring
            if len(wiring) == 5:
                self.output[wiring] = [2,3,5]
            if len(wiring) == 6:
                self.output[wiring] = [0,6,9]
            if len(wiring) == 7:
                self.output[wiring] = [8]
                self.outputDisp[8] = wiring

        # Find 3, 1 is a subset
        for key in self.output.keys():
            if len(key) == 5 and 0 not in [c in key for c in self.outputDisp[1]]:
                self.output[key] = [3]
                self.outputDisp[3] = key
        for key in self.output.keys():
            if len(key) == 5 and key != self.outputDisp[3]:
                self.output[key] = [2,5]

        # Find 6, 1 is not a sub set
        for key in self.output.keys():
            if len(key) == 6 and 0 in [c in key for c in self.outputDisp[1]]:
                print('Found 6')
                self.output[key] = [6]
                self.outputDisp[6] = key
        for key in self.output.keys():
            if len(key) == 6 and key != self.outputDisp[6]:
                self.output[key] = [0,9]

        # Find 5, a subset of 6, and also now 2
        for key in self.output.keys():
            if len(key) == 5 and 0 not in [c in self.outputDisp[6] for c in key]:
                print('Found 5')
                self.output[key] = [5]
                self.outputDisp[5] = key
        for key in self.output.keys():
            if len(key) == 5 and key != self.outputDisp[3] and key != self.outputDisp[5]:
                print('Found 2')
                self.output[key] = [2]

        # Find 9, 5 is a sub set, and also no 0
        for key in self.output.keys():
            if len(key) == 6 and key != self.outputDisp[6] and 0 not in [c in key for c in self.outputDisp[5]]:
                print('Found 9')
                self.output[key] = [9]
                self.outputDisp[9] = key
        for key in self.output.keys():
            if len(key) == 6 and key != self.outputDisp[6] and key != self.outputDisp[9]:
                print('Found 0')
                self.output[key] = [0]

    def calcValue(self, outputs):
        digits = ''
        for digit in outputs.split(' '):
            digit = ''.join(sorted(digit))
            digits += str(self.output[digit][0])
        print(int(digits))
        return int(digits)


            
sum = 0
for line in fp.readlines():
    #line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
    wirings, outputs = line.strip().split(' | ')
    print(wirings)
    disp = Output(wirings)
    print(disp.output)
    
    #print(disp.outputDisp)
    #print(disp.output)
    sum += disp.calcValue(outputs)
    print()

print(sum)
