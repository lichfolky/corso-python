from miaException import MioErrore
try:
    print(5/0)
    # 5 = 3838
except ZeroDivisionError as error:
    print("hai diviso per zero, non si fa!")

raise MioErrore("ciao")