import streamlit as st
import requests

# إعداد واجهة المستخدم
st.set_page_config(page_title="Promptify-Ed", page_icon="🤖", layout="centered")

# --- دالة إرسال البيانات بقناع المتصفح لتخطي قيود الأمان ---
def log_to_google_sheets(lang_used, support_type, user_word):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSd0a0DcAt3yJ_GsjHWBZUO2UVQmhJ00b1gOvYonNUcs5nNQRQ/formResponse"
    
    form_data = {
        "entry.2102841169": lang_used,     # حقل لغة الواجهة
        "entry.1661112924": support_type,  # حقل نوع الدعم التعليمي
        "entry.315119461": user_word       # حقل الكلمة/الفكرة المدخلة
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        requests.post(form_url, data=form_data, headers=headers)
    except:
        pass 

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
    txt_spinner = "⏳ جاري هندسة الأمر وتحسينه بالصور وتسجيل البيانات مجتمعياً..."
    txt_success = "✨ تم توليد الأمر الاحترافي بنجاح وتوثيقه حياً!"
    txt_result = "📋 الأمر الجاهز للنسخ (ضعيه in ChatGPT):"
    txt_info = "💡 نصيحة ذكية: انسخي الأمر أعلاه وضعي في ChatGPT أو Gemini للحصول على درس مبسط جداً وصور تناسبك!"
    txt_caption = "🔒 برنامج مجاني مجتمعي آمن لخدمة جميع فئات المجتمع ومؤتمت حياً مع جداول بيانات قوقل."
    
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
    txt_success = "✨ Professional prompt generated successfully and logged!"
    txt_result = "📋 Ready Prompt for ChatGPT (Copy below):"
    txt_info = "💡 Smart Tip: Copy the prompt above and paste it into ChatGPT or Gemini to get an ultra-simple lesson tailored for you!"
    txt_caption = "🔒 A free community application designed to serve all learners, integrated with Google Sheets."
    
    def get_prompt(support, prompt_text):
        if support == "Special Education - Ultra Simplified with Visual Images 📸":
            return (
                f"Act as a highly patient special education teacher who uses visual support. I want to learn about '{prompt_text}'. "
                f"First, generate a beautiful, simple, and clear image representing '{prompt_text}' to help me understand visually. "
                f"Second, explain the topic to me in English using ultra-short
