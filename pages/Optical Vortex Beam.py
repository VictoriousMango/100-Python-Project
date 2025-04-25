import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.title("Optical Vortex Beam")

with st.status("Fork Grating Analysis"):
    l = st.number_input("Topological Charge (ℓ)", min_value=1, max_value=100, value=1, step=1)

    col1, col2 = st.columns(2)

    with col1:
        grating = st.empty()
        # Parameters
        N = 500  # Grid size
        period = 40  # Grating period (pixels)
        period = st.number_input("Spatial Frequency of Grating", min_value=1, max_value=100, value=40, step=10)

        x = np.linspace(-N//2, N//2, N)
        y = np.linspace(-N//2, N//2, N)
        X, Y = np.meshgrid(x, y)
        Theta = np.arctan2(Y, X)

        # Fork grating phase
        phase_mask = np.cos(2 * np.pi * X / period + l * Theta)
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.imshow(phase_mask, cmap='gray')
        ax.set_title('Fork Grating Phase Mask')
        ax.axis('off')
        grating.pyplot(fig)
        # plt.imshow(phase_mask, cmap='gray')
        # plt.title('Fork Grating Phase Mask')
        # plt.axis('off')
        # plt.show()

    with col2:
        # Simulation parameters
        radius = 1
        frames = 50
        angle_step = 2 * np.pi / frames
        z_height = 2  # height of the spiral
        plot_area = st.empty()

        st.markdown(f"""
        - ℓ = {l} means the **phase wraps {l}× around** per full rotation.
        - The dot traces a **helical path**, representing a beam with Orbital Angular Momentum.
        """)

        # Total angle for full animation
        total_angle = l * 2 * np.pi

        for frame in range(frames):
            angle = frame * angle_step
            x = radius * np.cos(l * angle)
            y = radius * np.sin(l * angle)
            z = (z_height / frames) * frame

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot([0], [0], [0], 'k.')  # beam center
            ax.plot([x], [y], [z], 'ro', markersize=10)

            # Spiral path (for trail effect)
            theta_vals = np.linspace(0, angle, 300)
            x_vals = radius * np.cos(l * theta_vals)
            y_vals = radius * np.sin(l * theta_vals)
            z_vals = (z_height / frames) * (theta_vals / angle_step)
            ax.plot(x_vals, y_vals, z_vals, 'b-', alpha=0.6)

            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_zlim(0, z_height)
            ax.set_title(f"Helical Phase Front (ℓ = {l})")
            ax.view_init(elev=30, azim=45)  # Set view angle

            plot_area.pyplot(fig)
            time.sleep(0.05)

# with tab2:
#     # Streamlit page configuration
with st.status("Fork Grating and Diffraction Pattern Visualization"):
    # Parameters
    N = 500  # Increased grid size for better resolution
    l = 1     # Topological charge
    period = 40  # Grating period (pixels)

    # Create meshgrid
    x = np.linspace(-N//2, N//2, N)
    y = np.linspace(-N//2, N//2, N)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    # Gaussian beam
    w0 = 150  # Larger beam waist to cover more grating lines
    gaussian_beam = np.exp(-(X**2 + Y**2) / w0**2)

    # Binary fork grating
    grating = 0.5 * (1 + np.sign(np.cos(2 * np.pi * X / period + l * Theta)))

    # Field after grating
    field = gaussian_beam * grating

    # Far-field (Fraunhofer) diffraction pattern
    far_field = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(field)))

    # Display first set of plots
    st.subheader("Grating and Diffraction Patterns")
    fig1, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Fork Grating
    axes[0].imshow(grating, cmap='gray')
    axes[0].set_title('Fork Grating')
    axes[0].axis('off')

    # Gaussian Beam × Grating
    axes[1].imshow(gaussian_beam * grating, cmap='gray')
    axes[1].set_title('Gaussian Beam Vortex Beam Interference')
    axes[1].axis('off')

    # Far-field Pattern
    im = axes[2].imshow(np.log(np.abs(far_field)**2 + 1), cmap='inferno')
    axes[2].set_title('Far-field Pattern with Diffraction Orders')
    fig1.colorbar(im, ax=axes[2], label='Log Intensity')
    axes[2].axis('off')

    plt.tight_layout()
    st.pyplot(fig1)

# Zoomed-in diffraction pattern
with st.status("Zoomed Far-field Pattern"):
    fig2, ax = plt.subplots(figsize=(10, 8))

    # Crop to central region
    center_size = N // 2.5
    center = N // 2
    crop_slice = slice(int(center - center_size//2), int(center + center_size//2))
    zoomed_pattern = np.log(np.abs(far_field[crop_slice, crop_slice])**2 + 1)

    # Plot zoomed pattern
    im = ax.imshow(zoomed_pattern, cmap='inferno')
    ax.set_title('Zoomed Far-field Pattern - Diffraction Orders with Vortex Structures')
    fig2.colorbar(im, ax=ax, label='Log Intensity')

    # # Marker position logic
    # center_vis = center_size // 2
    # offset = int(N / period * (center_size / N))  # Simplifies to center_size / period

    # ax.plot(center_vis, center_vis, 'wo', markerfacecolor='none', label='0 order')
    # ax.plot(center_vis + offset, center_vis, 'go', markerfacecolor='none', label='+1 order')
    # ax.plot(center_vis - offset, center_vis, 'ro', markerfacecolor='none', label='-1 order')

    # ax.legend(loc='upper right')
    ax.axis('off')

    st.pyplot(fig2)