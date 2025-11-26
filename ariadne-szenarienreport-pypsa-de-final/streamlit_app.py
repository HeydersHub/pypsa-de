import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")

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
         
        
        For more detailed information, please refer to the full thesis document which you can download below.",

        **Introduction to the thesis topic**
        
        The German energy system is undergoing a fundamental transformation, driven by the urgent need to mitigate climate change.
        This shift necessitates a transition from conventional fossil fuel power plants to renewable energy sources.
        Germany reached a renewable electricity share of more than 60% for the first time in 2024 and has set the targets of 
        achieving an 80% renewable share by 2030 and climate neutrality by 2045. The vast majority of these renewables will be provided by variable
        renewable energy (VRE) sources, primarily PV and wind power. However, this transition also brings new challenges. 
        Unlike traditional power plants, which can be dispatched according to demand, variable renewable energy generation is highly
        dependent on weather conditions. As a result, the need for flexibility in the power system is increasing significantly.
        
        **Problem Statement**
        
        
        
        **Objectives and Research Question**
        
        The primary goal of this thesis is to outline possible pathways and scenarios for the deployment of battery energy storage systems.
        It aims to explore various battery-related metrics in depth, highlight their interdependencies, and investigate cost sensitivities as well as the elasticity of battery demand.
        Further, the role of different battery technology types will be analyzed. This thesis aims to provide a robust foundation for further grid- and energy system planning regarding battery storage.
        
        To achieve this, the current literature will be analyzed and scenarios will be developed using the open-source energy system model PyPSA-DE.
        
        The goal of this thesis is to answer the following key question:
        
        #### What role will utility-scale battery energy storage systems play in Germany’s energy transition toward climate neutrality by 2045 and what drives their deployment?
        
        To further define the scope of this question, the following objectives and subquestions will be examined.

        A set of Key Drivers regarding utility-scale battery deployment will be developed and investigated to examine the subquestions.
        
        ...
        
        **Structure of the Thesis**
        
        ... (to be added later)
        
        """)

    elif main_choice == "2. Key Driver for Battery Deployment":
        st.markdown("""
Based on a comprehensive review of the current literature, ten key drivers for utility-scale battery deployment were identified and grouped into 
four overarching categories.

The first category concerns the need for system flexibility. Historically, conventional power plants such as coal and gas units were capable
of adjusting their electricity generation to match demand, thereby reducing the requirement for energy storage. In contrast, variable renewable energy
sources such as solar PV and wind are intermittent and weather dependent, which significantly increases the need for storage to ensure that demand
can be reliably met at all times. 
To what extent can utility-scale batteries contribute to meeting this growing flexibility requirement? Flexibility needs can be distinguished across
different temporal dimensions like daily, weekly, and annual, allowing a clearer differentiation
between the roles of short-term and long-term storage technologies. Batteries are generally classified as short-term storage solutions as further
addressed in chapter xy.

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

Several studies have highlighted important thresholds for the deployment of storage technologies. Both \parencite{Cebulla2018} and \parencite{Thimet2023}
argue that once the VRE share surpasses approximately 65–67%, investment in energy storage grows disproportionately, with capacity expansion accelerating
rapidly beyond this point. Specifically, \parencite{Thimet2023} shows that utility-scale battery storage begins to scale significantly once VRE 
penetration exceeds 65% in the modeled system. This observation is in line with current developments in Germany, where a large amount of grid connection
requests for storage projects are concentrated in the period between 2026 and 2030, suggesting that the markets already anticipate passing this threshold 
in the near future.

The type of VRE mix also has a decisive influence on the required amount of storage. \parencite{Cebulla2018} suggests that PV-dominant systems demand
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
                    "Import/Export Capacities"
                ],
                "details": """
Battery storage does not operate in isolation. Competing and complementary technologies include:  

- **Expansion of other battery types**: The expansion of dezentralized prosumer home batteries and mobile V2G-enabled storage could reduce the demand for stationary large-scale battery storage.
This is due to them also competing for arbitrage on the spot markets. While the ancillary services are likely to be dominated by utility-scale batteries.
The reduction of the need of utility-scale batteries when decentralized prosumer batteries are expanding as well as EV V2G Batteries is part of this thesis.
If they will actually start to penetrate the market the same way as utility scale batteries is dependent on several 
factors especially their business cases / economic viability as well as regulatory decisions. .  
- **Other storage forms**: Such as PHS, hydrogen, or heat storage.  
- **Flexibility options**: Like Industry DSM, Heat Pumps, Electrolysers, EV Smart Charging.  
- **Cross-border trade**: The interconnector capacities are of especial importance here. 
Also how the used generation technologies and flexibilities in the neighbouring countries. 
The model will include the capacitites and imports/exports from germanys most important electricity trading partners.
                """
            },
            {
                "title": "Economic Drivers",
                "bullets": [
                    "Cost Developments / Trajectories",
                    "Markets (and Roles / Use Cases)",
                    "Economic Viability & Self-cannibalization effects",
                    "(indirectly Technical Parameters)"
                ],
                "details": """
Economics remain a decisive factor:  

- **Cost trajectories:** 
In recent years, the cost of batteries has experienced a steep decline, significantly improving their competitiveness in energy systems.
Looking ahead to 2045, however, the future cost trajectory of batteries remains highly uncertain. As shown in Table XY, cost assumptions
in different energy system studies vary widely, but all agree on the expectation of further reductions. Energy system studies typically
consider the total project costs of installing one kilowatt-hour (kWh) or one kilowatt (kW) of battery capacity. In contrast, most other
technology-focused studies report only battery cell or module costs. Since the battery modules represent the largest share of total project costs,
the latter can still serve as a useful benchmark for assessing broader cost developments.
According to a recent market overview by PV Magazine, investment costs for projects scheduled in 2025 are broadly in line with the assumptions
of the major system studies (Lichner, 2025). BloombergNEF, however, reports considerably lower global market prices in 2024, with battery pack
costs averaging 115 USD/kWh and prices as low as 94 USD/kWh in China (Catsaros, 2024). Moreover, a large-scale auction in China for 16 GWh of
storage capacity resulted in an average bid price of just 66 USD/kWh (Shaw, 2024). This value is already below the cost assumptions for 2045
in most of the aforementioned energy system studies. These findings underline both the pace of cost reductions and the difficulty of reliably 
projecting long-term trends.
Battery cell costs are currently dominated by developments in China, as the majority of the lithium iron phosphate (LFP) value chain is concentrated
there (see Figure XY). This heavy dependence on Chinese manufacturing introduces risks related to geopolitical tensions and the possibility of a trade
conflict, including the imposition of tariffs, which could significantly increase the cost of battery projects in Germany. Conversely, continued 
innovation in battery technologies and manufacturing processes could accelerate cost reductions beyond current expectations.
The current structure of project costs in Germany was recently described by the CEO of Ecostor, one of the leading developers of utility-scale
battery projects, in the podcast Batterie Geladen (citation needed). According to this source, a complete battery container imported from China,
including the battery management system (BMS) and cooling costs approximately 100 EUR/kWh. Battery modules account for around 35–45% of total project
costs, while inverters and transformers represent approximately 15–20%. For larger projects (exceeding 10 MW), the share of transformer costs is 
even higher. The remaining costs are attributable to construction, cabling, and external services. As the cost of batteries has decreased so substantially
in recent years, these external cost components have become increasingly important in determining overall project economics.
The same source reported that Ecostor relies on LFP batteries, which are expected to have a lifetime of about 15 years and a cycle life
of 7,000–8,000 cycles. The inverters typically last between 15 and 20 years. With a targeted operational strategy of 1.5 cycles per day 
equivalent to roughly 8,200 cycles over 15 years—their utility-scale projects currently operate across multiple markets, 
including frequency containment reserve (FCR), automatic frequency restoration reserve (aFRR), and spot markets. By pursuing this cross-market
strategy, the company expects to achieve an average annual return of about 15% of project costs, resulting in an amortization period of approximately
six to seven years. In the short term, returns are expected to be even higher, while a gradual decline is anticipated in the longer term as market
competition increases.
For the purposes of this thesis, the cost trajectories from the Ariadne Report 2025 will be adopted as the baseline. 
In addition, a sensitivity analysis will be conducted to capture the effects of uncertainty regarding future battery costs, 
thereby allowing for a more robust assessment of the role of battery storage in Germany’s energy transition.
 
- **Market design & roles:** Revenues from energy arbitrage, ancillary services, and congestion management. Further detailed in chapter xy.
- **Viability & self-cannibalization:** Profitability shapes investment attractiveness in battery storage and therefore their possible deployment/expansion. 
The business cases for battery storage are described in more detail in the chapter xy. 
As installed battery capacity grows, price signals (e.g., on spot markets) weaken, compressing margins for new storage projects and slowing further expansion.
To investigate the (quantitative) effect of more batteries on the spot market daily price spreads will be part of this thesis. 
A saturation of profitability for batteries can already be seen on the FCR market and is likely to be seen on the aFRR market in the future as well. 
- **Technical parameters:** Efficiency, cycle life, and degradation impact the use-cases / business-cases.  
                """
            },
            {
                "title": "Policy and Regulatory Decisions / Framework",
                "bullets": [
                    "Grid fees, ..."
                ],
                "details": """
Policy choices strongly influence battery deployment:  

- **Grid fees & levies:** Double charging must be avoided; exemptions can improve competitiveness.  
- **Market rules:** Strong imbalance pricing, locational signals, and capacity markets encourage flexibility. Future capacity market.
- **Permitting & interconnection:** Queue times and grid codes can be major bottlenecks. --> Permits from ÜNBs
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
This chapter documents the **scenario design** and the **core modelling assumptions** used in PyPSA-DE.

## Scenarios:

### The Base Scenario

The base scenario is aligned with the Net-Zero-Scenario pathway from the Ariadne Report 2025 \cite{Ariadne2025}.

For the base scenario in this thesis, the following adjustments to the model which was used in the Net-zero-Scenario were made:

\begin{itemize}
    \item Adjusted Spatial Resolution
    \item Adjusted Temporal Resolution
    \item Added Minimum Value for Home Battery Expansion
    \item Turned on V2G option and adjusted assumptions
    \item Adjusted Battery Lifetime assumption
\end{itemize}

The adjustments are described in more detail in chapter xy of the thesis.

### The V2G Scenarios

To examine the potential and the effects of different V2G rates, three different variations are examined. 

1. The base scenario but the V2G option is turned off
2. The base scenario but the min. morning SoC value rises to 60% instead of 40%. (Low V2G Scenario)
3. The base scenario but the V2G participation rate is higher as well as the BEV-DSM rate. 
Also the battery size per vehicle is higher in this scenario. (High V2G Scenario)

### The Cost Variation Scenarios

To examine the potential of cost variations on utility-scale batteries the following battery costs are variated:
1. Baseline cost level
2. A 20% cost decrease of the capital cost per kW and per kWh in each target year
3. A 20% cost increase of the capital cost per kW and per kWh in each target year

Further, a cost sensitivity analysis was conducted with more extreme cost variations of  +/- 50\% and +100\% as well as -99\%.

### The PV Variation Scenarios

In this scenario the amounts of PV deployment are variated to examine the effects on battery deployment. 

Method: In each target year from 2030 on the amount of battery deployment is set fix to a +/- 20% compared to the base scenario. 


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
        The findings of this thesis highlight the central role of utility-scale battery energy storage
systems in enabling Germany’s transition toward a climate-neutral energy system by
2045. Using the open-source PyPSA-DE framework, this study systematically analyzed
the deployment of different battery technologies under various scenarios. The results
provide a differentiated understanding of how utility-scale batteries interact with other
flexibility options such as prosumer home batteries and Vehicle-to-Grid systems, and
how these interactions shape the optimal design of a future renewable-dominated power
system. The model results demonstrate that batteries will become a core short-term flexibility
technology, balancing daily fluctuations in renewable generation and contributing
to price stabilization in the electricity spot markets. While utility-scale batteries will
become the dominant battery technology in the short- and medium term, it is likely that
prosumer home batteries and V2G enabled EVs become more relevant in the longer term.
For the scenario with high V2G penetration, almost no utility-scale get installed as the
daily flexibility provided by batteries is supplied by V2G and prosumer home batteries.
The model suggests a significant uptake in utility-scale battery installations between
2030 and 2035, reaching a combined total of approximately 400–500 GWh of installed
stationary storage capacity and effective available V2G battery capacity by 2045 across
most scenarios. The share of this capacity contributed by utility-scale batteries varies
substantially depending on the respective scenario assumptions. As the model captures
the full business case of batteries only limited, their current profitability as well as the
high current grid-connection requests suggests an already earlier uptake of utility-scale
batteries. The cost sensitivity analysis reveals a strong elasticity of battery deployment
with respect to capital cost changes. A 50% cost decrease nearly doubles installed energy
capacity, confirming that the pace of technological cost decline will remain one of the
most decisive factors for large-scale adoption. Conversely, a 100% cost increase from the
base scenario projections leads to almost no deployment of utility-scale batteries and
significantly higher price volatility in 2035 and 2040. This elasticity indicates that other
flexibility options can effectively substitute utility-scale battery storage for daily balancing
needs, although this comes at the cost of increased price peaks and volatility. The
primary substitutes in this context are other battery types, electrolysis, and electricity
imports and exports. Total system costs can be especially reduced in the High V2G
scenario as well as in the 50% battery cost reduction case. The High PV and Low PV
scenarios, as well as the High Cost scenario, result in only minor reductions in total
system costs.
        """)
