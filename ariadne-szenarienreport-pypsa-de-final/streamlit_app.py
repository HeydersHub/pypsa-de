import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")

# Pfad zur Thesis-PDF
THESIS_PDF_PATH = os.path.join(
    "ariadne-szenarienreport-pypsa-de-final",
    "Thesis_Moritz_Heyder.pdf"
)

def render_thesis_download_button():
    if os.path.exists(THESIS_PDF_PATH):
        with open(THESIS_PDF_PATH, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📄 Download full thesis as PDF",
            data=pdf_bytes,
            file_name="Thesis_Moritz_Heyder.pdf",
            mime="application/pdf",
        )
    else:
        st.warning("Thesis PDF not found on server. Please contact the author.")

# Titel
st.title("Master Thesis: The Role of Utility-scale Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("Navigate through the thesis structure on the left. Select a section to view the relevant plots or text.")

# ------------------------------
# Inhaltsverzeichnis-Struktur
# ------------------------------
toc = {
    "1. Introduction": None,
    "2. Key Driver for Battery Deployment": None,
    "3. Scenarios & Assumptions": None,
    "4. Model Results": {
        # 4.1 mit Unterkapiteln 4.1.1 und 4.1.2
        "4.1 Battery Technology Rollout": {
            "4.1.1 Key Parameters": {
                "label": "Choose plots for key battery parameters (power, energy, ratios, cycles):",
                "plots": [
                    # hier deine Plot-Dateinamen eintragen, z.B.:
                    # "Installed_Power_Capacity_All_Scenarios",
                    # "Installed_Energy_Capacity_All_Scenarios",
                    "FINAL_Battery_Rollout_Base_Scenario",
                    "FINAL_Installed_Energy_Capacity_All_Scenarios",
                    "FINAL_Annual_Battery_Discharge_All_Scenarios",
                ]
            },
            "4.1.2 Dispatch": {
                "label": "Choose plots for annual battery discharge:",
                "plots": [
                    # z.B.:
                    # "Annual_Battery_Discharge_All_Scenarios",
                    # "Annual_Battery_Discharge_Base_Scenario",
                    "FINAL_plot_Dispatch_week_jan_batteries_PV_Wind",
                    "FINAL_plot_Dispatch_week_june_batteries_PV_Wind",
                    "FINAL_plot_Dispatch_annual_batteries",
                    "FINAL_plot_Dispatch_monthly_batteries",
                    "FINAL_Annual_Dispatch_All_technologies",
                ]
            }
        },

        # 4.2 (ohne dritte Ebene)
        "4.2 Vehicle-to-Grid": {
            "label": "Choose V2G-related plots:",
            "plots": [
                # z.B.:
                # "plot_monthly_V2G_power_dispatch",
                # "plot_monthly_V2G_energy_dispatch",
                "FINAL_plot_V2G_Power_Dispatch",
                "FINAL_plot_V2G_Energy_Dispatch",
                "FINAL_plot_V2G_Power_Dispatch_All_Scenarios",
                "FINAL_plot_V2G_Energy_Dispatch_All_Scenarios",
            ]
        },

        # 4.3
        "4.3 Other Storages and Flexibilities": {
            "label": "Choose plots for other storage technologies and flexibility options:",
            "plots": [
                # z.B.:
                # "plot_stacked_bar_RES_capacity",
                # "plot_RES_curtailment",
                "FINAL_Total_Flexibility_Needs_Base_Scenario",
                "FINAL_Total_Flexibility_Needs_All_Scenarios",
                "FINAL_plot_Flex_Contributions_Base_Scenario",
                "FINAL_plot_Daily_Flex_Contributions_All_Scenarios",
                "FINAL_plot_Weekly_Flex_Contributions_All_Scenarios",
                "FINAL_plot_Annual_Flex_Contributions_All_Scenarios",
            ]
        },

        # 4.4
        "4.4 Cost Sensitivity Analysis": {
            "label": "Choose cost sensitivity plots:",
            "plots": [
                # z.B.:
                # "Cost_Sensitivity_Battery_Capacity",
                # "Cost_Sensitivity_Curtailment",
                "FINAL_plot_Sensitivity_Analysis_Base_Scenario",
                "FINAL_Sensitivity_Analysis_Flex_Needs",
                "FINAL_Sensitivity_Analysis_Daily_Flex_Contributions",
                
            ]
        },

        # 4.5 mit dritter Ebene
        "4.5 System Impact": {
            "4.5.1 Price Volatility": {
                "label": "Choose plots illustrating price volatility (PDC, daily spreads, TB spreads):",
                "plots": [
                    # z.B.:
                    # "plot_price_duration_curve",
                    # "plot_price_daily_spread",
                    # "plot_TB_spreads",
                    "FINAL_plot_price_daily_spread",
                    "FINAL_plot_TB_spreads",
                ]
            },
            "4.5.2 Total System Costs": {
                "label": "Choose plots for total system costs:",
                "plots": [
                    # z.B.:
                    # "plot_total_system_costs_all_scenarios",
                    "FINAL_plot_total_system_costs_delta",
                ]
            },
            "4.5.3 PV and Wind Expansion": {
                "label": "Choose plots for PV and wind capacity expansion:",
                "plots": [
                    # z.B.:
                    # "plot_stacked_bar_RES_capacity_all_scenarios",
                    "FINAL_plot_stacked_bar_RES_single_solar_capacity_all_scenarios",
                ]
            },
            "4.5.4 Renewable Curtailment": {
                "label": "Choose plots for renewable curtailment:",
                "plots": [
                    # z.B.:
                    # "plot_RES_curtailment",
                    "FINAL_plot_Rel_RES_Curtailment",
                ]
            }
        },

        # 4.6
        "4.6 Discussion Plots": {
            "label": "Choose visualisations from the discussion section:",
            "plots": [
                # z.B.:
                # "Summary_Battery_Capacity_All_Scenarios",
                # "Summary_System_Impact",
                "Study_Viewer_MA_Utility_scale_GW",
                "Study_Viewer_MA_Utility_scale_GWh",
            ]
        }
    },
    "5. Key Findings & Conclusion": None
}

# ------------------------------
# Sidebar Navigation (3 Ebenen)
# ------------------------------
with st.sidebar:
    main_choice = option_menu(
        menu_title="Thesis Contents",
        options=list(toc.keys()),
        icons=["book", "lightning", "sliders", "bar-chart", "chat-dots"],
        default_index=0,
    )

    sub_choice = None
    sub_sub_choice = None

    if isinstance(toc[main_choice], dict):
        sub_choice = option_menu(
            menu_title=f"{main_choice} – Subsections",
            options=list(toc[main_choice].keys()),
            icons=["battery-charging", "ev-front", "layers", "currency-dollar", "graph-up", "star"],
            default_index=0,
        )

        # Falls dritte Ebene existiert
        node = toc[main_choice][sub_choice]
        if isinstance(node, dict) and "plots" not in node:
            sub_sub_choice = option_menu(
                menu_title=f"{sub_choice} – Subsections",
                options=list(node.keys()),
                icons=["chevron-right" for _ in node],
                default_index=0,
            )


# ------------------------------
# Plot-Funktion
# ------------------------------
def show_plot(plot_name: str):
    filename = f"{plot_name}.html"
    filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, width=1200, scrolling=True)
    else:
        st.error(f"Die Datei `{filename}` wurde nicht gefunden.")

# ------------------------------
# Hilfsfunktion für Auswahl + Download
# ------------------------------
def handle_plot_selection(cfg):
    """Zeigt Selectbox + Plot + Download-Button, falls Plots konfiguriert sind."""
    plots = cfg.get("plots", [])
    if not plots:
        st.info("No plots configured yet for this subsection.")
        return

    selected_plot = st.selectbox(cfg["label"], plots)
    show_plot(selected_plot)

    file_path = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", f"{selected_plot}.html")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            st.download_button(
                label="🔍 Download Plot to view in Full Screen in your browser",
                data=f,
                file_name=f"{selected_plot}.html",
                mime="text/html"
            )

# ------------------------------
# Hauptbereich
# ------------------------------
if sub_choice and sub_sub_choice:
    # 3. Ebene aktiv (z.B. 4.1.1, 4.1.2, 4.5.1–4.5.4)
    cfg = toc[main_choice][sub_choice][sub_sub_choice]
    st.header(f"{main_choice} – {sub_choice} – {sub_sub_choice}")
    handle_plot_selection(cfg)

elif sub_choice:
    # 2. Ebene (z.B. 4.2, 4.3, 4.4, 4.6 oder 4.1 / 4.5 ohne 3. Ebene)
    cfg = toc[main_choice][sub_choice]

    # falls 4.1 oder 4.5 gewählt sind, aber noch keine dritte Ebene (unwahrscheinlich),
    # nur Hinweis anzeigen
    if isinstance(cfg, dict) and "plots" not in cfg:
        st.header(f"{main_choice} – {sub_choice}")
        st.info("Please select a subsection in the sidebar.")
    else:
        st.header(f"{main_choice} – {sub_choice}")
        handle_plot_selection(cfg)

else:
    # Kapitel ohne Untermenü (1, 2, 3, 5)
    st.header(main_choice)

    if main_choice == "1. Introduction":
        st.markdown("""
        
        ### Welcome to my Master's Thesis Dashboard.  
        This Dashboard provides interactive visualizations of the results of my thesis and an overview of the key topics and findings covered.
         
        
        ##### For more detailed information, please refer to the full thesis document which you can download below.

        **Introduction to the thesis topic**
        
        The German energy system is undergoing a fundamental transformation, driven by the urgent need to mitigate climate change.
        This shift necessitates a transition from conventional fossil fuel power plants to renewable energy sources.
        Germany reached a renewable electricity share of more than 60% for the first time in 2024 and has set the targets of 
        achieving an 80% renewable share by 2030 and climate neutrality by 2045. The vast majority of these renewables will be provided by variable
        renewable energy (VRE) sources, primarily PV and wind power. However, this transition also brings new challenges. 
        Unlike traditional power plants, which can be dispatched according to demand, variable renewable energy generation is highly
        dependent on weather conditions. As a result, the need for flexibility in the power system is increasing significantly.
        
        **Problem Statement**
        
        Battery storage systems have emerged as a key solution for providing flexibility. They
        are widely considered an essential component of a future climate-neutral energy system,
        particularly one that relies heavily on PV and wind power. In recent years, the demand
        for battery storage has surged, driven by declining costs and the increasing need for system
        flexibility. This trend is reflected in the current exponential rise in grid connection
        requests for utility-scale battery storage with a planned commissioning
        year before 2030, which now far exceed the projections until 2030 outlined in various
        studies, as illustrated in Figure 2.4 in the thesis. However, existing studies on battery storage deployment 
        present divergent assumptions
        and results, which are discussed in more detail in Chapter 2.2. Some studies lack transparency
        regarding their cost and technology assumptions, making it difficult to compare
        findings. Most of the studies focus on the entire sector-coupled energy system and therefore
        are not placing battery storage as the central subject of investigation which results
        in no comprehensive in-depth analysis regarding battery storage deployment and their
        key deployment driver. Different types of battery storage, such as stationary utility-scale
        storage, home PV battery storage, and mobile vehicle-to-grid-enabled storage are often
        not all included or clearly distinguished or comprehensively analyzed. Furthermore, these
        studies assume a purely market-oriented optimization and neglect potential additional
        revenue streams for battery storage, such as future capacity markets or ancillary system
        services. Moreover, key performance indicators such as the installed power capacity, energy capacity, 
        or annual discharge are often reported inconsistently, which further hinders comparison.
        
        The scenario framework for the 2023 German Grid Development Plan (NEP) does not
        rely on studies which include investment modeling for battery storage but instead applies
        a different methodological approach which relies mainly on the expansion of PV
        and wind power (NEP Szenariorahmen 2023). The 2025 draft scenario framework (NEP
        Szenariorahmenentwurf 2025) for the upcoming NEP notes that its assumptions regarding
        utility-scale battery storage are not based on top-down capacity optimization either,
        instead focusing on existing grid connection requests and market surveys. The report
        highlights that the assumed deployment of power and energy capacities is not supported
        by any further detailed analyses from the transmission system operators (TSOs) and
        that, from today’s perspective, the future deployment of utility-scale batteries remains
        highly uncertain. This further underscores the necessity of deeper investigation into the
        key drivers influencing battery development and possible deployment pathways. Comparing
        these approaches with investment modeling and capacity expansion techniques
        might be helpful complementing the bottom-up reasoning in the NEP.
        
        **Objectives and Research Question**
        
        The central research question that is guiding this thesis is the following:
        
        #### What role will utility-scale battery energy storage systems play in Germany’s energy transition toward climate neutrality by 2045 and what drives their deployment?
     
        The primary goal of this thesis is to outline possible pathways and scenarios for the
        deployment of utility-scale battery energy storage systems. It aims to explore various
        battery-related metrics in depth, highlight their interdependencies, and investigate cost
        sensitivities as well as the elasticity of battery demand. Further, the interplay and substitution
        effects through expansion of other battery technology types, especially prosumer
        home batteries and V2G-enabled EVs will be analyzed.
        
        ### Thesis Objectives

        This thesis addresses four interrelated objectives:

        1. **Quantify deployment pathways for different battery storage technologies.**  
        Develop scenarios for the expansion of utility-scale, decentralized, and mobile (V2G-enabled) battery systems using the open-source 
        capacity expansion model PyPSA-DE.  
        The analysis focuses on the evolution of installed power and energy capacities, annual electricity supply 
        through batteries and other key battery performance indicators while also determining the system’s flexibility needs across target years.

        2. **Analyze substitution effects between battery types and other flexibility options.**  
        Investigate the extent to which other battery types, such as prosumer home batteries and V2G-enabled EVs, can substitute utility-scale battery storage.  
        Furthermore, evaluate the contribution of other energy storage technologies and flexibility options to providing flexibility needs.

        3. **Assess cost sensitivities and the resulting elasticity of utility-scale battery deployment.**  
        Examine how variations in investment costs (CAPEX per kW and per kWh) affect the endogenous deployment of battery storage and identify cost 
        thresholds determining whether expansion becomes elastic or inelastic.  
        Additionally, analyze which technologies substitute utility-scale batteries under high-cost conditions and which are substituted by them in 
        low-cost scenarios.

        4. **Evaluate system-level impacts of battery deployment.**  
        Analyze how changes in battery costs and deployment levels influence renewable curtailment, electricity price volatility, total system costs, and
        the endogenous expansion of wind and PV capacities.  
        A particular focus lies on how price volatility affects the economic viability and investment attractiveness of utility-scale storage systems.
        
        Scenarios for battery storage development in the German energy system up to 2045
        will be created and analyzed using scientifically robust assumptions and the established
        energy system modeling framework PyPSA-DE. In addition to these quantitative objectives,
        the thesis provides a structured review and comparison of existing German energy
        system studies, highlighting differences in assumptions and methodological approaches
        regarding battery modeling. Further, key deployment driver for utility-scale batteries are
        developed to systematically evaluate the results of the model and the model limitations.
        By combining the qualitative assessment with model-based scenario analysis, this thesis
        aims to provide a transparent and reproducible foundation for future grid- and energy
        system planning regarding battery storage.
        
        """)
        
        render_thesis_download_button()

    elif main_choice == "2. Key Driver for Battery Deployment":
        st.markdown("""
Based on a comprehensive review of the current literature, eleven key drivers for utility-scale battery deployment were identified and grouped into 
four overarching categories.

The first category concerns the need for system flexibility. Historically, conventional power plants such as coal and gas units were capable
of adjusting their electricity generation to match demand, thereby reducing the requirement for energy storage. In contrast, variable renewable energy
sources such as solar PV and wind are intermittent and weather dependent, which significantly increases the need for storage to ensure that demand
can be reliably met at all times. 
To what extent can utility-scale batteries contribute to meeting this growing flexibility requirement? Flexibility needs can be distinguished across
different temporal dimensions like daily, weekly, and annual, allowing a clearer differentiation
between the roles of short-term and long-term storage technologies. Batteries are generally classified as short-term storage solutions as further
addressed later in this chapter.

When assessing the potential role of batteries in this context, it is essential to consider competing flexibility options. 
These include other forms of batteries, such as prosumer home batteries and vehicle-to-grid (V2G) solutions, as well as 
alternative storage technologies like pumped hydro storage (PHS), hydrogen, or thermal/heat storage. Demand-side management (DSM) options,
such as smart charging of EVs, flexible operation of heat pumps, or hydrogen production through electrolysis, also contribute to system flexibility.
Moreover, cross-border electricity trade via import and export capacities plays a role in balancing supply and demand.

A second key dimension is economic drivers for battery deployment. The competitiveness of batteries relative to other flexibility technologies
depends on their profitability and business case. Thus, cost trajectories and technological maturity for utility-scale batteries must be
evaluated alongside the market frameworks in which they operate and the specific services they can provide. Particular attention must be paid to
the phenomenon of self-cannibalization, where increasing battery penetration leads to diminishing returns and reduced profitability for 
individual assets. Technical parameters such as lifetime, round-trip efficiency, and the energy-to-power (E2P) ratio also play a critical role,
as they determine both the economic attractiveness and the potential applications of battery storage.

Finally, the regulatory framework and policy environment must be taken into account. Current and future regulatory decisions are pivotal in shaping
the economic viability of different technologies and can either accelerate or hinder the deployment of utility-scale batteries. In this sense,
regulatory frameworks not only influence investment decisions but also guide the overall trajectory of energy system transformation.
        """)

        # ---- Key Drivers: zentrale Datenstruktur mit DEINEN Detailtexten ----
        drivers = [
            {
                "title": "The Need for System Flexibility",
                "bullets": [
                    "Expansion of VRE, especially Wind and PV"
                ],
                "details": """
Germany reached a renewable energy share of more than 60% for the first time in 2024 and has set the targets of achieving an 80% renewable share
by 2030 and climate neutrality by 2045 (Ariadne, 2025). The vast majority of these renewables will be provided by variable renewable energy (VRE)
sources, primarily photovoltaic (PV) and wind power. The integration of such large shares of VRE poses challenges for system stability due to their
variability and limited dispatchability. In this context, flexibility options such as energy storage are expected to play a crucial role.

Several studies have highlighted important thresholds for the deployment of storage technologies. Both Cebulla et al. 2018 and
Thimet and Mavromatidis 2023 argue that once the VRE share surpasses approximately 65–67%, investment in energy storage grows disproportionately, with capacity expansion accelerating
rapidly beyond this point. Specifically, Thimet and Mavromatidis 2023 shows that utility-scale battery storage begins to scale significantly once VRE 
penetration exceeds 65% in the modeled system. This observation is in line with current developments in Germany, where a large amount of grid connection
requests for storage projects are concentrated in the period between 2026 and 2030, suggesting that the markets already anticipate passing this threshold 
in the near future.

The type of VRE mix also has a decisive influence on the required amount of storage. Cebulla et al. 2018 suggests that PV-dominant systems demand
higher levels of storage capacity compared to wind-dominant systems, since short-term storages such as batteries are particularly well-suited to balancing
diurnal fluctuations between day and night. Moreover, the same study indicates that while the demand for storage power capacity (GW) increases linearly
with the share of VRE, the demand for storage energy capacity (GWh) grows exponentially. This finding applies across both short-term and long-term
storage technologies and raises the question of whether a similar pattern can be observed specifically for battery storage.

In parallel, the literature supports the hypothesis that increasing variability on the supply side, coupled with limited flexibility on the demand side,
results in higher market price volatility. Energy storage systems, by providing flexibility, can mitigate these effects and contribute to more stable
electricity market prices. This dual role, enabling higher shares of VRE and stabilizing market outcomes, emphasizes the growing importance of battery
storage in the German energy transition.
                """
            },
            {
                "title": "Competitive Technologies",
                "bullets": [
                    "The expansion of other battery types",
                    "Other storage options",
                    "Other flexibility options",
                    "Import/export capacities"
                ],
                "details": """
Battery storage does not operate in isolation. Competing and complementary technologies include:  

- **Expansion of other battery types**: The expansion of dezentralized prosumer home batteries and mobile V2G-enabled storage could reduce the demand for stationary large-scale battery storage.
This is due to them also competing for arbitrage on the spot markets. While the ancillary services are likely to be dominated by utility-scale batteries.
The reduction of the need of utility-scale batteries when decentralized prosumer batteries are expanding as well as EV V2G Batteries is part of this thesis.
If they will actually start to penetrate the market the same way as utility scale batteries is dependent on several 
factors especially their business cases / economic viability as well as regulatory decisions.
- **Other storage forms**: Such as PHS, hydrogen, or heat storage.  
- **Flexibility options**: Such as Industry DSM, Heat Pumps, Electrolysers, EV Smart Charging.  
- **Cross-border trade**: The interconnector capacities are of especial importance here. 
Also the generation technologies and flexibilities in the neighbouring countries. 
The model will include the capacitites and imports/exports from germanys most important electricity trading partners.
                """
            },
            {
                "title": "Economic Drivers",
                "bullets": [
                    "Cost developments / trajectories",
                    "Markets & use cases",
                    "Economic viability & self-cannibalization effects",
                    "Technical parameters"
                ],
                "details": """
Economics remain a decisive factor:  

- **Cost trajectories:** 
In recent years, the cost of batteries has experienced a steep decline, significantly improving their competitiveness in energy systems.
Looking ahead to 2045, however, the future cost trajectory of batteries remains highly uncertain. As shown in Table 2.3 in the thesis, cost assumptions
in different energy system studies vary widely, but all agree on the expectation of further reductions. Energy system studies typically
consider the total project costs of installing one kilowatt-hour (kWh) or one kilowatt (kW) of battery capacity. In contrast, most other
technology-focused studies report only battery cell or module costs. Since the battery modules represent the largest share of total project costs,
the latter can still serve as a useful benchmark for assessing broader cost developments.
For the purposes of this thesis, the cost trajectories from the Ariadne Report 2025 will be adopted as the baseline. 
In addition, a sensitivity analysis will be conducted to capture the effects of uncertainty regarding future battery costs, 
thereby allowing for a more robust assessment of the role of battery storage in Germany’s energy transition.
 
- **Markets & use cases:** Revenues from energy arbitrage, ancillary services, and congestion management. Further detailed in chapter 2.4.
- **Viability & self-cannibalization:** Profitability shapes investment attractiveness in battery storage and therefore their possible deployment/expansion. 
The business cases for battery storage are described in more detail in the chapter 2.5. 
As installed battery capacity grows, price signals (e.g., on spot markets) weaken, compressing margins for new storage projects and slowing further expansion.
To investigate the (quantitative) effect of more batteries on the spot market daily price spreads will be part of this thesis. 
A saturation of profitability for batteries can already be seen on the FCR market and is likely to be seen on the aFRR market in the future as well. 
- **Technical parameters:** Efficiency, cycle life, and degradation impact the use-cases / business-cases.  
                """
            },
            {
                "title": "Policies and Regulatory Framework",
                "bullets": [
                    "Grid fees, taxes and levies",
                    "Smart grid infrastructure",
                ],
                "details": """
Policy choices strongly influence battery deployment:  

- **Grid fees & levies:** Double charging must be avoided; exemptions can improve competitiveness.  
- **Market rules:** Strong imbalance pricing, locational signals, and planned capacity markets encourage flexibility.
- **Permitting & interconnection:** Queue times and grid connection permits are currently major bottlenecks.
- **Standards & aggregation:** Interoperability and clear rules for V2G/DSM aggregation are crucial.  
- **Incentives & subsidies:** Targeted support can kickstart deployment but should be phased out as markets mature.
- **Digitalization & Smart Grids:** Advanced grid management and real-time data can enhance battery integration and operation.
                """
            }
        ]

        st.markdown("### Key Drivers")
        for i, section in enumerate(drivers, start=1):
            st.markdown(f"**{i}. {section['title']}**")
            st.markdown("\n".join([f"- {b}" for b in section["bullets"]]))
            with st.expander("Details", expanded=False):
                st.markdown(section["details"])

    elif main_choice == "3. Scenarios & Assumptions":
        st.markdown("""
This chapter documents the scenario design and the core modelling assumptions used in PyPSA-DE.

## Scenarios:

### The Base Scenario

The base scenario is aligned with the Net-Zero-Scenario pathway from the Ariadne Report 2025 \cite{Ariadne2025}.

For the base scenario in this thesis, the following adjustments to the model which was used in the Net-zero-Scenario were made:

- Adjusted Spatial Resolution
- Adjusted Temporal Resolution
- Added Minimum Value for Home Battery Expansion
- Turned on V2G option and adjusted assumptions
- Adjusted Battery Lifetime assumption

The adjustments are described in more detail in chapter 3.3 of the thesis.

### The V2G Scenarios

To examine the potential and the effects of different V2G rates, three different variations are examined. 

1. The base scenario but the V2G option is turned off
2. The base scenario but the min. morning SoC value rises to 60% instead of 40%. (Low V2G Scenario)
3. The base scenario but the V2G participation rate is higher as well as the BEV-DSM rate. 
Also the battery size per vehicle is higher in this scenario. (High V2G Scenario)

### The Cost Variation Scenarios

To examine the potential of cost variations on utility-scale batteries the following battery costs are variated:
1. Baseline cost level
2. A 20% cost decrease of the capital cost per kW and per kWh in each target year (Low Cost Scenario)
3. A 20% cost increase of the capital cost per kW and per kWh in each target year (High Cost Scenario)

Further, a cost sensitivity analysis was conducted with more extreme cost variations of  +/- 50\% and +100\% as well as -99\%.

### The PV Variation Scenarios

In this scenario the amounts of PV deployment are variated to examine the effects on battery deployment. 

Method: In each target year from 2030 on the amount of battery deployment is set fix to a +/- 20% compared to the base scenario (Low/High PV Scenario). 


        """)

    elif main_choice == "4. Model Results":
        st.markdown("""
        ## Model Results
        
        Use the subsections in the sidebar to explore:
        
        - **4.1 Battery Technology Rollout** (Key parameters & dispatch)
        - **4.2 Vehicle-to-Grid**
        - **4.3 Other Storages and Flexibilities**
        - **4.4 Cost Sensitivity Analysis**
        - **4.5 System Impact** (Price volatility, total costs, RES build-out, curtailment)
        - **4.6 Key Findings**
        """)

    elif main_choice == "5. Key Findings & Conclusion":
        st.markdown("""
        This section summarizes the key findings of the model results, structured into four main themes: technology deployment, flexibilities and substitution effects, battery cost sensitivity and demand elasticity, and overall system impacts.

        **Technology deployment**

        - **Timing of deployment:** Across scenarios, a marked step-change in utility-scale battery deployment occurs between 2030 and 2035. Even though daily flexibility needs increase already between 2025 and 2030, these needs are mostly covered by fossil fuel power plant and other storage options. Batteries become the cost-optimal substitute as coal is phased out, carbon costs rise, PV share grows, and battery CAPEX declines. In all scenarios, the majority of utility-scale capacity is added in 2035. Thereafter, the daily flexibility needs still grow significantly but the additional needs are increasingly met by prosumer home batteries, EV flexibility (smart charging and V2G) and other flexibilities.

        - **Magnitude and role:** In 2035, utility-scale batteries reach around 19 GW and 180 GWh of installed capacity. At that point, utility-scale, prosumer home, and V2G batteries offer similar power capacities, though utility-scale systems dominate in energy terms and serve as the primary flexibility providers. By 2045, rising V2G participation leads to V2G-enabled EV batteries surpassing utility-scale systems in both power and energy capacity, while home batteries exceed utility-scale units in power and reach about half their energy capacity. Despite these shifts in installed capacity, utility-scale batteries remain the main electricity supplier in 2045, delivering around 40 TWh, roughly half of the 80 TWh supplied by all battery technologies. The results highlight that while total battery-supplied electricity in 2045 remains within a consistent range of 65 to 100 TWh across scenarios, the underlying battery technology mix shifts significantly.

        - **System-optimal E2P and cycles:** The model indicates a broadly stable system-optimal E2P-ratio of around 9 hours for utility-scale batteries installed in 2035-2045. The annual full cycles tend to be around 200-300 cycles in 2035 to 2045, therefore they tend to be quite a bit lower than the expected annual full cycles for currently build utility-scale battery projects.

        - **Battery Dispatch:** While the battery dispatch in summer follows a clear day-night pattern, the dispatch during winter is less uniform. In summer batteries are mainly used to shift PV generation from day to night while in winter the dispatch is more closely tied to the fluctuations in wind generation. The battery dispatch shows further a clear seasonal pattern, with significantly higher discharge levels during summer compared to winter.

        **Flexibilities & substitution effects**

        - **Flexibility mix:** By 2045, battery technologies become the largest contributor to daily flexibility if BEV charging flexibility is included in all scenarios. Smart EV charging provides the dominant share (260 TWh), V2G contributes less (25 TWh), and stationary (utility-scale + prosumer home) batteries form the second-largest block while electrolysis follows as third. In 2025/2030, fossil fuel power plants still cover a large part of daily flexibility but their share decreases sharply afterwards. Weekly/annual flexibility remains the domain of electrolysis and cross-border exchanges mainly in 2045. Batteries play only a minor role at those horizons across scenarios.

        - **Substitution within battery types:** Stationary utility-scale, prosumer home batteries, and mobile V2G batteries compete and substitute each other to a high degree. In the High-V2G scenario, V2G together with home batteries can fully replace utility-scale deployment. Conversely, with low V2G uptake, utility-scale deployment rises significantly. While substitution effects within battery technologies are dominant, other flexibilities, especially electrolysis, import/export and resistive heaters are affected as well.

        **Battery cost sensitivity & demand elasticity**

        - **High elasticity to CAPEX:** Battery build-out is highly sensitive to utility-scale CAPEX. A +20% increase reduces utility-scale energy capacity markedly. +50% leads to significant further reduction and +100% essentially halts utility-scale deployment as other options substitute. Conversely, -20% to -50% shifts energy capacity volumes significantly upward. In the case of -50% cost reduction, significant deployment already starts earlier (2030 instead of 2035).

        - **PV build-out as demand driver:** Higher PV capacities increase daily flexibility needs and raise battery demand: in the High-PV scenario, total battery capacity rises from 475 GWh to 540 GWh, with utility-scale batteries accounting for most of the increase (from 173 GWh to 238 GWh and from 18 GW to 24 GW). Low-PV reduces these needs correspondingly. The renewable mix shift affects E2P only modestly on 2045 level. Timing effects are more pronounced (higher E2P in 2030 with early PV-led deployment).

        **System impacts**

        - **Curtailment and RES build-out:** Changes in total battery deployment changes the amount of renewable curtailment only marginally. Battery cost changes have little impact on endogenously built PV/wind capacities in base sensitivity ranges while the change in PV installations had the biggest effect on curtailment.

        - **Electricity prices and volatility:** Price volatility (captured through average daily spreads, price duration curves and top-bottom spreads) reaches its peak around 2035 across all scenarios. Higher battery integration mitigates extreme price hours and narrows daily spreads, indicating pronounced self-cannibalization effects for utility-scale batteries. In the base scenario, market saturation becomes evident after 2035: by 2045, average daily spreads are roughly halved, even though overall flexibility demand continues to rise. Scenarios with extensive battery deployment, such as the 50% cost reduction case, exhibit a markedly smoother price profile without a pronounced volatility spike in 2035. Similarly, high V2G participation significantly dampens price fluctuations. In contrast, scenarios with increased utility-scale battery costs show substantially higher volatility, underscoring that while alternative flexibility options can partially compensate for reduced battery deployment, the system must endure higher price volatility as a consequence.

        - **Total system costs:** The High PV, High Cost, and Low PV scenarios show only minor effects on overall system costs, indicating that variations in these dimensions have limited influence on the total expenditures of the energy system. The Low Cost scenario, by contrast, results in a modest reduction in system costs. Substantially larger reductions are achieved in the 50% battery cost reduction scenario and the High V2G scenario. Among these, the High V2G scenario has the most pronounced effect, lowering total system costs by up to around 12 billion euros in 2035.

        **Conclusion**

        The findings of this thesis highlight the central role of utility-scale battery energy storage systems in enabling Germany’s transition toward a climate-neutral energy system by 2045. Using the open-source PyPSA-DE framework, this study systematically analyzed the deployment of different battery technologies under various scenarios. The results provide a differentiated understanding of how utility-scale batteries interact with other flexibility options such as prosumer home batteries and Vehicle-to-Grid systems, and how these interactions shape the optimal design of a future renewable-dominated power system.

        The model results demonstrate that batteries will become a core short-term flexibility technology, balancing daily fluctuations in renewable generation and contributing to price stabilization in the electricity spot markets. While utility-scale batteries will become the dominant battery technology in the short- and medium term, it is likely that prosumer home batteries and V2G enabled EVs become more relevant in the longer term. For the scenario with high V2G penetration, almost no utility-scale get installed as the daily flexibility provided by batteries is supplied by V2G and prosumer home batteries.

        The model suggests a significant uptake in utility-scale battery installations between 2030 and 2035, reaching a combined total of approximately 400-500 GWh of installed stationary storage capacity and effective available V2G battery capacity by 2045 across most scenarios. The share of this capacity contributed by utility-scale batteries varies substantially depending on the respective scenario assumptions. As the model captures the full business case of batteries only limited, their current profitability as well as the high current grid-connection requests suggests an already earlier uptake of utility-scale batteries.

        The cost sensitivity analysis reveals a strong elasticity of battery deployment with respect to capital cost changes. A 50% cost decrease nearly doubles installed energy capacity, confirming that the pace of technological cost decline will remain one of the most decisive factors for large-scale adoption. Conversely, a 100% cost increase from the base scenario projections leads to almost no deployment of utility-scale batteries and significantly higher price volatility in 2035 and 2040.

        This elasticity indicates that other flexibility options can effectively substitute utility-scale battery storage for daily balancing needs, although this comes at the cost of increased price peaks and volatility. The primary substitutes in this context are other battery types, electrolysis, and electricity imports and exports. Total system costs can be especially reduced in the High V2G scenario as well as in the 50% battery cost reduction case. The High PV and Low PV scenarios, as well as the High Cost scenario, result in only minor reductions in total system costs.
        """)
