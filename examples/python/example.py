# insecure_code.py

import os
import sys

def insecure_input():
    user_input = input("Enter a command: ")
    os.system(user_input)  # 命令注入漏洞

def unsafe_eval():
    data = input("Enter data: ")
    result = eval(data)  # 不受信任的输入导致的代码执行

def sql_injection(cursor):
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)  # SQL注入漏洞

def insecure_deserialization(data):
    import pickle
    obj = pickle.loads(data)  # 可能导致任意代码执行

def hardcoded_password():
    password = "P@ssw0rd!"  # 硬编码的密码
    print("The password is:", password)

def main():
    insecure_input()
    # 其他功能调用

if __name__ == "__main__":
    main()
