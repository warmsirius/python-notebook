class Utility(object):
    """
    Utility工具类:
    将不同的功能封装成方法，就是可以直接通过调用方法使用它的功能，而无需考虑具体的功能实现细节。
    """

    @classmethod
    def read_menu_selection(cls):
        """用于界面菜单的选择。该方法读取键盘，如果用户键入1-4中任意字符，则方法返回，返回值为用户键入字符。"""
        while True:
            char = cls.read_keyboard(1)
            if char != "1" and char != "2" and char != "3" and char != "4":
                print("选择错误，请重新输入:")
            else:
                break
        return char

    @classmethod
    def read_confirm_selection(cls):
        """用于确认选择的输入。该方法从键盘中读取'Y'或'N'，并将其作为方法的返回值。"""
        while True:
            char = cls.read_keyboard(1)
            if char.upper() == "Y" or char.upper() == "N":
                break
            else:
                print("选择错误，请重新输入:")
        return char.upper()

    @classmethod
    def read_num(cls) -> int:
        """用于收入和支出金额的输入。该方法从键盘中读取一个不超过4位数长度的整数，并将其作为方法的返回值。"""
        while True:
            string = cls.read_keyboard(4)
            try:
                n = int(string)
                return n
            except ValueError:
                print("数字输入错误，请重新输入:")
        return n

    @classmethod
    def read_str(cls) -> str:
        """用于收入和支出说明的输入。该方法从键盘中读取一个不超过8位数长度的字符串，并将其作为方法的返回值。"""
        string = cls.read_keyboard(8)
        return string

    @classmethod
    def read_keyboard(cls, limit: int) -> str:
        """用户从键盘的输入。该方法从键盘中读取一个不超过limit位数长度的字符串，并将其作为方法的返回值。"""
        while True:
            string = input()
            if len(string) > limit:
                print("输入过长，请重新输入: ")
            else:
                return string
