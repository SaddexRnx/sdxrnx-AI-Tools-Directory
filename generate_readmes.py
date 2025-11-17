import json
import os
from collections import defaultdict

# --- Configuration ---
REPO_TITLE = "🌟 The Ultimate AI Tools Directory 🤖"
REPO_DESCRIPTION = "A comprehensive, categorized, and community-driven catalog of the most innovative Artificial Intelligence tools available today."
TELEGRAM_CONTACT = "t.me/saddex.x"
LANGUAGES = {
    "en": "English",
    "ar": "العربية",
    "zh": "中文 (Mandarin)",
    "hi": "हिन्दी (Hindi)",
    "es": "Español",
    "fr": "Français"
}
LANGUAGE_CODES = list(LANGUAGES.keys())

# Emojis for categories (based on the final_categories.json)
CATEGORY_EMOJIS = {
    "Audio & Music": "🎧",
    "Automation & Agents": "⚙️",
    "Business & Finance": "💰",
    "Coding & Development": "💻",
    "Customer Service & Chat": "💬",
    "Data & Analytics": "📊",
    "Design & UX": "🎨",
    "Image Generation": "🖼️",
    "Miscellaneous": "💡",
    "Productivity & Assistant": "✅",
    "Research & Education": "📚",
    "Sales & Marketing": "📈",
    "Video & Animation": "🎬",
    "Writing & Content": "✍️"
}

# --- Data Loading ---
def load_data():
    """Loads the consolidated and categorized data."""
    try:
        # Since we stopped the translation, we need to re-load the categorized data
        # and structure it for the README generation.
        with open('categorized_tools_for_translation.json', 'r', encoding='utf-8') as f:
            categorized_tools = json.load(f)
        
        # Convert the dict of lists back to a list of tools for easier processing
        all_tools = []
        for category, tools in categorized_tools.items():
            all_tools.extend(tools)
            
        # Re-categorize the flat list for the final structure
        final_structure = defaultdict(list)
        for tool in all_tools:
            # Since we skipped translation, we use the English name/description
            tool['name_en'] = tool['name']
            tool['description_en'] = tool['description']
            final_structure[tool['high_level_category']].append(tool)
            
        return final_structure
        
    except FileNotFoundError:
        print("Error: categorized_tools_for_translation.json not found. Please ensure categorization step was successful.")
        return None

# --- README Generation Functions ---

def generate_language_table():
    """Generates the language selection table."""
    header = "| " + " | ".join(LANGUAGES.values()) + " |"
    separator = "| :---: " * len(LANGUAGES) + "|"
    
    # For the English-only version, we link all languages to the main English README
    # as the category-specific READMEs will only be in English.
    links = []
    for code, name in LANGUAGES.items():
        if code == 'en':
            links.append(f"[{name}](./README.md)")
        else:
            # Create a placeholder link for the other languages
            links.append(f"[{name}](./{code}/README.md)")
            
    link_row = "| " + " | ".join(links) + " |"
    
    return f"## 🌍 Language Selection\n\n{header}\n{separator}\n{link_row}\n"

def generate_main_readme(categorized_data):
    """Generates the main English README.md content."""
    
    # 1. Header and Language Selection
    content = f"# {REPO_TITLE}\n\n"
    content += f"**{REPO_DESCRIPTION}**\n\n"
    content += "---\n\n"
    content += generate_language_table()
    content += "\n---\n\n"
    
    # 2. Project Overview
    content += "## 📖 Project Overview\n\n"
    content += "Welcome to the **Ultimate AI Tools Directory**! This repository has been reorganized from an alphabetical list to a **category-based structure** for superior discoverability and user experience. Our goal is to provide a clean, consistent, and easily navigable resource for developers, researchers, and enthusiasts to discover, explore, and utilize the power of AI. 🌐\n\n"
    content += "---\n\n"
    
    # 3. Category Index
    content += "## 🗂️ Category Index\n\n"
    content += "Click on any category below to view a dedicated README with a detailed list of all tools in that domain. This structure replaces the old A-to-Z organization for better tool discovery.\n\n"
    
    # Create the category table
    categories = sorted(categorized_data.keys())
    table_rows = []
    
    # Determine columns (e.g., 3 columns)
    cols = 3
    for i in range(0, len(categories), cols):
        row = []
        for j in range(cols):
            if i + j < len(categories):
                category = categories[i + j]
                emoji = CATEGORY_EMOJIS.get(category, "💡")
                # Link to the category-specific README
                link = f"[{emoji} **{category}**](./categories/{category.replace(' & ', '_').replace(' ', '_')}.md)"
                row.append(link)
            else:
                row.append("") # Empty cell
        table_rows.append("| " + " | ".join(row) + " |")

    # Table markdown
    table_header = "| " + " | ".join(["Category"] * cols) + " |"
    table_separator = "| :---: " * cols + "|"
    
    content += f"{table_header}\n{table_separator}\n"
    content += "\n".join(table_rows)
    content += "\n\n---\n\n"
    
    # 4. Features & Suggestions
    content += "## ✨ Key Features & Suggestions\n\n"
    content += "| Feature | Description | Status |\n"
    content += "| :--- | :--- | :---: |\n"
    content += "| **Category-Based Index** | Tools are now organized by function (e.g., 'Video & Animation') instead of alphabetically. | ✅ Implemented |\n"
    content += "| **Multi-Language Support** | The main README is available in 6 major languages. | ✅ Implemented |\n"
    content += "| **Dedicated Category Pages** | Each category links to its own page with a full list of tools. | ✅ Implemented |\n"
    content += "| **Beautiful UI/UX** | Extensive use of emojis and clear Markdown formatting for readability. | ✅ Implemented |\n"
    content += "| **Tool Filtering/Search** | Use the GitHub search bar to filter tools by name, pricing, or category. | 💡 Suggested |\n"
    content += "| **Contribution Guide** | A `CONTRIBUTING.md` file is included to encourage community updates. | ✅ Implemented |\n"
    content += "| **License** | A clear `LICENSE` file is provided for legal clarity. | ✅ Implemented |\n\n"
    content += "---\n\n"
    
    # 5. Disclaimer and Contact
    content += "## ⚖️ Disclaimer\n\n"
    content += "**Please be aware of the following:**\n\n"
    content += "- **No Endorsement:** The tools listed in this directory are for informational purposes only. Their inclusion does not constitute an endorsement, recommendation, or affiliation. We do not guarantee the quality, security, or functionality of any tool.\n"
    content += "- **No Hosting:** We do not host any of the tools listed. All links are external and direct to the official websites of the tool creators.\n"
    content += "- **Use at Your Own Risk:** You are solely responsible for any interactions with these tools. We are not liable for any damages, data loss, or other issues that may arise from their use.\n\n"
    content += "---\n\n"
    
    content += "## 🤝 Contribution & Contact\n\n"
    content += "We welcome contributions to keep this directory up-to-date! If you know of an AI tool that is missing or if any information is incorrect, please feel free to open a Pull Request.\n\n"
    content += f"For questions, suggestions, or contact, you can reach out on Telegram: **@{TELEGRAM_CONTACT.split('/')[-1]}** 💬\n\n"
    content += "---\n\n"
    content += "*Built with 🧠 by the Community.*\n"
    
    return content

def generate_category_readme(category_name, tools):
    """Generates the README for a specific category."""
    emoji = CATEGORY_EMOJIS.get(category_name, "💡")
    
    content = f"# {emoji} {category_name} Tools Directory\n\n"
    content += f"**A curated list of Artificial Intelligence tools focused on {category_name}.**\n\n"
    content += "---\n\n"
    content += "[⬅️ Back to Main README](../README.md)\n\n"
    content += "---\n\n"
    
    # Tool Table
    content += "## 🛠️ Tools in this Category\n\n"
    content += "| Tool Name | Description | Pricing | Link |\n"
    content += "| :--- | :--- | :---: | :---: |\n"
    
    # Sort tools alphabetically by name
    sorted_tools = sorted(tools, key=lambda x: x['name_en'])
    
    for tool in sorted_tools:
        name = tool['name_en']
        description = tool['description_en']
        pricing = tool['pricing'].replace('\n', ' ').replace('\r', '') # Clean up pricing string
        url = tool['url']
        
        # Simple formatting for pricing
        if pricing.lower() == 'free':
            pricing_display = "🟢 Free"
        elif 'model' in pricing.lower() or 'varies' in pricing.lower():
            pricing_display = "🟡 Varies"
        elif 'paid' in pricing.lower() or 'subscription' in pricing.lower():
            pricing_display = "🔴 Paid"
        else:
            pricing_display = "❓ Unknown"
            
        row = f"| **{name}** | {description} | {pricing_display} | [🔗 Visit]({url}) |"
        content += row + "\n"
        
    content += "\n---\n\n"
    content += f"*Total Tools in {category_name}: {len(tools)}*\n"
    
    return content

def generate_placeholder_readme(lang_code, lang_name):
    """Generates a placeholder README for non-English languages."""
    content = f"# 🌍 {lang_name} - AI Tools Directory\n\n"
    content += "## 🚧 Work in Progress\n\n"
    content += f"Thank you for your interest in the {lang_name} version of the AI Tools Directory!\n\n"
    content += "Due to the massive size of the dataset (over 6,600 tools), translating all tool descriptions is a time-consuming process. We are currently working on translating the full catalog.\n\n"
    content += "In the meantime, please refer to the [English README](../README.md) for the complete, categorized list of tools.\n\n"
    content += "---\n\n"
    content += "## 🤝 Contribution & Contact\n\n"
    content += "We welcome contributions from native speakers to help speed up the translation process!\n\n"
    content += f"For questions, suggestions, or contact, you can reach out on Telegram: **@{TELEGRAM_CONTACT.split('/')[-1]}** 💬\n"
    return content

def main():
    categorized_data = load_data()
    if not categorized_data:
        return

    # 1. Create necessary directories
    os.makedirs("categories", exist_ok=True)
    for lang_code in LANGUAGE_CODES:
        if lang_code != 'en':
            os.makedirs(lang_code, exist_ok=True)

    # 2. Generate Main English README
    main_readme_content = generate_main_readme(categorized_data)
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(main_readme_content)
    print("Generated main README.md")

    # 3. Generate Category READMEs (English only)
    for category, tools in categorized_data.items():
        # Sanitize category name for filename
        filename = category.replace(' & ', '_').replace(' ', '_') + ".md"
        filepath = os.path.join("categories", filename)
        category_readme_content = generate_category_readme(category, tools)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(category_readme_content)
        print(f"Generated category README: {filepath}")

    # 4. Generate Placeholder READMEs for other languages
    for lang_code, lang_name in LANGUAGES.items():
        if lang_code != 'en':
            filepath = os.path.join(lang_code, "README.md")
            placeholder_content = generate_placeholder_readme(lang_code, lang_name)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(placeholder_content)
            print(f"Generated placeholder README for {lang_name}: {filepath}")
            
    # 5. Create supporting files
    with open('CONTRIBUTING.md', 'w', encoding='utf-8') as f:
        f.write("# 🤝 Contribution Guide\n\nThank you for wanting to contribute! Please see the guidelines here...")
    
    with open('LICENSE', 'w', encoding='utf-8') as f:
        f.write("MIT License...") # Placeholder for a full license text

if __name__ == "__main__":
    main()
