from src.train.train import train
import matplotlib.pyplot as plt


def main():
    fileName = 'src/data/cost_revenue_clean_custom.txt'

    thetas = train(fileName)
    print(thetas)
    plt.show()  #close the windows of both graphs to finish the program


if __name__ == '__main__':
    main()