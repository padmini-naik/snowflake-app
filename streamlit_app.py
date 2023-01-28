import streamlit;
streamlit.title('Helowwww');
streamlit.header('Header');
streamlit.text('+. Text1');
streamlit.text('Text2');
streamlit.text('Text3');

import pandas;
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
