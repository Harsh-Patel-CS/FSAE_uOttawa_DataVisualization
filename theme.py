import dearpygui.dearpygui as dpg

dpg.create_context()

# ----------------------------
# NEON DARK THEME
# ----------------------------
with dpg.theme() as neon_theme:
    with dpg.theme_component(dpg.mvAll):

        # backgrounds
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (12, 15, 30))
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (18, 22, 45))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (25, 30, 60))

        # neon accents
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 200, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 150, 255))

        # text
        dpg.add_theme_color(dpg.mvThemeCol_Text, (210, 220, 255))

        # borders / highlights
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 200, 255))

        # rounding for modern look
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 10)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 10)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 6)

dpg.bind_theme(neon_theme)


# ----------------------------
# SAMPLE DATA (REPLACE THESE)
# ----------------------------
x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 1, 3, 2, 5, 4]

# replace with your own lists later:
# x_data = [...]
# y_data = [...]


# ----------------------------
# DASHBOARD WINDOW
# ----------------------------
with dpg.window(label="Neon Dashboard", width=900, height=500):

    dpg.add_text("Performance Monitor")
    dpg.add_spacer(height=10)

    # panel container
    with dpg.child_window(height=400, border=True):

        # line graph
        with dpg.plot(label="Line Graph", height=-1, width=-1):

            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="X")

            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Y")

            dpg.add_line_series(
                x_data,
                y_data,
                label="Data",
                parent=y_axis
            )
    with dpg.child_window(height=400, border=True, resizable_y=True):

        # line graph
        with dpg.plot(label="Line Graph", height=-1, width=-1):

            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="X")

            y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Y")

            dpg.add_line_series(
                x_data,
                y_data,
                label="Data",
                parent=y_axis
            )

# ----------------------------
# RUN
# ----------------------------
dpg.create_viewport(title="Dark Neon UI", width=900, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()