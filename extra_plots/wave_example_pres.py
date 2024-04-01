from analysisScripts.base import *

if __name__ == "__main__":
    figure_out_dir = None
    if len(sys.argv) >= 2:
        figure_out_dir = sys.argv[1]
    if figure_out_dir is not None:
        print(f'saving to {figure_out_dir}')

    colors = use_report_sh_style(
        3.5, figheight=3, interactive=figure_out_dir is None, advanced_latex=True)

    # Params
    wavelength = 2
    q0 = 2 * np.pi / wavelength

    s = np.pi
    R = 7

    L = 10
    N = 1001

    # The base data
    X, Y = np.meshgrid(np.linspace(-L, L, N), np.linspace(-L, L, N))

    r_mag = np.sqrt(X**2 + Y**2)
    nx = X / r_mag
    ny = Y / r_mag

    fig, ax = plt.subplots()

    # Do density plot
    def get_psi_(x, y):
        psim = np.clip((x - (-L/2)) / (L), 0, 1)
        r = np.sqrt(x**2 + y**2)
        if r < R:
            return psim
        else:
            rp = r - R
            return psim * np.exp(1j * s * rp)

    get_psis = np.vectorize(get_psi_)
    psi = get_psis(X, Y)

    density = 1 + np.abs(psi) * np.cos(q0 * r_mag + np.angle(psi) + np.pi)

    pcm = ax.pcolormesh(X, Y, density, cmap='Grays', rasterized=True)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.colorbar(pcm, ax=ax,
                 label='density, $\\rho$')

    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    ax.set_aspect('equal')

    fig.tight_layout()

    if figure_out_dir is not None:
        fig.savefig(path.join(figure_out_dir, 'layers_example.pdf'))
    else:
        plt.show()
