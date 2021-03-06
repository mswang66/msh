# -*- coding:utf8 -*-
import sys, os
from msh.service.color import UseStyle

SPACE = ' '
HORIZON_LINE = UseStyle('-',fore = 'blue')
VERTICAL_LINE = UseStyle('|',fore = 'blue')
EMPTY = 1
NEWLINE = '\n'
class OutputClient:

    def __init__(self):
        self.headers = None
        self.header_width = None
        self.values = None
        self.values_dict = None

    def set_header(self, headers, header_width):
        if not isinstance(headers, list) and not isinstance(header_width, list):
            raise Exception("The format of parameters is not correct")
        self.headers = headers
        self.header_width = header_width

    def set_values(self, values):
        self.values_dict = values
        self.values = self._convert(values)

    def _convert(self, ssh_list_dict):
        # if len(ssh_list_dict) == 0:
        #     return None
        ssh_list_list = []
        for i in range(len(ssh_list_dict)):
        # for ssh_dict in ssh_list_dict:
            ssh_dict = ssh_list_dict[i]
            ssh_list = []
            ssh_list.append(str(i + 1))
            ssh_list.append(ssh_dict.get('host'))
            ssh_list.append(ssh_dict.get('name'))
            ssh_list_list.append(ssh_list)
        return ssh_list_list

    def show(self):
        if self.values is None or self.headers is None or self.header_width is None:
            raise Exception("The parameters are not completed")

        output = self.print_header()
        output += self.print_values()
        return output

    def print_header(self):
        segment = ''
        value = VERTICAL_LINE
        for i in range(len(self.headers)):
            segment += (SPACE * 1 + self.header_width[i] * HORIZON_LINE)
            value += (SPACE * EMPTY
                      + UseStyle(self.headers[i],fore='red')
                      + (self.header_width[i] - len(self.headers[i]) - EMPTY) * SPACE
                      + VERTICAL_LINE)

        return segment + NEWLINE + value + NEWLINE + segment + NEWLINE

    def print_values(self):
        values_str = ''
        for value in self.values:
            values_str += self.print_value(value)
        return values_str

    def print_value(self, value):
        value_str = VERTICAL_LINE
        segmemt = ''
        for i in range(len(value)):
            val = UseStyle(value[i], fore='green') if i > 0 else UseStyle(value[i], mode='bold', fore='red')
            # val = value[i]
            value_str += (SPACE * EMPTY
                          + val
                          + (self.header_width[i] - len(value[i]) - EMPTY) * SPACE
                          + VERTICAL_LINE)
            segmemt += (SPACE * 1 + self.header_width[i] * HORIZON_LINE)
        value_str += NEWLINE
        segmemt += NEWLINE
        # return value_str
        return value_str + segmemt

    def select(self):
        index = raw_input("请选择需要登录的主机(index): ")

        while not self._is_num(index):
            index = raw_input("输入有误,请选择需要登录的主机(index): ")
        index = int(index)
        return self.values_dict[index - 1]

    def select_to_del(self):
        index = raw_input("请选择删除的主机(index): ")
        while not self._is_num(index):
            index = raw_input("输入有误,请选择删除的主机(index): ")
        index = int(index)
        return self.values_dict[index - 1]

    def select_to_update(self):
        index = raw_input("请选择更新的主机(index): ")
        while not self._is_num(index):
            index = raw_input("输入有误,请选择更新的主机(index): ")
        index = int(index)
        return self.values_dict[index - 1]

    def _is_num(self,index):
        try:
            index = int(index)
            if index > len(self.values_dict):
                return False
            return True
        except:
            return False

# a = [1,2]
# print isinstance(a, list)
# sys.stdout.write(' ------------------ ----------------- ----------------------------\n')
# sys.stdout.write('| HOST             |     USER        |                            |\n')
# sys.stdout.write(' ------------------ ----------------- ----------------------------\n')
# sys.stdout.write('| 888.888.888.888  |                 |                            |\n')
# sys.stdout.write(' ------------------ ----------------- ----------------------------\n')

# out = OutputClient()
# out.set_header(['a','xxxxxx'],[4, 10])
# out.set_values([['as','aaa'],['faaaaa','123']])
# print out.show()
#
# print -10 * '-' + '=='
# print int('a')