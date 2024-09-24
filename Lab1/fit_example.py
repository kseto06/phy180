# Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb
import numpy as np

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b

# Next, generate your data and errorbars. One way is to manually insert it here.

x = bb.np.array([0,1,2,3,4,5,6])
y = bb.np.array([0.1,0.9,2.1,2.9,4.1,4.9,6.1])
xerr = 0.05
yerr = bb.np.array([0.01,0.02,0.03,0.04,0.05,0.06,0.07])

# Note that xerr and yerr can either be an array of the same length as x&y, or a single value


# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values

# bb.plot_fit(linear, x, y, xerr, yerr)


# Let's try again, this time loading from a file like a CSV file.
# NOTE: The CSV file should not have commas to separate things! Spaces or tabs are fine.

# Again, start with a fitting function. This time it is quadratic.

def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

# Fits cosine function
def cosine(t, a, b, c, d):
    return a * np.cos(b * t + c) + d

# Now load the data from the file. The file should be in the same directory as this Python code.
# Some chance you will need an absolute path: "C:\\Users\\Brian\\Python\\mydata_fake.txt"

filename="lab1data.txt"
x, y, xerr, yerr = bb.load_data(filename)

# This time, let's use every single possible option available to bb.plot_fit()

#p0 = [A, B, C, D]
# From desmos regression: https://www.desmos.com/calculator/qhoyz3r0vu 
init_guess = (1.05996, 5.60458, -2.84426, 0.00842794) # guess for the best fit parameters
font_size = 20
xlabel = "Time (s)"
ylabel = "Angle (rad)"

# Now we make the plot, displayed on screen and saved in the directory, and print the best fit values
bb.plot_fit(linear, x, y, xerr, yerr, init_guess=None, font_size=font_size, xlabel=xlabel, ylabel=ylabel, title="Period vs. Angle (Lab 1) - Linear Fit")

# Note: for sinusoidal functions, guessing the period correctly with init_guess is critical

