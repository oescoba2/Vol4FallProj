from typing import List
from numpy.typing import ArrayLike
import matplotlib.pyplot as plt

def plot(t_vals:ArrayLike=[], sol_vals:ArrayLike=[], chemo_days:List=[],
         line_color:str='blue', chemo_line_color:str='red',
         chemo_line_alpha:float=1, chemo_linewidth:float=0.8,
         title:str="Growth Model", xlabel:str='$t$ (Days)', ylabel:str='Number of Cells', 
         normal_plot:bool=True, loglog:bool=False, semilogy:bool=False,
         semilogx:bool=False, plot_all:bool=False, sol:ArrayLike=[], save:bool=False, 
         fig_name:str='./images/image.pdf') -> None:
    """This functions accepts data and other parameters to make a plot
    showing the relationship between the t_vals (time values) and 
    sol_vals (the solution values for each time value). It can make a 
    full loglog plot, a semilogy plot, or a normal plot according to
    the booleans specified.
    
    Parameters:
        - t_vals (ArrayLike): the x-axis values, which correspond to
                              the time values of the ODE
        - sol_vals (ArrayLike): the y-axis values, which correspond to
                                values the ODE solution takes at certain
                                time values
        - chemo_days (List): a list indicating the time-values where a
                             patient is administered a chemotherapy dose
        - line_color (str): the color of the line of the ODE solution.
                            Defaulted to blue.
        - chemo_line_color (str): the color of the line indicating the
                                  day a chemotherapy dose is administered
        - chemo_line_alpha (float): the transparency of the chemo vertical
                                    line. Defaulted to 0.7.
        - chemo_linewidth (float): the width of the chemo vertical line. 
                                   Defaulted to 1.
        - title (str): the title of the plot. Defaulted to 'Growth Model'
        - xlabel (str): the title for the x-axis. Defaulted to 't'.
        - ylabel (str): the title for the y-axis. Defaulted to 'Tumor Burden'.
        - normal_plot (bool): whether to plot all the data in a normal plot.
                              Defaulted to True.
        - loglog (bool): whether to plot all the data in a loglog plot. Defa-
                         ulted to False. If you want either x or y (not both)
                         use semilogy or semilogx boolean.
        - semilogy (bool): whether to plot the y-axis data in logscale and 
                           x-axis data as normal. Defaulted to False.
        - semilogx (bool): whether to plot the x-axis data in logscale and
                           y-axis data as normal. Defaulted to False.
        - plot_all (bool): whether to plot all of the data
        - sol (ArrayLike): the scipy.integrate Bunch object containing all
                           the arrays of the ODE system
        - save (bool): whether to save the image to a pdf. Defaulted to False.
        - fig_name (str): the name of the saved pdf file containing the image.
                          Defaulted to './images/image.pdf'.

    Returns:
        - None
    """
    
    # Check input
    if not isinstance(normal_plot, bool):
        raise TypeError(f"Expected a boolean. Got: {type(normal_plot)}")
    if not isinstance(loglog, bool):
        raise TypeError(f"Expected a boolean. Got: {type(loglog)}")
    if not isinstance(semilogy, bool):
        raise TypeError(f"Expected a boolean. Got: {type(semilogy)}")
    if len(chemo_days) == 0:
        raise ValueError("Expected a list of values but got an empty list")
    ax = plt.subplot(111)

    if loglog:
        normal_plot = False
        semilogy = False
        semilogx = False

    elif semilogy:
        normal_plot = False
        loglog = False
        semilogx = False

    elif semilogx:
        normal_plot = False
        loglog = False
        semilogy = False

    # Plot data in normal plot
    if normal_plot:

        if not plot_all:
            ax.plot(t_vals, sol_vals, color=line_color, label='Population of Cells')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')
                
            plt.show()

        else:
            tumor, NK, CB8 = sol.y[0], sol.y[1], sol.y[2]
            tot_cells = tumor + NK + CB8
            t_vals = sol.t
            ax.plot(t_vals, tumor/tot_cells, color='blue', label='Tumor')
            ax.plot(t_vals, NK/tot_cells, color='orange', label='NK')
            ax.plot(t_vals, CB8/tot_cells, color='green', label='CB8$^+$')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')

            plt.show()

    # Plot all data in loglog
    elif loglog:
            
        if not plot_all:
            ax.loglog(t_vals, sol_vals, color=line_color, label='Population of Cells')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')

            plt.show()

        else:
            tumor, NK, CB8 = sol.y[0], sol.y[1], sol.y[2]
            tot_cells = tumor + NK + CB8
            t_vals = sol.t
            ax.loglog(t_vals, tumor/tot_cells, color='blue', label='Tumor')
            ax.loglog(t_vals, NK/tot_cells, color='orange', label='NK')
            ax.loglog(t_vals, CB8/tot_cells, color='green', label='CB8$^+$')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')

            plt.show()

    # Plot only the y-data in logscale
    elif semilogy:

        if not plot_all:
            ax.semilogy(t_vals, sol_vals, color=line_color, label='Population of Cells')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')

            plt.show()

        else:
            tumor, NK, CB8 = sol.y[0], sol.y[1], sol.y[2]
            tot_cells = tumor + NK + CB8
            t_vals = sol.t
            ax.semilogy(t_vals, tumor/tot_cells, color='blue', label='Tumor')
            ax.semilogy(t_vals, NK/tot_cells, color='orange', label='NK')
            ax.semilogy(t_vals, CB8/tot_cells, color='green', label='CB8$^+$')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')
            plt.show()

    # Plot only the x-data in a logscale
    elif semilogx:
        if not plot_all:
            ax.semilogx(t_vals, sol_vals, color=line_color, label='Population of Cells')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')

            plt.show()

        else:
            tumor, NK, CB8 = sol.y[0], sol.y[1], sol.y[2]
            tot_cells = tumor + NK + CB8
            t_vals = sol.t
            ax.semilogx(t_vals, tumor/tot_cells, color='blue', label='Tumor')
            ax.semilogx(t_vals, NK/tot_cells, color='orange', label='NK')
            ax.semilogx(t_vals, CB8/tot_cells, color='green', label='CB8$^+$')
            for i, chemo_day in enumerate(chemo_days):
                if i==0:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color, label='Day of Chemo Dosage')
                else:
                    ax.axvline(x=chemo_day, alpha=chemo_line_alpha, linewidth=chemo_linewidth, linestyle ="--", color=chemo_line_color)

            # Plot stuff
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.legend()

            if save:
                plt.savefig(fig_name, format='pdf')
            plt.show()
    
    else:
        raise ValueError(f"Expected only one boolean to be true in order to make plot. Got {normal_plot} and {semilogy} and {loglog}.")