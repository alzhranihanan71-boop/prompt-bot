import streamlit as st

# إعداد واجهة المستخدم
st.set_page_config(page_title="Promptify-Ed", page_icon="🤖", layout="centered")

st.title("🤖 Promptify-Ed | برومبتيفاي-إد")
st.write("اكتب فكرتك البسيطة، وسيقوم البوت بتحويلها إلى أمر ذكي واحترافي فوراً!")

# صندوق إدخال الفكرة العامة من المستخدم
user_prompt = st.text_area("✍️ اكتب فكرتك هنا (مثال: عائلة، حيوانات، قصة):", placeholder="اكتب هنا...")

# قائمة اختيار نوع الدعم (ميزة التربية الخاصة)
support_type = st.selectbox(
    "💡 اختر نوع الدعم التعليمي (Choose Support Type):",
    [
        "التعليم العام (General Learning)",
        "دعم التربية الفكرية - تبسيط مفرط (Special Education - Ultra Simplified)"
    ]
)

st.markdown("---")

if st.button("🚀 تحسين الأمر وتوليده"):
    if user_prompt.strip() == "":
        st.warning("⚠️ الرجاء كتابة فكرة أو كلمة أولاً!")
    else:
        with st.spinner("⏳ جاري هندسة الأمر وتحسينه..."):
            
            # منطق هندسة الأوامر بناءً على اختيار نوع التعليم
            if support_type == "دعم التربية الفكرية - تبسيط مفرط (Special Education - Ultra Simplified)":
                # أمر ذكي يجبر الذكاء الاصطناعي على التبسيط الشديد لطالبات فكري
                optimized_code = f"Act as a highly patient special education teacher. I want to learn about '{user_prompt}'. Explain it to me in English using ultra-short sentences, very basic vocabulary, friendly words, and break the topic into 3 simple bullet points. Avoid any complex terms."
            else:
                # الأمر المخصص للتعليم العام
                optimized_code = f"Act as an expert English teacher. Please provide a comprehensive guide and structured lesson about '{user_prompt}' with an introduction, main points, and a conclusion to help me practice my English."

            st.success("✨ تم توليد الأمر الاحترافي بنجاح!")
            
            # عرض النتيجة النهائية لتقوم الطالبة بنسخها
            st.subheader("📋 الأمر الجاهز للنسخ:")
            st.code(optimized_code)
            
            st.info("💡 نصيحة ذكية: انسخ الأمر أعلاه وضعه في ChatGPT أو Gemini للحصول على درس مبسط جداً يناسبك!")

st.markdown("---")
st.caption("🔒 برنامج مجاني آمن ومفتوح المصدر لخدمة جميع فئات المجتمع ومؤتمت مع جداول بيانات قوقل.")
