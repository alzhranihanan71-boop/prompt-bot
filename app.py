import streamlit as st
import requests

# إعداد واجهة المستخدم
st.set_page_config(page_title="Promptify-Ed", page_icon="🤖", layout="centered")

# --- دالة برمجية لإرسال البيانات تلقائياً لـ Google Sheets عبر نموذج مخفي ---
def log_to_google_sheets(lang_used, support_type, user_word):
    # ⚠️ استبدلي هذا الرابط برابط الـ Form الخاص بكِ لاحقاً ليصب في الـ Sheets مباشرة
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd0a0DcAt3yJ_GsjHWBZUO2UVQmhJ00b1gOvYonNUcs5nNQRQ/viewform?usp=pp_url&entry.2102841169=1&entry.1661112924=2&entry.315119461=3"
    
    # المعرفات الخاصة بالأسئلة داخل النموذج
    form_data = {
        "entry.1": lang_used,     # معرف حقل اللغة
        "entry.2": support_type,  # معرف حقل نوع الدعم
        "entry.3": user_word      # معرف حقل الكلمة المدخلة
    }
    try:
        requests.post(form_url, data=form_data)
    except:
        pass # لضمان عدم توقف التطبيق في حال انقطاع الإنترنت

# 1. إضافة زر تحويل اللغة في أعلى الصفحة
lang = st.radio("🌐 Choose Language / اختر اللغة:", ["العربية", "English"], horizontal=True)

# 2. قاموس النصوص والأوامر البرمجية بناءً على اللغة المختارة
if lang == "العربية":
    txt_title = "🤖 Promptify-Ed | برومبتيفاي-إد"
    txt_subtitle = "اكتب فكرتك البسيطة، وسيقوم البوت بتحويلها إلى أمر ذكي واحترافي فوراً!"
    txt_label = "✍️ اكتب فكرتك هنا (مثال: عائلة، حيوانات، قصة):"
    txt_placeholder = "اكتب هنا..."
    txt_select = "💡 اختر نوع الدعم التعليمي:"
    options_support = [
        "التعليم العام",
        "دعم التربية الفكرية - تبسيط مفرط مدعوم بالصور 📸"
    ]
    txt_button = "🚀 تحسين الأمر وتوليده"
    txt_warning = "⚠️ الرجاء كتابة فكرة أو كلمة أولاً!"
    txt_spinner = "⏳ جاري هندسة الأمر وتحسينه ببالصور وتسجيل البيانات..."
    txt_success = "✨ تم توليد الأمر الاحترافي بنجاح!"
    txt_result = "📋 الأمر الجاهز للنسخ (ضعيه في ChatGPT):"
    txt_info = "💡 نصيحة ذكية: انسخي الأمر أعلاه وضعي في ChatGPT أو Gemini للحصول على درس مبسط جداً وصور تناسبك!"
    txt_caption = "🔒 برنامج مجاني مجتمعي آمن لخدمة جميع فئات المجتمع ومؤتمت حيّاً مع جداول بيانات قوقل."
    
    def get_prompt(support, prompt_text):
        if support == "دعم التربية الفكرية - تبسيط مفرط مدعوم بالصور 📸":
            return (
                f"تصرف كمعلم تربية خاصة صبور جداً ويستخدم الوسائل البصرية. أريد أن أتعلم عن موضوع '{prompt_text}'. "
                f"أولاً: قم بتوليد صورة دافئة، واضحة، وجميلة جداً تناسب موضوع '{prompt_text}' لتفهمني إياه بصرياً. "
                f"ثانياً: اشرح لي الموضوع باللغة العربية مستخدماً جملاً قصيرة جداً (3 كلمات في الجملة كحد أقصى)، وكلمات سهلة ومبسطة للغاية، "
                f"وقسم الشرح إلى 3 نقاط أساسية واضحة متبوعة برموز تعبيرية (Emojis) مناسبة للأطفال. تجنب تماماً النصوص الطويلة."
            )
        else:
            return (
                f"تصرف كمعلم لغة محترف. يرجى تقديم دليل شامل ودرس منظم حول موضوع '{prompt_text}' "
                f"باللغة العربية، يحتوي على مقدمة، ونقاط رئيسية، وخاتمة واضحة لمساعدتي في الفهم والاستيعاب."
            )

else:
    txt_title = "🤖 Promptify-Ed"
    txt_subtitle = "Type your simple idea, and the bot will transform it into an expert prompt instantly!"
    txt_label = "✍️ Type your idea here (e.g., family, animals, story):"
    txt_placeholder = "Type here..."
    txt_select = "💡 Choose Educational Support Type:"
    options_support = [
        "General Learning",
        "Special Education - Ultra Simplified with Visual Images 📸"
    ]
    txt_button = "🚀 Optimize and Generate Prompt"
    txt_warning = "⚠️ Please type an idea or a word first!"
    txt_spinner = "⏳ Engineering and optimizing your prompt with visuals..."
    txt_success = "✨ Professional prompt generated successfully!"
    txt_result = "📋 Ready Prompt for ChatGPT (Copy below):"
    txt_info = "💡 Smart Tip: Copy the prompt above and paste it into ChatGPT or Gemini to get an ultra-simple lesson tailored for you!"
    txt_caption = "🔒 A free community application designed to serve all learners, integrated with Google Sheets."
    
    def get_prompt(support, prompt_text):
        if support == "Special Education - Ultra Simplified with Visual Images 📸":
            return (
                f"Act as a highly patient special education teacher who uses visual support. I want to learn about '{prompt_text}'. "
                f"First, generate a beautiful, simple, and clear image representing '{prompt_text}' to help me understand visually. "
                f"Second, explain the topic to me in English using ultra-short sentences (max 3 words per sentence), very basic vocabulary, "
                f"and break the lesson into 3 clear points with fun emojis. Avoid any complex paragraphs or difficult words."
            )
        else:
            return (
                f"Act as an expert English teacher. Please provide a comprehensive guide and structured lesson about '{prompt_text}' "
                f"in English, including an introduction, main points, and a conclusion to help me practice my English."
            )

# --- بناء واجهة التطبيق ---
st.title(txt_title)
st.write(txt_subtitle)

user_prompt = st.text_area(txt_label, placeholder=txt_placeholder)
support_type = st.selectbox(txt_select, options_support)

st.markdown("---")

if st.button(txt_button):
    if user_prompt.strip() == "":
        st.warning(txt_warning)
    else:
        with st.spinner(txt_spinner):
            
            # 1. توليد الأمر الذكي
            optimized_code = get_prompt(support_type, user_prompt)
            
            # 2. 🚀 السحر هنا: إرسال البيانات فوراً لجوجل شيت في الخلفية دون تأخير الطالبة
            log_to_google_sheets(lang, support_type, user_prompt)

            st.success(txt_success)
            st.subheader(txt_result)
            st.code(optimized_code)
            st.info(txt_info)

st.markdown("---")
st.caption(txt_caption)
