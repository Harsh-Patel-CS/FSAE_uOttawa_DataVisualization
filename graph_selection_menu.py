# Harsh Patel

#Libraries
import dearpygui.dearpygui as dpg

#Modules
import file_options


def graph_selection_menu(x_pos, y_pos, ht, wd):
    """Create a window for graph selection menu.


    Args:
        x_pos (int): x position wanted for the window.
        y_pos (int): y position wanted for the window.
        ht (int): height wanted for the window.
        wd (int): width wanted for the window.


    Returns:
        None, Creates a new window.
    """

    with dpg.window(pos=(x_pos, y_pos), height=ht, width=wd):

        with dpg.table(header_row=False,
                       policy=dpg.mvTable_SizingFixedFit,
                       no_host_extendX=True,                
                       borders_innerV=False,                   # set everything below to True to see table lines
                       borders_innerH=False,
                       borders_outerV=False,
                       borders_outerH=False,
                       ):

            dpg.add_table_column(width_stretch=True, init_width_or_weight=1.0)
            dpg.add_table_column(width_fixed=True, init_width_or_weight=0.0)
            dpg.add_table_column(width_stretch=True, init_width_or_weight=1.0)
            # middle column width is fixed, side columns are variable and will fill remaning space, keeping middle column centered

            for r in range(9):

                with dpg.table_row():
                    dpg.add_spacer()

                    if r == 3:

                        with dpg.group():  # allows vertical stacking of widgets within one cell

                            path_display = dpg.add_input_text(hint="Selected File Path", readonly=True, width=300)
                            file_path = dpg.add_button(label="Choose File", callback=lambda: file_options.choose_file(path_display))

                    elif r == 1:

                        graph_name = dpg.add_input_text(hint="Enter Graph Name", width=300)

                    elif r == 5:

                        graph_type = dpg.add_combo(
                            ["Line Graph", "Bar Chart", "Histogram", "Scatter Plot", "Pie Chart", "Heat Map"],
                            default_value="Choose Type of Graph",
                        )

                    elif (r == 7):

                        filter_type = dpg.add_combo(
                            ["High-Pass", "Low-Pass", "Band-Pass", "None"],
                            default_value="Choose Type of Filter",
                        )
                        dpg.add_button(label="Submit", callback=name_check, user_data=(graph_name, path_display, graph_type, filter_type))

                    else:

                        dpg.add_spacer(height=(ht - 150) / 6)  # vertical spacing between the rows that include widgets


def name_check(sender, app_data, user_data):
    """Verifiy the user entered a name.


    Args:
        sender (Not Used):
        app_data (Not Used):
        user_data (tuple): Expected Values:
            - "name" (input text widget): widget containing current name user entered.
            - "file_path" (input text widget): widget containing current chosen file path.
            - "graph_type" (combo widget): the menu widget for types of graphs.
            - "filter_type" (combo widget): the menu widget for types of filters.


    Returns:
        None, Calls file_path_check function.
    """

    name, file_path, graph_type, filter_type = user_data
    name = dpg.get_value(name)

    if (name == ""):

        if not dpg.does_item_exist("ask_name"):

            with dpg.window(label="Name", modal=True, tag="ask_name", no_title_bar=True, pos=[600, 400]):

                dpg.add_text("Please Enter A Name For The Graph!")
                dpg.add_separator()
                dpg.add_spacer(height=5)
                name_input = dpg.add_input_text(hint="Enter Graph Name", width=300)
                dpg.add_spacer(height=5)
                dpg.add_button(label="OK", width=75, callback=lambda: name_check(None, None, (name_input, file_path, graph_type, filter_type)))

    else:

        user_data = (name, file_path, graph_type, filter_type)
        dpg.delete_item("ask_name")
        dpg.split_frame()  # force Dpg to generate a frame and load new widget states, prevents multiple modals
        file_path_check(user_data)


def file_path_check(user_data):
    """Verifiy the user chose a file path.


    Args:
        user_data (tuple): Expected Values:
            - "name" (str): name of the graph.
            - "file_path" (input text widget): widget containing current chosen file path.
            - "graph_type" (combo widget): the menu widget for types of graphs.
            - "filter_type" (combo widget): the menu widget for types of filters.


    Returns:
        None, Calls graph_type_check function.
    """

    name, file_path, graph_type, filter_type = user_data
    file_path = dpg.get_value(file_path)

    if (file_path == ""):

        if not dpg.does_item_exist("ask_file"):

            with dpg.window(label="File Path", modal=True, tag="ask_file", no_title_bar=True, pos=[600, 400]):

                dpg.add_text("Please Choose A File For the Graph Data!")
                dpg.add_separator()
                dpg.add_spacer(height=5)
                path_display = dpg.add_input_text(hint="Selected File Path", readonly=True, width=300)
                file_path_button = dpg.add_button(label="Choose File", callback=lambda: file_options.choose_file(path_display))
                dpg.add_spacer(height=5)
                dpg.add_button(label="OK", width=75, callback=lambda: file_path_check((name, path_display, graph_type, filter_type)))

    else:

        user_data = (name, file_path, graph_type, filter_type)
        dpg.delete_item("ask_file")
        dpg.split_frame()  # force Dpg to generate a frame and load new widget states, prevents multiple modals
        graph_type_check(user_data)


def graph_type_check(user_data):
    """Checks if graph type and filter type are choosen and compatiable.


    Args:
        user_date (tuple): Expected Values:
            - "name" (str): name of the graph.
            - "file_path" (str): file path of csv containing data.
            - "graph_type" (combo widget): the menu widget for types of graphs.
            - "filter_type" (combo widget): the menu widget for types of filters.


    Returns:
        None, Calls make_graph function.
    """

    valid_graph_filter_pairs = {"Line Graph": ["High-Pass", "Low-Pass", "Band-Pass", "None"],
                                "Bar Chart": ["None"],
                                "Histogram": ["None"],
                                "Scatter Plot": ["High-Pass", "Low-Pass", "Band-Pass", "None"],
                                "Pie Chart": ["None"],
                                "Heat Map": ["High-Pass", "Low-Pass", "Band-Pass", "None"]
                                }

    name, file_path, graph_type, filter_type = user_data
    graph_type = dpg.get_value(graph_type)
    filter_type = dpg.get_value(filter_type)

    if (graph_type not in list(valid_graph_filter_pairs.keys()) or filter_type not in valid_graph_filter_pairs[graph_type]):

        if not dpg.does_item_exist("ask_graph"):

            with dpg.window(label="Type of Graph", modal=True, tag="ask_graph", no_title_bar=True, pos=[600, 400]):

                dpg.add_text("Please Reselect The Type of Graph!")
                dpg.add_separator()
                dpg.add_spacer(height=5)
                graph_type = dpg.add_combo(["Line Graph", "Bar Chart", "Histogram", "Scatter Plot", "Pie Chart", "Heat Map"],
                                           default_value="Choose Type of Graph")

                filter_type = dpg.add_combo(["High-Pass", "Low-Pass", "Band-Pass", "None"],
                                            default_value="Choose Type of Filter")

                dpg.add_spacer(height=5)
                dpg.add_button(label="OK", width=75, callback=lambda: graph_type_check((name, file_path, graph_type, filter_type)))

    else:

        dpg.delete_item("ask_graph")
        dpg.split_frame()  # force Dpg to generate a frame and load new widget states, close modal before making graph
        #make_graph(name, file_path, graph_type, filter_type)
