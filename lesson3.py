# _list = [1,2,3]
# print(_list)
# del _list[0]
# print(_list)
# del _list[:]
# print(_list)
#
# _dict = {'key1': 1, 'key2': 2}
# del _dict['key1']
# print(_dict)
#

# def foo1():
#     pass
#
#
# def foo_with_return():
#     return True
#
#
# def foo_with_params(param1: object = True, param2: object = True) -> object:
#     pass
#
#
# foo_with_params(False, False)

#CORTAGE
# def foo_args(*args):
#     print('FOO ARGS', args)
# foo_args(1,2,3,4,5)

# def foo_kwargs(**kwargs):
#     print('FOO KWARGS', kwargs)
# foo_kwargs(a=1, b=3)
#
# def foo_args_kwargs(*args, **kwargs):
#     print('FOO ARGS', args)
#     print('FOO KWARGS', kwargs)
# foo_args_kwargs(1, 2, 3, 4, 5, a=1, b=3, c=4)

#anonim function
# (lambda a, b: a + b)(1, 2)
#
# def foo_arr(_list, operation=None):
#     result = 0
#     for elem in _list:
#         result = operation(result, elem)
#     return result
# print(
#     foo_arr([1, 2, 3],
#     operation=lambda x, y: x + y)
# )
# print(
#     foo_arr([1, 2, 3],
#     operation=lambda x, y: x - y)
# )
# def foo1(x):
#     return 2 ** x
#
# def foo2(x):
#     return 2 * x
#
# def foo3(x):
#     return 2 * x-1
#
# def foo_result(x):
#     if -5 <= x < 5:
#         pass
#     elif x > 5:
#         pass
#     elif x < -5:
#         result = foo3()
#
# for i in range(-10, 10, 1):
#     print(foo_result(i))
print('Hello')
