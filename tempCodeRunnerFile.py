def main():
    try:
        a = int(input("input your number : "))
        print(f"Your number in the square {square(a)}")
    except SyntaxError:
        print("SyntaxError")
        #Python does not undestesnd your code structure 
        #it is like you missing : or unclose brackets "() {}"
    except IndentationError:
        print("IndentationError")
        #Incorrect indentatio (spaces/tabs)
    except NameError:
        print("NameError")
        #You used a variable or function that does not exist
    except TypeError:
        print("TypeError")
        #Wrong data types used together ir is like int + str
    except ValueError:
        print("ValueError")
        #when your value does not correct
    except IndexError:
        print("IndexError")
        #when you try to get from list npn existent value enough memori
    """
    RuntimeError is error during executing when you value does not have e
    """


def square(x):
    return x * x


if __name__ == "__main__":
    main()