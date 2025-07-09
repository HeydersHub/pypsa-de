import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")

# Titel und Einleitung
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("Select a category from the menu on the left and choose the desired plot in the main area.")

# -- Definition der Optionen und Plots pro Kategorie --
options = {
    "1. Battery Capacity": {
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
            "plot_e2p_ratio_all_scenarios",
            "plot_cycles_all_scenarios",
            "plot_bereitstellung_all_scenarios",
            "plot_bereitstellung_stacked_balken_alle_szenarien",
            "plot_entladeleistung_final_all_scenarios",
            "plot_entladeleistung_all_scenarios",
            "plot_kapazitaet_all_scenarios",
            "plot_kapazitaet_final_all_scenarios",
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
            "plot_monthly_V2G_energy_dispatch",
            "plot_monthly_V2G_energy_dispatch_High_V2G_Scenario",
            "plot_monthly_V2G_power_dispatch_High_V2G_Scenario",
            "plot_monthly_V2G_energy_dispatch_Low_V2G_Scenario",
            "plot_monthly_V2G_power_dispatch_Low_V2G_Scenario",    
        ]
    },
    "3. RES & Flexibilities": {
        "label": "Choose RES and other Flexibilities Plots:",
        "plots": [
            "plot_stacked_bar_RES_capacity",
            "plot_line_RES_capacity_Technologiemix",
            "plot_stacked_bar_RES_capacity_all_scenarios",
            "plot_stacked_bar_RES_single_solar_capacity_all_scenarios",
            "plot_RES_curtailment"
        ]
    },
    "4. Price Plots": {
        "label": "Choose Price Plots:",
        "plots": [ 
            #"plot_price_daily",
            "plot_price_year",
            "plot_price_yealy_new",
            "plot_price_daily_new",
            "plot_price_duration_curve",
            "plot_price_histogram",
            "plot_price_cov",
            "plot_price_daily_spread",
            
        ]
    }
}

# -- Sidebar-Navigation mit streamlit-option-menu --
with st.sidebar:
    category = option_menu(
        menu_title="Categories",                        
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
            "nav-link-selected": {"background-color": "#000000", "font-weight": "bold"},
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
