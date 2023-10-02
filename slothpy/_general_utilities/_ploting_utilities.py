from numpy import linspace
from matplotlib.colors import LinearSegmentedColormap
from cycler import cycler
import matplotlib.cm


def colour_map(name):
    """
    Creates matplotlib colour map object.

    Parameters
    ----------
    name: Unity["BuPi", "rainbow", "dark_rainbow", "light_rainbow",
        "light_rainbow_alt", "BuOr", "BuYl", "BuRd", "GnYl", "PrOr", "GnRd", "funmat", "NdCoN322bpdo",
        "NdCoNO222bpdo", "NdCoI22bpdo", "viridis", "plasma", "inferno", "magma", "cividis"] or list[str]
        One of defined names for colour maps: BuPi, rainbow, dark_rainbow, light_rainbow,light_rainbow_alt, BuOr,
        BuYl, BuRd, GnYl, PrOr, GnRd, funmat, NdCoN322bpdo, NdCoNO222bpdo, NdCoI22bpdo,
        viridis, plasma, inferno, magma, cividis or list of HTML colour codes from which colour map will be created
        by interpolation of colours between ones on a list. For predefined names modifiers can be applied: _l loops
        the list in a way that it starts and ends with the same colour, _r reverses the list.
    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap
        Matplotlib's colour map object used for plotting.
    Raises
    ------
    ValueError
        If input is not acceptable for creating colour map from list of colour codes or name of predefined colour
        map was incorrectly written.
    """
    cmap_list = []
    reverse = False
    loop = False
    if name[-2:] == "_l":
        name = name[:-2]
        loop = True

    if name[-2:] == "_r":
        reverse = True
        name = name[:-2]
    if type(name) == list:
        cmap_list = name
    elif name == "BuPi":
        cmap_list = [
            "#0091ad",
            "#1780a1",
            "#2e6f95",
            "#455e89",
            "#5c4d7d",
            "#723c70",
            "#a01a58",
            "#b7094c",
        ]
    elif name == "rainbow":
        cmap_list = [
            "#ff0000",
            "#ff8700",
            "#ffd300",
            "#deff0a",
            "#a1ff0a",
            "#0aff99",
            "#0aefff",
            "#147df5",
            "#580aff",
            "#be0aff",
        ]
    elif name == "dark_rainbow":
        cmap_list = [
            "#F94144",
            "#F3722C",
            "#F8961E",
            "#F9844A",
            "#F9C74F",
            "#90BE6D",
            "#43AA8B",
            "#4D908E",
            "#577590",
            "#277DA1",
        ]
    elif name == "light_rainbow":
        cmap_list = [
            "#FFADAD",
            "#FFD6A5",
            "#FDFFB6",
            "#CAFFBF",
            "#9BF6FF",
            "#A0C4FF",
            "#BDB2FF",
            "#FFC6FF",
        ]
    elif name == "light_rainbow_alt":
        cmap_list = [
            "#FBF8CC",
            "#FDE4CF",
            "#FFCFD2",
            "#F1C0E8",
            "#CFBAF0",
            "#A3C4F3",
            "#90DBF4",
            "#8EECF5",
            "#98F5E1",
            "#B9FBC0",
        ]
    elif name == "BuOr":
        cmap_list = [
            "#03045e",
            "#023e8a",
            "#0077b6",
            "#0096c7",
            "#00b4d8",
            "#ff9e00",
            "#ff9100",
            "#ff8500",
            "#ff6d00",
            "#ff5400",
        ]
    elif name == "BuRd":
        cmap_list = [
            "#033270",
            "#1368aa",
            "#4091c9",
            "#9dcee2",
            "#fedfd4",
            "#f29479",
            "#ef3c2d",
            "#cb1b16",
            "#65010c",
        ]
    elif name == "BuYl":
        cmap_list = [
            "#184e77",
            "#1e6091",
            "#1a759f",
            "#168aad",
            "#34a0a4",
            "#52b69a",
            "#76c893",
            "#99d98c",
            "#b5e48c",
            "#d9ed92",
        ]
    elif name == "GnYl":
        cmap_list = [
            "#007f5f",
            "#2b9348",
            "#55a630",
            "#80b918",
            "#aacc00",
            "#bfd200",
            "#d4d700",
            "#dddf00",
            "#eeef20",
            "#ffff3f",
        ]
    elif name == "PrOr":
        cmap_list = [
            "#240046",
            "#3c096c",
            "#5a189a",
            "#7b2cbf",
            "#9d4edd",
            "#ff9e00",
            "#ff9100",
            "#ff8500",
            "#ff7900",
            "#ff6d00",
        ]
    elif name == "GnRd":
        cmap_list = [
            "#005C00",
            "#2D661B",
            "#2A850E",
            "#27A300",
            "#A9FFA5",
            "#FFA5A5",
            "#FF0000",
            "#BA0C0C",
            "#751717",
            "#5C0000",
        ]
    elif name == "funmat":
        cmap_list = [
            "#1f6284",
            "#277ba5",
            "#2f94c6",
            "#49a6d4",
            "#6ab6dc",
            "#ffe570",
            "#ffe15c",
            "#ffda33",
            "#ffd20a",
            "#e0b700",
        ]
    elif name == "NdCoN322bpdo":
        cmap_list = [
            "#00268f",
            "#0046ff",
            "#009cf4",
            "#E5E4E2",
            "#ede76d",
            "#ffb900",
            "#b88700",
        ]
    elif name == "NdCoNO222bpdo":
        cmap_list = [
            "#A90F97",
            "#E114C9",
            "#f9bbf2",
            "#77f285",
            "#11BB25",
            "#0C831A",
        ]
    elif name == "NdCoI22bpdo":
        cmap_list = [
            "#075F5F",
            "#0B9898",
            "#0fd1d1",
            "#FAB3B3",
            "#d10f0f",
            "#720808",
        ]
    if cmap_list:
        if reverse:
            cmap_list.reverse()
        if loop:
            new_cmap_list = cmap_list.copy()
            for i in range(len(cmap_list)):
                new_cmap_list.append(cmap_list[-(i + 1)])
            cmap_list = new_cmap_list
        cmap = LinearSegmentedColormap.from_list("", cmap_list)
    elif name == "viridis":
        cmap = matplotlib.cm.viridis
        if reverse:
            cmap = matplotlib.cm.viridis_r
    elif name == "plasma":
        cmap = matplotlib.cm.plasma
        if reverse:
            cmap = matplotlib.cm.plasma_r
    elif name == "inferno":
        cmap = matplotlib.cm.inferno
        if reverse:
            cmap = matplotlib.cm.inferno_r
    elif name == "magma":
        cmap = matplotlib.cm.magma
        if reverse:
            cmap = matplotlib.cm.magma_r
    elif name == "cividis":
        cmap = matplotlib.cm.cividis
        if reverse:
            cmap = matplotlib.cm.cividis_r
    else:
        raise ValueError(
            f"""There is no such colour map as {name} use one of those: BuPi, rainbow, dark_rainbow, light_rainbow, 
                light_rainbow_alt, BuOr, BuYl, BuRd, GnYl, PrOr, GnRd, funmat, NdCoN322bpdo, NdCoNO222bpdo,
                NdCoI22bpdo, viridis, plasma, inferno, magma, cividis or enter list of HTML colour codes"""
        ) from None

    return cmap


def _custom_colour_cycler(number_of_colours: int, cmap1: str, cmap2: str):
    """
    Creates colour cycler from two colour maps in alternating pattern, suitable for use in matplotlib plots.

    Parameters
    ----------
    number_of_colours: int
        Number of colour in cycle.
    cmap1: str or list[str]
        Input of colour_map function.
    cmap2: str or list[str]
        Input of colour_map function.

    Returns
    -------
    cycler.cycler
        Cycler object created based on two input colour maps.

    Raises
    ------
    ValueError
        If unable to use given inputs. It should not be possible to trigger this error.
    """
    try:
        if number_of_colours % 2 == 0:
            increment = 0
            lst1 = colour_map(cmap1)(
                linspace(0, 1, int(number_of_colours / 2))
            )
            lst2 = colour_map(cmap2)(
                linspace(0, 1, int(number_of_colours / 2))
            )
            colour_cycler_list = []
            while increment < number_of_colours:
                if increment % 2 == 0:
                    colour_cycler_list.append(lst1[int(increment / 2)])
                else:
                    colour_cycler_list.append(lst2[int((increment - 1) / 2)])
                increment += 1
        else:
            increment = 0
            lst1 = colour_map(cmap1)(
                linspace(0, 1, int((number_of_colours / 2) + 1))
            )
            lst2 = colour_map(cmap2)(
                linspace(0, 1, int(number_of_colours / 2))
            )
            colour_cycler_list = []
            while increment < number_of_colours:
                if increment % 2 == 0:
                    colour_cycler_list.append(lst1[int(increment / 2)])
                else:
                    colour_cycler_list.append(lst2[int((increment - 1) / 2)])
                increment += 1
        return cycler(color=colour_cycler_list)
    except Exception as exc:
        raise ValueError(
            "If you see this message function you try to use has an error."
            " Contact us at email:"
        )
    # TODO: mail kontaktowy
