import os

LANGUAGES = {
    "ar": "العربية",
    "zh": "中文 (Mandarin)",
    "hi": "हिन्दी (Hindi)",
    "es": "Español",
    "fr": "Français"
}
TELEGRAM_CONTACT = "t.me/saddex.x"
TOOL_COUNT = "6,638"

# The core English message to be translated
ENGLISH_MESSAGE = """
# 🌍 {lang_name} - AI Tools Directory

## 🚧 Work in Progress

Thank you for your interest in the {lang_name} version of the AI Tools Directory!

Due to the massive size of the dataset (over {tool_count} tools), translating all tool descriptions is a time-consuming process. We are currently working on translating the full catalog.

In the meantime, please refer to the [English README](../README.md) for the complete, categorized list of tools.

---

## 🤝 Contribution & Contact

This is a community-driven effort! We would be happy to receive your help in translating the tool names and descriptions.

If you are a native speaker and would like to contribute to the translation effort, please reach out to the maintainer on Telegram: **@{telegram_contact}** 💬
"""

# Translations of the core message components
TRANSLATIONS = {
    "ar": {
        "title": "🌍 العربية - دليل أدوات الذكاء الاصطناعي",
        "wip": "🚧 العمل قيد التقدم",
        "body": "شكرًا لاهتمامك بالنسخة العربية من دليل أدوات الذكاء الاصطناعي!",
        "reason": "نظرًا للحجم الهائل لمجموعة البيانات (أكثر من {tool_count} أداة)، فإن ترجمة جميع أوصاف الأدوات تستغرق وقتًا طويلاً. نحن نعمل حاليًا على ترجمة الكتالوج بالكامل.",
        "fallback": "في غضون ذلك، يرجى الرجوع إلى [ملف README الإنجليزي](../README.md) للحصول على القائمة الكاملة والمصنفة للأدوات.",
        "contrib_title": "🤝 المساهمة والتواصل",
        "contrib_body": "هذا جهد مجتمعي! يسعدنا تلقي مساعدتكم في ترجمة أسماء وأوصاف الأدوات.",
        "contact": "إذا كنت متحدثًا أصليًا وترغب في المساهمة في جهود الترجمة، فيرجى التواصل مع المشرف على تيليجرام: **@{telegram_contact}** 💬"
    },
    "zh": {
        "title": "🌍 中文 (普通话) - AI 工具目录",
        "wip": "🚧 正在进行中",
        "body": "感谢您对 AI 工具目录中文版本的关注！",
        "reason": "由于数据集规模庞大（超过 {tool_count} 个工具），翻译所有工具描述非常耗时。我们目前正在努力翻译完整的目录。",
        "fallback": "在此期间，请参阅[英文 README](../README.md) 以获取完整、分类的工具列表。",
        "contrib_title": "🤝 贡献与联系",
        "contrib_body": "这是一项社区驱动的工作！我们非常乐意接受您在翻译工具名称和描述方面的帮助。",
        "contact": "如果您是母语人士并希望为翻译工作做出贡献，请通过 Telegram 联系维护者：**@{telegram_contact}** 💬"
    },
    "hi": {
        "title": "🌍 हिन्दी (Hindi) - AI उपकरण निर्देशिका",
        "wip": "🚧 काम प्रगति पर है",
        "body": "AI उपकरण निर्देशिका के हिन्दी संस्करण में आपकी रुचि के लिए धन्यवाद!",
        "reason": "डेटासेट के विशाल आकार (6,600 से अधिक उपकरण) के कारण, सभी उपकरण विवरणों का अनुवाद करने में काफी समय लगता है। हम वर्तमान में संपूर्ण कैटलॉग का अनुवाद करने पर काम कर रहे हैं।",
        "fallback": "इस बीच, उपकरणों की पूरी, वर्गीकृत सूची के लिए कृपया [अंग्रेजी README](../README.md) देखें।",
        "contrib_title": "🤝 योगदान और संपर्क",
        "contrib_body": "यह एक सामुदायिक प्रयास है! हमें उपकरण के नाम और विवरण का अनुवाद करने में आपकी सहायता प्राप्त करके खुशी होगी।",
        "contact": "यदि आप एक मूल वक्ता हैं और अनुवाद के प्रयास में योगदान करना चाहते हैं, तो कृपया टेलीग्राम पर अनुरक्षक से संपर्क करें: **@{telegram_contact}** 💬"
    },
    "es": {
        "title": "🌍 Español - Directorio de Herramientas de IA",
        "wip": "🚧 Trabajo en Progreso",
        "body": "¡Gracias por su interés en la versión en español del Directorio de Herramientas de IA!",
        "reason": "Debido al tamaño masivo del conjunto de datos (más de {tool_count} herramientas), traducir todas las descripciones de las herramientas es un proceso que consume mucho tiempo. Actualmente estamos trabajando en la traducción del catálogo completo.",
        "fallback": "Mientras tanto, consulte el [README en inglés](../README.md) para obtener la lista completa y categorizada de herramientas.",
        "contrib_title": "🤝 Contribución y Contacto",
        "contrib_body": "¡Este es un esfuerzo impulsado por la comunidad! Estaríamos encantados de recibir su ayuda para traducir los nombres y descripciones de las herramientas.",
        "contact": "Si es un hablante nativo y desea contribuir al esfuerzo de traducción, comuníquese con el encargado de mantenimiento en Telegram: **@{telegram_contact}** 💬"
    },
    "fr": {
        "title": "🌍 Français - Répertoire d'Outils d'IA",
        "wip": "🚧 Travail en Cours",
        "body": "Merci de votre intérêt pour la version française du Répertoire d'Outils d'IA !",
        "reason": "En raison de la taille massive de l'ensemble de données (plus de {tool_count} outils), la traduction de toutes les descriptions d'outils est un processus long. Nous travaillons actuellement à la traduction du catalogue complet.",
        "fallback": "En attendant, veuillez vous référer au [README en anglais](../README.md) pour la liste complète et catégorisée des outils.",
        "contrib_title": "🤝 Contribution et Contact",
        "contrib_body": "Ceci est un effort communautaire ! Nous serions ravis de recevoir votre aide pour traduire les noms et descriptions des outils.",
        "contact": "Si vous êtes un locuteur natif et souhaitez contribuer à l'effort de traduction, veuillez contacter le responsable sur Telegram : **@{telegram_contact}** 💬"
    }
}

def generate_translated_readme(lang_code, lang_name):
    """Generates the translated placeholder README content."""
    
    # Use the specific translation dictionary
    t = TRANSLATIONS.get(lang_code, {})
    
    # Format the content with dynamic values
    content = f"""
{t.get("title", f"# 🌍 {lang_name} - AI Tools Directory")}

## {t.get("wip", "🚧 Work in Progress")}

{t.get("body", "Thank you for your interest in the {lang_name} version of the AI Tools Directory!").format(lang_name=lang_name)}

{t.get("reason", "Due to the massive size of the dataset (over {tool_count} tools), translating all tool descriptions is a time-consuming process. We are currently working on translating the full catalog.").format(tool_count=TOOL_COUNT)}

{t.get("fallback", "In the meantime, please refer to the [English README](../README.md) for the complete, categorized list of tools.")}

---

## {t.get("contrib_title", "🤝 Contribution & Contact")}

{t.get("contrib_body", "This is a community-driven effort! We would be happy to receive your help in translating the tool names and descriptions.")}

{t.get("contact", "If you are a native speaker and would like to contribute to the translation effort, please reach out to the maintainer on Telegram: **@{telegram_contact}** 💬").format(telegram_contact=TELEGRAM_CONTACT.split('/')[-1])}
"""
    return content.strip()

def main():
    # Ensure we are in the correct directory

    
    for lang_code, lang_name in LANGUAGES.items():
        # 1. Create the language folder
        os.makedirs(lang_code, exist_ok=True)
        
        # 2. Generate the translated README content
        readme_content = generate_translated_readme(lang_code, lang_name)
        
        # 3. Write the README.md file inside the folder
        filepath = os.path.join(lang_code, "README.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"Generated translated README for {lang_name} at {filepath}")
        
    os.chdir("..")

if __name__ == "__main__":
    main()
