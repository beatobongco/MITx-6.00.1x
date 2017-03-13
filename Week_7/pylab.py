import matplotlib.pyplot as plt

samples = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(0, 30):
  samples.append(i)
  linear.append(i)
  quadratic.append(i**2)
  cubic.append(i**3)
  exponential.append(1.5**i)

plt.figure('lin')
plt.clf() #clear frame, good habit
plt.title('Linear')
plt.ylim(0, 1000)
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(samples, linear)

plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.ylim(0, 1000)
plt.plot(samples, quadratic)

plt.figure('cube')
plt.clf()
plt.title('Cubic')
plt.plot(samples, cubic)

plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.plot(samples, exponential)

# Go back to quadratic graph, put labels
# basically, call plt.figure(name) and labelling calls
# will affect that named figure
plt.figure('quad')
plt.ylabel('quadratic function')

plt.figure('lin quad')
plt.clf()
plt.subplot(211) #args: rows, cols, location
plt.ylim(0, 900)
plt.title('Linear vs. Quadratic')
plt.plot(samples, linear, 'b-', label='linear', linewidth=2.0)
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(samples, quadratic, 'ro', label='quadratic', linewidth=3.0)
plt.legend(loc='upper left')

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.title('Cubic vs. Exponential')
plt.plot(samples, cubic, 'g^', label='cubic', linewidth=4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(samples, exponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()

plt.figure('cube exp log')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.plot(samples, cubic, 'g^', label='cubic', linewidth=4.0)
plt.plot(samples, exponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()
plt.yscale('log') # !!!

plt.show()
