import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(layout="wide")

# Titel
st.title("Master Thesis: The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045")
st.markdown("Navigate through the thesis structure on the left. Select a section to view the relevant plots or text.")

# ------------------------------
# Struktur des Inhaltsverzeichnisses (ohne doppelte Emojis im Titel)
# ------------------------------
toc = {
    #"1. Introduction": "This notebook introduces my master thesis topic and results. The following gives a brief introduction and summary of the key points of the thesis results. For more detailed information, please refer to the full thesis document which you can download below.",
    "1. Introduction": None,
    "2. Key Driver for Battery Deployment": None,
    "3. Model Results": {
        "3.1 Battery Capacity": {
            "label": "Choose Battery Power-, Energy- and annual Discharge Capacity Plots:",
            "plots": [
                "Annual_Battery_Discharge_All_Scenarios",
                "Annual_Battery_Discharge_All_Scenarios_Stacked_Bar",
                "Annual_Battery_Discharge_Base_Scenario",
                "Annual_Battery_Discharge_Delta_All_Scenarios",
                "Installed_Power_Capacity_All_Scenarios",
                "Installed_Power_Capacity_Base_Scenario",
                "Installed_Power_Capacity_Delta_All_Scenarios",
                "Installed_Energy_Capacity_All_Scenarios",
                "Installed_Energy_Capacity_Base_Scenario",
                "Installed_Energy_Capacity_Delta_All_Scenarios",
                "Battery_E2P_Ratio_All_Scenarios",
                "Battery_E2P_Ratio_Base_Scenario",
                "Battery_E2P_Ratio_Delta_All_Scenarios",
                "Battery_Full_Cycles_All_Scenarios",
                "Battery_Full_Cycles_Base_Scenario",
                "Battery_Full_Cycles_Delta_All_Scenarios",
                #"line_plot_annual_elec",
                #"line_plot_discharge_capacity",
                #"line_plot_energy_capacity",
                #"plot_e2p_ratio",
                #"plot_cycles",
                "stacked_bar_plot_annual_elec",
                #"stacked_bar_plot_discharge_capacity",
                #"stacked_bar_plot_energy_capacity",
                #"plot_e2p_ratio_all_scenarios",
                #"plot_cycles_all_scenarios",
                "plot_bereitstellung_all_scenarios",
                "plot_bereitstellung_stacked_balken_alle_szenarien",
                #"plot_entladeleistung_final_all_scenarios",
                #"plot_entladeleistung_all_scenarien",
                #"plot_kapazitaet_all_scenarien",
                #"plot_kapazitaet_final_all_scenarien",
            ]
        },
        "3.2 Battery Dispatch": {
            "label": "Choose Battery Dispatch Plots:",
            "plots": [
                "plot_daily_battery__dispatch",
                "plot_weekly_battery_dispatch",
                "plot_monthly_battery_dispatch",
                "plot_annual_battery_dispatch",
                "plot_Annual_Dispatch_Base_Scenario_Test",
                "plot_annual_dispatch_all_technologies",
                "plot_monthly_V2G_power_dispatch",
                "plot_monthly_V2G_energy_dispatch",
                "plot_monthly_V2G_energy_dispatch_High_V2G_Scenario",
                "plot_monthly_V2G_power_dispatch_High_V2G_Scenario",
                "plot_monthly_V2G_energy_dispatch_Low_V2G_Scenario",
                "plot_monthly_V2G_power_dispatch_Low_V2G_Scenario",    
            ]
        },
        "3.3 RES & Flexibilities": {
            "label": "Choose RES and other Flexibilities Plots:",
            "plots": [
                "plot_stacked_bar_RES_capacity",
                "plot_line_RES_capacity_Technologiemix",
                "plot_stacked_bar_RES_capacity_all_scenarios",
                "plot_stacked_bar_RES_single_solar_capacity_all_scenarios",
                "plot_RES_curtailment"
            ]
        },
        "3.4 Price Plots": {
            "label": "Choose Price Plots:",
            "plots": [ 
                #"plot_price_year",
                "Average_Annual_Prices_All_Scenarios",
                "plot_price_yealy_new",
                "Average_Daily_Prices_All_Scenarios",
                "plot_price_daily_new",
                "Price_Duration_Curve_Base_Scenario",
                "plot_price_duration_curve",
                "plot_price_histogram",
                "plot_price_cov",
                "plot_price_daily_spread",
            ]
        },
        "3.5 Flexibility Needs": {
            "label": "Choose Flexibility Needs Plots:",
            "plots": [
                "plot_flexbedarf_total",
                "plot_flexbeiträge",
            ]
        }
    },
    #"4. Discussion/Conclusion": None
    "4. Key Findings & Conclusion": None
}

# ------------------------------
# Sidebar Navigation
# ------------------------------
with st.sidebar:
    # Hauptkapitel Menü
    main_choice = option_menu(
        menu_title="Thesis Contents",
        options=list(toc.keys()),
        icons=["book", "lightning", "bar-chart", "chat-dots"],  # Icons Hauptkapitel
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#e0e0e0"},
            "nav-link-selected": {"background-color": "#000000", "font-weight": "bold"},
        }
    )

    sub_choice = None
    if isinstance(toc[main_choice], dict):  # Falls Unterkapitel existieren
        sub_choice = option_menu(
            menu_title=f"{main_choice} – Subsections",
            options=list(toc[main_choice].keys()),
            icons=["battery-charging", "speedometer2", "graph-up", "currency-dollar", "gear"],  # Icons Subkapitel
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f9fafc"},
                "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "--hover-color": "#e6e6e6"},
                "nav-link-selected": {"background-color": "#333333", "font-weight": "bold"},
            }
        )

# ------------------------------
# Plot-Funktion
# ------------------------------

def show_plot(plot_name):
    filename = f"{plot_name}.html"
    filepath = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=800, width=1200, scrolling=True)
    else:
        st.error(f"Die Datei `{filename}` wurde nicht gefunden.") 

# ------------------------------
# Hauptbereich
# ------------------------------
if sub_choice:
    cfg = toc[main_choice][sub_choice]
    selected_plot = st.selectbox(cfg["label"], cfg["plots"])
    st.header(f"{main_choice} – {sub_choice}")

    # Eingebettetes Plotly-HTML (wie bisher)
    show_plot(selected_plot)

    # Und zusätzlich: Link zum Plot in neuem Tab (Full Screen) als download button
    file_path = os.path.join("ariadne-szenarienreport-pypsa-de-final", "Plots_MA", f"{selected_plot}.html")
    with open(file_path, "r", encoding="utf-8") as f:
        btn = st.download_button(
            label="🔍 Download Plot to view in Full Screen in your browser",
            data=f,
            file_name=f"{selected_plot}.html",
            mime="text/html"
        )


else:
    st.header(main_choice)

    if main_choice == "1. Introduction":
        st.markdown("""
        
        ### Welcome to my Master's Thesis Dashboard.  
        This Dashboard provides interactive visualizations of the results of my thesis and an overview of the key topics and findings covered.
         
        
        For more detailed information, please refer to the full thesis document which you can download below.",

        **Introduction to the thesis topic**
        
        The German energy system is undergoing a fundamental transformation, driven by the urgent need to mitigate climate change.
        This shift necessitates a transition from conventional power plants to renewable energy sources such as wind and PV.
        However, this transition also brings new challenges. Unlike traditional power plants, which can be dispatched according to demand, variable renewable energy generation is highly dependent on weather conditions.
        As a result, the need for flexibility in the power system is increasing significantly\parencite{Ariadne2025}.
        
        Battery storage systems have emerged as a key solution for providing this flexibility.
        They are widely considered an essential component of a future climate-neutral energy system, particularly one that relies heavily on PV and wind power.
        In recent years, the demand for battery storage has surged, driven by declining costs and the increasing need for system flexibility.
        This trend is reflected in the current exponential rise in grid connection requests for utility-scale battery storage \parencite{Enkhardt2025} with a planned commissioning year before 2030,
        which now far exceed the projections until 2030 outlined in various studies, as illustrated in Figure \ref{fig:Entwicklungspfade_Batteriespeicher}.
        
        **Problem Statement**
        
        Existing studies on battery storage deployment present divergent assumptions and results.
        Some studies lack transparency regarding their cost and technology assumptions, making it difficult to compare findings.
        This is detailed further in the next chapter. Most of the studies focus on the entire sector-coupled energy system and therefore are not placing battery storage as the central subject of investigation
        which results in no comprehensive in-depth analysis regarding battery storage deployment.
        Different types of battery storage, such as stationary large-scale storage, home PV battery storage, and mobile vehicle-to-grid-enabled storage are often not clearly distinguished
        or comprehensively analyzed. Furthermore, these studies assume a purely market-oriented optimization and neglect potential additional revenue streams for battery storage,
        such as future capacity markets, ancillary system services, self-consumption optimization, or industrial peak load shaving.
        Moreover, key performance indicators such as installed power capacity (GW), energy capacity (GWh), or annual discharge (TWh) are often reported inconsistently,
        which further hinders comparison.
        
        Furthermore, battery storage technologies compete with other flexibility options in the energy market. 
        Their future deployment will be influenced by various factors, including the expansion of renewable energy sources and the interactions between different storage and flexibility technologies.
        Therefore, a comprehensive analysis of these interdependencies is essential. The key drivers for battery storage deployment will be identified and their impact on future deployment scenarios assessed.
        The key drivers can be found in the next chapter.
        
        **Goals and Research Questions**
        
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
        ## Introduction
        # **"The Role of Battery Energy Storage Systems in Germany’s Energy Transition Toward Climate Neutrality by 2045"**.
        # This notebook introduces my master thesis topic and results. 
        # The following gives a brief introduction and summary of the key points of the thesis results.

    elif main_choice == "2. Key Driver for Battery Deployment":
        st.markdown("""
        In this chapter, the main drivers for the deployment of battery energy storage are discussed:

By conducting the current literature, I defined 10 key drivers for utility-scale battery deployment and grouped them into 4 categories.

The first category is the need for system flexibility. As the conventional power plants, like coal and gas power plants were able to adjust there electricity generation according to the demand, 
less energy storage was needed. But for renewables like PV and Wind, more Energy Storage is gonna be needed to supply the demand at all times. 
Here the question is how much of that demand/need can/will be proivded by utility-scale battery storage?
The need for system flexibility can be divided into daily, weekly and annual flexibility needs to make a more clear distinction between
the use-case and amount needed of short-term vs. long-term energy storages. Batteries are considered as short-term storages.

To investigate that, the other competitive technologies to provide that flexibility have to be taken into account.
Here, mainly other battery technologies like Prosumer Home Batteries and V2G, as well as other energy storage options like PHS, Hydrogen or Thermal/Heat Storages have to be considered.
Further, flexibility can also be provided by DSM, like Smart Charging of EVs, Heat Pumps or Electrolysis production. At last also the Import and Export Capacities have to be considered as they can also provide flexibility.

To further look into more detail what role batteries can play in providing the flexibility its important to consider the economic drivers for battery deployment.
If they have a good business case and are more profitable than their competing technologies it will be likely that they provide a bigger share of the needed flexibility.
Therefore the cost developments/trajectories for utility-scale batteries have to be considered as well as the markets they operate on and their specific use-cases / roles.
Their economic viability and business cases have to be investigated as well. Here, especially the self-cannibalization effects will be examined, which describe a market saturation and therefore less profitability for individual batteries.
The technical parameters like the lifetime and efficiency (and the E2P ratio) is further important as they shape the economic attractiveness and use-cases of the technology as well.

At last the current and possible future regulatory decisions / framework need to be considered as they shape further the attractiveness of certain technologies and lead the way for deployment. 
        """)

        # ---- Alles zentral in einer Liste verwaltet ----
        drivers = [
            {
                "title": "The Need for System Flexibility",
                "bullets": [
                    "Expansion of VRE, especially Wind and PV"
                ],
                "details": """
                \parencite{Cebulla2018} suggests that the amount of storage systems will be higher in a PV dominant system than in a Wind dominant system.
                This is (could be) even more so for Kurzzeitspeicher like Battery Storage because they mainly store/balance the day/night difference of battery storages.
Hypothese: More variability in the supply side and a inflexible/inelastic demand side, results in more market price volatility. 
Storage system can, in providing flexibility, result in less volatile market prices.
-The expansion of wind and PV will be taken from the Ariadne 2025 report --> wie ist es da genau? ich glaube exogen bis 2030 vorgegeben anhand der Ausbauziele der Regierung und danach endogener Ausbau.\\
-In \parencite{Cebulla2018} (nochmal suchen wo genau) and \parencite{Thimet2023} is argued that after around 67\% VRE share, the investment in energy storage capacities grows exponentially.
% 67\% VRE share is an important threshold.
-In \parencite{Thimet2023} this is also true for battery storage which gets mainly build after the VRE share exceeds 65\% in the model. 
Currently Germanys VRE share was above 60\% the first time in 2024 and set the goal of 80\% VRE in 2030. 
This seems to be in line with the current Netzanschlussanfragen which mainly want to build between 2026 and 2030.
The markets seem to anticipating passing the threshold soon.
-The results in \parencite{Cebulla2018} suggest that the amount of (bzw. the need/demand of) Energy storage power capacity (GW) grows linear
with the VRE-share and the amount of Energy storage capacity (GWh) grows exponentially with the VRE-share. This includes long-term and short-term storages.
Is there a similar behaviour for battery storages?

Germany reached a share of renewables above 60\% for the first time in 2024 and set the goal of 80\% renewables in 2030 as well as carbon neutrality in 2045.
The vast majority of renewables will be provided by PV and Wind power plants which are VRE (Ariadne 2025). 

In \parencite{Cebulla2018} (nochmal suchen wo genau) and \parencite{Thimet2023} is argued that after around 67\% VRE share,
the investment in energy storage capacities grows exponentially. This includes short- as well as long-term storages.
In \parencite{Thimet2023} this is also true for battery storage which gets mainly build after the VRE share exceeds 65\% in the model.
\parencite{Cebulla2018} suggests that the amount of storage systems will be higher in a PV dominant system than in a Wind dominant system.
This is (could be) even more so for Kurzzeitspeicher like Battery Storage because they mainly store/balance the day/night difference of battery storages.
The results in \parencite{Cebulla2018} suggest that the amount of (bzw. the need/demand of) Energy storage power capacity (GW) grows linear with the VRE-share
and the amount of Energy storage capacity (GWh) grows exponentially with the VRE-share. This includes long-term and short-term storages. 
Is there a similar behaviour for battery storages?  
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
The cost developments for batteries has been a steep drop in recent years. Regarding future cost trajectories until 2045, the development is related to high uncertainty. 
The Assumptions of costs per kWh in different Energy System Studies have a broad range but all expect a further decline in cost as is shown in Table xy. 
For Energy System Studies the total project costs for installing a kWh or kW of batteries is relevant, even though most other studies consider the battery cell or battery module costs. 
But since the batteries are the biggest cost driver of the project costs, these studies are a good indicator as well. 
According to the most recent market overview by PV Magazine, investment costs for projects scheduled for 2025 fall within the range assumed in these studies (Lichner 2025). 
BloombergNEF, however, reports significantly lower prices for battery packs and cells in 2024, down to 115 USD per kWh for battery packs globally, and as low as 94 USD per kWh in China (Catsaros 2024).
In a recent auction in China for 16 GWh of battery storage projects, the average price of the bids was at 66 USD per kWh (Shaw 2024), which is already lower than the assumed cost per kWh for 2045 in most of the above-mentioned studies.
The battery cell costs are mainly driven by china since most of the value chain of LFP Battery Production is there as is shown in the Graph xy.
Therefore geopolitical tensions as well as a trade war with increasing tariffs could significantly impact the costs of battery projects in germany. 
On the other hand further breakthroughs in battery technology and battery manufacturing could lead to significant cost reductions earlier than excpected.
The current costs for a battery project in Germany are described by the CEO of Ecostor, a leading company in battery projects, as the following in the recent "Batterie Geladen" Podcast (zitieren): 
A full battery container from china, including BMS and cooling systems, is available for around 100 Euro/kWh. 
The battery modules make up currently around 35-45 \% of the total project costs and the Inverter and transformers around 15-20 \%. For bigger projects (more than 10 MW) the percentage for transformers is even higher. 
Construction, Cabling and external services make up the rest.
He states that the external costs (inverters, transformers, cabling, ...) are becoming incresingly important as the battery costs decreased so much in the recent years. 
They further states that their projects use LFP Batteries and they expect a battery lifetime of 15 years as well as a cycle life of 7000-8000 cycles.
The inverter lifetime is expected to be around 15 to 20 years. 
With there current marketing strategy they expect an average of 1,5 cycles per day which would be 8200 cycles in 15 years. 
There utility scale batteries operate on the FCR and aFRR markets as well as on the spot markets. 
The follow a cross market strategy, maximising their revenue on the these three markets. 
With this strategy they expect an annual return of around 15\% of their project costs and an amortization period of around 6 to 7 years.
In the short term they expect even higher annual returns and in the long run smaller returns.
For this thesis the cost trajectories of the Ariadne Report 2025 will be used and an sensitivity analysis will
be used to see the impact of the uncertainty related to future battery costs.
 
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

        # ---- Ausgabe ----
        st.markdown("### Key Drivers")

        for i, section in enumerate(drivers, start=1):
            st.markdown(f"**{i}. {section['title']}**")
            st.markdown("\n".join([f"- {b}" for b in section["bullets"]]))
            with st.expander("Details", expanded=False):
                st.markdown(section["details"])


    elif main_choice == "3. Model Results":
        st.markdown("""
        ## Results
        
        This section contains the **quantitative results** of the modelling study.  
        Use the subsections in the sidebar to explore different result categories:
        
        - 🔋 **Battery Capacity**: Installed power (GW), energy (GWh), and discharge (TWh)  
        - 📈 **Battery Dispatch**: Daily, weekly, monthly, and annual utilization  
        - 🌱 **RES & Flexibilities**: Build-out of renewables and interaction with flexibility options  
        - 💰 **Price Plots**: Wholesale price dynamics, spreads, and volatility  
        - 🔧 **Flexibility Needs**: Contribution of BESS, V2G, and other technologies to residual load balancing  
        """)

    #elif main_choice == "4. Discussion/Conclusion":
    elif main_choice == "4. Key Findings & Conclusion":
        st.markdown("""
          **Main insights:**
          **Limitations:**
          **Conclusion:**
        """)
    else:
        st.info("Please choose a section from the sidebar to view its content.")
        
