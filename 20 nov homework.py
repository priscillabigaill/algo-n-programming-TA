class Point:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    
p = Point(1,2)

def get_json_str(other):
    return {"__class__": "Point","x": other.get_x(),"y": other.get_y()}

def read_json_str(s):
    p = Point(int(s),0)
    return get_json_str(p)

# a) Implement a method called get_json_str(p) 
# that receives a point p as input and returns 
# a json string that describes the object as output. 
# As an example, the following code:

# p=Point(1,2)
# z=(get _json_str(p))
# print(z)
# should produce the following output:

z = (get_json_str(p))
print(z)

# b) Now implement a function called read_json_str(s) 
# that receives a string s as input and returns a Point object as output.

b = read_json_str("9")
print(b)
