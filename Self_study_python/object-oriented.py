# 面向对象编程（OOP）是Python中一种重要的编程范式，它通过类和对象来组织代码，并通过继承、多态等特性来提高代码的可重用性和扩展性。
# 类（Class）：类是对象的蓝图或模板，它定义了一类对象的属性和行为。
# 对象（Object）：对象是类的实例，拥有类中的属性和方法。
# 继承与多态
# 继承（Inheritance）：一个类可以继承另一个类的属性和方法，继承可以避免重复代码，提高代码的复用性。
# 多态（Polymorphism）：多态允许使用父类的引用来调用子类的实现，不同的子类可以有不同的实现方式。
# 代码设计的一部分
# 父类声明 forward 方法作为抽象方法（即声明但不实现）是设计模式中的一种惯用方式，尤其是在模板方法模式中。它强制所有的子类都必须提供该方法的实现。这可以防止你在创建新层时忘记实现必需的方法，并确保代码结构的一致性。

# 定义一个类
class Animal:
    def __init__(self, name, sound):
        self.name = name  # 属性
        self.sound = sound

    def make_sound(self):  # 方法
        print(f"{self.name} makes a {self.sound} sound")

# 创建对象
dog = Animal("Dog", "bark")
cat = Animal("Cat", "meow")

# 使用对象
dog.make_sound()  # 输出: Dog makes a bark sound
cat.make_sound()  # 输出: Cat makes a meow sound



# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # 留空，让子类实现具体功能

# 子类继承父类
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

# 多态
animals = [Dog("Rover"), Cat("Whiskers")]

for animal in animals:
    animal.make_sound()  # 根据对象类型调用不同的实现

# 以神经网络举例
# 继承：DenseLayer（全连接层）和 ConvLayer（卷积层）都继承了 Layer（基础层）这个基类，它们都共享 input_size 和 output_size 的定义。
# 多态：虽然 DenseLayer 和 ConvLayer 都是从同一个 Layer 类继承的，但它们的 forward 方法实现方式不同（一个是简单的矩阵乘法，另一个是卷积操作）
# 我们可以用同样的接口（forward 方法）来计算它们的输出，而不用关心它们的具体实现。



# 在实际项目中，即使父类中的方法如 forward 被声明为 NotImplementedError，它仍然有几个重要的作用：
#
# 1. 定义接口
# 父类中声明的方法（即使未实现）定义了一个接口或规范，这样所有子类都知道它们需要实现什么样的方法。这种做法确保了所有继承自父类的子类都具备某些共同的行为。这种设计可以增强代码的一致性和可读性。
# 2.提供统一的调用方式
# 通过在父类中定义 forward 方法，你可以使用统一的接口来处理所有子类对象。即使子类中 forward 方法的实现方式不同，你仍然可以通过相同的调用方式来处理不同的层类型。这是多态的一个关键点。

# 4. 文档和注释
# 在父类中声明一个方法，并抛出 NotImplementedError，也可以作为一种文档和注释的形式，说明子类需要实现这个方法。这使得代码的意图更加明确，也方便其他开发者理解类的设计。
#
# 5. 面向接口编程
# 通过定义接口，你可以遵循面向接口编程的原则，而不是面向具体实现。这样可以更容易地扩展系统，添加新的层类型时只需要继承基类并实现 forward 方法即可，而不需要修改现有的代码。
# 基类: 通用神经网络层



class Layer:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
    def forward(self, inputs):
        raise NotImplementedError("This method should be overridden by subclasses")

# 子类: 全连接层 (继承自 Layer)
class DenseLayer(Layer):
    def __init__(self, input_size, output_size):
        super().__init__(input_size, output_size)
        # 假设我们有权重矩阵
        self.weights = [[0.5] * output_size for _ in range(input_size)]  # 简化的权重

    def forward(self, inputs):
        # 简单实现: 输入和权重相乘（忽略偏置）
        outputs = [sum(x * w for x, w in zip(inputs, self.weights[i])) for i in range(self.output_size)]
        return outputs

# 子类: 卷积层 (继承自 Layer)
class ConvLayer(Layer):
    def __init__(self, input_size, output_size, kernel_size):
        super().__init__(input_size, output_size)
        self.kernel_size = kernel_size
        # 假设我们有简单的卷积核
        self.kernel = [0.1] * kernel_size

    def forward(self, inputs):
        # 简单实现: 卷积操作（忽略步幅和填充）
        outputs = []
        for i in range(len(inputs) - self.kernel_size + 1):
            window = inputs[i:i + self.kernel_size]
            conv_result = sum(x * k for x, k in zip(window, self.kernel))
            outputs.append(conv_result)
        return outputs

# 测试多态
def run_forward(layer, inputs):
    return layer.forward(inputs)

# 创建对象
# 创建全连接层和卷积层
dense_layer = DenseLayer(3, 2)
conv_layer = ConvLayer(5, 3, kernel_size=3)

# 输入数据
inputs_dense = [1.0, 2.0, 3.0]
inputs_conv = [1.0, 2.0, 3.0, 4.0, 5.0]
#多态
# 调用相同的 forward 方法，不同层有不同的实现方式
print("Dense Layer Output:", run_forward(dense_layer, inputs_dense))
print("Conv Layer Output:", run_forward(conv_layer, inputs_conv))
# 魔术方法（Magic Methods）
# 魔术方法：也称为“特殊方法”或“dunder methods”，是Python中以双下划线开头和结尾的方法。这些方法使得类的实例可以具有一些内置行为（如运算符重载）。
# 常见的魔术方法有：
# __init__: 构造函数，用于初始化对象。
# __str__: 定义对象的字符串表示。
# __len__: 定义对象的长度。
# __add__: 实现对象相加的行为。
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        # 实现两个 Book 对象的“相加”行为，返回总页数
        return self.pages + other.pages

# 创建对象
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(book1)  # 输出: '1984' by George Orwell
print(len(book1))  # 输出: 328
print(book1 + book2)  # 输出: 440 (两本书的总页数)













