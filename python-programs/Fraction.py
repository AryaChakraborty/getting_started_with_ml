# created for fraction operations
class Fraction :
    def __init__(self, n, d) :
        self.num = n
        self.deno = d
    
    def __str__(self) : # gets triggered when print() is called
        return "{}/{}".format(self.num, self.deno)
        
    def __add__(self, other) : # gets triggered when + is called
        res_num = self.num*other.deno + other.num*self.deno
        res_deno = self.deno*other.deno
        return "{}/{}".format(res_num, res_deno)
    
    def __sub__(self, other) : # gets triggered when - is called
        res_num = self.num*other.deno - other.num*self.deno
        res_deno = self.deno*other.deno
        return "{}/{}".format(res_num, res_deno)
        
    def __mul__(self, other) : # gets triggered when * is called
        res_num = self.num*other.num
        res_deno = self.deno*other.deno
        return "{}/{}".format(res_num, res_deno)
        
    def __truediv__(self, other) : # gets triggered when / is called
        res_num = self.num*other.deno
        res_deno = self.deno*other.num
        return "{}/{}".format(res_num, res_deno)    
        
x = Fraction(1, 2)
y = Fraction(1, 3)
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
