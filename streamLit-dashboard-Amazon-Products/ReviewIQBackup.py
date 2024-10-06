import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the CSV files
df_beauty = pd.read_csv('All_Beauty_With_Sentiment_1.csv')
df_gift_cards = pd.read_csv('Gift_Cards_with_sentiment.csv')

# Convert timestamp to datetime format for time-based analysis
for df in [df_beauty, df_gift_cards]:
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['month'] = df['timestamp'].dt.to_period('M').astype(str)

# Streamlit UI
st.sidebar.title("ReviewIQ")
category = st.sidebar.selectbox("Select Category", ["Beauty", "Gift Cards"])
asin_input = st.sidebar.text_input("Enter ASIN")
search_button = st.sidebar.button("Search")

# Select the dataframe based on the category chosen
df = df_beauty if category == "Beauty" else df_gift_cards

# Product-Level Sentiment Analysis
product_sentiment = df.groupby('asin')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean()

# Find the top 10 products with highest positive sentiment
top_positive_products = product_sentiment.sort_values(by='positive_sentiment', ascending=False).head(10)
top_positive_products['Rank'] = range(1, 11)

# Find the top 10 products with highest negative sentiment
top_negative_products = product_sentiment.sort_values(by='negative_sentiment', ascending=False).head(10)
top_negative_products['Rank'] = range(1, 11)

def search_product(asin):
    if asin in product_sentiment.index:
        product_info = product_sentiment.loc[asin]
        positive_rank = (top_positive_products.index == asin).argmax() + 1 if asin in top_positive_products.index else "Not in Top 10 Positive"
        negative_rank = (top_negative_products.index == asin).argmax() + 1 if asin in top_negative_products.index else "Not in Top 10 Negative"
        
        result = {
            'ASIN': asin,
            'Positive Sentiment Score': product_info['positive_sentiment'],
            'Negative Sentiment Score': product_info['negative_sentiment'],
            'Neutral Sentiment Score': product_info['neutral_sentiment'],
            'Top 10 Positive Rank': positive_rank,
            'Top 10 Negative Rank': negative_rank
        }
        return result
    else:
        return {'Error': 'ASIN not found in the dataset'}

if search_button and asin_input:
    result = search_product(asin_input)
    if 'Error' in result:
        st.error(result['Error'])
    else:
        st.subheader(f"Search Results for ASIN: {asin_input}")
        st.write(result)
        if st.button('Back'):
            st.session_state.search_done = True
            st.experimental_rerun()
else:
    if category == "Beauty":
        st.markdown("## Beauty Category Analysis")
    else:
        st.markdown("## Gift Cards Category Analysis")

    st.markdown("### Average Sentiment Scores by Rating")
    rating_sentiment = df.groupby('rating')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean()
    fig_rating = px.bar(rating_sentiment, title='Average Sentiment Scores by Rating', color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_rating, use_container_width=True)

    st.markdown("### Sentiment Over Time")
    sentiment_over_time = df.groupby('month')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean()
    fig_time = px.line(sentiment_over_time, title='Sentiment Over Time', labels={'month': 'Month'}, color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig_time, use_container_width=True)

    st.markdown(f"### Top 10 Products with Highest Positive Sentiment in {category}")
    st.dataframe(top_positive_products.style.background_gradient(cmap='Blues'))

    st.markdown(f"### Top 10 Products with Highest Negative Sentiment in {category}")
    st.dataframe(top_negative_products.style.background_gradient(cmap='Reds'))

    st.markdown("### Sentiment vs Helpfulness")
    fig_helpfulness = px.scatter(df, x='helpful_vote', y='positive_sentiment', color='positive_sentiment', title='Sentiment vs Helpfulness', color_continuous_scale='Teal')
    st.plotly_chart(fig_helpfulness, use_container_width=True)

    st.markdown("### Sentiment by Verified Purchase")
    verified_sentiment = df.groupby('verified_purchase')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean()
    fig_verified = px.bar(verified_sentiment, title='Sentiment by Verified Purchase', labels={'index': 'Verified Purchase', 'value': 'Average Sentiment Score'}, color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_verified, use_container_width=True)

    st.markdown("### Distribution of User Sentiment")
    fig_user_sentiment = px.histogram(df.groupby('user_id')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean(), nbins=50, title='Distribution of User Sentiment', color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_user_sentiment, use_container_width=True)

    st.markdown("### Parent-Child Product Sentiment Comparison")
    parent_child_sentiment = df.groupby('parent_asin')[['positive_sentiment', 'negative_sentiment', 'neutral_sentiment']].mean()
    fig_parent_child = px.bar(parent_child_sentiment, title='Parent-Child Product Sentiment Comparison', color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig_parent_child, use_container_width=True)
