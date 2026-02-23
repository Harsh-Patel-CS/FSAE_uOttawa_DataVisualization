# Harsh Patel

#Libraries
import dearpygui.dearpygui as dpg

#Modules
import file_options 
import graph_selection_menu
import image_options
import database_manager

db_manager = database_manager.database_manager()


def main():
    dpg.create_context()


    with dpg.font_registry():
        try:
            font_path = ("C:/Windows/Fonts/segoeui.ttf")  # will fail on non-Windows
            segoe = dpg.add_font(font_path, 18)
            dpg.bind_font(segoe)  # only runs if add_font worked
        except Exception:
            pass


    with dpg.theme() as global_theme:

        with dpg.theme_component(dpg.mvButton):

            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10.0)

    dpg.bind_theme(global_theme)


    dpg.create_viewport(title='Formula uOttawa Telemetry Software', width=800, height=600)


    with dpg.viewport_menu_bar(tag="Main Menu Bar"):  # Menu Bar will be revised and corrected soon

        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Save Project", callback=lambda: file_options.save_project())
            dpg.add_menu_item(label="Load Project", callback=lambda: file_options.load_project())
            
                
        with dpg.menu(label="Graph"):
            dpg.add_menu_item(label="Make New Graph", callback=lambda: graph_selection_menu.graph_selection_menu(400, 150, 450, 770))
                
                

        with dpg.menu(label="Filter"):
            pass
            
        with dpg.menu(label="Trim"):
            pass

        with dpg.menu(label="Correlation"):
            pass


    with dpg.window(tag="Home Window", no_move=True, no_resize=True, pos=(0, 0)):
        
        with dpg.table(header_row=False,
                        policy=dpg.mvTable_SizingFixedFit,
                        no_host_extendX=True,                
                        borders_innerV=False,                # Set the following all to True to see the table lines
                        borders_innerH=False,
                        borders_outerV=False,
                        borders_outerH=False,
                        ):

            dpg.add_table_column(width_stretch=True, init_width_or_weight=1.0)
            dpg.add_table_column(width_fixed=True, init_width_or_weight=0.0)
            dpg.add_table_column(width_stretch=True, init_width_or_weight=1.0)
        

            with dpg.table_row():
                dpg.add_spacer(height=150)
            

            with dpg.table_row():

                dpg.add_spacer()
                dpg.add_image(image_options.import_static_image("Assets/formula_logo.png"), height=150, width=699)


            with dpg.table_row():
                dpg.add_spacer(height=150)


            with dpg.table_row():
                dpg.add_spacer()
                with dpg.group(horizontal=True, horizontal_spacing=4):

                    dpg.add_spacer(width=63)


                    with dpg.group():

                        with dpg.group(horizontal=True):
                            dpg.add_spacer(width=80)
                            dpg.add_text("New Project")

                        dpg.add_image_button(image_options.import_static_image("Assets/plus.png"), background_color=(0,0,0,70), frame_padding=0, width=250, height=250)


                    dpg.add_spacer(width=60)


                    with dpg.group():

                        with dpg.group(horizontal=True):
                            dpg.add_spacer(width=82)
                            dpg.add_text("Load Project")

                        dpg.add_image_button(image_options.import_static_image("Assets/file_icon.png"), background_color=(0,0,0,70), frame_padding=0, width=250, height=250)
                    dpg.add_spacer(width=63)


            with dpg.table_row():
                dpg.add_spacer(height=97)


            with dpg.table_row():
                dpg.add_text(default_value="Version: Pre-alpha", color=[255, 255, 255, 120])
                

    dpg.set_primary_window("Home Window", True)
    dpg.set_viewport_large_icon("Assets/Formula_uottawa.ico")
    dpg.setup_dearpygui()
    dpg.set_viewport_pos([0, 0])
    dpg.show_viewport(maximized=True)  # prevents window sizing and positioning from failing on intital creation
    dpg.start_dearpygui()
    dpg.destroy_context()


main()







