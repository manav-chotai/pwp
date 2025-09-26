import numpy as np
import matplotlib.pyplot as plt

# Make a 2x3 grid of plots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Signal Examples', fontsize=16)

# 1) Add two sine waves
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs)
y = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t)

plt.plot(t[:200], y[:200])
plt.title('5Hz + 10Hz Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


# 2) Multiply sine and cosine
import numpy as np
import matplotlib.pyplot as plt

fs = 500
t = np.linspace(0, 2, fs*2)
y = np.sin(2*np.pi*5*t) * np.cos(2*np.pi*10*t)

plt.plot(t[:200], y[:200])
plt.title('5Hz Sine * 10Hz Cosine')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


# 3) Time shift
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
y = np.sin(2*np.pi*5*t)
shift = int(0.1*1000)

plt.plot(t[:300], y[:300], label='Original')
plt.plot(t[:300], np.roll(y, shift)[:300], label='Shifted')
plt.title('Time Shift of 5Hz Sine')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


# 4) Amplitude scaling
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.5, 500)
y = np.sin(2*np.pi*10*t)

plt.plot(t, y, label='Amplitude=1')
plt.plot(t, 3*y, label='Amplitude=3')
plt.title('Amplitude Scaling')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


# 5) Time reversal
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
y = np.sin(2*np.pi*5*t)

plt.plot(t[:300], y[:300], label='Original')
plt.plot(t[:300], np.flip(y)[:300], label='Reversed')
plt.title('Time Reversal of 5Hz Sine')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
