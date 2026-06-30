import streamlit as st
import json
from google import genai

# "AIzaSy..." wali apni real key yahan double quotes mein likh do

# 🎨 BRAND CONFIGURATION & UI SETUP
# ==========================================
st.set_page_config(page_title="VibeLift AI", page_icon="🧠", layout="centered")

# Custom Title and the Selected Option C Tagline
st.title("🧠 VibeLift AI")
st.markdown("##### *\"Not feeling it? No pressure. Let’s shift your vibe and unlock your momentum.\"*")
st.caption("Neurobiological Friction Interception Engine | Vibe2Ship 2026")
st.divider()

# ==========================================
# 🔑 API CONFIGURATION (Put your key here!)
# ==========================================
API_KEY = "AQ.Ab8RN6J3MAIFISl6Lbg4LNDWwUkqJa2GwhEWZOaCQsci1e2iwQ"
client = genai.Client(api_key=API_KEY)
def clean_json_response(raw_text):
    """Pro-level JSON cleaner to ensure absolute parsing success"""
    text = raw_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.endswith("```"):
        text = text[:-3]
    return json.loads(text.strip())

# ==========================================
# 🚀 USER INTERFACE & INTERACTION
# ==========================================
user_input = st.text_area(
    "What is currently blocking your momentum?", 
    placeholder="Example: I have a project due tonight but I'm completely drained and unmotivated...",
    height=120
)

if st.button("ELEVATE MY VIBE ⚡", type="primary", use_container_width=True):
    if not user_input:
        st.warning("👋 Hey, no pressure! Just type what's on your mind or what you're avoiding so we can fix it together.")
    else:
        with st.spinner("🧠 Shifting cognitive loops... Finding your motivation hook..."):
            try:
                    # Initialize Google GenAI Client
                    client = genai.Client(api_key=API_KEY)
                    
                    # Call Gemini Model with VibeLift Persona
                    interaction = client.interactions.create(
                        model='gemini-3-flash-preview',
                        input=user_input,
                        system_instruction="""<system_identity>
                    
You are 'VibeLift', an elite, highly empathetic yet strategic cognitive performance coach. Your objective is to help the user bypass task paralysis without inducing guilt. Acknowledge their >
</system_identity>

<output_protocol>
You must output ONLY raw, valid JSON. Do not wrap the JSON in markdown formatting.
{
  "internal_reasoning": "Empathetic analysis of user's current friction point",
  "task_classification": "Academic/Habit/Self-Growth/Admin/Crisis",
  "escalation_triggered": false,
  "suggested_micro_task": "One atomic, super easy, 2-minute entry task to break friction",
  "dopamine_reward": "A micro-comfort or reward to unlock upon finishing",
  "assistant_reply": "A warm, encouraging, yet action-oriented message in English that acts as the hook."
}
</output_protocol>"""
                    )
                    
                    # Process the JSON safely (Yahan try ke andar)
                    data = clean_json_response(interaction.output_text)
                    
                    # Display Results in a Beautiful Layout
                    st.markdown("### 🎯 Your Vibe Upgrade")
                    st.info(data.get('assistant_reply', "Let's start with a tiny step together.")) 

                    # Multi-column response for clear UI layout
                    col1, col2 = st.columns(2)  # Pehle columns define karo

                    with col1:  # Phir 'with' use karo
                        st.markdown("#### ⚡ The 2-Min Entry Step")
                        st.error(data.get('suggested_micro_task', 'Just open your project file.'))

                    with col2:
                        st.markdown("#### 🎁 Your Micro-Reward")
                        st.success(data.get('dopamine_reward', 'A refreshing 5-minute break.'))
            
            except Exception as e: # <-- Ab except block sabse aakhiri mein aayega
                st.error(f"🚨 Connection glitch: {str(e)}")