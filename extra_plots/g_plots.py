from analysisScripts.base import *

data_dir = '~/Projects/MPhys/data/240110_LGMtest1'
dL0_path = path.join(data_dir, 'tmpL0_idk_not_bad_actually')
dL2_path = path.join(data_dir, 'tmpL2_seems_best_to_me')
dL3_path = path.join(data_dir, 'tmpL3_resetdg3')
figure_out_dir = '../latex/figures/misc'

if __name__ == "__main__":
    save_fig = False
    if len(sys.argv) >= 2:
        if eval(sys.argv[1]):
            save_fig = True
    if save_fig:
        print(f'saving to {figure_out_dir}')

    colors = use_report_sh_style(6, figheight=2.9, interactive=not save_fig, advanced_latex=True)

    dt = 0.001
    data0 = SmecticDataReader(dL0_path).get_eig_averages()
    data2 = SmecticDataReader(dL2_path).get_eig_averages()
    data3 = SmecticDataReader(dL3_path).get_eig_averages()

    fig, ax = plt.subplots()

    times0 = data0.index * dt
    times2 = data2.index * dt
    times3 = data3.index * dt

    ax.plot(times0, data0.g_norm, '-+', color=colors[0], label='no LGM')
    ax.plot(times2, data2.g_norm, '-+', color=colors[1], label='Soft constraints')
    ax.plot(times3, data3.g_norm, '-+', color=colors[2], label='Mihajlovic multiplier')

    ax.set_ylim(0, max(data3.g_norm) * 1.1)
    ax.legend()

    if save_fig:
        fig.savefig(path.join(figure_out_dir, 'g_plots_comp.pdf'))
    else:
        plt.show()
