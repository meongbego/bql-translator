from bql import BQLParser
import pprint
from neo.clis import Ls
from tabulate import tabulate


p = BQLParser(debug=False)


def query(query):
    result = p.parse(query)
    command = list()
    tableref = list()
    table_column = list()
    return_data = list()
    where_return = list()
    # headers = ["ID", "Name", "Status", "Created", "Updated"]
    # print(tabulate("", headers=headers, tablefmt="grid"))
    if (len(result[0][2]) > 2):
        where_list = list()
        op_where = list()
        for i in result:
            command = i[0]
            table_column = i[1]
            tableref = i[2]['from'][0][1]
            where_data = i[2]['where']
            for b in where_data:
                where = []
                first_op = []
                if type(b) is tuple:
                    for c in b:
                        if(c == "="):
                            where = {
                                "where_var_op": c
                            }
                        elif(c == ">="):
                            where = {
                                "where_var_op": c
                            }
                        elif(c == "<="):
                            where = {
                                "where_var_op": c
                            }
                        elif(c == ">"):
                            where = {
                                "where_var_op": c
                            }
                        elif(c == "<"):
                            where = {
                                "where_var_op": c
                            }
                        elif(type(c) is str):
                            where = {
                                "where_var": c
                            }
                        else:
                            where = {
                                "where_value": c[1]
                            }
                        where_list.append(where)
                else:
                    op_where = b

            where_return.append({
                'first_op': op_where,
                'where_data': where_list
            })
            print(where_return)
            # return_data.append({
            #     "command": command,
            #     "table_list": table_column,
            #     "table_ref": tableref,
            #     "where_list": where_list
            # })
    else:
        for i in result:
            command = i[0]
            table_list = i[1]
            tableref = i[2]['from'][0][1]

    # pprint.pprint(return_data)


query("SELECT ID,NAME FROM vm WHERE NAME='UBUNTU' AND ID='123';")
# query("SELECT ID,NAME FROM vm;")
# query("SELECT * FROM vm;")
# while True:
#     q = input("BQL> ")
#     query("{};".format(q))
