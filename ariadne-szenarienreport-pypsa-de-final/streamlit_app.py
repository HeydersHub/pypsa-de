import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")

# Titel und Einleitung
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("Select a category from the menu on the left and choose the desired plot in the main area.")

# -- Definition der Optionen und Plots pro Kategorie --
options = {
    "1. Battery Power/Energy/Discharge Capacity": {
        "label": "Choose Battery Power-, Energy- and annual Discharge Capacity Plots:",
        "plots": [
            "line_plot_annual_elec",
            "line_plot_discharge_capacity",
            "line_plot_energy_capacity",
            "plot_e2p_ratio",
            "plot_cycles",
            "stacked_bar_plot_annual_elec",
            "stacked_bar_plot_discharge_capacity",
            "stacked_bar_plot_energy_capacity",
        ]
    },
    "2. Battery Dispatch": {
        "label": "Choose Battery Dispatch Plots:",
        "plots": [
            "plot_daily_battery__dispatch",
            "plot_weekly_battery_dispatch",
            "plot_monthly_battery_dispatch",
            "plot_annual_battery_dispatch",
            "plot_annual_dispatch_all_technologies",
            "plot_monthly_V2G_power_dispatch",
            "plot_monthly_V2G_energy_dispatch"
        ]
    },
    "3. RES & Flexibilities": {
        "label": "Choose RES and other Flexibilities Plots:",
        "plots": [
            "plot_stacked_bar_RES_capacity",
            "plot_line_RES_capacity_Technologiemix"
        ]
    },
    "4. Price Plots": {
        "label": "Choose Price Plots:",
        "plots": [
            "plot_price_daily",
            "plot_price_year"
        ]
    }
}

# -- Sidebar-Navigation mit streamlit-option-menu --
with st.sidebar:
    category = option_menu(
        menu_title=None,                        # keine Überschrift
        options=list(options.keys()),          # die vier Kategorien
        icons=["battery-charging",             # Icons optional
               "speedometer2",
               "graph-up",
               "currency-dollar"],
        menu_icon="cast",                      # Icon über der Liste (optional)
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#e0e0e0"},
            "nav-link-selected": {"background-color": "#d0e1ff", "font-weight": "bold"},
        }
    )

# -- Dropdown für die gewählte Kategorie im Hauptbereich --
cfg = options[category]
selected_plot = st.selectbox(cfg["label"], cfg["plots"])

# Funktion zum Einbinden der HTML-Datei
def show_plot(plot_name):
    filename = f"{plot_name}.html"
    filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, width=1200, scrolling=True)
    else:
        st.error(f"Die Datei `{filename}` wurde nicht gefunden.")

# Plot anzeigen
st.header(category)
show_plot(selected_plot)
