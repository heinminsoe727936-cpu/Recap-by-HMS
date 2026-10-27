import streamlit as st
import google.generativeai as genai

# Page Title
st.set_page_config(page_title="Movie Recap AI Tool", page_icon="🎬")
st.title("🎬 Mobile Movie Recap Assistant")

# API Key ထည့်ရန် နေရာ
api_key = st.text_input("Google Gemini API Key ထည့်ပါ", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Model နာမည်ကို ပိုမိုသင့်လျော်သော ဗားရှင်းသို့ ပြောင်းထားပါသည်
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Subtitle သို့မဟုတ် ဇာတ်လမ်းအကျဉ်း ထည့်ရန်
        source_text = st.text_area("ရုပ်ရှင် Subtitle (သို့) အင်္ဂလိပ်/တရုတ် ဇာတ်လမ်းအကျဉ်းကို ထည့်ပါ")

        if st.button("မြန်မာလို Recap Script ဖန်တီးမည်"):
            if source_text:
                with st.spinner("AI ဖြင့် Script ရေးသားနေပါပြီ..."):
                    prompt = f"""
                    You are a professional Burmese movie recap creator. 
                    Convert the following text/subtitles into an engaging, dramatic 3-minute Burmese movie recap script.
                    Make sentences concise for voiceover sync. Include dramatic hooks.
                    
                    Source Text:
                    {source_text}
                    """
                    response = model.generate_content(prompt)
                    
                    st.subheader("📝 ထွက်လာသော မြန်မာ Recap Script:")
                    st.write(response.text)
            else:
                st.warning("ကျေးဇူးပြု၍ စာသားအရင် ထည့်ပါ။")
    except Exception as e:
        st.error(f"ချိတ်ဆက်မှု အမှားအယွင်း ရှိနေပါသည်: {e}")
else:
    st.info("စတင်အသုံးပြုရန် Gemini API Key ထည့်ပေးပါ။")
