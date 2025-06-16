"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.title("Test Plots MA")

plots_dir = "ariadne-szenarienreport-pypsa-de-final/Plots_MA"

if not plots_dir.exists():
    st.warning(
        "No plot directory found. Execute `Test_Plots_MA.ipynb` or `Test_Plots_MA.py` to create plots."
    )
else:
    html_files = sorted(plots_dir.glob("*.html"))
    if not html_files:
        st.warning(f"No HTML plots found in {plots_dir}")
    else:
        names = [f.name for f in html_files]
        choice = st.selectbox("Select plot", names)
        html = html_files[names.index(choice)].read_text()
        components.html(html, height=600, scrolling=True)
"""      
import streamlit as st
import plotly.io as pio
import os

st.set_page_config(layout="wide")

# Titel und Einleitung
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("""
Select a plot to display the corresponding plotly graphic.
""")

# Dropdowns für Szenario und Jahr
szenarien = ["plot_discharge_capacity_line", "plot_energy_capacity_line", "plot_annual_elec_line", "plot_energy_capacity_stacked_balken", "plot_discharge_capacity_stacked_balken", "plot_annual_elec_stacked_balken"]
#jahre = list(range(2020, 2051, 5))

scenario = st.selectbox("Szenario wählen:", szenarien)
#year = st.selectbox("Jahr wählen:", jahre)

# Dateiname basierend auf Auswahl
filename = f"{scenario}.html"
#filepath = os.path.join("Plots_MA", filename)
filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)


# HTML-Plot einbinden
if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1200, width=1200, scrolling=True)
else:
    st.error(f"Die Datei `{filename}` wurde nicht gefunden.")

# Optional: Begleittext
#st.markdown(f"""
#**Hinweis:** Diese Grafik zeigt das Szenario **{scenario}** für das Jahr ****.
#Weitere Details siehe Kapitel XY der Arbeit.
#""")
