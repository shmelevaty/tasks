class Kassa:
    s=34567 
    def top_up(self, x):
        self.x=x
        x+=Kassa.s
        return f"в кассе {x}"
    def count_1000(self):
        print(Kassa.s//1000)
    def take_away(self, x):
        if x<=self.s:
            self.s-=x
            print("выполнена операция по счету")
        else:
            return f"недостаточно денег"

h=Kassa()
print(h.s)
print(h.top_up(125))
h.count_1000()
h.take_away(1000)
print(h.s)
