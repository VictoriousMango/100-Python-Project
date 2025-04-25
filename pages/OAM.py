import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

# Streamlit app title
st.title("Optical Vortex Beam: Orbital Angular Momentum Animation")
st.write("Visualize a rotating ray representing OAM with adjustable topological charge (l).")

# Slider for topological charge
l = st.slider("Topological Charge (l)", min_value=1, max_value=5, value=2, step=1)

# Parameters for animation
radius = 1.0  # Radius of the circular path
num_frames = 30  # Number of frames for animation
theta = np.linspace(0, 2 * np.pi, num_frames)  # Angles for one full rotation

# Generate frames
frames = []
for angle in theta:
    # Create a figure for this frame
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Orbital Angular Momentum\n(Rotating Ray, l={l})')
    ax.grid(True)
    ax.set_aspect('equal')
    
    # Calculate ray position
    x = radius * np.cos(l * angle)
    y = radius * np.sin(l * angle)
    
    # Plot ray and center
    ax.plot([0, x], [0, y], 'b-', linewidth=2, label='Rotating Ray')
    ax.plot(0, 0, 'ko', markersize=5, label='Center')
    ax.legend()
    
    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img = Image.open(buf)
    frames.append(img)
    plt.close(fig)

# Save as GIF
gif_path = "oam_animation.gif"
frames[0].save(
    gif_path,
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=100,  # milliseconds per frame
    loop=0,  # 0 means loop forever
)

# Display the animation in Streamlit
st.image(gif_path, caption=f'Rotating Ray Animation (l={l})')