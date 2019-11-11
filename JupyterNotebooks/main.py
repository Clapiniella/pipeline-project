
import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a,b=b,a+b 
    return a


def Main():
    parser=argparse.ArgumentParser(description='suma numeros')
    parser.add_argument('num', help="un int", type=int)
    parser.add_argument('-o','--output', help="Output result to a file", action="store_true")
    args=parser.parse_args()
    result=fib(args.num)
    print("The "+str(args.num)+ "th fib number is "+str(result))

    if args.output:
        f=open("resultados.txt", "a")
        f.write(str(result)+'\n')

if __name__=='__main__':
        Main()