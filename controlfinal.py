import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import tkinter as tk
import control as ct


def plot_frequency_response(num, den, title, plot_type):
    # Convert numerator and denominator as numpy array
    num = np.array(num)
    den = np.array(den)
    # Convert the numerator and denominator coefficients to a TransferFunction object
    system = signal.TransferFunction(num, den)
    G = ct.tf(num, den)

    # Generate the frequency response of the system
    if plot_type == "Bode Plot":
        w, mag, phase = signal.bode(system)
    elif plot_type == "Nyquist Plot":
        w, h = signal.freqresp(system)

    # Stability margins and crossover frequencies
    gm, pm, wcg, wcp = ct.margin(G)

    # Convert gm to Decibel
    gmdb = 20 * np.log10(gm)
    print("wc =", f"{wcp:.2f}", "rad/s")
    print("w180 =", f"{wcg:.2f}", "rad/s")
    print("GM =", f"{gmdb:.2f}", "dB")
    print("PM =", f"{pm:.2f}", "deg")

    # Plot the frequency response
    plt.figure(figsize=(10, 5))
    if plot_type == "Bode Plot":
        plt.subplot(2, 1, 1)
        plt.semilogx(w, mag, "r")
        plt.grid(True, which="both", axis="both")
        plt.xlabel("Frequency [rad/s]")
        plt.ylabel("Magnitude [dB]")
        plt.title(title + " - Magnitude Response")

        plt.subplot(2, 1, 2)
        plt.semilogx(w, phase, "b")
        plt.grid(True, which="both", axis="both")
        plt.xlabel("Frequency [rad/s]")
        plt.ylabel("Phase [degrees]")
        plt.title(title + " - Phase Response")
    elif plot_type == "Nyquist Plot":
        plt.plot(h.real, h.imag)
        plt.plot(h.real, -h.imag)
        plt.grid(True)
        plt.xlabel("Real")
        plt.ylabel("Imaginary")
        plt.title(title + " - Nyquist Plot")

    plt.tight_layout()
    plt.show()
    


def get_frequency_response():
    # get the input by user from GUI
    try:
        num = [float(n) for n in num_entry.get().split(",")]
        den = [float(d) for d in den_entry.get().split(",")]
        title = title_entry.get()
        plot_type = plot_var.get()
        plot_frequency_response(num, den, title, plot_type)
      
    except Exception as e:
        print("Please enter a valid input\n", e)


# GUI Setup
root = tk.Tk()
root.title("Frequency Response Plotter")
root.geometry("480x256")
root.config(bg="#ccffcc")


# Frame for the inputs
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(side="top", padx=0, pady=5)

# label for plot type selection
plot_type_label = tk.Label(
    input_frame, text="Plot Type:", font=("comicsansms", 10, "bold")
)
plot_type_label.grid(row=3, column=0, sticky="w")

# Plot type selection
plot_var = tk.StringVar(root)
plot_var.set("Bode Plot")  # default value
plot_menu = tk.OptionMenu(input_frame, plot_var, "Bode Plot", "Nyquist Plot")
plot_menu.grid(row=3, column=1, sticky="ew")


tk.Label(
    input_frame,
    text="Numerator Coefficients (comma-separated):",
    font=("comicsansms", 10, "bold"),
).grid(row=0, column=0, sticky="w")
num_entry = tk.Entry(input_frame, bg="#ffffcc", relief="solid")
num_entry.grid(row=0, column=1, sticky="e")

tk.Label(
    input_frame,
    text="Denominator Coefficients (comma-separated):",
    font=("comicsansms", 10, "bold"),
).grid(row=1, column=0, sticky="w")
den_entry = tk.Entry(input_frame, bg="#ffffcc", relief="solid")
den_entry.grid(row=1, column=1, sticky="e")

tk.Label(input_frame, text="System Title:", font=("comicsansms", 10, "bold")).grid(
    row=2, column=0, sticky="w"
)
title_entry = tk.Entry(input_frame, bg="#ffffcc", relief="solid")
title_entry.grid(row=2, column=1, sticky="e")


# functions for hover color change
def on_hover(event):
    event.widget.configure(bg="#00994d")


def on_defult(event):
    event.widget.configure(bg="#00cc66")


# Button to trigger the calculation
btn = tk.Button(
    button_frame,
    text="Plot Frequency Response",
    font="helvetica 8 bold",
    fg="#ffffff",
    bg="#00cc66",
    cursor="hand2",
    activebackground="#00cc66",
    activeforeground="#ffffff",
    relief="raised",
    command=get_frequency_response,
)
btn.grid(row=3, columnspan=2)
btn.bind("<Enter>", on_hover)
btn.bind("<Leave>", on_defult)


root.mainloop()
