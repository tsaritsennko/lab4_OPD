import unittest

test_numbers = \
    {
        1,
        5,
        6,
        4
    }

def discriminantFunction(a, b, c):
    if not (a in test_numbers):
        return -1
    if not (b in test_numbers):
        return -1
    if not (c in test_numbers):
        return -1
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def discriminant_two_roots(a, b, c):
    if not (a in test_numbers):
        return -1
    if not (b in test_numbers):
        return -1
    if not (c in test_numbers):
        return -1
    root1 = (-b + discriminantFunction(a, b, c) ** 0.5) / (2 * a)
    root2 = (-b - discriminantFunction(a, b, c) ** 0.5) / (2 * a)
    return f"Корни уравнения: {root1}, {root2}"


def discriminant_one_root(a, b):
    if not (a in test_numbers):
        return -1
    if not (b in test_numbers):
        return -1
    root = -b / (2 * a)
    return f"Уравнение имеет один корень: {root}"


def discriminant_none():
    return "Уравнение не имеет действительных корней"




class AppTest(unittest.TestCase):
    # проверка на дурака (нельзя вводить буквы в числовые поля)
    def test_syntax(self):
        self.assertEqual(discriminantFunction("Один", "Пять", "Шесть"), -1)
        self.assertEqual(discriminant_two_roots("Один", "Пять", "Шесть"), -1)
        self.assertEqual(discriminant_one_root("Один", "Пять"), -1)
    # проверка на корректность результата
    def test_correct(self):
        self.assertEqual(discriminantFunction(1, 1, 1), -3)
        self.assertEqual(discriminant_two_roots(1, 5, 6), "Корни уравнения: -2.0, -3.0")
        self.assertEqual(discriminant_one_root(1, 4), "Уравнение имеет один корень: -2.0")
        self.assertEqual(discriminant_none(), "Уравнение не имеет действительных корней")
    # проверка вывода на отрицательные числа
    def test_negative(self):
        self.assertEqual(discriminantFunction(-1, -5, -6), -1)
        self.assertEqual(discriminant_two_roots(-1, -5, -6), -1)
        self.assertEqual(discriminant_one_root(-1, -5), -1)


if __name__ == '__main__':
    unittest.main()

