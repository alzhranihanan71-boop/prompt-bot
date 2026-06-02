import streamlit as st

# إعداد واجهة المستخدم
st.set_page_config(page_title="Promptify-Ed", page_icon="🤖", layout="centered")

# 1. إضافة زر تحويل اللغة في أعلى اليمين
lang = st.radio("🌐 Choose Language / اختر اللغة:", ["العربية", "English"], horizontal=True)

# 2. قاموس النصوص للتحويل بين اللغتين تلقائياً
if lang == "العربية":
    txt_title = "🤖 Promptify-Ed | برومبتيفاي-إد"
    txt_subtitle = "اكتب فكرتك البسيطة، وسيقوم البوت بتحويلها إلى أمر ذكي واحترافي فوراً!"
    txt_label = "✍️ اكتب فكرتك هنا (مثال: عائلة، حيوانات، قصة):"
    txt_placeholder = "اكتب هنا..."
    txt_select = "💡 اختر نوع الدعم التعليمي:"
    options_support = [
        "التعليم العام",
        "دعم التربية الفكرية - تبسيط مفرط"
    ]
    txt_button = "🚀 تحسين الأمر وتوليده"
    txt_warning = "⚠️ الرجاء كتابة فكرة أو كلمة أولاً!"
    txt_spinner = "⏳ جاري هندسة الأمر وتحسينه..."
    txt_success = "✨ تم توليد الأمر الاحترافي بنجاح!"
    txt_result = "📋 الأمر الجاهز للنسخ (ضعيه في ChatGPT):"
    txt_info = "💡 نصيحة ذكية: انسخي الأمر أعلاه وضعي في ChatGPT أو Gemini للحصول على درس مبسط جداً يناسبك!"
    txt_caption = "🔒 برنامج مجاني مجتمعي آمن لخدمة جميع فئات المجتمع ومؤتمت مع جداول بيانات قوقل."
else:
    txt_title = "🤖 Promptify-Ed"
    txt_subtitle = "Type your simple idea, and the bot will transform it into an expert prompt instantly!"
    txt_label = "✍️ Type your idea here (e.g., family, animals, story):"
    txt_placeholder = "Type here..."
    txt_select = "💡 Choose Educational Support Type:"
    options_support = [
        "General Learning",
        "Special Education - Ultra Simplified Support"
    ]
    txt_button = "🚀 Optimize and Generate Prompt"
    txt_warning = "⚠️ Please type an idea or a word first!"
    txt_spinner = "⏳ Engineering and optimizing your prompt..."
    txt_success = "✨ Professional prompt generated successfully!"
    txt_result = "📋 Ready Prompt for ChatGPT (Copy below):"
    txt_info = "💡 Smart Tip: Copy the prompt above and paste it into ChatGPT or Gemini to get an ultra-simple lesson tailored for you!"
    txt_caption = "🔒 A free community application designed to serve all learners, integrated with Google Sheets."

# --- بناء واجهة التطبيق بناءً على اللغة المختارة ---
st.title(txt_title)
st.write(txt_subtitle)

# صندوق إدخال الفكرة
user_prompt = st.text_area(txt_label, placeholder=txt_placeholder)

# قائمة اختيار نوع الدعم
support_type = st.selectbox(txt_select, options_support)

st.markdown("---")

if st.button(txt_button):
    if user_prompt.strip() == "":
        st.warning(txt_warning)
    else:
        with st.spinner(txt_spinner):
            
            # هندسة الأوامر الذكية (تظل بالإنجليزية لأنها موجهة للـ AI)
            if support_type in ["دعم التربية الفكرية - تبسيط مفرط", "Special Education - Ultra Simplified Support"]:
                optimized_code = f"Act as a highly patient special education teacher. I want to learn about '{user_prompt}'. Explain it to me in English using ultra-short sentences, very basic vocabulary, friendly words, and break the topic into 3 simple bullet points. Avoid any complex terms."
            else:
                optimized_code = f"Act as an expert English teacher. Please provide a comprehensive guide and structured lesson about '{user_prompt}' with an introduction, main points, and a conclusion to help me practice my English."

            st.success(txt_success)
            
            # عرض النتيجة النهائية لتقوم الطالبة بنسخها
            st.subheader(txt_result)
            st.code(optimized_code)
            
            st.info(txt_info)

st.markdown("---")
st.caption(txt_caption)
