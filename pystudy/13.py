import random

def main():
    dic = {
        "test" : 10
    }
    var =0
    for i in range(0,20):
        dic["a" + str(var)] = "test" 
        var += 1
    print(dic)



if __name__ == "__main__":
    main()