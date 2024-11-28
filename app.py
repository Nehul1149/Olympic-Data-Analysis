import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

st.set_page_config(
    page_title="Olympic Analysis",
    page_icon="🏅",
    layout="wide"
)
st.sidebar.title("🏆 Olympic Analysis")
st.sidebar.image("Olympic_rings.png")
user_menu = st.sidebar.radio(
    '📊 Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-Wise Analysis', 'Athlete wise Analysis')
)

st.title("🏆 Olympic Data Analysis")
st.write("Welcome to the Olympic data analysis dashboard. Explore insights from historical Olympic events! 🥇")

if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.counter_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("🌍 Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("📅 Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " Overall Performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title("🏅" + selected_country + " Performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)


if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title('📊 Top Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    # Heatmap for No. of event over time
    st.title("📈 No. of Events over time(Every Sports)")
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)


    st.title("🏅 Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox("Select a Sport", sport_list)

    x = helper.most_successful_athletes(df, selected_sport)
    st.table(x)


    # Country Wise Analysis
if user_menu == "Country-Wise Analysis":
    st.sidebar.title('Country Wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.year_wise_medal_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    # Most Successful Athlete Top 10
    st.title("Top 10 Athletes of " + selected_country)
    top10_df = helper.most_successful_athletes_countrywise(df, selected_country)
    st.table(top10_df)


# 4.
# Athlete wise Analysis
if user_menu == "Athlete wise Analysis":
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    # Distribution of Ages according to the Sports
    # WRT to Gold Medalist
    # x = []
    # name = []
    # famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
    #                  'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
    #                  'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
    #                  'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Equestrianism',
    #                  'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
    #                  'Tennis', 'Golf', 'Softball', 'Archery',
    #                  'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
    #                  'Rhythmic Gymnastics', 'Rugby Sevens', 'Trampolining',
    #                  'Beach Volleyball', 'Triathlon', 'Rugby', 'Lacrosse', 'Polo',
    #                  'Cricket', 'Ice Hockey']
    # for sport in famous_sports:
    #     temp_df = athlete_df[athlete_df['Sport'] == sport]
    #     x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
    #     name.append(sport)
    #
    # fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    # fig.update_layout(autosize=False, width=1000, height=600)
    # st.title("Distribution of Age with respect to Sports(Gold Medalist)")
    # st.plotly_chart(fig)
    #
    # # WRT to Silver Medalist
    # x = []
    # name = []
    # for sport in famous_sports:
    #     temp_df = athlete_df[athlete_df['Sport'] == sport]
    #     x.append(temp_df[temp_df['Medal'] == 'Silver']['Age'].dropna())
    #     name.append(sport)
    #
    # fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    # fig.update_layout(autosize=False, width=1000, height=600)
    # st.title("Distribution of Age with respect to Sports(Silver Medalist)")
    # st.plotly_chart(fig)



    medal_type = st.selectbox(
        "Select Medal Type to Display Age Distribution:",
        ["Gold Medalists", "Silver Medalists", "Bronze Medalists"]
    )
    # Initialize lists for age data
    x = []
    names = []

    famous_sports = [
        'Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming',
        'Badminton', 'Sailing', 'Gymnastics', 'Art Competitions', 'Handball',
        'Weightlifting', 'Wrestling', 'Water Polo', 'Hockey', 'Rowing', 'Fencing',
        'Equestrianism', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving',
        'Canoeing', 'Tennis', 'Golf', 'Softball', 'Archery', 'Volleyball',
        'Synchronized Swimming', 'Table Tennis', 'Baseball', 'Rhythmic Gymnastics',
        'Rugby Sevens', 'Trampolining', 'Beach Volleyball', 'Triathlon', 'Rugby',
        'Lacrosse', 'Polo', 'Cricket', 'Ice Hockey'
    ]

    # Filter data based on selected medal type
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]

        # Check medal type selected
        if medal_type == "Gold Medalists":
            ages = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        elif medal_type == "Silver Medalists":
            ages = temp_df[temp_df['Medal'] == 'Silver']['Age'].dropna()
        else:
            ages = temp_df[temp_df['Medal'] == 'Bronze']['Age'].dropna()

        # Append data if available
        if not ages.empty:
            x.append(ages)
            names.append(sport)

    # Create the distribution plot
    fig = ff.create_distplot(x, names, show_hist=False, show_rug=False)
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        title=f"Distribution of Age with Respect to Sports ({medal_type})",
        legend_title="Sport"
    )
    # Display the plot
    st.title(f"Age Distribution for {medal_type}")
    st.plotly_chart(fig)



    # Height vs Weight Graph for any particular Sport
    st.title("📊 Height vs Weight")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sport_HW_Plot = st.selectbox("Select a Sport", sport_list)

    temp_df = helper.weight_vs_height(df,selected_sport_HW_Plot)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x = temp_df['Weight'], y = temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=20)
    st.pyplot(fig)

    # Over the year Man vs Women participation
    st.title("📊 Man vs Women participation over the Years")
    final = helper.man_vs_women_participation(df)
    fig = px.line(final, x="Year", y=["Male", "Female"], color_discrete_map={"Male": "blue", "Female": "green"})
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
