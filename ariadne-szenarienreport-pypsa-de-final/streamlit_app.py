import streamlit as st
import os

st.set_page_config(layout="wide")

# Titel und Einleitung
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("Select a category from the menu on the left and choose the desired plot in the main area.")

# -- Sidebar-Menü --
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

# Kategorie auswählen
category = st.sidebar.selectbox("Category", list(options.keys()))

# Dropdown und Plot für die ausgewählte Kategorie
cfg = options[category]
selected_plot = st.selectbox(cfg["label"], cfg["plots"])

def show_plot(plot_name):
    filename = f"{plot_name}.html"
    filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, width=1200, scrolling=True)
    else:
        st.error(f"Die Datei `{filename}` wurde nicht gefunden.")

# Header nur zur Klarheit
st.header(category)
show_plot(selected_plot)
