import json
import os

def create_language_files():
    # English language content
    en_content = {
        "task_added": "Task added for {}",
        "task_removed": "Removed task: {}",
        "no_tasks": "No tasks found!",
        "invalid_task": "Invalid task number!",
        "invalid_time": "Invalid time format. Use HH:MM",
        "your_tasks": "Your tasks:",
        "reminder": "Reminder: {}",
        "task_list_item": "{}. {} {} - {}",
        "help": {
            "title": "Task Management Bot Commands:",
            "setlang": "!setlang [en/ar] - Set your preferred language",
            "addtask": "!addtask [HH:MM] [task] - Add a new task",
            "viewtasks": "!viewtasks - View all your tasks",
            "removetask": "!removetask [number] - Remove a task by number",
            "help": "!help - Show this help message"
        }
    }

    # Arabic language content
    ar_content = {
        "task_added": "{} تمت إضافة المهمة في",
        "task_removed": "{} :تم حذف المهمة",
        "no_tasks": "!لم يتم العثور على مهام",
        "invalid_task": "!رقم المهمة غير صحيح",
        "invalid_time": "HH:MM تنسيق الوقت غير صحيح. استخدم",
        "your_tasks": ":مهامك",
        "reminder": "{} :تذكير",
        "task_list_item": "{} {} - {} .{}",
        "help": {
            "title": ":أوامر بوت إدارة المهام",
            "setlang": "!setlang [en/ar] - تعيين لغتك المفضلة",
            "addtask": "!addtask [HH:MM] [المهمة] - إضافة مهمة جديدة",
            "viewtasks": "!viewtasks - عرض جميع مهامك",
            "removetask": "!removetask [الرقم] - حذف مهمة برقمها",
            "help": "!help - إظهار رسالة المساعدة هذه"
        }
    }

    # Get current directory
    current_dir = os.getcwd()
    print(f"Creating files in: {current_dir}")

    # Create English file
    en_file_path = os.path.join(current_dir, 'lang_en.json')
    with open(en_file_path, 'w', encoding='utf-8') as f:
        json.dump(en_content, f, ensure_ascii=False, indent=4)
    print(f"Created English language file at: {en_file_path}")

    # Create Arabic file
    ar_file_path = os.path.join(current_dir, 'lang_ar.json')
    with open(ar_file_path, 'w', encoding='utf-8') as f:
        json.dump(ar_content, f, ensure_ascii=False, indent=4)
    print(f"Created Arabic language file at: {ar_file_path}")

if __name__ == "__main__":
    create_language_files()
    print("Language files created successfully!")
