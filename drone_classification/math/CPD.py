import matplotlib.pyplot as plt
import ruptures as rpt

# algo = rpt.Dynp(model="rbf").fit(y1c)              # dynamic programing O(k*n^2)
# algo = rpt.Binseg(model="rbf").fit(y)              # binary segmentation O(nlogn)
# algo = rpt.Window(width = 100, model="rbf").fit(y)  # window-based O(n)

def changepoint_detection(signal, bkps = 1, window_width = 100, display = False):
    algo = rpt.Window(width=window_width, model="rbf").fit(signal)
    breakpoints = algo.predict(n_bkps=bkps)
    if display:
        rpt.display(signal, breakpoints)
        plt.show()
    return breakpoints







