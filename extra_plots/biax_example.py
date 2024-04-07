from analysisScripts.base import *

if __name__ == "__main__":
    figure_out_dir = None
    if len(sys.argv) >= 2:
        figure_out_dir = sys.argv[1]
    if figure_out_dir is not None:
        print(f'saving to {figure_out_dir}')

    colors = use_report_sh_style(
        4.5, figheight=3, interactive=figure_out_dir is None, advanced_latex=True)

    # Params
    qx = 2 * np.pi / 2
    qy = 2 * np.pi / 3

    L = 10
    N = 1001

    # The base data
    X, Y = np.meshgrid(np.linspace(-L, L, N), np.linspace(-L, L, N))

    density = 2 + np.cos(X * qx) + np.cos(Y * qy)

    # Plotting
    fig, axs = plt.subplots(2, 2, width_ratios=(
        1, 3), height_ratios=(1, 3), sharex='col', sharey='row', constrained_layout=True)
    axs[0, 0].remove()
    x_ax = axs[0, 1]
    y_ax = axs[1, 0]
    d_ax = axs[1, 1]

    pcm = d_ax.pcolormesh(X, Y, density, cmap='Grays', rasterized=True)
    x_ax.plot(X[-1, :], np.cos(X * qx)[-1, :])
    y_ax.plot(np.cos(Y * qy)[:, 0], Y[:, 0])

    d_ax.set_xlabel('x')
    d_ax.set_ylabel('y')
    fig.colorbar(pcm, ax=d_ax,
                 label='density, $\\rho$')

    d_ax.set_xlim(-L, L)
    d_ax.set_ylim(-L, L)
    d_ax.set_aspect('equal')
    d_ax.yaxis.set_label_position("right")
    d_ax.yaxis.tick_right()

    if figure_out_dir is not None:
        fig.savefig(path.join(figure_out_dir, 'layers_example.pdf'))
    else:
        plt.show()
