## Library that uses Matplotlib underneath to plot graphs
# Used to vizualize random disributions

#example of plotting a Distplot
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

#Plotting a Distplot without Histogram

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()