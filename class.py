class Amimal(object):
    def run(self):
        print("animal is running.")
class Dog(Amimal):
    def run(self):
        print('dog is running')
class Cat(Amimal):
    def run(self):
        print('cat is running')
'''
    静态语言 vs 动态语言
    对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
    否则，将无法调用run()方法。

    对于Python这样的动态语言来说，则不一定需要传入Animal类型。
    我们只需要保证传入的对象有一个run()方法就可以了：
'''
class Timer(object):
    def run(self):
        print('start...')
'''
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''
def run_twice(animal):
    animal.run()
if __name__=='__main__':
    dog=Dog()
    dog.run()
    cat=Cat()
    cat.run()
    run_twice(Dog())
    run_twice(Cat())
    run_twice(Timer())
