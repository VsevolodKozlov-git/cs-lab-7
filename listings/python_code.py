def f(x):
    return (5*x / (4-x**2))

def main():
    #init figure
    fig = plt.figure()
    y = f(x)
    #clear vert. asymptots
    y[y>30] = np.inf
    y[y<-30] = -np.inf
    #plot main graphic
    plt.plot(x, y)
    #plot horizontal asymptots
    for i in [-2, 2]:
        plt.axvline(x=i,  linestyle='dashed', color="black")
    #plot vertical asymptots
    plt.axhline(0, linestyle='dashed', color="black")
    #configuring plot size
    plt.xlim(-5, 5)
    plt.ylim(-20, 20)
    #saving picture
    fig.savefig("mainPlot.eps", format = "eps", dpi = 1200)


if __name__ == '__main__':
    main()
