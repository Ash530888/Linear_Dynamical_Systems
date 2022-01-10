import matplotlib.pyplot as plt
import numpy as np


def main():
    N=100
    a=0.95
    c=5.0
    sd_w=1
    sd_v=1
    m0=0
    sd_w0=1

    x=np.array([0 for i in range(N)])
    y=np.array([0 for i in range(N)])

    x[0]=np.random.normal(m0, sd_w0)
    w=np.random.normal(0, sd_w, N)
    v=np.random.normal(0, sd_v, N)

    t = np.array([i for i in range(N)])

    for i in range(1, N):
        x[i]=(a*x[i-1])+w[i-1]
        y[i-1]=(c*x[i-1])+v[i-1]

    fig, ax = plt.subplots()

    line1,=ax.plot(t,x,label='x')
    line2,=ax.plot(t,y,label='y')

    leg=ax.legend()

    lines = [line1, line2]
    lined = {}  # Will map legend lines to original lines.

    for legline, origline in zip(leg.get_lines(), lines):
        legline.set_picker(True)  # Enable picking on the legend line.
        lined[legline] = origline


    plt.xlabel('Time Step')
    plt.ylabel('Value')

    plt.grid(alpha=.4,linestyle='--')

    fig.canvas.mpl_connect('pick_event', on_pick)

    plt.show()


def on_pick(event):
    # On the pick event, find the original line corresponding to the legend
    # proxy line, and toggle its visibility.
    legline = event.artist
    origline = lined[legline]
    visible = not origline.get_visible()
    origline.set_visible(visible)
    # Change the alpha on the line in the legend so we can see what lines
    # have been toggled.
    legline.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()


if __name__=="__main__":
    main()
