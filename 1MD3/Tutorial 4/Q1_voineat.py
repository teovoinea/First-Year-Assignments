def main():
    mark = eval(input("Please enter a mark"))
    print(letterGrade(mark))
def letterGrade(score):
    if score >= 0 and score <= 100:
        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"
    else:
        print("Bad input")
main()
