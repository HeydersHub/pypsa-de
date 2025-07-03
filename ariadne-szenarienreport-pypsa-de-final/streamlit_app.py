import streamlit as st
import plotly.io as pio
import os

st.set_page_config(layout="wide")

# Titel und Einleitung
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("""
Select a plot to display the corresponding plotly graphic.
""")

# --- Dropdown 1 (bereits vorhanden) ---
szenarien = [
    "line_plot_annual_elec", "line_plot_discharge_capacity", "line_plot_energy_capacity",
    "stacked_bar_plot_annual_elec", "stacked_bar_plot_discharge_capacity", "stacked_bar_plot_energy_capacity",
    "plot_e2p_ratio", "plot_cycles"
]
scenario = st.selectbox("Choose Battery Power-, Energy- and annual Discharge Capacity Plots:", szenarien)

# --- Dropdown 2 (neu) ---
additional_plots1 = [
    "plot_daily_battery__dispatch", "plot_weekly_battery_dispatch", "plot_monthly_battery_dispatch",
    "plot_annual_battery_dispatch", "plot_annual_dispatch_all_technologies", "plot_monthly_V2G_power_dispatch",
    "plot_monthly_V2G_energy_dispatch",  # <- hier deine echten Dateinamen einfügen
]
extra1 = st.selectbox("Choose Battery Dispatch Plots:", additional_plots1)

# --- Dropdown 3 (neu) ---
additional_plots2 = [
    "plot_stacked_bar_RES_capacity", "plot_line_RES_capacity_Technologiemix",  # <- hier deine echten Dateinamen einfügen
]
extra2 = st.selectbox("Choose RES and other Flexibilities Plots:", additional_plots2)

# --- Dropdown 4 (neu) ---
additional_plots3 = [
    "plot_price_daily", "plot_price_year" # <- hier deine echten Dateinamen einfügen
]
extra3 = st.selectbox("Choose Price Plots:", additional_plots3)


# Funktion zum Einbinden einer HTML-Datei
def show_plot(plot_name):
    filename = f"{plot_name}.html"
    filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, width=1200, scrolling=True)
    else:
        st.error(f"Die Datei `{filename}` wurde nicht gefunden.")

# Anzeige der ausgewählten Plots
st.header("1. Battery Power-, Energy- and annual Discharge Capacity Plots")
show_plot(scenario)

st.header("2. Battery Dispatch Plots")
show_plot(extra1)

st.header("3. RES and other Flexibilities Plots")
show_plot(extra2)

st.header("4. Price Plots")
show_plot(extra3)   
