import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
import randomcolor
style_list = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
#plt.style.use(fivethirtyeight)
#fivethirtyeight, ggplot

#plt.skkcd()


# Set up the grid size and initialize the grid
grid_size = 100
grid = np.zeros((grid_size, grid_size))

# Set the initial smoke source at the center of the grid
source_x = grid_size // 2
source_y = grid_size // 2
grid[source_x, source_y] = 255

# Define the Van-Neumann neighborhood
neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Function to update the animation frame
def update(frame):
    new_grid = np.zeros((grid_size, grid_size))
    
    # Update the smoke diffusion for each cell
    for i in range(grid_size):
        for j in range(grid_size):
            total = 0
            count = 0
            for dx, dy in neighbors:
                if i + dx >= 0 and i + dx < grid_size and j + dy >= 0 and j + dy < grid_size:
                    total += grid[i + dx, j + dy]
                    count += 1
            new_grid[i, j] = total // count
    
    # Update the grid with the new values and add randomness
    new_grid += np.random.randint(0, 20, size=(grid_size, grid_size))
    new_grid = np.clip(new_grid, 0, 255)
    
    # Update the grid with the new values
    grid[:,:] = new_grid
    
    # Create the smoke screen effect plot
    ax.clear()
    ax.imshow(grid, cmap='gray', vmin=0, vmax=255, alpha=0.2)
    ax.axis('off')
    
# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()