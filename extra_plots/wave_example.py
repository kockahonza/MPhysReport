from analysisScripts.base import *

# figure_out_dir = '../latex/figures/misc'

if __name__ == "__main__":
    save_fig = None
    if len(sys.argv) >= 2:
        figure_out_dir = sys.argv[1]
    if save_fig is not None:
        print(f'saving to {figure_out_dir}')

    colors = use_report_sh_style(6, figheight=2.9, interactive=save_fig is None, advanced_latex=True)

    # Params
    wavelength = 2
    q0 = 2 * np.pi / wavelength

    s = np.pi
    R = 5

    L = 10
    N = 1001

    # The base data
    X, Y = np.meshgrid(np.linspace(-L, L, N), np.linspace(-L, L, N))

    r_mag = np.sqrt(X**2 + Y**2)
    nx = X / r_mag
    ny = Y / r_mag

    fig, [director_ax, density_ax] = plt.subplots(1, 2, width_ratios=(1, 1.24))

    # Do director/phi plot
    dir_step = 100
    director_ax.quiver(X[::dir_step, ::dir_step], Y[::dir_step, ::dir_step],
                       nx[::dir_step, ::dir_step], ny[::dir_step, ::dir_step], scale=12, pivot='middle', label='director')

    ic_color = mcolors.to_rgba(colors[1], 0.5)
    oc_color = mcolors.to_rgba(colors[2], 0.5)

    ic = mpatches.Circle((0, 0), R, facecolor=ic_color)
    director_ax.add_patch(ic)

    oc = mpatches.Annulus((0, 0), 10 * L, 10 * L - R, facecolor=oc_color)
    director_ax.add_patch(oc)

    ic_handle=mpatches.Patch(color=ic_color, label='$\\phi=0$')
    oc_handle=mpatches.Patch(color=oc_color, label='$\\phi=\\frac{\\pi}{\\si{L}}(r - 5\\si{L})$')
    quivlike_handle = mlines.Line2D(
        [], [], color='k', marker='', linestyle='-', label='director $\\su{N}$')
    director_ax.legend(handles=[quivlike_handle, ic_handle, oc_handle], fontsize='xx-small')

    director_ax.set_xlabel('x in units of \\si{L}')
    director_ax.set_ylabel('y in units of \\si{L}')

    # Do density plot
    def get_psi_(x, y):
        r = np.sqrt(x**2 + y**2)
        if r < R:
            return 1
        else:
            rp = r - R
            return np.exp(1j * s * rp)

    get_psis = np.vectorize(get_psi_)
    psi = get_psis(X, Y)

    density = 1 + np.abs(psi) * np.cos(q0 * r_mag + np.angle(psi) + np.pi)

    pcm = density_ax.pcolormesh(X, Y, density, cmap='Grays', rasterized=True)

    density_ax.set_xlabel('x in units of \\si{L}')
    density_ax.set_ylabel('y in units of \\si{L}')
    fig.colorbar(pcm, ax=density_ax,
                 label='density in units of $\\rho_0$')
                 # label='density, $1 + \\Re(e^{i(\\ssu{q_0}\\cdot\\ssu{r} + \\phi)})$')

    director_ax.set_title('(a)', size='small')
    director_ax.set_xlim(-L, L)
    director_ax.set_ylim(-L, L)
    director_ax.set_aspect('equal')
    density_ax.set_title('(b)', size='small')
    density_ax.set_xlim(-L, L)
    density_ax.set_ylim(-L, L)
    density_ax.set_aspect('equal')

    if save_fig:
        fig.savefig(path.join(figure_out_dir, 'wave_phi_example.pdf'))
    else:
        plt.show()
