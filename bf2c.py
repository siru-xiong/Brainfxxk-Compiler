# -*- coding: utf-8 -*- 
import sys
import os

def trans_w(w):
    dic = {
        '>' : "++p;\n",
        '<' : "--p;\n",
        '+' : "++*p;\n",
        '-' : "--*p;\n",
        '.' : "putchar(*p);\n",
        ',' : "*p=getchar();\n",
        '[' : "while(*p){\n",
        ']' : "};\n"
    }
    return dic.get(w, "")

def trans_s(s):
    prefix = "// C source code translated from bf\n"
    prefix += "#include <stdio.h>\n"
    prefix += "char tape[10000];\n"
    prefix += "char *p = tape;\n"
    prefix += "int main()\n{\n"
    core = ''.join([trans_w(i) for i in s])
    suffix = "\n return 0;"
    suffix += "}\n"
    full = prefix + core + suffix
    return full

def main(filename):
    with open(filename) as f:
        bf_source = f.read()
    c_source = trans_s(bf_source)
    savename = filename + ".c"
    execname = filename + ".out"
    with open(savename, "w") as f:
        f.write(c_source)
    print("Wrote C source code to: " + savename)
    print("Compiling")
    os.system("gcc " + savename + " -o " + execname)
    print("Completed, running ./" + execname)
    os.system("./" + execname)
    
if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)