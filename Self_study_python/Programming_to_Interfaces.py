# 接口和面向接口编程（Programming to Interfaces）是面向对象编程中的核心概念，它们有助于提高代码的灵活性、可扩展性和维护性。让我们深入探讨这些概念：
#
# 什么是接口？
# 在编程中，接口是一种约定或规范，它定义了类应该提供哪些方法，但不具体实现这些方法。接口的作用是确保实现它的类提供了一组特定的功能或行为。这种设计方式可以使代码更加模块化，并允许不同的实现互换。
#
# 接口的特点：
# 定义方法：接口只定义方法的签名（即方法的名字、参数和返回类型），而不包含方法的具体实现。
# 不包含状态：接口不包含字段或数据（有些语言允许接口有默认的实现，但一般来说接口不包含状态）。
# 实现：具体的类需要实现接口定义的所有方法。
# 面向接口编程
# 面向接口编程（Programming to Interfaces）是一种编程原则，指的是编写代码时依赖于接口而不是具体的实现。这种方法可以使代码更加灵活，易于扩展和维护。
#
# 面向接口编程的优势：
# 解耦：代码依赖于接口而不是具体的实现类，使得系统的不同部分之间的耦合度降低。更改某个实现类不会影响依赖于接口的其他代码。
# 可扩展性：新实现可以很容易地添加到系统中，只要它们遵循接口定义。系统可以在不修改现有代码的情况下扩展功能。
# 可测试性：使用接口可以方便地进行单元测试。可以创建实现接口的假对象（Mock）来测试依赖于接口的代码，而不需要依赖于具体的实现类。

# 并不是所有的父类都可以看作接口。父类可以包含具体实现，而接口则不包含。
# 但父类可以像接口一样工作，尤其是在父类只定义方法而不提供实现时。这样的父类被称为抽象类，它与接口类似，主要用于定义子类必须实现的行为。
# 接口的关键作用是定义一组行为，而父类的作用更多是提供共享的功能或属性。
# 因此，你可以认为抽象类更接近接口的概念，而不是所有的父类都是接口。
# 示例：接口的定义与使用
# 例子：接口在 Python 中的使用
# 在 Python 中，接口可以通过抽象基类（abc 模块）来模拟：
from abc import ABC, abstractmethod
# 定义接口
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 实现接口的具体类
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius * self.radius

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# 使用接口
def print_shape_info(shape: Shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
# 对象
rect = Rectangle(10, 5)
circ = Circle(7)

print_shape_info(rect)
print_shape_info(circ)

# Shape 类是一个接口，它定义了 area 和 perimeter 方法，但不提供实现。
# Rectangle 和 Circle 类实现了 Shape 接口，并提供了具体的实现。
# print_shape_info 函数接受一个 Shape 类型的参数，并调用它的方法，这样无论传入的是 Rectangle 还是 Circle 对象，都能正常工作。
# 总结
# 接口 是一种定义方法而不提供具体实现的工具。
# 面向接口编程 是编写代码时依赖于接口而不是具体实现的原则。这种方法可以使代码更具灵活性和可维护性。
# 通过理解和应用接口及面向接口编程的概念，你可以设计出更加模块化、可扩展和易于维护的系统。


# 抽象父类 (类似接口)
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# 子类必须实现 sound 方法
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# 使用
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())  # 输出: Bark 和 Meow
