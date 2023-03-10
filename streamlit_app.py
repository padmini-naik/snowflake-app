import streamlit;
streamlit.title('Helowwww');
streamlit.header('Header');
streamlit.text('+. Text1');
streamlit.text('Text2');
streamlit.text('Text3');

import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit');
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index));
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show);
