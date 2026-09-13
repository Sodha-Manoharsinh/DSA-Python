class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self,x):
        if self.top >= self.size-1 :
            print("Stack Overflow")
            return
        self.top += 1
        self.stack.append(x)

    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return
        self.top -= 1
        x = self.stack.pop()
        return x

    def peep(self,i):
        if self.top < 0:
            print("Stack Underflow")
            return
        
        position = self.top - i + 1

        if position<0 or position>self.top:
            print("Invalid Value")
            return

        x = self.stack[position]
        return x

    def change(self,i,x):
        if self.top < 0:
            print("Stack Underflow")
            return
        
        position = self.top - i + 1

        if position<0 or position>self.top:
            print("Invalid Value")
            return
        
        self.stack[position] = x

    def display(self):
        if self.top < 0:
            print("Stack Underflow")
            return
        for i in range(self.top,0,-1):
            print(self.stack[i],end=" ")
        print(self.stack[0])

    def displayAsStack(self):
        if self.top < 0:
            width = 6  
        else:
            width = max(len(str(item)) for item in self.stack) + 4

        for i in range(self.size-1,-1,-1):
            # center() centers the text and pads the rest with spaces
            try:
                print(f"|{str(self.stack[i]).center(width)}|")
            except:
                print(f"|{' '.center(width)}|")

        # Print a solid bottom base for the container
        print("=" * (width + 2))

    def isEmpty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    print("Hello World")

