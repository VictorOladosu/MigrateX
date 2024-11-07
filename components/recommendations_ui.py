import streamlit as st
from components.ai_recommendations import get_category_specific_recommendations

def display_recommendations(category):
    with st.expander("🤖 AI-Powered Recommendations", expanded=True):
        recommendations = get_category_specific_recommendations(category)
        
        if "error" in recommendations:
            st.error(f"Could not generate recommendations: {recommendations['error']}")
            return
            
        if recommendations.get("optimization_score"):
            st.metric("Optimization Score", f"{recommendations['optimization_score']}%")
        
        recommendations_list = recommendations.get("recommendations", [])
        if recommendations_list:
            for rec in recommendations_list:
                with st.container():
                    st.markdown(f"**{rec.get('title', 'Recommendation')}**")
                    st.markdown(rec.get('description', ''))
                    if 'impact' in rec:
                        st.progress(rec['impact'])
        else:
            st.info("No recommendations available at this time.")
