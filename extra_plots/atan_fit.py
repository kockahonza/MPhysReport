import matplotlib.widgets as mws

from analysisScripts.twist_analysis.base import *

colors = use_sh_style(7.2, interactive=True)

if __name__ == "__main__":
    Xs = np.linspace(0, 1, 100)

    fig = plt.figure()
    gs = GridSpec(2, 1, height_ratios=[1/30, 1])
    gui_ax = fig.add_subplot(gs[0, 0])
    ax = fig.add_subplot(gs[1, 0])

    def plot(a):
        Ys = fit_atan_fvec(Xs, a)

        return ax.plot(Xs, Ys, '.-', color=colors[0])

    global ax_objs
    ax_objs = plot(1)

    # Setup up GUI/bar
    sld = mws.Slider(ax=gui_ax,
                     label='Time',
                     valmin=0,
                     valmax=100,
                     valstep=0.0000000001,
                     valinit=1
                     )

    def update(val):
        global ax_objs
        for ax_obj in ax_objs:
            ax_obj.remove()
        ax_objs = plot(val)

    sld.on_changed(update)
    plt.show()
