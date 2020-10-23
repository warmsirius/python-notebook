from 练习1_家庭记账软件.Utility import Utility


class FamilyAccount(object):
    """
    FamilyAccount类: 实现家庭记账功能
    """

    @classmethod
    def run(cls):
        """家庭记账功能主要实现逻辑"""
        balance = 200
        account_detail = "收支\t账户金额\t收支金额\t说   明\n"
        is_flag = True

        while is_flag:
            print("------------家庭收支记账软件-------------")
            print("            1.收支明细")
            print("            2.登记收入")
            print("            3.登记支出")
            print("            4.退   出\n")
            print("            请选择(1-4):")

            selection = Utility.read_menu_selection()
            if selection == "1":
                print("1.收支明细")
                print("------------当前收入明细记录-------------")
                print(account_detail)
                print("---------------------------------------")

            elif selection == "2":
                print("2.登记收入")
                print("请输入收入金额:")

                income = Utility.read_num()
                balance += income
                print("请输入收入来源:")
                income_reason = Utility.read_str()
                account_detail += f"收入\t{balance}\t{income}\t{income_reason}\n"
                print("------------登记完成-------------")

            elif selection == "3":
                print("3.登记支出")
                print("请输入支出金额:")

                outcome = Utility.read_num()
                if balance >= outcome:
                    balance -= outcome
                    print("请输入支出理由:")
                    outcome_reason = Utility.read_str()
                    account_detail += f"支出\t{balance}\t{outcome}\t{outcome_reason}\n"
                else:
                    print("支出超出账户额度，支付失败!")

            elif selection == "4":
                print("是否要退出(Y/N)?")

                is_exit = Utility.read_confirm_selection()
                is_flag = True if is_exit == "Y" else False


if __name__ == "__main__":
    FamilyAccount.run()
