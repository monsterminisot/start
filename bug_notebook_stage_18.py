# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: BugNotebook
import re, os

def add_tag(tag):
    if not tag or len(tag.strip()) == 0:
        print("Tag must be non-empty.")
        return False
    if len(tag) > 50:
        print("Tag too long (max 50 chars).")
        return False
    tags = get_tags()
    if tag in tags:
        print(f"Tag '{tag}' already exists. Use remove_tag to delete it.")
        return False
    tags.append(tag)
    save_tags(tags)
    print(f"Added tag: {tag}")
    return True

def remove_tag(tag):
    if not tag or len(tag.strip()) == 0:
        print("Tag must be non-empty.")
        return False
    tags = get_tags()
    if tag not in tags:
        print(f"Tag '{tag}' does not exist. Use add_tag to create it first.")
        return False
    new_tags = [t for t in tags if t != tag]
    save_tags(new_tags)
    print(f"Removed tag: {tag}")
    return True

def get_tags():
    try:
        with open("tags.txt", "r") as f:
            content = f.read().strip()
            if not content:
                return []
            tags = [line.strip() for line in content.split("\n") if line.strip()]
            return tags
    except FileNotFoundError:
        save_tags([])
        return []

def save_tags(tags):
    with open("tags.txt", "w") as f:
        f.write("\n".join(tags))
