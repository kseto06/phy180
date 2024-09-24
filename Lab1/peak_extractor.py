import fit_black_box as bb
import numpy as np

# Period vs Angle
filename="lab1data.txt"
x_full, y_full, x_full_err, y_full_err = bb.load_data(filename)

# Initialize x_peaks, y_peaks -- peaks show up from the first (0) index to the 38th index
x_peaks, y_peaks = [], []
for i in range(0, len(x_full), 19):
    x_peaks.append(x_full[i])
    y_peaks.append(y_full[i])

# Init x_peaks_err, y_peaks_err
x_peaks_err = [0.002] * len(x_peaks)
y_peaks_err = [0.001] * len(y_peaks)

def quadratic(t, a, b, c):
    t = np.array(t)
    return a*t**2 + b*t + c

# Printing the x_peaks, y_peaks data
print(x_peaks)
print(y_peaks)

# Data points: https://www.desmos.com/calculator/jlolygub0b 
init_guess = (-0.000341949, 0.0131072, -0.105344) # guess for the best fit parameters
font_size = 20
xlabel = "Angle (rad)"
ylabel = "Time (s)"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(quadratic, y_peaks, x_peaks, y_peaks_err, x_peaks_err, init_guess=None, font_size=font_size, xlabel=xlabel, ylabel=ylabel, title="Period (s) vs. Angle (rad) -- Quadratic Fit")